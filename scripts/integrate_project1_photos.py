import re
import base64
import os

standalone_path = "/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/standalone.html"
portfolio_path = "/Users/morganjanot/.gemini/antigravity/brain/04838ef3-4249-4209-97cb-1440ffec4bcd/portfolio.html"

# Load image data as base64
def get_b64(path, mime):
    with open(path, "rb") as f:
        data = f.read()
    b64_str = base64.b64encode(data).decode('utf-8')
    return f"data:{mime};base64,{b64_str}"

img_floating = get_b64("/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/public/images/project-01/fog-chair-floating-16-9.png", "image/png")
img_portrait = get_b64("/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/public/images/project-01/fog-chair-standing-portrait-3-4.png", "image/png")
img_stack = get_b64("/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/public/images/project-01/fog-chair-stacked-square-1-1.jpg", "image/jpeg")
img_poster = get_b64("/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/public/images/project-01/fog-chair-poster-manifesto.png", "image/png")

print(f"Loaded base64 for 4 images: lengths = {[len(img_floating), len(img_portrait), len(img_stack), len(img_poster)]}")

# Read standalone.html
with open(standalone_path, "r", encoding="utf-8") as f:
    html = f.read()

# Add CSS for has-image and image-caption-pill if not present
extra_css = """
    /* =============================================================
       PHOTO INTEGRATION & BESPOKE ADAPTED CASES
       ============================================================= */
    .white-image-box.has-image {
      padding: 0;
      background-color: #f7f7f7;
    }

    .white-image-box.has-image img {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      z-index: 10;
      transition: transform 600ms cubic-bezier(0.16, 1, 0.3, 1);
    }

    .white-image-box.has-image:hover img {
      transform: scale(1.025);
    }

    .image-caption-pill {
      position: absolute;
      bottom: clamp(14px, 2vw, 22px);
      left: clamp(14px, 2vw, 22px);
      z-index: 20;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(12px);
      padding: 8px 16px;
      border-radius: 2px;
      border: 1px solid rgba(255, 255, 255, 0.18);
      color: #ffffff;
      display: flex;
      flex-direction: column;
      gap: 2px;
      pointer-events: none;
      transition: transform 380ms ease, opacity 380ms ease, background 380ms ease;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.45);
    }

    .white-image-box.has-image:hover .image-caption-pill {
      background: rgba(0, 0, 0, 0.95);
      border-color: rgba(255, 255, 255, 0.4);
      transform: translateY(-2px);
    }

    .caption-tag {
      font-size: 9px;
      font-weight: 900;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: #ccff00;
    }

    .caption-title {
      font-size: clamp(11px, 1.1vw, 13px);
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: #ffffff;
    }
"""

if ".white-image-box.has-image" not in html:
    css_insert_target = ".project-detail-section {"
    pos_css = html.find(css_insert_target)
    if pos_css != -1:
        html = html[:pos_css] + extra_css + "\n    " + html[pos_css:]
        print("Added extra CSS for image integration.")

# Extract SVG for Project 01
p1_start = html.find("id=\"view-project-01\"")
p2_start = html.find("id=\"view-project-02\"")
chunk_p1 = html[p1_start:p2_start]

svg_match = re.search(r"(<div class=\"frame-illustration\">[\s\S]*?</div>)", chunk_p1)
if not svg_match:
    raise Exception("Project 01 SVG not found!")
svg_p1 = svg_match.group(1).strip()

