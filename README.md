
# Personal Portfolio Website

# Personal Portfolio — Zaki Haider

This repository contains a static personal portfolio website that showcases projects, skills, and experience. It is implemented with plain HTML, CSS and JavaScript and is intended to be deployed as a static site (for example on GitHub Pages or Netlify). The contact form is configured to use Formspree for email delivery.

## Table of contents
- [Features](#features)
- [Tech stack](#tech-stack)
- [Repository contents](#repository-contents)
- [Local preview](#local-preview)
- [Deploying](#deploying)
- [Contact form (Formspree)](#contact-form-formspree)
- [Tips & security](#tips--security)
- [Contributing](#contributing)
- [License](#license)

## Features
- Home: hero section with profile, title and badges.
- About: short bio, education (CGPA), and stat cards.
- Skills: accordion-style grouped skills (Programming, Frontend, AI/ML, Databases, Tools).
- Experience & Qualification: timeline and education modal details.
- Projects: horizontal, swipeable project carousel with images and links.
- Contact: contact information and a form (wired to Formspree) that forwards messages to your email.
- Theme toggle (dark/light) and AOS entry animations.

## Tech stack
- HTML, CSS (assets/newcss.css)
- JavaScript (assets/ptj.js)
- Images and resume PDFs in `assets/`

## Repository contents
Recommended files/folders to push to GitHub:

- `index.html`
- `assets/`
	- `assets/newcss.css` — styles
	- `assets/ptj.js` — frontend scripts
	- `assets/MyCV.pdf` — downloadable CV
	- `assets/img/` — project and profile images (see list below)
- `README.md` (this file)
- `Resume-Zaki.pdf`, `Zaki-Haider_Resume.pdf` (reference PDFs)
- utility scripts (optional): `fix_aos.py`, `modify_cssjs.py`, `modify_html.py`

Contents of `assets/img/` (present in this repo):
`about.jpg`, `car.png`, `career-connect.png`, `freelance-platform.png`, `gesture-drawing.png`, `pacman.png`, `Pro.jpg`, `Pro.png`, `smartmail.png`, `timetable-generator.png`, `transit-analyser.png`, `workout-platform.png`

Files/folders to ignore (do not push):
- `.venv/` (local Python virtual environment)

Create a `.gitignore` with at least:

```
.venv/
.DS_Store
node_modules/
```

## Local preview
1. Clone or copy the project to your machine.
2. Open `index.html` in your browser to preview. No build step is required.

Notes:
- Some integrations (server-side email delivery, serverless functions) require deployment to a hosting provider. The Formspree contact form works after you verify your email in Formspree.

## Deploying
Two simple free hosting options are recommended:

### Option A — GitHub Pages (static, free)
1. Create a GitHub repo (or use the existing `https://github.com/Zakihayder/PortFolio`).
2. Push the project to the `main` branch.
3. In the repository Settings → Pages, set the source to `main` branch (root) and save.
4. Wait a minute — your site will be available at `https://<your-username>.github.io/<repo>/`.

Example commands:

```bash
git init
git add .
git commit -m "Initial portfolio"
git remote add origin https://github.com/<your-username>/<repo>.git
git branch -M main
git push -u origin main
```

### Option B — Netlify (drag & drop or Git)
- Drag & drop the project folder at https://app.netlify.com/drop for a one-click deploy.
- Or connect your GitHub repository for continuous deploys.
- Netlify also supports form handling and serverless functions if you later switch from Formspree.

## Contact form (Formspree)
This site is pre-configured to use Formspree. Current endpoint:

```
https://formspree.io/f/xqejbynv
```

Steps to activate and test:
1. Sign in or create a free Formspree account.
2. Verify your email address when Formspree sends the confirmation message.
3. Submit the contact form on the deployed site — Formspree will forward messages to your verified address.
4. The site is configured to redirect to `./?sent=1` (success) or `./?sent=0` (failure). A small status message will appear in the Contact section after redirect.

If you prefer full control, you can replace Formspree with:
- a self-hosted PHP endpoint using PHPMailer + SMTP, or
- a serverless function (Vercel/Netlify) that calls an email provider API (SendGrid, Mailgun, Postmark).

## Tips & security
- Do NOT store API keys, SMTP passwords, or other secrets in repository files. Use environment variables in serverless functions or your hosting provider's secret store.
- Add basic spam protection (honeypot field or reCAPTCHA) if you receive spam through the form.
- Test the contact form end-to-end after deployment — Formspree requires the origin to be deployed to forward messages reliably.

## Contributing
- This repository is yours. If you want me to make further refinements (styling, animations, deploy automation), tell me what to change and I will apply it.

## License
This repository has no license file by default. If you want a permissive license, I can add an `MIT` license file for you.

---
If you want, I can:
- add a styled success banner (CSS) for the contact status message,
- add `.github/workflows` with a simple deploy action, or
- add a small `deploy.sh` that automates pushing and enabling Pages (you will still need to enable Pages in GitHub settings).




