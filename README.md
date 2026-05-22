
# Personal Portfolio Website

This repository is a static portfolio site built with HTML, CSS and JavaScript. It showcases projects, skills, experience, and includes a contact form (wired to Formspree).

## What to push to GitHub
- `index.html`
- `assets/` (includes `newcss.css`, `ptj.js`, `MyCV.pdf`, and the `img/` folder)
	- `assets/img/` contains: `about.jpg`, `car.png`, `career-connect.png`, `freelance-platform.png`, `gesture-drawing.png`, `pacman.png`, `Pro.jpg`, `Pro.png`, `smartmail.png`, `timetable-generator.png`, `transit-analyser.png`, `workout-platform.png`
- `README.md`
- `fix_aos.py`, `modify_cssjs.py`, `modify_html.py` (utility scripts, optional)
- `Resume-Zaki.pdf`, `Zaki-Haider_Resume.pdf`

Do NOT push: the local Python virtual environment folder `.venv/`. Add a `.gitignore` with at least the line:

```
.venv/
```

## Quick local preview
- Open `index.html` in your browser (double-click or `Open File`) to preview locally. Some features (forms, theme persistence) work offline; server-side form delivery requires deployment.

## Contact form (Formspree)
- The site is already configured to use Formspree. The contact form posts to:

	`https://formspree.io/f/xqejbynv`

- Steps to activate and test:
	1. Sign in to Formspree and verify the email address they send you for the form.
	2. Deploy the site (see GitHub Pages below) or test the form from a local file — Formspree accepts form POSTs from deployed sites.
	3. Submit the form — Formspree will forward messages to your verified email and then redirect the browser to `./?sent=1` as configured.

## Deploy to GitHub Pages (free, recommended)
1. Create a GitHub repository and push this project to it:

```bash
git init
git add .
git commit -m "Initial portfolio commit"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo>.git
git push -u origin main
```

2. On GitHub: Settings → Pages → Source: `main` branch, folder `/ (root)` → Save.
3. After a minute your site will be live at `https://<your-username>.github.io/<repo>/`.

Notes:
- If you prefer drag-and-drop deploys and built-in form handling, Netlify is another free option (drag & drop the site folder at app.netlify.com/drop).
- If you want to use serverless email (SendGrid, etc.) instead of Formspree, I can add a Vercel/Netlify function and instruct how to set env vars.

## Add a `.gitignore` (recommended)
Create a `.gitignore` file in the repo root with:

```
.venv/
# macOS
.DS_Store
# Node (if you ever add)
node_modules/
```

---
If you want, I can:
- create/update `.gitignore` and commit it,
- add a short success/failure message UI when the form redirects (`?sent=1`),
- or push the repo to GitHub and enable Pages for you (you'll need to provide your GitHub username and repo name or grant access).



