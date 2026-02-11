#!/usr/bin/env python3
"""
Convert MediaWiki XML dump to Markdown files for GitHub Pages
"""

import xml.etree.ElementTree as ET
import re
import os
from pathlib import Path
from urllib.parse import quote


def sanitize_filename(title):
    """Convert page title to a safe filename"""
    # Replace spaces with hyphens
    filename = title.replace(' ', '-')
    # Remove or replace special characters
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    # Remove leading/trailing dots and spaces
    filename = filename.strip('. ')
    # Ensure it's not empty
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
    text = re.sub(r'\[\[([^\|\]]+)\|([^\]]+)\]\]', r'[\2](\1.md)', text)
    text = re.sub(r'\[\[([^\]]+)\]\]', r'[\1](\1.md)', text)

    # Convert external links: [http://example.com Display] or [http://example.com]
    text = re.sub(r'\[([^ \]]+)\s+([^\]]+)\]', r'[\2](\1)', text)
    text = re.sub(r'\[([^\]]+)\]', r'[\1](\1)', text)

    # Convert images: [[Image:foo.png]] or [[File:foo.png]]
    text = re.sub(r'\[\[(?:Image|File):([^\|\]]+)(?:\|[^\]]*)?\]\]', r'![Image](\1)', text)

    # Convert unordered lists: * item to - item (Markdown style)
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

    # Convert code blocks: <code>text</code> to `text`
    text = re.sub(r'<code>(.+?)</code>', r'`\1`', text, flags=re.DOTALL)

    # Convert <pre> blocks to ``` code blocks
    text = re.sub(r'<pre>(.*?)</pre>', r'```\n\1\n```', text, flags=re.DOTALL)

    # Convert <nowiki> tags (remove them, keep content)
    text = re.sub(r'<nowiki>(.*?)</nowiki>', r'\1', text, flags=re.DOTALL)

    # Convert <big> tags (remove them, keep content)
    text = re.sub(r'<big>(.*?)</big>', r'\1', text, flags=re.DOTALL)

    # Remove HTML comments
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)

    # Convert <br> and <br/> to newlines
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)

    return text.strip()


def clean_xml_file(xml_file):
    """Clean XML file to fix common issues"""
    print(f"Cleaning XML file...")

    # Try different encodings
    encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']

    content = None
    for encoding in encodings:
        try:
            with open(xml_file, 'r', encoding=encoding, errors='replace') as f:
                content = f.read()
            print(f"Successfully read file with {encoding} encoding")
            break
        except Exception as e:
            print(f"Failed with {encoding}: {e}")
            continue

    if content is None:
        raise ValueError("Could not read file with any known encoding")

    # Fix unescaped ampersands (but not already escaped ones)
    # This handles & that are not part of &amp; &lt; &gt; &quot; &apos;
    content = re.sub(r'&(?!amp;|lt;|gt;|quot;|apos;|#\d+;|#x[0-9a-fA-F]+;)', '&amp;', content)

    return content


def parse_mediawiki_dump(xml_file, output_dir):
    """Parse MediaWiki XML dump and create markdown files"""

    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    # Clean and parse XML
    print(f"Parsing {xml_file}...")

    try:
        # Try with lxml parser after cleaning
        from lxml import etree as lxml_et
        cleaned_content = clean_xml_file(xml_file)
        parser = lxml_et.XMLParser(recover=True, encoding='utf-8', huge_tree=True)
        root = lxml_et.fromstring(cleaned_content.encode('utf-8'), parser)
        print("Using lxml parser")
    except Exception as e:
        print(f"lxml failed: {e}")
        # Fall back to standard parser with cleaned content
        print("Using standard parser with cleaned XML...")
        cleaned_content = clean_xml_file(xml_file)
        root = ET.fromstring(cleaned_content)
        print("Using standard parser")

    # MediaWiki namespace
    ns = {'mw': 'http://www.mediawiki.org/xml/export-0.11/'}

    # Statistics
    total_pages = 0
    converted_pages = 0
    skipped_pages = 0

    # Process each page
    for page in root.findall('mw:page', ns):
        total_pages += 1

        title_elem = page.find('mw:title', ns)
        if title_elem is None:
            continue

        title = title_elem.text

        # Skip special pages (Talk, User, MediaWiki, Template, etc.)
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

        latest_revision = revisions[-1]  # Last revision is the most recent

        text_elem = latest_revision.find('mw:text', ns)
        if text_elem is None or text_elem.text is None:
            continue

        wikitext = text_elem.text

        # Convert to markdown
        markdown = convert_wikitext_to_markdown(wikitext)

        # Add frontmatter for Jekyll/GitHub Pages
        frontmatter = f"""---
title: {title}
---

"""
        full_content = frontmatter + markdown

        # Generate filename
        filename = sanitize_filename(title)
        output_file = output_path / filename

        # Write file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_content)

        print(f"Converted: {title} -> {filename}")
        converted_pages += 1

    # Print statistics
    print(f"\n{'='*60}")
    print(f"Conversion complete!")
    print(f"Total pages: {total_pages}")
    print(f"Converted: {converted_pages}")
    print(f"Skipped: {skipped_pages}")
    print(f"Output directory: {output_path.absolute()}")


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

    parse_mediawiki_dump(xml_dump, output_dir)
