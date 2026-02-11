#!/usr/bin/env python3
"""
Complete MediaWiki to GitHub Pages Converter
Converts MediaWiki XML dump to Markdown with Jekyll support
"""

import xml.etree.ElementTree as ET
import re
import os
from pathlib import Path
from urllib.parse import quote


def sanitize_filename(title):
    """Convert page title to a safe filename"""
    filename = title.replace(' ', '-')
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    filename = filename.strip('. ')
    if not filename:
        filename = 'unnamed'
    return filename + '.md'


def convert_wikitext_to_markdown(wikitext):
    """Convert MediaWiki syntax to Markdown"""
    if not wikitext:
        return ""

    text = wikitext

    # Convert headings: = Heading = to # Heading
    text = re.sub(r'^======\s*(.+?)\s*======\s*$', r'###### \1', text, flags=re.MULTILINE)
    text = re.sub(r'^=====\s*(.+?)\s*=====\s*$', r'##### \1', text, flags=re.MULTILINE)
    text = re.sub(r'^====\s*(.+?)\s*====\s*$', r'#### \1', text, flags=re.MULTILINE)
    text = re.sub(r'^===\s*(.+?)\s*===\s*$', r'### \1', text, flags=re.MULTILINE)
    text = re.sub(r'^==\s*(.+?)\s*==\s*$', r'## \1', text, flags=re.MULTILINE)
    text = re.sub(r'^=\s*(.+?)\s*=\s*$', r'# \1', text, flags=re.MULTILINE)

    # Convert bold: '''text''' to **text**
    text = re.sub(r"'''(.+?)'''", r'**\1**', text)

    # Convert italic: ''text'' to *text*
    text = re.sub(r"''(.+?)''", r'*\1*', text)

    # Convert internal links: [[Page]] or [[Page|Display]]
    text = re.sub(r'\[\[([^\|\]]+)\|([^\]]+)\]\]', r'[\2](\1.html)', text)
    text = re.sub(r'\[\[([^\]]+)\]\]', r'[\1](\1.html)', text)

    # Convert external links: [http://example.com Display] or [http://example.com]
    text = re.sub(r'\[([^ \]]+)\s+([^\]]+)\]', r'[\2](\1)', text)
    text = re.sub(r'\[([^\]]+)\]', r'[\1](\1)', text)

    # Convert images: [[Image:foo.png]] or [[File:foo.png]]
    text = re.sub(r'\[\[(?:Image|File):([^\|\]]+)(?:\|[^\]]*)?\]\]', r'![Image](\1)', text)

    # Convert unordered lists: * item to - item
    text = re.sub(r'^\*\s+', r'- ', text, flags=re.MULTILINE)

    # Convert ordered lists: # item to 1. item
    lines = text.split('\n')
    in_ordered_list = False
    for i, line in enumerate(lines):
        if re.match(r'^#+\s+', line):
            if not in_ordered_list:
                in_ordered_list = True
            level = len(re.match(r'^(#+)', line).group(1))
            lines[i] = '  ' * (level - 1) + '1. ' + line.lstrip('#').strip()
        else:
            in_ordered_list = False
    text = '\n'.join(lines)

    # Convert code blocks
    text = re.sub(r'<code>(.+?)</code>', r'`\1`', text, flags=re.DOTALL)
    text = re.sub(r'<pre>(.*?)</pre>', r'```\n\1\n```', text, flags=re.DOTALL)

    # Remove or convert special tags
    text = re.sub(r'<nowiki>(.*?)</nowiki>', r'\1', text, flags=re.DOTALL)
    text = re.sub(r'<big>(.*?)</big>', r'\1', text, flags=re.DOTALL)
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)

    return text.strip()


