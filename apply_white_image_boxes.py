import re, shutil

with open('standalone.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract projects info
pattern = r'<article class="project-card" id="(project-0[1-6])"[^>]*>.*?background-color:\s*([^;\"]+);.*?<svg([^>]*)>(.*?)</svg>.*?<div class="frame-category">([^<]+)</div>.*?<h2 class="frame-title">([^<]+)</h2>'
matches = re.findall(pattern, content, re.DOTALL)

pdata = {}
order = []
for m in matches:
    pid = m[0]
    order.append(pid)
    pdata[pid] = {
        'id': pid,
        'bg_color': m[1].strip(),
        'svg_attrs': m[2].strip(),
        'svg_inner': m[3].strip(),
        'category': m[4].strip(),
        'title': m[5].strip(),
        'num': pid.replace('project-', '')
    }

def make_white_box(img_num, title, subtitle, aspect_ratio="16/10", style=""):
    return f"""      <div class="white-image-box" style="aspect-ratio: {aspect_ratio}; {style}">
        <span class="placeholder-crosshair cross-tl"></span>
        <span class="placeholder-crosshair cross-tr"></span>
        <span class="placeholder-crosshair cross-bl"></span>
        <span class="placeholder-crosshair cross-br"></span>
        <div class="placeholder-inner">
          <div class="placeholder-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
              <circle cx="8.5" cy="8.5" r="1.5"/>
              <polyline points="21 15 16 10 5 21"/>
            </svg>
          </div>
          <span class="placeholder-tag">EMPLACEMENT PHOTO</span>
          <h4 class="placeholder-title">{img_num}</h4>
          <span class="placeholder-sub">{subtitle}</span>
        </div>
      </div>"""

def make_top_bar(idx):
    pid = order[idx]
    prev_pid = order[(idx - 1 + 6) % 6]
    next_pid = order[(idx + 1) % 6]
    num = str(idx + 1).zfill(2)
    return f"""      <div class="project-header-bar">
        <button type="button" class="project-nav-btn btn-back-portfolio" data-target="portfolio">
          <span aria-hidden="true">&larr;</span>
          <span class="link-line">Retourner au portfolio</span>
        </button>
        <div class="project-counter-pill">PROJET [ {num} / 06 ]</div>
        <div class="project-nav-arrows">
          <button type="button" class="project-nav-btn prev btn-switch-project" data-target-project="{prev_pid}" aria-label="Projet précédent">
            <span aria-hidden="true">&larr;</span>
            <span>Précédent</span>
          </button>
          <button type="button" class="project-nav-btn next btn-switch-project" data-target-project="{next_pid}" aria-label="Projet suivant">
            <span>Suivant</span>
            <span aria-hidden="true">&rarr;</span>
          </button>
        </div>
      </div>"""

def make_footer(idx):
    next_pid = order[(idx + 1) % 6]
    np = pdata[next_pid]
    return f"""      <div class="project-footer-card">
        <div class="next-teaser-info">
          <div class="next-teaser-swatch" style="background-color: {np['bg_color']};"></div>
          <div>
            <div style="font-size: 11px; font-weight: 900; letter-spacing: 0.2em; text-transform: uppercase; color: #888888; margin-bottom: 4px;">
              Projet Suivant &bull; {np['num']}
            </div>
            <div style="font-size: clamp(18px, 1.8vw, 24px); font-weight: 900; color: #ffffff;">
              {np['title']}
            </div>
          </div>
        </div>
        <button type="button" class="project-nav-btn next btn-switch-project" data-target-project="{next_pid}" style="font-size: 13px;">
          <span>Découvrir la pièce</span>
          <span aria-hidden="true">&rarr;</span>
        </button>
      </div>"""

# Replace the project detail sections
p1 = pdata['project-01']
top_0 = make_top_bar(0)
foot_0 = make_footer(0)
box1_p1 = make_white_box("IMAGE 01", "Vue d Ensemble", "Perspective principale &bull; 16/10", "16/10")
box2_p1 = make_white_box("IMAGE 02", "Detail Textile", "Gros plan texture laine bouclee &bull; 16/9", "16/9")
box3_p1 = make_white_box("IMAGE 03", "En Situation", "Mise en scene architecturale &bull; 16/9", "16/9")

sec_p1 = f"""    <!-- VIEW DETAIL: PROJET 01 (FAUTEUIL NUAGE) -->
    <section id="view-project-01" class="view-panel project-detail-section">
{top_0}

      <div class="editorial-tag-row">
        <span class="editorial-tag">01 // Mobilier Éditorial</span>
        <span class="chroma-badge" style="background: rgba(204, 255, 0, 0.2); color: #ccff00; border: 1px solid rgba(204, 255, 0, 0.4);">
          * ÉDITION LIMITÉE 12 EX. *
        </span>
      </div>

      <h1 class="editorial-h1" style="margin-bottom: 12px;">Fauteuil Nuage</h1>
      <p class="editorial-lead" style="max-width: 820px; margin-bottom: 24px;">
        Assise sculpturale explorant la densité d'un volume gonflé d'air et l'intensité tactile du vert acide.
      </p>

      <!-- Fiche technique épurée -->
      <div class="project-specs-bar">
        <span>Dimensions : <span class="spec-val">94 &times; 102 &times; H 82 cm</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Matière : <span class="spec-val">Laine bouclée &amp; mousse HR</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Poids : <span class="spec-val">28 kg</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Tirage : <span class="spec-val">12 pièces numérotées</span></span>
      </div>

      <!-- GRILLE D'IMAGES 1 : Hero Asymétrique + 3 Cases Blanches -->
      <div class="grid-p01-top">
        <div class="project-art-frame" style="background-color: {p1['bg_color']}; aspect-ratio: 16/10;">
          <div class="frame-illustration">
            <svg {p1['svg_attrs']}>
              {p1['svg_inner']}
            </svg>
          </div>
          <div class="project-detail-cartouche">
            <div class="detail-cartouche-tag">01 — Architecture d'Assise // Paris</div>
            <h2 class="detail-cartouche-title">* FAUTEUIL NUAGE *</h2>
            <div class="detail-cartouche-meta">
              <span>ESTAMPE D'ATELIER</span>
              <span style="font-size: 13px;">*</span>
              <span>VERT ACIDE</span>
            </div>
          </div>
        </div>

{box1_p1}
      </div>

      <div class="grid-p01-bottom">
{box2_p1}
{box3_p1}
      </div>

{foot_0}
    </section>"""

# Project 02
p2 = pdata['project-02']
top_1 = make_top_bar(1)
foot_1 = make_footer(1)
box1_p2 = make_white_box("IMAGE 01", "Deploiement 360", "Course du bras &bull; Format 9/16", "9/16", "min-height: 480px;")
box2_p2 = make_white_box("IMAGE 02", "Pivot Laiton", "Detail usinage &bull; Format 1/1", "1/1")
box3_p2 = make_white_box("IMAGE 03", "Ambiance Nuit", "Faisceau 38&deg; &bull; Format 1/1", "1/1")

sec_p2 = f"""    <!-- VIEW DETAIL: PROJET 02 (LAMPADAIRE ARTICULÉ) -->
    <section id="view-project-02" class="view-panel project-detail-section">
{top_1}

      <div class="editorial-tag-row">
        <span class="editorial-tag">02 // Design d'Espace</span>
        <span class="chroma-badge" style="background: rgba(255, 0, 127, 0.2); color: #ff55a3; border: 1px solid rgba(255, 0, 127, 0.4);">
          * PROTOTYPE CINÉTIQUE *
        </span>
      </div>

      <h1 class="editorial-h1" style="margin-bottom: 12px;">Lampadaire Articulé</h1>
      <p class="editorial-lead" style="max-width: 820px; margin-bottom: 24px;">
        Équilibre mécanique par pivot à friction sèche et balancier en porte-à-faux 360&deg;.
      </p>

      <div class="project-specs-bar">
        <span>Portée : <span class="spec-val">220 cm</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Débattement : <span class="spec-val">110 à 240 cm</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Source : <span class="spec-val">LED 2700K CRI 98</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Contrepoids : <span class="spec-val">Laiton massif 8.4 kg</span></span>
      </div>

      <!-- GRILLE D'IMAGES 2 : 3 Colonnes Verticales Asymétriques -->
      <div class="grid-p02-vertical">
        <div class="project-art-frame" style="background-color: {p2['bg_color']}; aspect-ratio: 9/16; min-height: 480px;">
          <div class="frame-illustration">
            <svg {p2['svg_attrs']}>
              {p2['svg_inner']}
            </svg>
          </div>
          <div class="project-detail-cartouche">
            <div class="detail-cartouche-tag">02 — Cinétique &bull; Studio Janot</div>
            <h2 class="detail-cartouche-title">* LAMPADAIRE *</h2>
            <div class="detail-cartouche-meta">
              <span>ROTATION 360&deg;</span>
              <span style="font-size: 13px;">*</span>
              <span>CYBER MAGENTA</span>
            </div>
          </div>
        </div>

{box1_p2}

        <div style="display: flex; flex-direction: column; gap: clamp(16px, 2.2vw, 28px);">
{box2_p2}
{box3_p2}
        </div>
      </div>

{foot_1}
    </section>"""

# Project 03
p3 = pdata['project-03']
top_2 = make_top_bar(2)
foot_2 = make_footer(2)
box1_p3 = make_white_box("IMAGE 01", "Suspension Flottante", "Vue generale en levitation &bull; 16/10", "16/10")
box2_p3 = make_white_box("IMAGE 02", "Ancrage Plafond", "Platine titane usinee &bull; 4/3", "4/3")
box3_p3 = make_white_box("IMAGE 03", "Tension Textile", "Gros plan lacage aramide &bull; 16/10", "16/10")

sec_p3 = f"""    <!-- VIEW DETAIL: PROJET 03 (CHAISE SUSPENDUE) -->
    <section id="view-project-03" class="view-panel project-detail-section">
{top_2}

      <div class="editorial-tag-row">
        <span class="editorial-tag">03 // Structure Géométrique</span>
        <span class="chroma-badge" style="background: rgba(0, 245, 255, 0.2); color: #00f0ff; border: 1px solid rgba(0, 245, 255, 0.4);">
          * SUSPENSION ZÉRO GRAVITÉ *
        </span>
      </div>

      <h1 class="editorial-h1" style="margin-bottom: 12px;">Chaise Suspendue</h1>
      <p class="editorial-lead" style="max-width: 820px; margin-bottom: 24px;">
        Suppression totale des pieds terrestres par un treillis triangulé en titane et aramide.
      </p>

      <div class="project-specs-bar">
        <span>Suspension : <span class="spec-val">Câbles Dyneema SK78 4mm</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Armature : <span class="spec-val">Titane Ti-6Al-4V microbillé</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Charge certifiée : <span class="spec-val">260 kg dynamique</span></span>
      </div>

      <!-- GRILLE D'IMAGES 3 : Damier en Quinconce -->
      <div class="grid-p03-offset-row1">
{box1_p3}

        <div class="project-art-frame" style="background-color: {p3['bg_color']}; aspect-ratio: 4/3;">
          <div class="frame-illustration">
            <svg {p3['svg_attrs']}>
              {p3['svg_inner']}
            </svg>
          </div>
          <div class="project-detail-cartouche">
            <div class="detail-cartouche-tag">03 — Tension Géométrique</div>
            <h2 class="detail-cartouche-title">* SUSPENDUE *</h2>
            <div class="detail-cartouche-meta">
              <span>DYNEEMA SK78</span>
              <span style="font-size: 13px;">*</span>
              <span>LASER AQUA</span>
            </div>
          </div>
        </div>
      </div>

      <div class="grid-p03-offset-row2">
{box2_p3}
{box3_p3}
      </div>

{foot_2}
    </section>"""

# Project 04
p4 = pdata['project-04']
top_3 = make_top_bar(3)
foot_3 = make_footer(3)
box1_p4 = make_white_box("IMAGE 01", "Vue Panoramique", "Perspective 3/4 face &bull; 16/10", "16/10")
box2_p4 = make_white_box("IMAGE 02", "Orbe Mobile", "Sphere cuir patine 42 cm &bull; 1/1", "1/1")
box3_p4 = make_white_box("IMAGE 03", "Texture &amp; Pores", "Grain du cuir cire a la main &bull; 4/5", "4/5")

sec_p4 = f"""    <!-- VIEW DETAIL: PROJET 04 (CANAPÉ GALET) -->
    <section id="view-project-04" class="view-panel project-detail-section">
{top_3}

      <div class="editorial-tag-row">
        <span class="editorial-tag">04 // Recherche Formelle</span>
        <span class="chroma-badge" style="background: rgba(255, 94, 0, 0.2); color: #ff904d; border: 1px solid rgba(255, 94, 0, 0.4);">
          * MONOLITHE &amp; CUIR PATINÉ *
        </span>
      </div>

      <h1 class="editorial-h1" style="margin-bottom: 12px;">Canapé Galet</h1>
      <p class="editorial-lead" style="max-width: 820px; margin-bottom: 24px;">
        Silhouette géologique continue modelée sans arête vive, accompagnée d'un orbe mobile en cuir ciré.
      </p>

      <div class="project-specs-bar">
        <span>Dimensions : <span class="spec-val">L 285 &times; P 138 &times; H 76 cm</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Cuir : <span class="spec-val">Taurillon pleine fleur ciré</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Poids : <span class="spec-val">115 kg</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Délai : <span class="spec-val">Sur commande (8 semaines)</span></span>
      </div>

      <!-- Estampe panoramique paysage -->
      <div class="project-art-frame" style="background-color: {p4['bg_color']}; width: 100%; aspect-ratio: 21/9; max-height: 440px; margin-bottom: clamp(16px, 2.5vw, 28px);">
        <div class="frame-illustration">
          <svg {p4['svg_attrs']}>
            {p4['svg_inner']}
          </svg>
        </div>
        <div class="project-detail-cartouche">
          <div class="detail-cartouche-tag">04 — Recherche Formelle &bull; Atelier Janot</div>
          <h2 class="detail-cartouche-title">* CANAPÉ GALET *</h2>
          <div class="detail-cartouche-meta">
            <span>VOLUME GÉOLOGIQUE</span>
            <span style="font-size: 13px;">*</span>
            <span>SAFETY TANGERINE</span>
          </div>
        </div>
      </div>

      <!-- Triptyque horizontal 3 cases blanches -->
      <div class="grid-p04-triptych">
{box1_p4}
{box2_p4}
{box3_p4}
      </div>

{foot_3}
    </section>"""

# Project 05
p5 = pdata['project-05']
top_4 = make_top_bar(4)
foot_4 = make_footer(4)
box1_p5 = make_white_box("IMAGE 01", "Lumiere Naturelle", "Diffraction ultraviolet &bull; 16/10", "16/10")
box2_p5 = make_white_box("IMAGE 02", "Col en Fusion", "Bouche evasee &bull; 1/1", "1/1")
box3_p5 = make_white_box("IMAGE 03", "Gravure Pointe", "Signature atelier &bull; 1/1", "1/1")

sec_p5 = f"""    <!-- VIEW DETAIL: PROJET 05 (VASE COROLLE) -->
    <section id="view-project-05" class="view-panel project-detail-section">
{top_4}

      <div class="editorial-tag-row">
        <span class="editorial-tag">05 // Édition Limitée</span>
        <span class="chroma-badge" style="background: rgba(200, 75, 255, 0.2); color: #d97dff; border: 1px solid rgba(200, 75, 255, 0.4);">
          * CRISTAL DE MURANO *
        </span>
      </div>

      <h1 class="editorial-h1" style="margin-bottom: 12px;">Vase Corolle</h1>
      <p class="editorial-lead" style="max-width: 820px; margin-bottom: 24px;">
        Corolle asymétrique soufflée à la canne, teintée par diffraction d'oxydes de manganèse à 1 250&deg;C.
      </p>

      <div class="project-specs-bar">
        <span>Hauteur : <span class="spec-val">48 cm</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Diamètre : <span class="spec-val">36 cm</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Cristal : <span class="spec-val">24% PbO (9.2 kg)</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Tirage : <span class="spec-val">8 pièces numérotées</span></span>
      </div>

      <!-- GRILLE D'IMAGES 5 : Double page / Quadruple galerie -->
      <div class="grid-p05-gallery">
        <div class="project-art-frame" style="background-color: {p5['bg_color']}; aspect-ratio: 4/5; min-height: 480px;">
          <div class="frame-illustration">
            <svg {p5['svg_attrs']}>
              {p5['svg_inner']}
            </svg>
          </div>
          <div class="project-detail-cartouche">
            <div class="detail-cartouche-tag">05 — Verrerie d'Art // Murano</div>
            <h2 class="detail-cartouche-title">* VASE COROLLE *</h2>
            <div class="detail-cartouche-meta">
              <span>SOUFFLÉ À LA VOLÉE</span>
              <span style="font-size: 13px;">*</span>
              <span>ULTRAVIOLET</span>
            </div>
          </div>
        </div>

        <div class="grid-p05-subcol">
{box1_p5}
          <div class="grid-p05-twins">
{box2_p5}
{box3_p5}
          </div>
        </div>
      </div>

{foot_4}
    </section>"""

# Project 06
p6 = pdata['project-06']
top_5 = make_top_bar(5)
foot_5 = make_footer(5)
box1_p6 = make_white_box("IMAGE 01", "Nef Biennale de Milan", "Vue immersive plein format &bull; 21/9", "21/9", "width: 100%; max-height: 460px;")
box2_p6 = make_white_box("IMAGE 02", "Moire Cinetique", "Decalage angulaire 2.5&deg; &bull; 4/3", "4/3")
box3_p6 = make_white_box("IMAGE 03", "Clavetage Invisible", "Usinage CNC &bull; 4/3", "4/3")

sec_p6 = f"""    <!-- VIEW DETAIL: PROJET 06 (ARCHE RADIALE) -->
    <section id="view-project-06" class="view-panel project-detail-section">
{top_5}

      <div class="editorial-tag-row" style="justify-content: center;">
        <span class="editorial-tag">06 // Manifesto &amp; Archive</span>
        <span class="chroma-badge" style="background: rgba(255, 235, 0, 0.2); color: #ffeb00; border: 1px solid rgba(255, 235, 0, 0.4);">
          * BIENNALE DE MILAN 2025 *
        </span>
      </div>

      <div style="text-align: center; max-width: 820px; margin: 0 auto 24px auto;">
        <h1 class="editorial-h1" style="font-size: clamp(38px, 6vw, 84px); margin-bottom: 12px;">* ARCHE RADIALE *</h1>
        <p class="editorial-lead" style="margin: 0 auto;">
          Installation monumentale de 42 arches concentriques en aluminium jaune produisant un moiré optique.
        </p>
      </div>

      <div class="project-specs-bar" style="justify-content: center;">
        <span>Envergure : <span class="spec-val">6.40 m</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Hauteur : <span class="spec-val">4.80 m</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Matériau : <span class="spec-val">Aluminium 6061 anodisé</span></span>
        <span class="spec-sep">&bull;</span>
        <span>Arches : <span class="spec-val">42 arcs (340 kg)</span></span>
      </div>

      <!-- GRILLE D'IMAGES 6 : Monumentale (1 Grand Panoramique + 3 Colonnes) -->
{box1_p6}

      <div class="grid-p06-monumental-bottom">
        <div class="project-art-frame" style="background-color: {p6['bg_color']}; aspect-ratio: 4/3;">
          <div class="frame-illustration">
            <svg {p6['svg_attrs']}>
              {p6['svg_inner']}
            </svg>
          </div>
          <div class="project-detail-cartouche">
            <div class="detail-cartouche-tag">06 — Installation Monumentale</div>
            <h2 class="detail-cartouche-title">* ARCHE RADIALE *</h2>
            <div class="detail-cartouche-meta">
              <span>42 ARCS CONCENTRIQUES</span>
              <span style="font-size: 13px;">*</span>
              <span>JAUNE FLUO</span>
            </div>
          </div>
        </div>

{box2_p6}
{box3_p6}
      </div>

{foot_5}
    </section>"""

all_sections = "\n\n".join([sec_p1, sec_p2, sec_p3, sec_p4, sec_p5, sec_p6])

# 2. Build CSS for White Image Boxes
new_css = """
    /* =============================================================
       WHITE IMAGE BOXES & PHOTO GRIDS FOR PROJECT DETAIL PAGES
       ============================================================= */
    .white-image-box {
      position: relative;
      background-color: #ffffff;
      color: #000000;
      overflow: hidden;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: clamp(20px, 3vw, 36px);
      box-sizing: border-box;
      transition: transform 380ms cubic-bezier(0.16, 1, 0.3, 1), box-shadow 380ms ease;
      cursor: pointer;
      text-decoration: none;
      user-select: none;
    }

    .white-image-box:hover {
      transform: translateY(-4px) scale(1.008);
      box-shadow: 0 24px 50px rgba(0, 0, 0, 0.6);
    }

    .white-image-box img {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      z-index: 10;
    }

    .placeholder-inner {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      gap: 8px;
      pointer-events: none;
    }

    .placeholder-icon {
      width: 40px;
      height: 40px;
      border: 2px dashed rgba(0, 0, 0, 0.3);
      border-radius: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: rgba(0, 0, 0, 0.5);
      margin-bottom: 4px;
    }

    .placeholder-tag {
      font-size: 10px;
      font-weight: 900;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: rgba(0, 0, 0, 0.45);
    }

    .placeholder-title {
      font-size: clamp(20px, 2.4vw, 32px);
      font-weight: 900;
      letter-spacing: -0.02em;
      color: #000000;
      line-height: 1.05;
      text-transform: uppercase;
      margin: 0;
    }

    .placeholder-sub {
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: rgba(0, 0, 0, 0.55);
    }

    /* Modernist corner marks */
    .placeholder-crosshair {
      position: absolute;
      width: 12px;
      height: 12px;
      pointer-events: none;
    }
    .cross-tl { top: 12px; left: 12px; border-top: 2px solid rgba(0, 0, 0, 0.25); border-left: 2px solid rgba(0, 0, 0, 0.25); }
    .cross-tr { top: 12px; right: 12px; border-top: 2px solid rgba(0, 0, 0, 0.25); border-right: 2px solid rgba(0, 0, 0, 0.25); }
    .cross-bl { bottom: 12px; left: 12px; border-bottom: 2px solid rgba(0, 0, 0, 0.25); border-left: 2px solid rgba(0, 0, 0, 0.25); }
    .cross-br { bottom: 12px; right: 12px; border-bottom: 2px solid rgba(0, 0, 0, 0.25); border-right: 2px solid rgba(0, 0, 0, 0.25); }

    /* Minimalist workshop specs line */
    .project-specs-bar {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: clamp(10px, 1.8vw, 20px);
      padding: 14px 20px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.1);
      margin-bottom: 36px;
      font-size: 12px;
      font-weight: 700;
      color: #aaaaaa;
      text-transform: uppercase;
      letter-spacing: 0.14em;
    }
    .project-specs-bar span.spec-val {
      color: #ffffff;
      font-weight: 900;
    }
    .project-specs-bar span.spec-sep {
      color: rgba(255, 255, 255, 0.2);
    }

    /* Grids */
    .grid-p01-top {
      display: grid;
      grid-template-columns: 1.25fr 1fr;
      gap: clamp(16px, 2.5vw, 28px);
      margin-bottom: clamp(16px, 2.5vw, 28px);
    }
    .grid-p01-bottom {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: clamp(16px, 2.5vw, 28px);
    }
    @media (max-width: 860px) {
      .grid-p01-top, .grid-p01-bottom { grid-template-columns: 1fr; }
    }

    .grid-p02-vertical {
      display: grid;
      grid-template-columns: 1fr 1fr 0.9fr;
      gap: clamp(16px, 2.2vw, 28px);
      align-items: stretch;
    }
    @media (max-width: 960px) {
      .grid-p02-vertical { grid-template-columns: 1fr; }
    }

    .grid-p03-offset-row1 {
      display: grid;
      grid-template-columns: 1.35fr 1fr;
      gap: clamp(16px, 2.5vw, 28px);
      margin-bottom: clamp(16px, 2.5vw, 28px);
    }
    .grid-p03-offset-row2 {
      display: grid;
      grid-template-columns: 1fr 1.35fr;
      gap: clamp(16px, 2.5vw, 28px);
    }
    @media (max-width: 860px) {
      .grid-p03-offset-row1, .grid-p03-offset-row2 { grid-template-columns: 1fr; }
    }

    .grid-p04-triptych {
      display: grid;
      grid-template-columns: 1.3fr 1fr 1fr;
      gap: clamp(16px, 2.2vw, 28px);
    }
    @media (max-width: 920px) {
      .grid-p04-triptych { grid-template-columns: 1fr; }
    }

    .grid-p05-gallery {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: clamp(16px, 2.5vw, 28px);
    }
    .grid-p05-subcol {
      display: flex;
      flex-direction: column;
      gap: clamp(16px, 2.5vw, 28px);
    }
    .grid-p05-twins {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: clamp(16px, 2.5vw, 28px);
    }
    @media (max-width: 860px) {
      .grid-p05-gallery { grid-template-columns: 1fr; }
      .grid-p05-twins { grid-template-columns: 1fr; }
    }

    .grid-p06-monumental-bottom {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: clamp(16px, 2.2vw, 28px);
      margin-top: clamp(16px, 2.5vw, 28px);
    }
    @media (max-width: 880px) {
      .grid-p06-monumental-bottom { grid-template-columns: 1fr; }
    }
"""

# Replace existing project views in standalone.html
sec_start = content.find('<!-- VIEW DETAIL: PROJET 01')
sec_end = content.find('<!-- VIEW 2: ABOUT (ACCESSIBLE VIA ROULETTE WITH * ABOUT *) -->')

if sec_start != -1 and sec_end != -1:
    content = content[:sec_start] + all_sections + "\n\n    " + content[sec_end:]
    print("Replaced project views with white image boxes and streamlined text.")
else:
    print("Error: Could not locate project views slice!", sec_start, sec_end)

# Insert the new CSS
css_target_tag = "/* =============================================================\n       DEDICATED PROJECT DETAIL VIEWS (6 DISTINCT EDITORIAL LAYOUTS)"
idx_css = content.find(css_target_tag)
if idx_css != -1:
    content = content[:idx_css] + new_css + "\n    " + content[idx_css:]
    print("CSS for white image boxes inserted.")
else:
    print("Warning: css_target_tag not found!")

with open('standalone.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved standalone.html successfully. New size:", len(content))
