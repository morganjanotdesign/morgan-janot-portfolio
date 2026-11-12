import os

standalone_path = '/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/standalone.html'
portfolio_path = '/Users/morganjanot/.gemini/antigravity/brain/04838ef3-4249-4209-97cb-1440ffec4bcd/portfolio.html'

with open(standalone_path, 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '    <!-- VIEW DETAIL: PROJET 03'
end_marker = '    <!-- VIEW DETAIL: PROJET 05 (DAA-DAA) -->'

idx1 = text.find(start_marker)
idx2 = text.find(end_marker)

assert idx1 != -1, "start_marker not found"
assert idx2 != -1, "end_marker not found"

new_p3_p4 = """    <!-- VIEW DETAIL: PROJET 03 (CANAPÉ GALET) -->
    <section id="view-project-03" class="view-panel project-detail-section">
      <!-- Top Navigation Bar -->
      <div class="project-header-bar">
        <button type="button" class="project-nav-btn btn-back-portfolio" data-target="portfolio">
          <span aria-hidden="true">&larr;</span>
          <span class="link-line">Retourner au portfolio</span>
        </button>
        <div class="project-counter-pill">PROJET [ 03 / 06 ]</div>
        <div class="project-nav-arrows">
          <button type="button" class="project-nav-btn prev btn-switch-project" data-target-project="project-02" aria-label="Projet précédent">
            <span aria-hidden="true">&larr;</span>
            <span>Précédent</span>
          </button>
          <button type="button" class="project-nav-btn next btn-switch-project" data-target-project="project-04" aria-label="Projet suivant">
            <span>Suivant</span>
            <span aria-hidden="true">&rarr;</span>
          </button>
        </div>
      </div>

      <!-- 1. HERO DUAL ROW : CARTE COULEUR & TEXTE EXPLICATIF CÔTE À CÔTE -->
      <div class="project-hero-dual reverse-side">
        <!-- Carte Couleur Signature avec Texture Papier -->
        <div class="hero-card-col">
          <div class="project-art-frame" style="background-color: rgb(0, 140, 70); aspect-ratio: 16/10;">
            <div class="frame-illustration">
          <svg viewBox="0 0 582 521" preserveAspectRatio="xMinYMid meet" fill="none" stroke="rgb(0, 85, 42)" stroke-width="13" stroke-linecap="round" stroke-linejoin="round">
            <path d="M 389.16 235.05 C 389.16 287.22 346.27 329.51 293.38 329.51 C 240.48 329.51 197.59 287.22 197.59 235.05 C 197.59 182.88 240.48 140.59 293.38 140.59 C 346.27 140.59 389.16 182.88 389.16 235.05 Z M 85.57 32.00 L 137.19 32.00 C 137.19 32.00 186.86 42.20 188.80 89.42 C 190.75 136.63 188.80 235.05 188.80 235.05 C 188.80 235.05 186.60 336.42 293.38 340.26 L 345.61 340.26 C 345.61 340.26 395.28 337.38 398.20 391.17 L 398.20 436.31 C 398.20 436.31 398.20 485.30 344.63 487.22 C 291.07 489.14 161.53 487.22 161.53 487.22 C 161.53 487.22 33.95 479.54 32.97 357.55 C 32.00 235.57 32.97 89.42 32.97 89.42 C 32.97 89.42 35.89 38.79 85.57 32.00 Z M 325.18 487.71 L 370.93 488.08 L 415.73 488.08 C 539.43 488.12 547.21 360.43 547.21 360.43 C 547.21 360.43 550.14 228.84 547.21 179.86 C 544.29 130.87 493.65 127.03 493.65 127.03 L 447.87 127.03 C 447.87 127.03 399.18 130.87 398.20 178.90 L 397.23 226.92 L 384.04 265.61" />
          </svg>
        </div>
            <div class="project-detail-cartouche">
              <div class="detail-cartouche-tag">03 — Recherche Formelle // Atelier Janot</div>
              <h2 class="detail-cartouche-title">* CANAPÉ GALET *</h2>
              <div class="detail-cartouche-meta">
                <span>VOLUME MONOBLOC</span>
                <span style="font-size: 13px;">*</span>
                <span>VERT PROFOND</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Texte Explicatif : Base du projet, pourquoi & specs -->
        <div class="hero-text-col">
          <div class="editorial-tag-row" style="margin-bottom: 16px;">
            <span class="editorial-tag">03 // Recherche Formelle</span>
            <span class="chroma-badge" style="background: rgba(0, 140, 70, 0.16); color: #00e676; border: 1px solid rgba(0, 140, 70, 0.42);">
              * MONOLITHE SCULPTURAL &amp; CUIR PATINÉ *
            </span>
          </div>

          <h1 class="hero-concept-title">Canapé Galet</h1>
          <p class="hero-concept-thesis">Masse rocheuse adoucie par l'érosion géologique, accueillant un orbe sphérique mobile en cuir naturel ciré.</p>

          <div class="hero-narrative-card">
            <div class="narrative-header">
              <span class="narrative-dot" style="background: rgb(0, 140, 70);"></span>
              <span>GENÈSE &amp; BASE DU PROJET</span>
            </div>
            <div class="narrative-body">
              <p>Pourquoi ce projet ? La volonté d'échapper à la monotonie rectiligne des canapés modulaires. Le dessin est né de l'observation des roches de granit érodées par l'océan Atlantique : une forme continue qui s'adapte intuitivement aux différentes postures d'assise (formelle, lecture ou méridienne).</p>
              <p>L'orbe mobile en cuir ciré à chaud apporte une ponctuation sculpturale vivante : confectionné en taurillon pleine fleur, il devient au gré des envies un accoudoir ergonomique, un cale-dos amovible ou un objet de contemplation autonome.</p>
            </div>
          </div>

          <!-- Fiche technique atelier épurée -->
          <div class="project-specs-bar" style="margin-bottom: 0;">
            <span>Dimensions : <span class="spec-val">L 285 &times; P 138 &times; H 76 cm</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Cuir : <span class="spec-val">Taurillon pleine fleur ciré</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Structure : <span class="spec-val">Multiplis de hêtre &amp; mousse végétale</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Poids : <span class="spec-val">115 kg monobloc</span></span>
          </div>
        </div>
      </div>

      <!-- 2. GRANDE IMAGE PLEIN ÉCRAN (QUI FAIT TOUT L'ÉCRAN) -->
      <div class="full-screen-image-block">
      <div class="white-image-box" style="aspect-ratio: 21/9;">
        <span class="placeholder-crosshair cross-tl"></span>
        <span class="placeholder-crosshair cross-tr"></span>
        <span class="placeholder-crosshair cross-bl"></span>
        <span class="placeholder-crosshair cross-br"></span>
        <div class="placeholder-inner">
          <div class="placeholder-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
              <circle cx="8.5" cy="8.5" r="1.5"/>
              <polyline points="21 15 16 10 5 21"/>
            </svg>
          </div>
          <span class="placeholder-tag">PLEIN ÉCRAN // FORMAT CINÉMA 21:9</span>
          <h4 class="placeholder-title">IMAGE 01 — GRANDE VUE PLEIN ÉCRAN</h4>
          <span class="placeholder-sub">Mégalithe sculptural dans une pièce de réception baignée de lumière &bull; Plein écran 21/9</span>
        </div>
      </div>
      </div>

      <!-- 3. IMAGES PLUS PETITES ET ESPACÉES -->
      <div class="gallery-spaced-pair asymmetric-left">
      <div class="white-image-box" style="aspect-ratio: 16/10;">
        <span class="placeholder-crosshair cross-tl"></span>
        <span class="placeholder-crosshair cross-tr"></span>
        <span class="placeholder-crosshair cross-bl"></span>
        <span class="placeholder-crosshair cross-br"></span>
        <div class="placeholder-inner">
          <div class="placeholder-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
              <circle cx="8.5" cy="8.5" r="1.5"/>
              <polyline points="21 15 16 10 5 21"/>
            </svg>
          </div>
          <span class="placeholder-tag">VUE D'ENSEMBLE TROIS-QUARTS</span>
          <h4 class="placeholder-title">IMAGE 02</h4>
          <span class="placeholder-sub">Perspective trois-quarts et profilage d'assise &bull; 16/10</span>
        </div>
      </div>
      <div class="white-image-box" style="aspect-ratio: 1/1;">
        <span class="placeholder-crosshair cross-tl"></span>
        <span class="placeholder-crosshair cross-tr"></span>
        <span class="placeholder-crosshair cross-bl"></span>
        <span class="placeholder-crosshair cross-br"></span>
        <div class="placeholder-inner">
          <div class="placeholder-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
              <circle cx="8.5" cy="8.5" r="1.5"/>
              <polyline points="21 15 16 10 5 21"/>
            </svg>
          </div>
          <span class="placeholder-tag">PETITE VUE DÉTAIL MATIÈRE</span>
          <h4 class="placeholder-title">IMAGE 03</h4>
          <span class="placeholder-sub">Gros plan matière : cuir patiné manuellement &bull; 1/1</span>
        </div>
      </div>
      </div>

      <div class="gallery-centered-small">
      <div class="white-image-box" style="aspect-ratio: 4/5;">
        <span class="placeholder-crosshair cross-tl"></span>
        <span class="placeholder-crosshair cross-tr"></span>
        <span class="placeholder-crosshair cross-bl"></span>
        <span class="placeholder-crosshair cross-br"></span>
        <div class="placeholder-inner">
          <div class="placeholder-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
              <circle cx="8.5" cy="8.5" r="1.5"/>
              <polyline points="21 15 16 10 5 21"/>
            </svg>
          </div>
          <span class="placeholder-tag">PETIT FORMAT PORTRAIT USAGE</span>
          <h4 class="placeholder-title">IMAGE 04</h4>
          <span class="placeholder-sub">L'orbe sphérique mobile utilisé en accoudoir &bull; 4/5</span>
        </div>
      </div>
      </div>

      <!-- 4. Universal Next Project Teaser Footer -->
      <div class="project-footer-card" style="margin-top: clamp(80px, 10vw, 150px);">
        <div class="next-teaser-info">
          <div class="next-teaser-swatch" style="background-color: rgb(227, 6, 19);"></div>
          <div>
            <div style="font-size: 11px; font-weight: 900; letter-spacing: 0.2em; text-transform: uppercase; color: #888888; margin-bottom: 4px;">
              Projet Suivant &bull; 04
            </div>
            <div style="font-size: clamp(18px, 1.8vw, 24px); font-weight: 900; color: #ffffff;">
              Chaise Suspendue
            </div>
          </div>
        </div>
        <button type="button" class="project-nav-btn next btn-switch-project" data-target-project="project-04" style="font-size: 13px;">
          <span>Découvrir la pièce</span>
          <span aria-hidden="true">&rarr;</span>
        </button>
      </div>
    </section>

    <!-- VIEW DETAIL: PROJET 04 (CHAISE SUSPENDUE) -->
    <section id="view-project-04" class="view-panel project-detail-section">
      <!-- Top Navigation Bar -->
      <div class="project-header-bar">
        <button type="button" class="project-nav-btn btn-back-portfolio" data-target="portfolio">
          <span aria-hidden="true">&larr;</span>
          <span class="link-line">Retourner au portfolio</span>
        </button>
        <div class="project-counter-pill">PROJET [ 04 / 06 ]</div>
        <div class="project-nav-arrows">
          <button type="button" class="project-nav-btn prev btn-switch-project" data-target-project="project-03" aria-label="Projet précédent">
            <span aria-hidden="true">&larr;</span>
            <span>Précédent</span>
          </button>
          <button type="button" class="project-nav-btn next btn-switch-project" data-target-project="project-05" aria-label="Projet suivant">
            <span>Suivant</span>
            <span aria-hidden="true">&rarr;</span>
          </button>
        </div>
      </div>

      <!-- 1. HERO DUAL ROW : CARTE COULEUR & TEXTE EXPLICATIF CÔTE À CÔTE -->
      <div class="project-hero-dual ">
        <!-- Carte Couleur Signature avec Texture Papier -->
        <div class="hero-card-col">
          <div class="project-art-frame" style="background-color: rgb(227, 6, 19); aspect-ratio: 4/3;">
            <div class="frame-illustration">
            <svg viewBox="0 0 400 520" preserveAspectRatio="xMinYMid meet" fill="none" stroke="rgb(150, 4, 13)" stroke-width="13" stroke-linecap="round" stroke-linejoin="round">
              <path d="M 32.07 32.00 L 32.00 64.75 L 331.06 145.27 C 331.06 145.27 337.31 147.64 337.53 153.44 C 337.75 159.23 337.53 189.94 337.53 189.94 L 58.32 474.28 C 56.29 476.35 55.08 479.15 55.25 482.04 C 55.41 484.75 56.65 487.49 60.96 487.60 C 69.59 487.81 87.25 487.60 87.25 487.60 C 87.25 487.60 88.92 487.34 91.97 484.36 C 95.02 481.39 323.86 248.32 323.86 248.32 C 323.86 248.32 333.52 239.44 337.39 252.61 C 341.26 265.77 337.63 482.26 337.63 482.26 C 337.63 482.26 337.64 488.57 343.44 488.57 L 362.58 488.57 C 362.58 488.57 368.78 487.36 368.78 481.45 C 368.78 475.55 368.45 121.48 368.45 121.48 C 368.45 121.48 368.82 116.28 362.12 114.44 C 355.43 112.61 32.07 32.00 32.07 32.00 Z M 359.90 221.84 C 359.90 225.03 357.30 227.62 354.09 227.62 C 350.88 227.62 348.27 225.03 348.27 221.84 C 348.27 218.64 350.88 216.05 354.09 216.05 C 357.30 216.05 359.90 218.64 359.90 221.84 Z M 39.60 48.38 C 39.69 58.71 42.19 157.46 125.01 216.05 C 190.94 262.69 281.15 265.05 354.09 221.84" />
            </svg>
          </div>
            <div class="project-detail-cartouche">
              <div class="detail-cartouche-tag">04 — Structure Géométrique // Paris</div>
              <h2 class="detail-cartouche-title">* CHAISE SUSPENDUE *</h2>
              <div class="detail-cartouche-meta">
                <span>ANCRAGE MONOPHONIQUE</span>
                <span style="font-size: 13px;">*</span>
                <span>ROUGE SUISSE</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Texte Explicatif : Base du projet, pourquoi & specs -->
        <div class="hero-text-col">
          <div class="editorial-tag-row" style="margin-bottom: 16px;">
            <span class="editorial-tag">04 // Structure Géométrique</span>
            <span class="chroma-badge" style="background: rgba(227, 6, 19, 0.16); color: #ff4d4d; border: 1px solid rgba(227, 6, 19, 0.42);">
              * ÉTUDE TENSIONNELLE EN APESANTEUR *
            </span>
          </div>

          <h1 class="hero-concept-title">Chaise Suspendue</h1>
          <p class="hero-concept-thesis">L'abolition des pieds traditionnels au profit d'un treillis autoportant ancré au plafond par des liens invisibles.</p>

          <div class="hero-narrative-card">
            <div class="narrative-header">
              <span class="narrative-dot" style="background: rgb(227, 6, 19);"></span>
              <span>GENÈSE &amp; BASE DU PROJET</span>
            </div>
            <div class="narrative-body">
              <p>Pourquoi cette recherche ? Pour libérer complètement la surface au sol et éprouver le vide comme matériau structural. En suspendant l'assise au plafond par des filins en fibre Dyneema ultra-résistante, l'objet s'affranchit des contraintes d'appui et réagit aux oscillations du corps pour une sensation de lévitation intégrale.</p>
              <p>L'arceau triangulé en titane microbillé distribue les tensions mécaniques de manière isotrope. La membrane textile thermoformée épouse la posture sans point dur, rappelant l'aéronautique et le gréement nautique de haute mer.</p>
            </div>
          </div>

          <!-- Fiche technique atelier épurée -->
          <div class="project-specs-bar" style="margin-bottom: 0;">
            <span>Envergure : <span class="spec-val">78 &times; 82 &times; H 115 cm</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Câblage : <span class="spec-val">Dyneema SK78 (&gt; 1 800 kg)</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Armature : <span class="spec-val">Titane Ti-6Al-4V</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Charge : <span class="spec-val">260 kg certifiée</span></span>
          </div>
        </div>
      </div>

      <!-- 2. GRANDE IMAGE PLEIN ÉCRAN (QUI FAIT TOUT L'ÉCRAN) -->
      <div class="full-screen-image-block">
      <div class="white-image-box" style="aspect-ratio: 21/9;">
        <span class="placeholder-crosshair cross-tl"></span>
        <span class="placeholder-crosshair cross-tr"></span>
        <span class="placeholder-crosshair cross-bl"></span>
        <span class="placeholder-crosshair cross-br"></span>
        <div class="placeholder-inner">
          <div class="placeholder-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
              <circle cx="8.5" cy="8.5" r="1.5"/>
              <polyline points="21 15 16 10 5 21"/>
            </svg>
          </div>
          <span class="placeholder-tag">PLEIN ÉCRAN // FORMAT CINÉMA 21:9</span>
          <h4 class="placeholder-title">IMAGE 01 — GRANDE VUE PLEIN ÉCRAN</h4>
          <span class="placeholder-sub">Suspension dans un grand volume d'architecture contemporaine &bull; Plein écran 21/9</span>
        </div>
      </div>
      </div>

      <!-- 3. IMAGES PLUS PETITES ET ESPACÉES -->
      <!-- Images plus petites et espacées -->
      <div class="gallery-spaced-pair asymmetric-left">
      <div class="white-image-box" style="aspect-ratio: 4/5;">
        <span class="placeholder-crosshair cross-tl"></span>
        <span class="placeholder-crosshair cross-tr"></span>
        <span class="placeholder-crosshair cross-bl"></span>
        <span class="placeholder-crosshair cross-br"></span>
        <div class="placeholder-inner">
          <div class="placeholder-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
              <circle cx="8.5" cy="8.5" r="1.5"/>
              <polyline points="21 15 16 10 5 21"/>
            </svg>
          </div>
          <span class="placeholder-tag">PETIT FORMAT PORTRAIT D'ANCRAGE</span>
          <h4 class="placeholder-title">IMAGE 02</h4>
          <span class="placeholder-sub">Point d'attache zénithal &amp; anneau d'accroche titane &bull; 4/5</span>
        </div>
      </div>
      <div class="white-image-box" style="aspect-ratio: 16/10;">
        <span class="placeholder-crosshair cross-tl"></span>
        <span class="placeholder-crosshair cross-tr"></span>
        <span class="placeholder-crosshair cross-bl"></span>
        <span class="placeholder-crosshair cross-br"></span>
        <div class="placeholder-inner">
          <div class="placeholder-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
              <circle cx="8.5" cy="8.5" r="1.5"/>
              <polyline points="21 15 16 10 5 21"/>
            </svg>
          </div>
          <span class="placeholder-tag">VUE MATIÈRE MOYENNE</span>
          <h4 class="placeholder-title">IMAGE 03</h4>
          <span class="placeholder-sub">Détail d'atelier : tressage des fibres Dyneema &bull; 16/10</span>
        </div>
      </div>
      </div>

      <div class="gallery-centered-small">
      <div class="white-image-box" style="aspect-ratio: 1/1;">
        <span class="placeholder-crosshair cross-tl"></span>
        <span class="placeholder-crosshair cross-tr"></span>
        <span class="placeholder-crosshair cross-bl"></span>
        <span class="placeholder-crosshair cross-br"></span>
        <div class="placeholder-inner">
          <div class="placeholder-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
              <circle cx="8.5" cy="8.5" r="1.5"/>
              <polyline points="21 15 16 10 5 21"/>
            </svg>
          </div>
          <span class="placeholder-tag">PETIT CARRÉ D'ASSEMBLAGE</span>
          <h4 class="placeholder-title">IMAGE 04</h4>
          <span class="placeholder-sub">Membrane thermoformée &amp; ergonomie en apesanteur &bull; 1/1</span>
        </div>
      </div>
      </div>

      <!-- 4. Universal Next Project Teaser Footer -->
      <div class="project-footer-card" style="margin-top: clamp(80px, 10vw, 150px);">
        <div class="next-teaser-info">
          <div class="next-teaser-swatch" style="background-color: rgb(0, 130, 255);"></div>
          <div>
            <div style="font-size: 11px; font-weight: 900; letter-spacing: 0.2em; text-transform: uppercase; color: #888888; margin-bottom: 4px;">
              Projet Suivant &bull; 05
            </div>
            <div style="font-size: clamp(18px, 1.8vw, 24px); font-weight: 900; color: #ffffff;">
              DAA-DAA
            </div>
          </div>
        </div>
        <button type="button" class="project-nav-btn next btn-switch-project" data-target-project="project-05" style="font-size: 13px;">
          <span>Découvrir la pièce</span>
          <span aria-hidden="true">&rarr;</span>
        </button>
      </div>
    </section>

    
"""

new_text = text[:idx1] + new_p3_p4 + text[idx2:]

# Update swatch 02 in palette if violet
old_swatch_02 = '<div class="palette-swatch" style="background-color: rgb(185, 45, 255);" title="02 — Violet Fluo (Lampadaire Articulé)">'
new_swatch_02 = '<div class="palette-swatch" style="background-color: rgb(180, 185, 192);" title="02 — Gris Minéral (Lampadaire Articulé)">'
if old_swatch_02 in new_text:
    new_text = new_text.replace(old_swatch_02, new_swatch_02)
    print("Updated swatch 02 to Gris Minéral")

with open(standalone_path, 'w', encoding='utf-8') as f:
    f.write(new_text)
print("Successfully updated standalone.html!")

# Now also copy standalone.html directly to portfolio.html (artifact)
with open(portfolio_path, 'w', encoding='utf-8') as f:
    f.write(new_text)
print("Successfully synced portfolio.html artifact!")