def fix_yaml_frontmatter(content):
    """Fix YAML frontmatter by quoting titles with special characters"""
    if not content.startswith('---\n'):
        return content

    match = re.match(r'^(---\n)(.*?\n)(---\n)(.*)$', content, re.DOTALL)
    if not match:
        return content

    start_marker = match.group(1)
    frontmatter = match.group(2)
    end_marker = match.group(3)
    body = match.group(4)

    # Fix title line - quote it if it contains a colon and isn't already quoted
    lines = frontmatter.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('title:'):
            title_part = line[6:].strip()
            if ':' in title_part and not (title_part.startswith('"') or title_part.startswith("'")):
                lines[i] = f'title: "{title_part}"'

    new_frontmatter = '\n'.join(lines)
    return start_marker + new_frontmatter + end_marker + body


def fix_malformed_templates(content):
    """Clean up malformed MediaWiki template syntax"""
    # Fix incomplete {{fullurl:...}} patterns
    content = re.sub(r'\{\{fullurl:[^}]*?\)', '', content)

    # Fix {{:Page}} patterns - convert to just [Page]
    content = re.sub(r'\{\{:([^}]+?)\}\}', r'[\1]', content)

    # Fix templates with trailing ) but no closing }}
    content = re.sub(r'\{\{([^}]*?)\)\s*(?!\}\})', r'`{{\1}}`', content)

    # Fix incomplete templates at end of line
    content = re.sub(r'\{\{([^}]*?)$', r'`{{\1`', content, flags=re.MULTILINE)

    # Fix templates with ?action=purge
    content = re.sub(r'\{\{([^}]*?[/:].*?)\}\}\?action=purge', r'', content)

    # Escape remaining problematic templates in backticks
    content = re.sub(r'\{\{([a-zA-Z][a-zA-Z0-9_\-/: ]*?)\}\}', r'`{{\1}}`', content)

    return content


def clean_xml_file(xml_file):
    """Clean XML file to fix common issues"""
    print(f"Cleaning XML file...")

    encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']
    content = None

    for encoding in encodings:
        try:
            with open(xml_file, 'r', encoding=encoding, errors='replace') as f:
                content = f.read()
            print(f"Successfully read file with {encoding} encoding")
            break
        except Exception as e:
            continue

    if content is None:
        raise ValueError("Could not read file with any known encoding")

    # Fix unescaped ampersands
    content = re.sub(r'&(?!amp;|lt;|gt;|quot;|apos;|#\d+;|#x[0-9a-fA-F]+;)', '&amp;', content)

    return content


def parse_mediawiki_dump(xml_file, output_dir):
    """Parse MediaWiki XML dump and create markdown files"""

    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    print(f"Parsing {xml_file}...")

    try:
        from lxml import etree as lxml_et
        cleaned_content = clean_xml_file(xml_file)
        parser = lxml_et.XMLParser(recover=True, encoding='utf-8', huge_tree=True)
        root = lxml_et.fromstring(cleaned_content.encode('utf-8'), parser)
        print("Using lxml parser")
    except Exception as e:
        print(f"lxml failed: {e}, using standard parser")
        cleaned_content = clean_xml_file(xml_file)
        root = ET.fromstring(cleaned_content)

    ns = {'mw': 'http://www.mediawiki.org/xml/export-0.11/'}

    total_pages = 0
    converted_pages = 0
    skipped_pages = 0

    for page in root.findall('mw:page', ns):
        total_pages += 1

        title_elem = page.find('mw:title', ns)
        if title_elem is None:
            continue

        title = title_elem.text

        # Skip special pages
        if ':' in title and title.split(':')[0] in [
            'Talk', 'User', 'User talk', 'File', 'File talk',
            'MediaWiki', 'MediaWiki talk', 'Template', 'Template talk',
            'Help', 'Help talk', 'Category', 'Category talk', 'Special'
        ]:
            print(f"Skipping: {title}")
            skipped_pages += 1
            continue

        # Get the latest revision
        revisions = page.findall('mw:revision', ns)
        if not revisions:
            continue

        latest_revision = revisions[-1]
        text_elem = latest_revision.find('mw:text', ns)
        if text_elem is None or text_elem.text is None:
            continue

        wikitext = text_elem.text

        # Convert to markdown
        markdown = convert_wikitext_to_markdown(wikitext)

        # Add frontmatter
        frontmatter = f"""---
title: {title}
---

"""
        full_content = frontmatter + markdown

        # Fix YAML frontmatter
        full_content = fix_yaml_frontmatter(full_content)

        # Fix malformed templates
        full_content = fix_malformed_templates(full_content)

        # Generate filename
        filename = sanitize_filename(title)
        output_file = output_path / filename

        # Write file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_content)

        print(f"Converted: {title} -> {filename}")
        converted_pages += 1

    print(f"\n{'='*60}")
    print(f"Conversion complete!")
    print(f"Total pages: {total_pages}")
    print(f"Converted: {converted_pages}")
    print(f"Skipped: {skipped_pages}")
    print(f"Output directory: {output_path.absolute()}")

    return converted_pages


