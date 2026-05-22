import re

with open(r'd:\Download\PortFolio-main\PortFolio-main\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix AOS Init
html = html.replace('<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>\n</body>', '<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>\n  <script>AOS.init({ duration: 800, once: true });</script>\n</body>')

with open(r'd:\Download\PortFolio-main\PortFolio-main\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open(r'd:\Download\PortFolio-main\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Fixed HTML AOS Init')

# Add Light Mode to CSS
light_theme_css = """

/*==================== LIGHT THEME ====================*/
body.light-theme {
    --bg-color: #f0f2f5;
    --text-color: #333333;
    --card-bg: rgba(255, 255, 255, 0.7);
    --hover-bg: rgba(255, 255, 255, 0.9);
}

body.light-theme .header {
    background: rgba(240, 242, 245, 0.8);
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
}

body.light-theme .nav__menu {
    background: var(--bg-color);
}

body.light-theme .skills__content,
body.light-theme .services__modal-content,
body.light-theme .portfolio__content,
body.light-theme .contact__form {
    background: var(--card-bg);
    border: 1px solid rgba(0, 0, 0, 0.05);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
}

body.light-theme .nav__logo, 
body.light-theme .nav__link, 
body.light-theme .nav__icon, 
body.light-theme .change-theme, 
body.light-theme .home__title, 
body.light-theme .home__subtitle, 
body.light-theme .section__title, 
body.light-theme .skills__title,
body.light-theme .portfolio__title,
body.light-theme .contact__title {
    color: #1a1a1a;
}
"""

with open(r'd:\Download\PortFolio-main\assets\newcss.css', 'r', encoding='utf-8') as f:
    css = f.read()

if 'body.light-theme' not in css:
    css += light_theme_css

with open(r'd:\Download\PortFolio-main\assets\newcss.css', 'w', encoding='utf-8') as f:
    f.write(css)
with open(r'd:\Download\PortFolio-main\PortFolio-main\assets\newcss.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Fixed CSS Light Theme')
