# CommonTK Wiki Archive

This repository contains the converted CommonTK (CTK - The Common Toolkit) wiki content from MediaWiki format to Markdown for use with GitHub Pages.

## Conversion Details

- **Source**: MediaWiki XML dump (`commontk-wiki-dumpbackup.xml`)
- **Total pages in dump**: 423
- **Pages converted**: 108
- **Pages skipped**: 314 (Files, User pages, Talk pages, Templates, etc.)
- **Output format**: Markdown with Jekyll frontmatter

## Structure

- `/docs/` - Contains all converted markdown files
- `convert_mediawiki_to_md.py` - Python conversion script

## Conversion Features

The conversion script handles:
- MediaWiki headings (`=`) to Markdown headings (`#`)
- Bold (`'''text'''`) and italic (`''text''`) formatting
- Internal wiki links (`[[Page]]` or `[[Page|Display]]`)
- External links
- Lists (ordered and unordered)
- Code blocks and inline code
- Images (syntax converted, though image files not extracted)

## Note on Templates and Images

Some MediaWiki-specific syntax may still be present, including:
- Template syntax (`{{template}}`)
- Some special MediaWiki markup
- Image references (image files themselves were not extracted from the dump)

## Using with GitHub Pages

To publish this as a GitHub Pages site:

1. Ensure the `docs` folder contains all your markdown files
2. Go to your repository Settings → Pages
3. Select "Deploy from a branch"
4. Choose the `main` branch and `/docs` folder
5. Your site will be published at `https://yourusername.github.io/repository-name/`

You may want to add a `_config.yml` file in the `docs` folder to customize the theme:

```yaml
theme: jekyll-theme-minimal
title: CommonTK Wiki Archive
description: Archived wiki content from the CommonTK project
```

## License

The original CommonTK content is licensed under Apache 2.0. See [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0).
