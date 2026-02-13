#!/usr/bin/env python3
"""
Complete MediaWiki to GitHub Pages Converter
Converts MediaWiki XML dump to Markdown with Jekyll support
"""

import xml.etree.ElementTree as ET
import re
import os
import shutil
from pathlib import Path
from urllib.parse import quote


def build_image_map(images_dir):
    """Build a lookup dict mapping lowercase filenames to their full paths.

    MediaWiki stores images in hash-based subdirectories (e.g., images/4/42/File.png).
    This walks the tree and creates a flat lookup for resolving image references.
    """
    image_map = {}
    images_path = Path(images_dir)
    if not images_path.exists():
        print(f"Warning: Images directory '{images_dir}' not found")
        return image_map

    for path in images_path.rglob('*'):
        if path.is_file() and path.suffix.lower() in (
            '.png', '.jpg', '.jpeg', '.gif', '.svg', '.bmp', '.tiff', '.ico', '.webp'
        ):
            image_map[path.name.lower()] = path
    print(f"Found {len(image_map)} images in {images_dir}/")
    return image_map


def resolve_image_filename(filename, image_map):
    """Resolve a MediaWiki image reference to an actual file path.

    Handles MediaWiki conventions:
    - Spaces in wiki refs map to underscores on disk
    - First character is case-insensitive in MediaWiki
    """
    # Try exact match first
    key = filename.lower()
    if key in image_map:
        return image_map[key]

    # Try replacing spaces with underscores
    key_underscore = filename.replace(' ', '_').lower()
    if key_underscore in image_map:
        return image_map[key_underscore]

    # Try flipping first character case with underscores
    if key_underscore:
        flipped = key_underscore[0].swapcase() + key_underscore[1:]
        if flipped in image_map:
            return image_map[flipped]

    return None


def convert_image_reference(match, image_map, referenced_images, path_prefix=''):
    """Convert a MediaWiki image/file reference to Markdown.

    Parses parameters like thumb, size, alignment, link, and caption.
    Returns Markdown image syntax with correct path.
    """
    full_match = match.group(0)
    filename = match.group(1).strip()
    params_str = match.group(2) or ''

    # Parse parameters
    params = [p.strip() for p in params_str.split('|') if p.strip()]

    link = None
    caption_parts = []

    for param in params:
        param_lower = param.lower()
        # Skip layout/display keywords
        if param_lower in ('thumb', 'thumbnail', 'frame', 'frameless', 'border',
                           'right', 'left', 'center', 'none', 'upright',
                           'baseline', 'middle', 'sub', 'super', 'top',
                           'text-top', 'bottom', 'text-bottom'):
            continue
        # Skip size specs
        if re.match(r'^\d+px$', param_lower) or re.match(r'^x\d+px$', param_lower) or re.match(r'^\d+x\d+px$', param_lower):
            continue
        # Extract link parameter
        if param_lower.startswith('link='):
            link_target = param[5:].strip()
            if link_target:
                link = link_target
            continue
        # Extract alt parameter
        if param_lower.startswith('alt='):
            continue
        # Everything else is caption text
        caption_parts.append(param)

    # Build caption - strip HTML tags and remnants for alt text
    caption = ' '.join(caption_parts)
    caption = re.sub(r'<[^>]+>', '', caption)
    # Strip HTML tag remnants from XML entity resolution (e.g., &lt;big&gt; → big)
    caption = re.sub(r'^big', '', caption)
    caption = re.sub(r'/big$', '', caption)
    caption = re.sub(r'!?/big', '', caption)
    caption = re.sub(r'^small', '', caption)
    caption = re.sub(r'/small$', '', caption)
    caption = re.sub(r'(?:/?br/?)', ' ', caption)
    caption = ' '.join(caption.split()).strip()
    if not caption:
        caption = os.path.splitext(filename)[0].replace('_', ' ').replace('-', ' ')

    # Resolve the actual image file
    resolved = resolve_image_filename(filename, image_map)
    if resolved:
        # Use the actual filename from disk (preserves case)
        disk_filename = resolved.name
        referenced_images.add(disk_filename)
        img_path = f'{path_prefix}images/{disk_filename}'
    else:
        # Image not found - use the wiki filename with underscores
        disk_filename = filename.replace(' ', '_')
        img_path = f'{path_prefix}images/{disk_filename}'

    # Build markdown
    if link:
        # Image with link
        if link.startswith('http://') or link.startswith('https://'):
            return f'[![{caption}]({img_path})]({link})'
        else:
            # Internal wiki link
            link_page = path_prefix + sanitize_link(link)
            return f'[![{caption}]({img_path})]({link_page})'
    else:
        return f'![{caption}]({img_path})'


