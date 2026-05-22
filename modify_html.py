import re

with open(r'd:\Download\PortFolio-main\PortFolio-main\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add AOS CSS to Head
if 'aos.css' not in content:
    content = content.replace('</head>', '  <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">\n</head>')

# 2. Add AOS JS to Body
if 'aos.js' not in content:
    content = content.replace('</body>', '  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>\n</body>')

# 3. Fix SVG image tag
content = re.sub(
    r'<image class="home__blob-img" x="-79" y="-46" xlink:href="assets/img/Pro.jpg" />',
    '<image class="home__blob-img" x="-20" y="-20" width="230" height="230" preserveAspectRatio="xMidYMid slice" xlink:href="assets/img/Pro.jpg" />',
    content
)

# 4. Update About Stats
content = re.sub(
    r'<span class="about__info-title">.*?</span>\s*<span class="about__info-name">Aggregate <br />CGPA</span>',
    '<span class="about__info-title">3.1+</span>\n              <span class="about__info-name">Aggregate <br />CGPA</span>',
    content, flags=re.DOTALL
)
content = re.sub(
    r'<span class="about__info-title">.*?</span>\s*<span class="about__info-name">\s*Projects</span>',
    '<span class="about__info-title">20+</span>\n              <span class="about__info-name">Projects</span>',
    content, flags=re.DOTALL
)

# Update About summary text
old_about = "AI-Powered Full-Stack Engineer focused on designing and delivering intelligent, scalable products that drive real impact. I aim to build reliable systems and turn complex problems into elegant solutions, with a long-term goal of leading AI-driven product development."
new_about = "Final-year Software Engineering student at FAST-NUCES with hands-on expertise in AI, Machine Learning, Computer Vision, and full-stack development using the MERN stack. Proven track record of delivering production-grade systems and winning national hackathons. Actively seeking AI and web engineering opportunities to build scalable, intelligent products."
content = content.replace(old_about, new_about)

# 5. Add data-aos to sections
content = content.replace('<div class="home__content grid">', '<div class="home__content grid" data-aos="fade-up">')
content = content.replace('<div class="about__container container grid">', '<div class="about__container container grid" data-aos="fade-up">')
content = content.replace('<div class="skills__container container grid">', '<div class="skills__container container grid" data-aos="fade-up">')
content = content.replace('<div class="qualification__container container grid services__container">', '<div class="qualification__container container grid services__container" data-aos="fade-up">')
content = content.replace('<div class="portfolio__container container swiper-container">', '<div class="portfolio__container container swiper-container" data-aos="fade-up">')
content = content.replace('<div class="contact__container container grid">', '<div class="contact__container container grid" data-aos="fade-up">')

with open(r'd:\Download\PortFolio-main\PortFolio-main\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open(r'd:\Download\PortFolio-main\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML formatting applied successfully.")
