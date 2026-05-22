import re

for filepath in [r'd:\Download\PortFolio-main\assets\newcss.css', r'd:\Download\PortFolio-main\PortFolio-main\assets\newcss.css']:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            css = f.read()

        # Fix qualification line alignment
        css = css.replace('transform: translate(6px, -7px);', 'transform: translate(6px, 0); margin-top: -10px;')
        
        # Add padding to skills list so text doesn't overflow right
        css = css.replace('.skills__list { row-gap: 1.5rem; padding-left: 2.7rem; }', '.skills__list { row-gap: 1.5rem; padding-left: 2.7rem; padding-right: 1rem; }')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(css)
    except Exception as e:
        print(f"Failed CSS {filepath}: {e}")

for filepath in [r'd:\Download\PortFolio-main\assets\ptj.js', r'd:\Download\PortFolio-main\PortFolio-main\assets\ptj.js']:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            js = f.read()

        if 'AOS.init' not in js:
            js += "\n\n/*==================== AOS ANIMATION ====================*/\ndocument.addEventListener('DOMContentLoaded', () => {\n  if(typeof AOS !== 'undefined') {\n    AOS.init({ duration: 1000, once: true });\n  }\n});\n"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(js)
    except Exception as e:
        print(f"Failed JS {filepath}: {e}")

print("CSS and JS formatting applied successfully.")