def copy_referenced_images(image_map, referenced_images, output_dir):
    """Copy only the referenced images to the output directory."""
    images_out = Path(output_dir) / 'images'
    images_out.mkdir(exist_ok=True)

    copied = 0
    for filename in referenced_images:
        key = filename.lower()
        if key in image_map:
            src = image_map[key]
            dst = images_out / filename
            if not dst.exists() or src.stat().st_mtime > dst.stat().st_mtime:
                shutil.copy2(src, dst)
                copied += 1

    print(f"Copied {copied} images to {images_out}/")
    print(f"Total referenced images: {len(referenced_images)}")


def _sanitize_path(title):
    """Core sanitization: convert page title to a safe path (no extension).

    Wiki titles with '/' become subdirectory paths.
    Spaces and underscores become hyphens, colons and other special chars are removed.
    """
    parts = title.split('/')
    sanitized_parts = []
    for part in parts:
        # MediaWiki treats underscores and spaces as equivalent
        p = part.replace('_', '-').replace(' ', '-')
        p = re.sub(r'[<>:"/\\|?*]', '', p)
        p = p.strip('. ')
        if p:
            sanitized_parts.append(p)
    return '/'.join(sanitized_parts) if sanitized_parts else 'unnamed'


def sanitize_filename(title):
    """Convert page title to a safe .md filename for file creation.

    'Documentation/Whitepaper' → 'Documentation/Whitepaper.md'
    """
    return _sanitize_path(title) + '.md'


def sanitize_link(title):
    """Convert page title to a .html link target for Jekyll output.

    'Documentation/Whitepaper' → 'Documentation/Whitepaper.html'
    """
    return _sanitize_path(title) + '.html'


