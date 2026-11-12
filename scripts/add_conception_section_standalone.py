import os
import shutil
import base64
import re

standalone_path = 'standalone.html'
portfolio_artifact_path = '/Users/morganjanot/.gemini/antigravity/brain/df18ad40-ac30-4b7a-b04f-f3de4961c66b/portfolio.html'
webp_dir = 'src/assets/images_webp/project-01'

with open(standalone_path, 'r', encoding='utf-8') as f:
    html = f.read()

p1_start = html.find('id="view-project-01"')
assert p1_start != -1, "view-project-01 not found"
p2_start = html.find('id="view-project-02"')
assert p2_start != -1, "view-project-02 not found"

sec1 = html[p1_start:p2_start]

# 1. Enlarge Photo 3 while keeping text beside it
photo3_pat = r'<!-- 4\. PHOTO 03 : TROIS CONFIGURATIONS EN GRAND AVEC TEXTE RÉDUIT -->.*?</div>\s*</div>\s*(?=<!-- 5\. Universal Next Project Teaser)'
m3 = re.search(photo3_pat, sec1, re.DOTALL)
assert m3 is not None, "Photo 3 block not found in sec1"

# Extract existing b64 for photo 3
p3_chunk = m3.group(0)
img3_m = re.search(r'src="(data:image/webp;base64,[^"]+)"', p3_chunk)
assert img3_m is not None, "b64 for photo 3 not found"
b64_img3 = img3_m.group(1)

enlarged_photo3_block = f"""<!-- 4. PHOTO 03 : TROIS CONFIGURATIONS EN TRÈS GRAND FORMAT AVEC TEXTE À CÔTÉ -->
      <div class="gallery-spaced-pair photo-with-side-text" style="grid-template-columns: 0.8fr 2.2fr; gap: clamp(36px, 6vw, 90px); align-items: center; max-width: 1600px; margin: clamp(60px, 8vw, 120px) auto; padding: 0 clamp(16px, 4vw, 48px);">
        <!-- Texte explicatif à gauche (compact & élégant) -->
        <div class="photo-side-text-col" style="display: flex; flex-direction: column; justify-content: center; max-width: 380px; justify-self: end;">
          <div style="font-size: clamp(13px, 1.05vw, 15px); line-height: 1.75; font-weight: 300; color: #d0d0d0;">
            <p style="margin: 0; padding: 0; color: #d0d0d0;">
              Un même ensemble de pièces permet de composer trois configurations de chaise. Déclinable en plusieurs coloris, le projet offre différentes possibilités pour s’adapter aux intérieurs et aux préférences de chacun. La chaise devient un mobilier évolutif, avec lequel on retrouve le plaisir de jouer à l’âge adulte.
            </p>
          </div>
        </div>
        <!-- Photo 03 à droite (très grand format dominant) -->
        <div class="white-image-box has-image chair-trans-box" style="aspect-ratio: 4/5; max-height: 98vh; width: 100%; background: transparent !important; background-color: transparent !important; box-shadow: none !important; border: none !important; display: flex; align-items: center; justify-content: center;">
          <img src="{b64_img3}" alt="Fog Chair Modèle 001 - Trio de chaises en équilibre (Tangerine, Vert Acide, Magenta) sans fond" style="position: static !important; max-width: 100%; max-height: 98vh; width: 100%; height: auto; object-fit: contain; filter: drop-shadow(0 35px 70px rgba(0, 0, 0, 0.95));">
        </div>
      </div>
"""

# 2. Base64 for conception photos 1 to 5
b64_c = {}
for i in range(1, 6):
    wpath = os.path.join(webp_dir, f'{i}.webp')
    assert os.path.exists(wpath), f"Webp file not found: {wpath}"
    with open(wpath, 'rb') as fp:
        b64_c[i] = f"data:image/webp;base64,{base64.b64encode(fp.read()).decode('ascii')}"

