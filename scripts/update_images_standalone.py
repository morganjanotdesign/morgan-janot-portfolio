import os
import base64
import re

def to_base64_uri(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.png':
        mime = 'image/png'
    elif ext in ['.jpg', '.jpeg']:
        mime = 'image/jpeg'
    elif ext == '.webp':
        mime = 'image/webp'
    else:
        mime = 'image/png'
    with open(file_path, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode('ascii')
    return f'data:{mime};base64,{b64}'

replacement_map = [
    # Project 01
    ("Fog Chair Modèle 001 - Vue perspective isométrique aérienne en suspension sans fond", "src/assets/images/project-01/15.png"),
    ("Fog Chair Modèle 001 - Vue trois-quarts en élévation sur piètement courbé", "src/assets/images/project-01/12.png"),
    ("Fog Chair Modèle 001 - Trio de chaises en équilibre sculptural", "src/assets/images/project-01/13.png"),
    
    # Project 02
    ("Lampadaire articulé avec socle en béton brut et câble orange", "src/assets/images/project-02/Gemini_Generated_Image_hpc2n0hpc2n0hpc2.jpg"),
    ("Détail macro rotule sphérique chromée usinée", "src/assets/images/project-02/usm-creative-since-1965-keyvisual-04-5mch2z.webp"),
    ("Bras articulé télescopique et passage de câble orange", "src/assets/images/project-02/Gemini_Generated_Image_ntm565ntm565ntm5.jpg"),
    ("Gros plan sur la rotule à facettes et l'anneau passe-câble", "src/assets/images/project-02/Gemini_Generated_Image_np88z9np88z9np88.jpg"),
    ("Cube connecteur géométrique à facettes usiné avec filetages", "src/assets/images/project-02/Gemini_Genemage_45c55i45c55i45c5.jpg"),
    
    # Project 04
    ("Chaise géométrique minimale et assise en tension textile", "src/assets/images/project-04/Gemini_Generated_Image_bbgjp7bbgjp7bbgj.jpg"),
    ("Détail vue éclatée de la traverse et des vis d'assemblage", "src/assets/images/project-04/Gemini_Generated_Image_thwtruthwtruthwt.jpg"),
    
    # Project 05
    ("Enceintes acoustiques stéréophoniques, vue trois-quarts perspective sans fond blanc", "src/assets/images/project-05/enceinte1.png"),
    ("Enceintes acoustiques en situation réelle sur table basse circulaire en chrome et tapis bleu cobalt", "src/assets/images/project-05/402051861.jpg"),
    ("Détail du geste ergonomique réglant les commandes analogiques de l'enceinte", "src/assets/images/project-05/main.png"),
    ("Roues en uréthane bleu cobalt translucide 70mm 78A à l'origine du concept des modules acoustiques", "src/assets/images/project-05/Untitled.png"),
    ("Enceintes acoustiques, grande vue arrière connectique et chambres acoustiques sans fond blanc", "src/assets/images/project-05/enceinte3.png"),
    ("Gros plan macro sur les membranes des haut-parleurs et potentiomètres analogiques sans fond blanc", "src/assets/images/project-05/enceinte4.png"),
    ("Enceintes acoustiques, grande vue de face en contre-plongée sans fond blanc", "src/assets/images/project-05/enceinte2bis.png"),
    
    # Project 06
    ("LEO-11 - Luminaire d'ambiance, vue perspective en suspension", "src/assets/images/project-06/f.png"),
    ("LEO-11 - Luminaire d'ambiance en situation in situ sur bloc de bois brut", "src/assets/images/project-06/fi.png"),
]

with open('standalone.html', 'r', encoding='utf-8') as f:
    html = f.read()

count = 0
for alt_text, img_file in replacement_map:
    uri = to_base64_uri(img_file)
    pattern = rf'(<img\s+[^>]*?alt="{re.escape(alt_text)}"[^>]*?src=")[^"]+("[^>]*?>)'
    m = re.search(pattern, html)
    if not m:
        pattern = rf'(<img\s+[^>]*?src=")[^"]+("[^>]*?alt="{re.escape(alt_text)}"[^>]*?>)'
        m = re.search(pattern, html)
    if m:
        # Replace the src portion
        start_replace = m.start() + len(m.group(1))
        end_replace = m.end() - len(m.group(2))
        html = html[:start_replace] + uri + html[end_replace:]
        print(f"Replaced: {alt_text[:40]}... with {img_file}")
        count += 1
    else:
        print(f"NOT FOUND: {alt_text}")

print(f"Total replaced: {count} / {len(replacement_map)}")

with open('standalone.html', 'w', encoding='utf-8') as f:
    f.write(html)

portfolio_path = '/Users/morganjanot/.gemini/antigravity/brain/df18ad40-ac30-4b7a-b04f-f3de4961c66b/portfolio.html'
with open(portfolio_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated standalone.html and portfolio.html successfully!")
