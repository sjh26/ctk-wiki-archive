# Deployment Guide for CommonTK Wiki Archive

## ✅ Conversion Complete

Your MediaWiki dump has been successfully converted to Markdown:
- **108 pages converted** to Markdown format
- **314 pages skipped** (Files, Templates, User pages, etc.)
- All files in the `/docs` folder

## Local Testing

### Current Setup
A Python HTTP server is running at: **http://localhost:8000/**

To stop the server:
```bash
# Find the process
ps aux | grep "python serve.py"
# Kill it
kill <process_id>
```

To restart it:
```bash
python serve.py
```

### Jekyll (Optional)
Jekyll setup encountered issues with MediaWiki template syntax. A `.nojekyll` file has been created to bypass Jekyll processing on GitHub Pages.

## Deploying to GitHub Pages

### Step 1: Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `ctk-pages` (or your preferred name)
3. Description: "CommonTK Wiki Archive"
4. Make it Public
5. **Don't** initialize with README (we already have files)
6. Click "Create repository"

### Step 2: Push to GitHub
```bash
cd d:\ctk-pages

# Initialize git (if not already done)
git init

# Add all files
git add .

# Create first commit
git commit -m "Add CommonTK wiki archive

- Converted 108 pages from MediaWiki to Markdown
- Added Python local server for testing
- Configured for GitHub Pages deployment"

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/ctk-pages.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages
1. Go to your repository on GitHub
2. Click **Settings** → **Pages** (in the sidebar)
3. Under "Source":
   - Branch: `main`
   - Folder: `/docs`
4. Click **Save**
5. Wait 1-2 minutes for deployment

Your site will be available at:
`https://YOUR_USERNAME.github.io/ctk-pages/`

## File Structure

```
d:\ctk-pages\
├── docs/                    # All converted markdown files
│   ├── .nojekyll           # Disables Jekyll processing
│   ├── index.html          # Homepage with navigation
│   ├── _config.yml         # Jekyll config (not used with .nojekyll)
│   ├── Main-Page.md        # Converted pages...
│   └── ...
├── commontk-wiki-dumpbackup.xml  # Original MediaWiki dump
├── convert_mediawiki_to_md.py    # Conversion script
├── serve.py                # Local Python server
├── README.md               # Repository documentation
└── SETUP.md                # Local testing setup guide
```

## Notes on Content

### MediaWiki Syntax Remaining
Some MediaWiki-specific syntax may still be visible:
- Template calls: `{{template}}`
- Some formatting that doesn't have Markdown equivalents
- Image references (images weren't extracted from the dump)

### Future Improvements
If you want to improve the conversion:
1. Extract and add images from the original wiki
2. Manually clean up remaining MediaWiki syntax
3. Add custom CSS styling in `docs/assets/css/style.css`
4. Create a proper navigation structure

## Troubleshooting

### Pages don't load on GitHub Pages
- Ensure `.nojekyll` file exists in `/docs`
- Check that repository is Public
- Wait a few minutes after enabling Pages

### Links don't work
- Internal links use `.md` extensions
- GitHub Pages will handle these automatically
- If not, you may need to update links to use `.html`

### Want to use Jekyll after all?
1. Delete `.nojekyll` file
2. Fix template syntax in problematic files
3. Or exclude them in `_config.yml`
