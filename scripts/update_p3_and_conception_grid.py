import os
import shutil
import base64
import re

standalone_path = 'standalone.html'
portfolio_artifact_path = '/Users/morganjanot/Documents/antigravity/agitated-davinci/portfolio.html'
portfolio_brain_path = '/Users/morganjanot/.gemini/antigravity/brain/df18ad40-ac30-4b7a-b04f-f3de4961c66b/portfolio.html'
webp_dir = 'src/assets/images_webp/project-01'

with open(standalone_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS rules to <style>
new_css = """    /* Photo 3 Giant & Conception Unified Grid with strictly uniform gaps */
    .p3-giant-wrapper {
      max-width: 1750px !important;
      width: 96% !important;
      grid-template-columns: minmax(260px, 320px) 1fr !important;
      gap: clamp(40px, 6vw, 100px) !important;
      align-items: center !important;
      margin: clamp(80px, 10vw, 160px) auto !important;
    }
    .p3-giant-box {
      width: 100% !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
    }
    .p3-giant-box img {
      width: 100% !important;
      max-width: 1250px !important;
      height: auto !important;
      max-height: 110vh !important;
      object-fit: contain !important;
      filter: drop-shadow(0 40px 85px rgba(0, 0, 0, 0.96)) !important;
    }
    .conception-unified-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: clamp(18px, 2.2vw, 32px);
      align-items: stretch;
    }
    .conception-unified-grid .conception-card-std {
      aspect-ratio: 4 / 3;
      width: 100%;
      height: 100%;
      border-radius: 4px;
      overflow: hidden;
      background-color: #121214;
      border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .conception-unified-grid .conception-card-tall {
      grid-column: 3;
      grid-row: 1 / span 2;
      width: 100%;
      height: 100%;
      border-radius: 4px;
      overflow: hidden;
      background-color: #121214;
      border: 1px solid rgba(255, 255, 255, 0.1);
    }
    @media (max-width: 860px) {
      .p3-giant-wrapper {
        grid-template-columns: 1fr !important;
      }
      .conception-unified-grid {
        grid-template-columns: 1fr !important;
      }
      .conception-unified-grid .conception-card-tall {
        grid-column: 1 !important;
        grid-row: auto !important;
        aspect-ratio: 4 / 5 !important;
      }
    }
"""

if '/* Photo 3 Giant & Conception Unified Grid' not in html:
    style_end = html.find('</style>')
    assert style_end != -1, "</style> not found"
    html = html[:style_end] + new_css + html[style_end:]
    print("Added CSS for Photo 3 giant & Conception unified grid.")

# 2. Update view-project-01
p1_start = html.find('id="view-project-01"')
assert p1_start != -1, "view-project-01 not found"
p2_start = html.find('id="view-project-02"')
assert p2_start != -1, "view-project-02 not found"

sec1 = html[p1_start:p2_start]

# Base64 data from disk
def b64_file(name):
    p = os.path.join(webp_dir, name)
    assert os.path.exists(p), f"File not found: {p}"
    with open(p, 'rb') as fp:
        return f"data:image/webp;base64,{base64.b64encode(fp.read()).decode('ascii')}"

b64_img3 = b64_file('13.webp')
b64_c = {i: b64_file(f'{i}.webp') for i in range(1, 6)}

# Find chunk from photo 3 up to Universal Next Project Teaser Footer
chunk_pat = r'<!-- 4\. PHOTO 03 : TROIS CONFIGURATIONS.*?(?=<!-- 5\. Universal Next Project Teaser)'
m_chunk = re.search(chunk_pat, sec1, re.DOTALL)
assert m_chunk is not None, "Target chunk not found in sec1"

new_chunk = f"""<!-- 4. PHOTO 03 : TROIS CONFIGURATIONS EN FORMAT GÉANT AVEC TEXTE À CÔTÉ -->
      <div class="gallery-spaced-pair photo-with-side-text p3-giant-wrapper">
        <!-- Texte explicatif à gauche (compact & élégant) -->
        <div class="photo-side-text-col" style="display: flex; flex-direction: column; justify-content: center; max-width: 320px; justify-self: end;">
          <div style="font-size: clamp(13px, 1.05vw, 15px); line-height: 1.8; font-weight: 300; color: #d0d0d0;">
            <p style="margin: 0; padding: 0; color: #d0d0d0;">
              Un même ensemble de pièces permet de composer trois configurations de chaise. Déclinable en plusieurs coloris, le projet offre différentes possibilités pour s’adapter aux intérieurs et aux préférences de chacun. La chaise devient un mobilier évolutif, avec lequel on retrouve le plaisir de jouer à l’âge adulte.
            </p>
          </div>
        </div>
        <!-- Photo 03 à droite (format géant pleine colonne sans contrainte d'aspect-ratio) -->
        <div class="white-image-box has-image chair-trans-box p3-giant-box" style="background: transparent !important; background-color: transparent !important; box-shadow: none !important; border: none !important;">
          <img src="{b64_img3}" alt="Fog Chair Modèle 001 - Trio de chaises en équilibre (Tangerine, Vert Acide, Magenta) sans fond" loading="lazy">
        </div>
      </div>

      <!-- 5. SECTION CONCEPTION : RECHERCHES & MAQUETTES (PHOTOS 01 À 05 - ÉCARTS PARFAITEMENT UNIFORMES) -->
      <div class="project-conception-section" style="margin-top: clamp(80px, 10vw, 150px); margin-bottom: clamp(60px, 8vw, 120px); max-width: 1440px; margin-left: auto; margin-right: auto; padding: 0 clamp(16px, 4vw, 48px);">
        <!-- En-tête de section Conception -->
        <div style="border-top: 1px solid rgba(255, 255, 255, 0.12); padding-top: clamp(40px, 5vw, 64px); margin-bottom: clamp(36px, 4.5vw, 56px);">
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

        <!-- Grille Conception Unifiée : 3 colonnes, 2 rangées, écarts strictement identiques partout -->
        <div class="conception-unified-grid">
          <!-- Col 1, Row 1 : Photo 1 -->
          <div class="white-image-box has-image conception-card-std">
            <img src="{b64_c[1]}" alt="Conception Fog Chair - Exploration maquette 01" loading="lazy" style="width: 100%; height: 100%; object-fit: cover;">
          </div>

          <!-- Col 2, Row 1 : Photo 2 -->
          <div class="white-image-box has-image conception-card-std">
            <img src="{b64_c[2]}" alt="Conception Fog Chair - Exploration maquette 02" loading="lazy" style="width: 100%; height: 100%; object-fit: cover;">
          </div>

          <!-- Col 3, Row 1-2 : Photo 5 (Portrait pleine hauteur, alignée au millimètre sur les deux rangées) -->
          <div class="white-image-box has-image conception-card-tall">
            <img src="{b64_c[5]}" alt="Conception Fog Chair - Exploration maquette 05" loading="lazy" style="width: 100%; height: 100%; object-fit: cover;">
          </div>

          <!-- Col 1, Row 2 : Photo 3 -->
          <div class="white-image-box has-image conception-card-std">
            <img src="{b64_c[3]}" alt="Conception Fog Chair - Exploration maquette 03" loading="lazy" style="width: 100%; height: 100%; object-fit: cover;">
          </div>

          <!-- Col 2, Row 2 : Photo 4 -->
          <div class="white-image-box has-image conception-card-std">
            <img src="{b64_c[4]}" alt="Conception Fog Chair - Exploration maquette 04" loading="lazy" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
        </div>
      </div>

      """

updated_sec1 = sec1[:m_chunk.start()] + new_chunk + sec1[m_chunk.end():]
html = html[:p1_start] + updated_sec1 + html[p2_start:]

assert html.strip().endswith('</html>'), "HTML structure compromised"
print(f"Updated standalone.html size: {len(html):,} chars")

with open(standalone_path, 'w', encoding='utf-8') as fp:
    fp.write(html)
print("Saved standalone.html successfully.")

for dest in [portfolio_brain_path, portfolio_artifact_path]:
    if os.path.exists(os.path.dirname(dest)):
        shutil.copyfile(standalone_path, dest)
        print(f"Copied to {dest} ({os.path.getsize(dest):,} bytes)")