conception_section_html = f"""
      <!-- 5. SECTION CONCEPTION : RECHERCHES, MAQUETTES & PROCESSUS (PHOTOS 01 À 05 DU DOSSIER 1) -->
      <div class="project-conception-section" style="margin-top: clamp(80px, 10vw, 150px); margin-bottom: clamp(60px, 8vw, 120px); max-width: 1440px; margin-left: auto; margin-right: auto; padding: 0 clamp(16px, 4vw, 48px);">
        <!-- En-tête de la section Conception -->
        <div style="border-top: 1px solid rgba(255, 255, 255, 0.12); padding-top: clamp(40px, 5vw, 64px); margin-bottom: clamp(40px, 5vw, 64px);">
          <div style="display: flex; align-items: center; gap: 10px; font-size: 11px; font-weight: 900; letter-spacing: 0.22em; text-transform: uppercase; color: #888888; margin-bottom: 12px;">
            <span style="width: 8px; height: 8px; border-radius: 2px; background: rgba(255, 255, 255, 0.6);"></span>
            <span>01 // PROCESSUS &amp; RECHERCHES</span>
          </div>
          <h2 style="font-size: clamp(28px, 3.2vw, 46px); font-weight: 900; letter-spacing: -0.02em; color: #ffffff; margin: 0 0 14px 0; line-height: 1.1;">
            Conception
          </h2>
          <p style="font-size: clamp(14px, 1.15vw, 17px); font-weight: 300; line-height: 1.65; color: #bbbbbb; max-width: 720px; margin: 0;">
            Recherches de formes, exploration des principes d’assemblage et maquettes d’atelier. Décomposition des modules et expérimentation de la modularité à l'échelle.
          </p>
        </div>

        <!-- Rangée 1 : Photos 01 & 02 en duo horizontal -->
        <div class="gallery-spaced-pair equal conception-pair" style="grid-template-columns: 1fr 1fr; gap: clamp(20px, 3vw, 40px); margin-top: 0; margin-bottom: clamp(20px, 3vw, 40px);">
          <div class="white-image-box has-image" style="aspect-ratio: 1886/1375; background-color: #121214;">
            <img src="{b64_c[1]}" alt="Conception Fog Chair - Exploration maquette 01" loading="lazy" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <div class="white-image-box has-image" style="aspect-ratio: 1780/1324; background-color: #121214;">
            <img src="{b64_c[2]}" alt="Conception Fog Chair - Exploration maquette 02" loading="lazy" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
        </div>

        <!-- Rangée 2 : Photos 03, 04 & 05 (03 et 04 empilées à gauche, 05 portrait plein format à droite) -->
        <div class="gallery-spaced-pair equal conception-pair" style="grid-template-columns: 1fr 1fr; gap: clamp(20px, 3vw, 40px); align-items: stretch; margin-top: 0; margin-bottom: 0;">
          <div style="display: flex; flex-direction: column; gap: clamp(20px, 3vw, 40px); justify-content: space-between;">
            <div class="white-image-box has-image" style="aspect-ratio: 2056/1525; background-color: #121214;">
              <img src="{b64_c[3]}" alt="Conception Fog Chair - Exploration maquette 03" loading="lazy" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            <div class="white-image-box has-image" style="aspect-ratio: 2089/1504; background-color: #121214;">
              <img src="{b64_c[4]}" alt="Conception Fog Chair - Exploration maquette 04" loading="lazy" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
          </div>
          <div class="white-image-box has-image" style="aspect-ratio: 1399/2218; height: 100%; background-color: #121214;">
            <img src="{b64_c[5]}" alt="Conception Fog Chair - Exploration maquette 05" loading="lazy" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
        </div>
      </div>

"""

updated_sec1 = sec1[:m3.start()] + enlarged_photo3_block + conception_section_html + sec1[m3.end():]
html = html[:p1_start] + updated_sec1 + html[p2_start:]

# 3. Add responsive style for conception-pair
conception_responsive_css = """    @media (max-width: 860px) {
      .conception-pair {
        grid-template-columns: 1fr !important;
      }
    }
"""
if '.conception-pair' not in html:
    style_end = html.find('</style>')
    assert style_end != -1, "</style> not found"
    html = html[:style_end] + conception_responsive_css + html[style_end:]
    print("Added responsive CSS for conception-pair.")

# 4. Save and copy
assert html.strip().endswith('</html>'), "HTML does not end with </html>"
print(f"Updated standalone.html size: {len(html):,} chars")

with open(standalone_path, 'w', encoding='utf-8') as fp:
    fp.write(html)
print("Saved standalone.html successfully.")

if os.path.exists(os.path.dirname(portfolio_artifact_path)):
    shutil.copyfile(standalone_path, portfolio_artifact_path)
    print(f"Copied to artifact {portfolio_artifact_path} ({os.path.getsize(portfolio_artifact_path):,} bytes)")

