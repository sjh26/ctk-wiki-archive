# MediaWiki to GitHub Pages Conversion Guide

## Quick Start

Convert a MediaWiki XML dump to a GitHub Pages-ready site in one command:

```bash
python convert_wiki.py
```

That's it! The script will:
1. ✅ Parse the MediaWiki XML dump
2. ✅ Convert wiki syntax to Markdown
3. ✅ Fix YAML frontmatter issues
4. ✅ Fix malformed template syntax
5. ✅ Create index pages
6. ✅ Generate Jekyll configuration

## Usage

### Basic Usage
```bash
python convert_wiki.py [xml_file] [output_dir]
```

**Parameters:**
- `xml_file` - Path to MediaWiki XML dump (default: `commontk-wiki-dumpbackup.xml`)
- `output_dir` - Output directory for markdown files (default: `docs`)

### Examples

Convert with default settings:
```bash
python convert_wiki.py
```

Convert custom XML file:
```bash
python convert_wiki.py my-wiki-dump.xml
```

Convert to custom directory:
```bash
python convert_wiki.py my-dump.xml output
```

## What Gets Converted

### ✅ Converted
- Wiki headings (`=`) → Markdown headings (`#`)
- Bold (`'''text'''`) → `**text**`
- Italic (`''text''`) → `*text*`
- Internal links (`[[Page]]`) → `[Page](Page.html)`
- External links
- Lists (ordered and unordered)
- Code blocks
- Images (syntax only, files not extracted)

### ⚠️ Needs Manual Review
- MediaWiki templates (converted to backticks for safety)
- Complex tables
- Special MediaWiki extensions

### ❌ Skipped
- Talk pages
- User pages
- File uploads (only syntax converted)
- Templates
- Special pages

## Testing the Output

### Option 1: Jekyll (Full Preview)
```bash
cd docs
bundle install
bundle exec jekyll serve
```
View at: http://localhost:4000/

### Option 2: Python Server (Quick Preview)
```bash
python serve.py
```
View at: http://localhost:8000/

## Troubleshooting

### Missing lxml
If you get an lxml error:
```bash
pip install lxml
```

### Encoding Errors
The script tries multiple encodings automatically. If it still fails, check your XML file encoding.

### Jekyll Build Warnings
Yellow warnings about Liquid syntax are normal and don't prevent the site from working.

## File Structure After Conversion

```
docs/
├── _config.yml              # Jekyll configuration
├── index.md                 # Site homepage
├── Main-Page.md            # Converted pages
├── Getting-Started.md
├── Documentation.md
└── ...                     # All other converted pages
```

## Deployment to GitHub Pages

1. **Initialize Git:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: MediaWiki conversion"
   ```

2. **Push to GitHub:**
   ```bash
   git remote add origin https://github.com/USERNAME/REPO.git
   git push -u origin main
   ```

3. **Enable Pages:**
   - Go to repository Settings → Pages
   - Source: `main` branch, `/docs` folder
   - Save

4. **Access your site:**
   `https://USERNAME.github.io/REPO/`

## Re-running the Conversion

If you need to reconvert:
1. Delete or backup the `docs` folder
2. Run the script again: `python convert_wiki.py`

The script will overwrite existing files in the output directory.