# Build the bespoke Project 01 section with adapted boxes
new_project_01 = f"""    <!-- VIEW DETAIL: PROJET 01 (FOG CHAIR - MODÈLE 001) -->
    <section id="view-project-01" class="view-panel project-detail-section">
      <!-- Top Navigation Bar -->
      <div class="project-header-bar">
        <button type="button" class="project-nav-btn btn-back-portfolio" data-target="portfolio">
          <span aria-hidden="true">&larr;</span>
          <span class="link-line">Retourner au portfolio</span>
        </button>
        <div class="project-counter-pill">PROJET [ 01 / 06 ]</div>
        <div class="project-nav-arrows">
          <button type="button" class="project-nav-btn prev btn-switch-project" data-target-project="project-06" aria-label="Projet précédent">
            <span aria-hidden="true">&larr;</span>
            <span>Précédent</span>
          </button>
          <button type="button" class="project-nav-btn next btn-switch-project" data-target-project="project-02" aria-label="Projet suivant">
            <span>Suivant</span>
            <span aria-hidden="true">&rarr;</span>
          </button>
        </div>
      </div>

      <!-- 1. HERO DUAL ROW : CARTE COULEUR & TEXTE EXPLICATIF CÔTE À CÔTE -->
      <div class="project-hero-dual">
        <!-- Carte Couleur Signature avec Texture Papier -->
        <div class="hero-card-col">
          <div class="project-art-frame" style="background-color: rgb(204, 255, 0); aspect-ratio: 1/1;">
            {svg_p1}
            <div class="project-detail-cartouche">
              <div class="detail-cartouche-tag">01 — Fog Chair // C001 Paris</div>
              <h2 class="detail-cartouche-title">* FOG CHAIR &bull; MODEL-001 *</h2>
              <div class="detail-cartouche-meta">
                <span>CHAISE MODÈLE 001</span>
                <span style="font-size: 13px;">*</span>
                <span>TANGERINE &amp; VERT ACIDE</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Texte Explicatif : Base du projet, pourquoi & specs -->
        <div class="hero-text-col">
          <div class="editorial-tag-row" style="margin-bottom: 16px;">
            <span class="editorial-tag">01 // Architecture d'Assise &bull; Fog C001</span>
            <span class="chroma-badge" style="background: rgba(204, 255, 0, 0.15); color: #ccff00; border: 1px solid rgba(204, 255, 0, 0.4);">
              * MODÈLE 001 &bull; ÉDITION ORIGINALE *
            </span>
          </div>

          <h1 class="hero-concept-title">Fog Chair &bull; Modèle 001</h1>
          <p class="hero-concept-thesis">
            Pensée avec une approche minimaliste et fonctionnelle, elle explore l'équilibre entre forme simple, répétition modulaire et présence forte.
          </p>

          <div class="hero-narrative-card">
            <div class="narrative-header">
              <span class="narrative-dot" style="background: rgb(204, 255, 0);"></span>
              <span>GENÈSE &amp; BASE DU PROJET</span>
            </div>
            <div class="narrative-body">
              <p>
                « La chaise Modèle 001 est la première création de Fog. Pensée avec une approche minimaliste et fonctionnelle, elle explore l'équilibre entre forme simple et présence forte. Son design explore l'équilibre, la répétition et la couleur, affirmant une esthétique ludique tout en restant structurée. »
              </p>
              <p>
                La structure repose sur un assemblage continu de cylindres rembourrés montés sur un piétement tubulaire courbé en porte-à-faux. Chaque élément modulaire répété apporte un confort enveloppant, tandis que la pureté des lignes tubulaires affirme un caractère architectural affirmé, décliné en finitions monochromes vibrantes.
              </p>
            </div>
          </div>

          <!-- Fiche technique atelier épurée -->
          <div class="project-specs-bar" style="margin-bottom: 0;">
            <span>Modèle : <span class="spec-val">Fog Chair C001</span></span>
            <span class="spec-sep">&bull;</span>
            <span>Dimensions : <span class="spec-val">82 &times; 76 &times; H 78 cm</span></span>
            <span class="spec-sep">&bull;</span>
            <span>Matière : <span class="spec-val">Laine texturée &amp; acier thermolaqué</span></span>
            <span class="spec-sep">&bull;</span>
            <span>Variantes : <span class="spec-val">Tangerine, Vert Acide, Magenta</span></span>
          </div>
        </div>
      </div>

      <!-- 2. GRANDE IMAGE PLEIN ÉCRAN : ADAPTÉE AU FORMAT 16/9 CINÉMATIQUE -->
      <div class="full-screen-image-block">
        <div class="white-image-box has-image" style="aspect-ratio: 16/9; max-height: 80vh;">
          <img src="{img_floating}" alt="Fog Chair Modèle 001 vue tridimensionnelle en suspension dans l'espace" loading="lazy" />
          <span class="placeholder-crosshair cross-tl"></span>
          <span class="placeholder-crosshair cross-tr"></span>
          <span class="placeholder-crosshair cross-bl"></span>
          <span class="placeholder-crosshair cross-br"></span>
          <div class="image-caption-pill">
            <span class="caption-tag">01 // VUE EN APESANTEUR &bull; PLEIN ÉCRAN 16:9</span>
            <span class="caption-title">Fog Chair Model-001 &bull; Châssis tubulaire Tangerine</span>
          </div>
        </div>
      </div>

      <!-- 3. IMAGES PLUS PETITES ET ESPACÉES : FORMAT PORTRAIT 3/4 & CARRÉ 1/1 -->
      <div class="gallery-spaced-pair" style="grid-template-columns: 1fr 1.15fr; gap: clamp(36px, 5.5vw, 80px); align-items: stretch;">
        <!-- Photo 2 : Format Portrait 3/4 adapté (786 x 1024) -->
        <div class="white-image-box has-image" style="aspect-ratio: 786/1024;">
          <img src="{img_portrait}" alt="Fog Chair Modèle 001 vue en élévation trois-quarts" loading="lazy" />
          <span class="placeholder-crosshair cross-tl"></span>
          <span class="placeholder-crosshair cross-tr"></span>
          <span class="placeholder-crosshair cross-bl"></span>
          <span class="placeholder-crosshair cross-br"></span>
          <div class="image-caption-pill">
            <span class="caption-tag">02 // ÉLÉVATION ARCHITECTURALE &bull; 3:4</span>
            <span class="caption-title">Assise basse et piétement incliné</span>
          </div>
        </div>

        <!-- Photo 3 : Format Carré 1/1 adapté (1024 x 1024) -->
        <div class="white-image-box has-image" style="aspect-ratio: 1/1;">
          <img src="{img_stack}" alt="Fog Chair Modèle 001 trio de chaises en équilibre acrobatique" loading="lazy" />
          <span class="placeholder-crosshair cross-tl"></span>
          <span class="placeholder-crosshair cross-tr"></span>
          <span class="placeholder-crosshair cross-bl"></span>
          <span class="placeholder-crosshair cross-br"></span>
          <div class="image-caption-pill">
            <span class="caption-tag">03 // CHROMATIQUE &amp; ÉQUILIBRE &bull; 1:1</span>
            <span class="caption-title">Empilement acrobatique : Tangerine, Vert Acide &amp; Magenta</span>
          </div>
        </div>
      </div>

      <!-- 4. PLANCHE MANIFESTE CENTRÉE : FORMAT AFFISSE (842 x 595) -->
      <div class="gallery-centered-small" style="max-width: 980px; margin-top: clamp(60px, 8vw, 120px); margin-bottom: clamp(60px, 8vw, 120px);">
        <div class="white-image-box has-image" style="aspect-ratio: 842/595;">
          <img src="{img_poster}" alt="Planche manifeste Fog Chair C001 Model-001" loading="lazy" />
          <span class="placeholder-crosshair cross-tl"></span>
          <span class="placeholder-crosshair cross-tr"></span>
          <span class="placeholder-crosshair cross-bl"></span>
          <span class="placeholder-crosshair cross-br"></span>
          <div class="image-caption-pill">
            <span class="caption-tag">04 // PLANCHE MANIFESTE &bull; ÉDITION C001</span>
            <span class="caption-title">Typographie d'atelier, répétition et recherche de silhouette</span>
          </div>
        </div>
      </div>

      <!-- 5. Universal Next Project Teaser Footer -->
      <div class="project-footer-card" style="margin-top: clamp(80px, 10vw, 150px);">
        <div class="next-teaser-info">
          <div class="next-teaser-swatch" style="background-color: rgb(255, 0, 127);"></div>
          <div>
            <div style="font-size: 11px; font-weight: 900; letter-spacing: 0.2em; text-transform: uppercase; color: #888888; margin-bottom: 4px;">
              Projet Suivant &bull; 02
            </div>
            <div style="font-size: clamp(18px, 1.8vw, 24px); font-weight: 900; color: #ffffff;">
              Lampadaire Articulé
            </div>
          </div>
        </div>
        <button type="button" class="project-nav-btn next btn-switch-project" data-target-project="project-02" style="font-size: 13px;">
          <span>Découvrir la pièce</span>
          <span aria-hidden="true">&rarr;</span>
        </button>
      </div>
    </section>
"""

# Replace project 01 section
sec_p1_end = html.find("</section>", p1_start) + len("</section>")
html = html[:p1_start] + new_project_01.strip() + "\n\n" + html[sec_p1_end:]

# Write to standalone.html
with open(standalone_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Updated standalone.html! New file size: {len(html)}")

# Write to portfolio.html
with open(portfolio_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Updated portfolio.html! New file size: {len(html)}")