def create_index_files(output_dir):
    """Create index.md and index.html for the site"""
    output_path = Path(output_dir)

    # Create index.md
    index_md = """---
layout: default
title: CommonTK Wiki Archive
---

# CommonTK Wiki Archive

Welcome to the CommonTK (CTK - The Common Toolkit) wiki archive. This is a converted version of the original MediaWiki content.

## Main Pages

- [Main Page](Main-Page.html)
- [Getting Started](Getting-Started.html)
- [Documentation](Documentation.html)
- [The Team](The-Team.html)
- [News](News.html)
- [Events](Events.html)
- [Contributing to CTK](Contributing-to-CTK.html)

## Key Topics

### DICOM
- [DICOM Overview](DocumentationDICOM-Overview.html)
- [CtkDICOM](CtkDICOM.html)
- [DICOM Application Hosting](DocumentationDicomApplicationHosting.html)

### Plugin Framework
- [Plugin Framework Introduction](DocumentationCTK-Plugin-Framework-Introduction.html)
- [Plugin Framework Getting Started](DocumentationCTK-Plugin-Framework-Getting-Started.html)
- [Plugin Framework Tutorials](DocumentationCTK-Plugin-Framework-Tutorials.html)

### Widgets & UI
- [Widgets Documentation](DocumentationWidgets.html)
- [Image Gallery](DocumentationImageGallery.html)
- [CTK In QtDesigner](CTK-In-QtDesigner.html)

### Build & Development
- [Build Instructions](Build-Instructions.html)
- [Build Options](DocumentationBuild-Options.html)
- [Dashboard Setup](Dashboard-setup.html)

### Command Line Interface
- [CLI Support in CTK](DocumentationCLI-Support-in-CTK.html)
- [CLI Modules](DocumentationCLI-Modules.html)

## About

This wiki archive was converted from MediaWiki format to Markdown for GitHub Pages.
"""

    with open(output_path / 'index.md', 'w', encoding='utf-8') as f:
        f.write(index_md)
    print("Created index.md")


def create_jekyll_config(output_dir):
    """Create _config.yml for Jekyll"""
    output_path = Path(output_dir)

    config = """title: CommonTK Wiki Archive
description: Archived documentation from the CommonTK project
markdown: kramdown
theme: jekyll-theme-cayman

# Exclude files from processing
exclude:
  - Gemfile
  - Gemfile.lock
"""

    with open(output_path / '_config.yml', 'w', encoding='utf-8') as f:
        f.write(config)
    print("Created _config.yml")


if __name__ == '__main__':
    import sys

    # Configuration
    xml_dump = 'commontk-wiki-dumpbackup.xml'
    output_dir = 'docs'

    if len(sys.argv) > 1:
        xml_dump = sys.argv[1]
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]

    if not os.path.exists(xml_dump):
        print(f"Error: File '{xml_dump}' not found")
        sys.exit(1)

    print("="*60)
    print("MediaWiki to GitHub Pages Converter")
    print("="*60)

    # Run conversion
    converted_count = parse_mediawiki_dump(xml_dump, output_dir)

    # Create supporting files
    create_index_files(output_dir)
    create_jekyll_config(output_dir)

    print("\n" + "="*60)
    print("All done! Next steps:")
    print("="*60)
    print("1. Install Jekyll dependencies:")
    print("   cd docs && bundle install")
    print("2. Test locally:")
    print("   bundle exec jekyll serve")
    print("3. View at: http://localhost:4000/")
    print("="*60)
