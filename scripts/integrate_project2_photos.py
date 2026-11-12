import re
import base64
import os

standalone_path = "/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/standalone.html"
portfolio_path = "/Users/morganjanot/.gemini/antigravity/brain/04838ef3-4249-4209-97cb-1440ffec4bcd/portfolio.html"

def get_b64(path, mime):
    with open(path, "rb") as f:
        data = f.read()
    b64_str = base64.b64encode(data).decode('utf-8')
    return f"data:{mime};base64,{b64_str}"

# Project 2 images
img_concrete_base = get_b64("/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/public/images/project-02/lamp-concrete-base-full-16-9.jpg", "image/jpeg")
img_upper_articulation = get_b64("/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/public/images/project-02/lamp-upper-articulation-16-9.png", "image/png")
img_joint_closeup = get_b64("/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/public/images/project-02/lamp-joint-closeup-16-9.jpg", "image/jpeg")
img_cube_connector = get_b64("/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/public/images/project-02/lamp-cube-connector-16-9.jpg", "image/jpeg")
img_ball_joint = get_b64("/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/public/images/project-02/lamp-usm-ball-joint-portrait-3-4.webp", "image/webp")

# Project 1 images
img_floating = get_b64("/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/public/images/project-01/fog-chair-floating-16-9.png", "image/png")
img_portrait = get_b64("/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/public/images/project-01/fog-chair-standing-portrait-3-4.png", "image/png")
img_stack = get_b64("/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/public/images/project-01/fog-chair-stacked-square-1-1.jpg", "image/jpeg")
img_poster = get_b64("/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/public/images/project-01/fog-chair-poster-manifesto.png", "image/png")

print("All base64 images prepared successfully.")

