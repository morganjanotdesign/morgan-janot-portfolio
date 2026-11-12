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

# Base64 data from disk
def b64_file(name):
    p = os.path.join(webp_dir, name)
    assert os.path.exists(p), f"File not found: {p}"
    with open(p, 'rb') as fp:
        return f"data:image/webp;base64,{base64.b64encode(fp.read()).decode('ascii')}"

b64_img3 = b64_file('13.webp')
b64_c = {i: b64_file(f'{i}.webp') for i in range(1, 6)}

# 1. Update CSS in <style>
# Remove previous .p3-giant and .conception-unified-grid if present, and replace with clean rock-solid rules
css_block = """    /* Photo 3 & Conception 3-column perfect-gap layout */
    .p3-side-layout {
      display: grid !important;
      grid-template-columns: minmax(220px, 280px) 1fr !important;
      gap: clamp(32px, 5vw, 80px) !important;
      align-items: center !important;
      max-width: 1650px !important;
      width: 95% !important;
      margin: clamp(60px, 8vw, 120px) auto !important;
      padding: 0 clamp(16px, 4vw, 48px) !important;
    }
    .p3-side-img-box {
      width: 100% !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
    }
    .p3-side-img-box img {
      position: static !important;
      width: 100% !important;
      max-width: 1200px !important;
      height: auto !important;
      max-height: 96vh !important;
      object-fit: contain !important;
      filter: drop-shadow(0 35px 75px rgba(0, 0, 0, 0.96)) !important;
      display: block !important;
    }
    .conception-fixed-gap-grid {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: clamp(16px, 2vw, 24px);
      align-items: stretch;
      max-width: 1440px;
      margin: 0 auto;
    }
    .conception-fixed-gap-grid .conception-col {
      display: flex;
      flex-direction: column;
      gap: clamp(16px, 2vw, 24px);
    }
    .conception-fixed-gap-grid .conception-thumb {
      width: 100%;
      border-radius: 4px;
      overflow: hidden;
      background-color: #121214;
      border: 1px solid rgba(255, 255, 255, 0.1);
      position: relative;
    }
    .conception-fixed-gap-grid .conception-thumb.aspect-4-3 {
      aspect-ratio: 4 / 3;
    }
    .conception-fixed-gap-grid .conception-thumb.tall-fill {
      height: 100%;
    }
    .conception-fixed-gap-grid .conception-thumb img {
      position: static !important;
      width: 100% !important;
      height: 100% !important;
      object-fit: cover !important;
      display: block !important;
      transition: transform 0.5s ease !important;
    }
    .conception-fixed-gap-grid .conception-thumb:hover img {
      transform: scale(1.035) !important;
    }
    @media (max-width: 800px) {
      .p3-side-layout {
        grid-template-columns: 1fr !important;
      }
      .conception-fixed-gap-grid {
        grid-template-columns: 1fr !important;
      }
      .conception-fixed-gap-grid .conception-thumb.tall-fill {
        aspect-ratio: 4 / 5 !important;
        height: auto !important;
      }
    }
"""

# Replace old css if present
old_css_pat = r'/\* Photo 3 Giant & Conception Unified Grid.*?(?=</style>)'
if re.search(old_css_pat, html, re.DOTALL):
    html = re.sub(old_css_pat, css_block.strip() + '\n', html, flags=re.DOTALL)
    print("Replaced existing Photo 3 & Conception CSS.")
else:
    style_end = html.find('</style>')
    assert style_end != -1, "</style> not found"
    html = html[:style_end] + css_block + html[style_end:]
    print("Appended new Photo 3 & Conception CSS.")

# 2. Update view-project-01
p1_start = html.find('id="view-project-01"')
assert p1_start != -1, "view-project-01 not found"
p2_start = html.find('id="view-project-02"')
assert p2_start != -1, "view-project-02 not found"

sec1 = html[p1_start:p2_start]

# Find chunk from photo 3 up to Universal Next Project Teaser Footer
chunk_pat = r'<!-- 4\. PHOTO 03 : TROIS CONFIGURATIONS.*?(?=<!-- 5\. Universal Next Project Teaser)'
m_chunk = re.search(chunk_pat, sec1, re.DOTALL)
assert m_chunk is not None, "Target chunk not found in sec1"

new_chunk = f"""<!-- 4. PHOTO 03 : TROIS CONFIGURATIONS EN FORMAT GÉANT AVEC TEXTE À CÔTÉ -->
      <div class="gallery-spaced-pair photo-with-side-text p3-side-layout">
        <!-- Texte explicatif à gauche (compact, épuré) -->
        <div class="photo-side-text-col" style="display: flex; flex-direction: column; justify-content: center; max-width: 280px;">
          <div style="font-size: 13px; line-height: 1.75; font-weight: 300; color: #c0c0c0;">
            <p style="margin: 0; padding: 0; color: #c0c0c0;">
              Un même ensemble de pièces permet de composer trois configurations de chaise. Déclinable en plusieurs coloris, le projet offre différentes possibilités pour s’adapter aux intérieurs et aux préférences de chacun. La chaise devient un mobilier évolutif, avec lequel on retrouve le plaisir de jouer à l’âge adulte.
            </p>
          </div>
        </div>
        <!-- Photo 03 à droite (grand format sans fond) -->
        <div class="p3-side-img-box">
          <img src="{b64_img3}" alt="Fog Chair Modèle 001 - Trio de chaises en équilibre (Tangerine, Vert Acide, Magenta) sans fond" loading="lazy">
        </div>
      </div>

      <!-- 5. SECTION CONCEPTION : RECHERCHES & MAQUETTES (PHOTOS 01 À 05 - ÉCARTS PARFAITEMENT IDENTIQUES PARTOUT) -->
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

        <!-- Grille Conception Unifiée : Écarts strictement identiques verticalement et horizontalement -->
        <div class="conception-fixed-gap-grid">
          <!-- Colonne 1 : Photos 01 & 03 -->
          <div class="conception-col">
            <div class="conception-thumb aspect-4-3">
              <img src="{b64_c[1]}" alt="Conception Fog Chair - Exploration maquette 01" loading="lazy">
            </div>
            <div class="conception-thumb aspect-4-3">
              <img src="{b64_c[3]}" alt="Conception Fog Chair - Exploration maquette 03" loading="lazy">
            </div>
          </div>

          <!-- Colonne 2 : Photos 02 & 04 -->
          <div class="conception-col">
            <div class="conception-thumb aspect-4-3">
              <img src="{b64_c[2]}" alt="Conception Fog Chair - Exploration maquette 02" loading="lazy">
            </div>
            <div class="conception-thumb aspect-4-3">
              <img src="{b64_c[4]}" alt="Conception Fog Chair - Exploration maquette 04" loading="lazy">
            </div>
          </div>

          <!-- Colonne 3 : Photo 05 (Portrait pleine hauteur, aligné sur les 2 rangées) -->
          <div class="conception-thumb tall-fill">
            <img src="{b64_c[5]}" alt="Conception Fog Chair - Exploration maquette 05" loading="lazy">
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