def convert_wikitext_to_markdown(wikitext, image_map=None, referenced_images=None, page_depth=0):
    """Convert MediaWiki syntax to Markdown.

    Args:
        page_depth: Number of subdirectory levels this page is in (e.g., 0 for top-level,
                    1 for Documentation/Whitepaper.md). Used to compute relative paths.
    """
    if not wikitext:
        return ""
    if image_map is None:
        image_map = {}
    if referenced_images is None:
        referenced_images = set()

    # Compute prefix for root-relative paths (images, etc.)
    path_prefix = '../' * page_depth if page_depth > 0 else ''

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

    # Convert images: [[Image:foo.png|...]] or [[File:foo.png|...]]
    # Use placeholders to prevent link regexes from corrupting image markdown
    image_placeholders = []

    def image_placeholder(m):
        md = convert_image_reference(m, image_map, referenced_images, path_prefix)
        idx = len(image_placeholders)
        image_placeholders.append(md)
        return f'\x00IMG{idx}\x00'

    text = re.sub(
        r'\[\[(?:Image|File):([^\|\]]+)((?:\|[^\]]*)?)\]\]',
        image_placeholder,
        text,
        flags=re.IGNORECASE
    )

    # Convert internal links: [[Page]] or [[Page|Display]]
    # Use placeholders to prevent external link regex from corrupting them
    link_placeholders = []

    def make_internal_link(target, display):
        """Create a markdown link from a wiki target, handling anchors."""
        # Separate anchor from page name: "Page#Section" → ("Page", "#Section")
        anchor = ''
        if '#' in target:
            target, anchor = target.split('#', 1)
            anchor = '#' + anchor.replace(' ', '-')
        link_path = path_prefix + sanitize_link(target.strip()) + anchor
        idx = len(link_placeholders)
        link_placeholders.append(f'[{display}]({link_path})')
        return f'\x00LNK{idx}\x00'

    def internal_link_with_display(m):
        target = m.group(1).strip()
        display = m.group(2).strip()
        return make_internal_link(target, display)

    def internal_link_simple(m):
        target = m.group(1).strip()
        display = target.split('/')[-1].split('#')[0]  # Use last part as display
        return make_internal_link(target, display)

    text = re.sub(r'\[\[([^\|\]]+)\|([^\]]+)\]\]', internal_link_with_display, text)
    text = re.sub(r'\[\[([^\]]+)\]\]', internal_link_simple, text)

    # Convert external links: [http://example.com Display] or [http://example.com]
    text = re.sub(r'\[(https?://[^ \]]+)\s+([^\]]+)\]', r'[\2](\1)', text)
    text = re.sub(r'\[(https?://[^\]]+)\]', r'[\1](\1)', text)

    # Restore all placeholders (images and links)
    for idx, md in enumerate(image_placeholders):
        text = text.replace(f'\x00IMG{idx}\x00', md)
    for idx, md in enumerate(link_placeholders):
        text = text.replace(f'\x00LNK{idx}\x00', md)

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


def parse_mediawiki_dump(xml_file, output_dir, images_dir='imagesSource'):
    """Parse MediaWiki XML dump and create markdown files"""

    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    # Build image lookup map
    image_map = build_image_map(images_dir)
    referenced_images = set()

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
        # Compute page depth for relative path resolution
        page_depth = sanitize_filename(title).count('/')
        markdown = convert_wikitext_to_markdown(wikitext, image_map, referenced_images, page_depth)

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

        # Generate filename (may include subdirectory path)
        filename = sanitize_filename(title)
        output_file = output_path / filename

        # Create subdirectories if needed
        output_file.parent.mkdir(parents=True, exist_ok=True)

        # Write file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_content)

        print(f"Converted: {title} -> {filename}")
        converted_pages += 1

    # Copy referenced images to output directory
    if image_map:
        copy_referenced_images(image_map, referenced_images, output_dir)

    print(f"\n{'='*60}")
    print(f"Conversion complete!")
    print(f"Total pages: {total_pages}")
    print(f"Converted: {converted_pages}")
    print(f"Skipped: {skipped_pages}")
    print(f"Images referenced: {len(referenced_images)}")
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
- [DICOM Overview](Documentation/DICOM-Overview.html)
- [CtkDICOM](CtkDICOM.html)
- [DICOM Application Hosting](Documentation/DicomApplicationHosting.html)

### Plugin Framework
- [Plugin Framework Introduction](Documentation/CTK-Plugin-Framework-Introduction.html)
- [Plugin Framework Getting Started](Documentation/CTK-Plugin-Framework-Getting-Started.html)
- [Plugin Framework Tutorials](Documentation/CTK-Plugin-Framework-Tutorials.html)

### Widgets & UI
- [Widgets Documentation](Documentation/Widgets.html)
- [Image Gallery](Documentation/ImageGallery.html)
- [CTK In QtDesigner](CTK-In-QtDesigner.html)

### Build & Development
- [Build Instructions](Build-Instructions.html)
- [Build Options](Documentation/Build-Options.html)
- [Dashboard Setup](Dashboard-setup.html)

### Command Line Interface
- [CLI Support in CTK](Documentation/CLI-Support-in-CTK.html)
- [CLI Modules](Documentation/CLI-Modules.html)

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
repository: sjh26/ctk-wiki-archive

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
