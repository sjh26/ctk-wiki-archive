# Local Testing Setup Guide

This guide provides multiple options for testing your GitHub Pages site locally.

## Option 1: Quick Test with Python (No Jekyll Processing)

**Pros**: Fastest setup, no additional installations needed
**Cons**: Doesn't process Jekyll templates or themes

```bash
python serve.py
```

Then open http://localhost:8000/ in your browser.

This serves the raw markdown files but won't render the Jekyll theme.

---

## Option 2: Full Jekyll Setup (Recommended for Production Testing)

**Pros**: Exact preview of how it will look on GitHub Pages
**Cons**: Requires Ruby installation

### Step 1: Install Ruby

**Windows**:
1. Download and install Ruby+Devkit from: https://rubyinstaller.org/downloads/
   - Recommended: Ruby+Devkit 3.2.x (x64)
2. During installation, check "Add Ruby to PATH"
3. Run `ridk install` when prompted (choose option 3)

**Mac** (if you switch machines):
```bash
brew install ruby
```

**Linux**:
```bash
sudo apt-get install ruby-full build-essential zlib1g-dev
```

### Step 2: Install Bundler

```bash
gem install bundler
```

### Step 3: Install Jekyll Dependencies

```bash
cd docs
bundle install
```

### Step 4: Run Jekyll Locally

```bash
bundle exec jekyll serve
```

Or with live reload:
```bash
bundle exec jekyll serve --livereload
```

Then open http://localhost:4000/ in your browser.

---

## Option 3: Docker (Alternative)

If you have Docker installed:

```bash
docker run --rm -it \
  -v "%cd%/docs:/srv/jekyll" \
  -p 4000:4000 \
  jekyll/jekyll \
  jekyll serve
```

Then open http://localhost:4000/

---

## Troubleshooting

### Port Already in Use
If you get "port already in use" errors:
- For Python: Change `PORT = 8000` in `serve.py` to another number
- For Jekyll: Run `bundle exec jekyll serve --port 4001`

### Jekyll Build Errors
If Jekyll fails to build:
1. Check `docs/_config.yml` for syntax errors
2. Ensure all markdown files have valid frontmatter
3. Run `bundle exec jekyll build --verbose` for detailed errors

### Theme Not Showing
If the theme doesn't appear:
1. Make sure `_config.yml` is in the `docs/` folder
2. Verify the theme name matches a valid GitHub Pages theme
3. Try clearing Jekyll cache: `bundle exec jekyll clean`