with open(standalone_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Project 01 Name on homepage card, drawer, sticky title, palette
html = html.replace('<h2 class="frame-title">Fauteuil Nuage</h2>', '<h2 class="frame-title">Fog Chair</h2>')
html = html.replace('aria-label="01 — Fauteuil Nuage: Mobilier éditorial"', 'aria-label="01 — Fog Chair: Mobilier éditorial"')
html = html.replace('<span class="drawer-project-name">Fauteuil Nuage</span>', '<span class="drawer-project-name">Fog Chair</span>')
html = html.replace("'project-01': 'Fauteuil Nuage'", "'project-01': 'Fog Chair'")
html = html.replace('title="01 — Vert Acide (Fauteuil Nuage)"', 'title="01 — Vert Acide (Fog Chair)"')
html = html.replace('Projet Suivant &bull; 01\n            </div>\n            <div style="font-size: clamp(18px, 1.8vw, 24px); font-weight: 900; color: #ffffff;">\n              Fauteuil Nuage', 'Projet Suivant &bull; 01\n            </div>\n            <div style="font-size: clamp(18px, 1.8vw, 24px); font-weight: 900; color: #ffffff;">\n              Fog Chair')

# 2. In Project 01, remove the little rectangles (caption pills & crosshairs on photos)
clean_p1_images_html = f"""      <!-- 2. GRANDE IMAGE PLEIN ÉCRAN : FORMAT 16/9 SANS PETITS RECTANGLES SUR LA PHOTO -->
      <div class="full-screen-image-block">
        <div class="white-image-box has-image" style="aspect-ratio: 16/9; max-height: 80vh;">
          <img src="{img_floating}" alt="Fog Chair Modèle 001 vue tridimensionnelle en suspension dans l'espace" loading="lazy" />
        </div>
      </div>

      <!-- 3. IMAGES PLUS PETITES ET ESPACÉES : FORMAT PORTRAIT 3/4 & CARRÉ 1/1 SANS RECTANGLES -->
      <div class="gallery-spaced-pair" style="grid-template-columns: 1fr 1.15fr; gap: clamp(36px, 5.5vw, 80px); align-items: stretch;">
        <!-- Photo 2 : Format Portrait 3/4 adapté (786 x 1024) -->
        <div class="white-image-box has-image" style="aspect-ratio: 786/1024;">
          <img src="{img_portrait}" alt="Fog Chair Modèle 001 vue en élévation trois-quarts" loading="lazy" />
        </div>

        <!-- Photo 3 : Format Carré 1/1 adapté (1024 x 1024) -->
        <div class="white-image-box has-image" style="aspect-ratio: 1/1;">
          <img src="{img_stack}" alt="Fog Chair Modèle 001 trio de chaises en équilibre acrobatique" loading="lazy" />
        </div>
      </div>

      <!-- 4. PLANCHE MANIFESTE CENTRÉE : FORMAT AFFICHE (842 x 595) SANS RECTANGLE -->
      <div class="gallery-centered-small" style="max-width: 980px; margin-top: clamp(60px, 8vw, 120px); margin-bottom: clamp(60px, 8vw, 120px);">
        <div class="white-image-box has-image" style="aspect-ratio: 842/595;">
          <img src="{img_poster}" alt="Planche manifeste Fog Chair C001 Model-001" loading="lazy" />
        </div>
      </div>"""

# Replace in project 01
p1_start = html.find("id=\"view-project-01\"")
p2_start = html.find("id=\"view-project-02\"")
p1_chunk = html[p1_start:p2_start]

# Find where section 2 starts in p1
p1_sec2 = p1_chunk.find("<!-- 2. GRANDE IMAGE PLEIN ÉCRAN")
p1_sec5 = p1_chunk.find("<!-- 5. Universal Next Project Teaser Footer -->")
if p1_sec2 != -1 and p1_sec5 != -1:
    new_p1_chunk = p1_chunk[:p1_sec2] + clean_p1_images_html + "\n\n      " + p1_chunk[p1_sec5:]
    html = html[:p1_start] + new_p1_chunk + html[p2_start:]
    print("Project 01 photos cleaned: removed little overlay rectangles.")

# 3. Now let's extract Project 02 SVG
p2_start = html.find("id=\"view-project-02\"")
p3_start = html.find("id=\"view-project-03\"")
p2_chunk = html[p2_start:p3_start]
svg_p2_match = re.search(r"(<div class=\"frame-illustration\">[\s\S]*?</div>)", p2_chunk)
if not svg_p2_match:
    raise Exception("Project 02 SVG not found!")
svg_p2 = svg_p2_match.group(1).strip()

# Build the bespoke Project 02 section with the 5 photos, adapted sizes, and NO little rectangles on photos
new_project_02 = f"""    <!-- VIEW DETAIL: PROJET 02 (LAMPADAIRE ARTICULÉ) -->
    <section id="view-project-02" class="view-panel project-detail-section">
      <!-- Top Navigation Bar -->
      <div class="project-header-bar">
        <button type="button" class="project-nav-btn btn-back-portfolio" data-target="portfolio">
          <span aria-hidden="true">&larr;</span>
          <span class="link-line">Retourner au portfolio</span>
        </button>
        <div class="project-counter-pill">PROJET [ 02 / 06 ]</div>
        <div class="project-nav-arrows">
          <button type="button" class="project-nav-btn prev btn-switch-project" data-target-project="project-01" aria-label="Projet précédent">
            <span aria-hidden="true">&larr;</span>
            <span>Précédent</span>
          </button>
          <button type="button" class="project-nav-btn next btn-switch-project" data-target-project="project-03" aria-label="Projet suivant">
            <span>Suivant</span>
            <span aria-hidden="true">&rarr;</span>
          </button>
        </div>
      </div>

      <!-- 1. HERO DUAL ROW : CARTE COULEUR & TEXTE EXPLICATIF CÔTE À CÔTE -->
      <div class="project-hero-dual reverse-side">
        <!-- Carte Couleur Signature avec Texture Papier -->
        <div class="hero-card-col">
          <div class="project-art-frame" style="background-color: rgb(255, 0, 127); aspect-ratio: 9/16; min-height: 480px;">
            {svg_p2}
            <div class="project-detail-cartouche">
              <div class="detail-cartouche-tag">02 — Cinétique &amp; Lumière // Studio</div>
              <h2 class="detail-cartouche-title">* LAMPADAIRE ARTICULÉ *</h2>
              <div class="detail-cartouche-meta">
                <span>ROTULES GÉOMÉTRIQUES &amp; SOCLE BÉTON</span>
                <span style="font-size: 13px;">*</span>
                <span>CYBER MAGENTA</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Texte Explicatif : Base du projet, pourquoi & specs -->
        <div class="hero-text-col">
          <div class="editorial-tag-row" style="margin-bottom: 16px;">
            <span class="editorial-tag">02 // Design d'Espace &bull; Luminaire Cinétique</span>
            <span class="chroma-badge" style="background: rgba(255, 0, 127, 0.15); color: #ff55a3; border: 1px solid rgba(255, 0, 127, 0.4);">
              * BÉTON BRUT &amp; ACIER ARTICULÉ *
            </span>
          </div>

          <h1 class="hero-concept-title">Lampadaire Articulé</h1>
          <p class="hero-concept-thesis">
            Un système d'éclairage cinétique né du dialogue entre la masse brute du béton, la finesse des profilés chromés et la tension graphique d'un câble orange.
          </p>

          <div class="hero-narrative-card">
            <div class="narrative-header">
              <span class="narrative-dot" style="background: rgb(255, 0, 127);"></span>
              <span>GENÈSE &amp; BASE DU PROJET</span>
            </div>
            <div class="narrative-body">
              <p>
                Pourquoi ce projet ? Ce lampadaire explore la liberté de mouvement dans l'espace habité. Plutôt qu'un luminaire figé, il est pensé comme une grue cinétique légère : un piétement ancré dans un bloc de béton brut, relié à des segments tubulaires télescopiques orientables grâce à des connecteurs géométriques usinés.
              </p>
              <p>
                Le câble électrique orange vif n'est pas dissimulé : il traverse les articulations via des anneaux de guidage et devient un élément graphique majeur, traçant une onde colorée dans l'espace qui contraste avec l'épure métallique et la rugosité minérale du socle.
              </p>
            </div>
          </div>

          <!-- Fiche technique atelier épurée -->
          <div class="project-specs-bar" style="margin-bottom: 0;">
            <span>Socle : <span class="spec-val">Bloc béton brut coulé à la main</span></span>
            <span class="spec-sep">&bull;</span>
            <span>Structure : <span class="spec-val">Acier chromé &amp; connecteurs usinés</span></span>
            <span class="spec-sep">&bull;</span>
            <span>Câblage : <span class="spec-val">Câble gainé orange haute flexibilité</span></span>
            <span class="spec-sep">&bull;</span>
            <span>Articulations : <span class="spec-val">Rotules géométriques multidirectionnelles</span></span>
          </div>
        </div>
      </div>

      <!-- 2. GRANDE IMAGE PLEIN ÉCRAN : SOCLE BÉTON & ÉLÉVATION COMPLÈTE (16:9) -->
      <div class="full-screen-image-block">
        <div class="white-image-box has-image" style="aspect-ratio: 16/9; max-height: 80vh;">
          <img src="{img_concrete_base}" alt="Lampadaire articulé avec socle en béton brut et câble orange" loading="lazy" />
        </div>
      </div>

      <!-- 3. DUO ASYMÉTRIQUE ESPACÉ : ROTULE SPHÉRIQUE PORTRAIT 3/4 & BRAS ARTICULÉ 16/9 -->
      <div class="gallery-spaced-pair" style="grid-template-columns: 1fr 1.35fr; gap: clamp(36px, 5.5vw, 80px); align-items: center;">
        <!-- Photo 2 : Gros plan connecteur sphérique chrome en format Portrait 3/4 (768 x 1024) -->
        <div class="white-image-box has-image" style="aspect-ratio: 768/1024;">
          <img src="{img_ball_joint}" alt="Détail macro rotule sphérique chromée usinée" loading="lazy" />
        </div>

        <!-- Photo 3 : Bras supérieur articulé et câble orange en format 16/9 (1024 x 576) -->
        <div class="white-image-box has-image" style="aspect-ratio: 16/9;">
          <img src="{img_upper_articulation}" alt="Bras articulé télescopique et passage de câble orange" loading="lazy" />
        </div>
      </div>

      <!-- 4. DUO GÉOMÉTRIQUE D'ATELIER : DÉTAIL ROTULE FACETTÉE & DÉ CONNECTEUR (16/9) -->
      <div class="gallery-spaced-pair equal" style="margin-top: clamp(60px, 8vw, 120px); margin-bottom: clamp(60px, 8vw, 120px);">
        <!-- Photo 4 : Gros plan rotule à facettes et guide-câble (1024 x 571) -->
        <div class="white-image-box has-image" style="aspect-ratio: 16/9;">
          <img src="{img_joint_closeup}" alt="Gros plan sur la rotule à facettes et l'anneau passe-câble" loading="lazy" />
        </div>

        <!-- Photo 5 : Le cube connecteur à facettes usiné isolé (1024 x 576) -->
        <div class="white-image-box has-image" style="aspect-ratio: 16/9;">
          <img src="{img_cube_connector}" alt="Cube connecteur géométrique à facettes usiné avec filetages" loading="lazy" />
        </div>
      </div>

      <!-- 5. Universal Next Project Teaser Footer -->
      <div class="project-footer-card" style="margin-top: clamp(80px, 10vw, 150px);">
        <div class="next-teaser-info">
          <div class="next-teaser-swatch" style="background-color: rgb(0, 240, 255);"></div>
          <div>
            <div style="font-size: 11px; font-weight: 900; letter-spacing: 0.2em; text-transform: uppercase; color: #888888; margin-bottom: 4px;">
              Projet Suivant &bull; 03
            </div>
            <div style="font-size: clamp(18px, 1.8vw, 24px); font-weight: 900; color: #ffffff;">
              Chaise Suspendue
            </div>
          </div>
        </div>
        <button type="button" class="project-nav-btn next btn-switch-project" data-target-project="project-03" style="font-size: 13px;">
          <span>Découvrir la pièce</span>
          <span aria-hidden="true">&rarr;</span>
        </button>
      </div>
    </section>
"""

# Replace project 02 in standalone.html
p2_start = html.find("id=\"view-project-02\"")
p3_start = html.find("id=\"view-project-03\"")
sec_p2_start = html.rfind("<section", 0, p2_start)
sec_p2_end = html.find("</section>", p2_start) + len("</section>")

html = html[:sec_p2_start] + new_project_02.strip() + "\n\n    " + html[sec_p2_end:]

with open(standalone_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Updated standalone.html! New size: {len(html)}")

with open(portfolio_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Updated portfolio.html! New size: {len(html)}")
