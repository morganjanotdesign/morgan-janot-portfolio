import re, shutil

# Create backup
shutil.copyfile('standalone.html', 'standalone.html.bak')

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

# 2. Build CSS
css_block = """
    /* =============================================================
       DEDICATED PROJECT DETAIL VIEWS (6 DISTINCT EDITORIAL LAYOUTS)
       ============================================================= */
    .project-detail-section {
      width: 100%;
      max-width: 1360px;
      margin: 0 auto;
      padding: clamp(20px, 4vh, 40px) clamp(24px, 5vw, 80px) 140px;
      box-sizing: border-box;
    }

    /* Top navigation bar inside each project */
    .project-header-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      padding-bottom: 24px;
      margin-bottom: 40px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.15);
    }

    .project-nav-btn {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: none;
      border: none;
      cursor: pointer;
      font-size: 12px;
      font-weight: 900;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: #ffffff;
      padding: 6px 0;
      transition: opacity 200ms ease, transform 200ms ease;
    }

    .project-nav-btn:hover {
      opacity: 0.65;
      transform: translateX(-3px);
    }

    .project-nav-btn.next:hover {
      transform: translateX(3px);
    }

    .project-counter-pill {
      font-size: 11px;
      font-weight: 900;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: #aaaaaa;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 6px 14px;
      border-radius: 2px;
    }

    .project-nav-arrows {
      display: flex;
      align-items: center;
      gap: 20px;
    }

    /* Universal Project Frame with tactile paper grain */
    .project-art-frame {
      position: relative;
      overflow: hidden;
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.6);
      transition: transform 450ms cubic-bezier(0.16, 1, 0.3, 1),
                  box-shadow 450ms cubic-bezier(0.16, 1, 0.3, 1),
                  filter 350ms ease;
    }

    .project-art-frame:hover {
      transform: translate3d(0, -6px, 0) scale(1.012);
      box-shadow: 0 32px 72px rgba(0, 0, 0, 0.75);
      filter: brightness(1.02);
    }

    .project-art-frame::before {
      content: "";
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 3;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 250 250' width='250' height='250'%3E%3Cfilter id='paperFibers' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.62' numOctaves='4' result='noise' stitchTiles='stitch'/%3E%3CfeColorMatrix type='matrix' values='3.5 0 0 0 -1.2  0 3.5 0 0 -1.2  0 0 3.5 0 -1.2  0 0 0 1 0' in='noise' result='contrasted'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23paperFibers)'/%3E%3C/svg%3E");
      background-size: 200px 200px;
      mix-blend-mode: multiply;
      opacity: 0.58;
      transition: opacity 350ms ease;
    }

    .project-art-frame::after {
      content: "";
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 4;
      background-image: 
        radial-gradient(ellipse at 50% 40%, rgba(255, 255, 255, 0.15) 0%, rgba(0, 0, 0, 0.30) 100%),
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 250 250' width='250' height='250'%3E%3Cfilter id='paperGrainTooth' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.78' numOctaves='3' result='noise' stitchTiles='stitch'/%3E%3CfeColorMatrix type='matrix' values='2.5 0 0 0 -0.7  0 2.5 0 0 -0.7  0 0 2.5 0 -0.7  0 0 0 1 0' in='noise' result='contrasted'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23paperGrainTooth)'/%3E%3C/svg%3E");
      background-size: 100% 100%, 160px 160px;
      background-repeat: no-repeat, repeat;
      mix-blend-mode: overlay;
      opacity: 0.80;
      box-shadow: inset 0 0 80px rgba(0, 0, 0, 0.22);
      transition: opacity 350ms ease;
    }

    .project-art-frame:hover::before { opacity: 0.68; }
    .project-art-frame:hover::after { opacity: 0.95; }

    .project-art-frame .frame-illustration {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: clamp(16px, 2.5vw, 36px);
      box-sizing: border-box;
      pointer-events: none;
      transition: transform 450ms cubic-bezier(0.16, 1, 0.3, 1);
    }

    .project-art-frame:hover .frame-illustration {
      transform: translate3d(2px, -3px, 0) scale(1.018);
    }

    .project-art-frame .frame-illustration svg {
      width: auto;
      height: 90%;
      max-width: 92%;
      object-fit: contain;
    }

    /* Cartouche signature translucide en bas avec léger flou */
    .project-detail-cartouche {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      width: 100%;
      box-sizing: border-box;
      z-index: 25;
      pointer-events: none;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: center;
      padding: clamp(20px, 2.6vw, 34px) clamp(22px, 3vw, 40px);
      background: rgba(255, 255, 255, 0.16);
      backdrop-filter: blur(8px) saturate(130%);
      -webkit-backdrop-filter: blur(8px) saturate(130%);
      border: none;
      box-shadow: 0 -1px 0 rgba(255, 255, 255, 0.22), 0 -8px 20px rgba(0, 0, 0, 0.04);
    }

    .detail-cartouche-tag {
      font-size: 11px;
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: 0.2em;
      color: rgba(0, 0, 0, 0.85);
      margin-bottom: 4px;
    }

    .detail-cartouche-title {
      font-size: clamp(24px, 3.2vw, 46px);
      font-weight: 900;
      letter-spacing: -0.03em;
      color: #000000;
      line-height: 1.05;
      margin: 0 0 6px 0;
    }

    .detail-cartouche-meta {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 10px;
      font-weight: 900;
      letter-spacing: 0.18em;
      color: rgba(0, 0, 0, 0.7);
    }

    /* SPECIFIC LAYOUT 01: STAGGERED ASYMMETRIC (FAUTEUIL NUAGE) */
    .layout-01-grid {
      display: grid;
      grid-template-columns: 1.35fr 1fr;
      gap: clamp(32px, 4vw, 64px);
      align-items: start;
      margin-bottom: 48px;
    }

    @media (max-width: 960px) {
      .layout-01-grid { grid-template-columns: 1fr; }
    }

    .layout-01-grid .project-art-frame {
      aspect-ratio: 440 / 380;
      min-height: 420px;
    }

    .layout-01-card-spec {
      background: rgba(204, 255, 0, 0.05);
      border-left: 3px solid #ccff00;
      padding: 24px 28px;
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      margin-top: 28px;
    }

    .layout-01-bottom-stats {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      padding-top: 36px;
      border-top: 1px solid rgba(255, 255, 255, 0.14);
      margin-top: 40px;
    }

    @media (max-width: 640px) {
      .layout-01-bottom-stats { grid-template-columns: 1fr; }
    }

    .stat-pill-box {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.10);
      padding: 16px 20px;
      font-size: 11px;
      font-weight: 900;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    /* SPECIFIC LAYOUT 02: 3-COLUMN BLUEPRINT (LAMPADAIRE ARTICULÉ) */
    .layout-02-blueprint-grid {
      display: grid;
      grid-template-columns: 1fr 1.3fr 1fr;
      gap: clamp(24px, 3vw, 44px);
      align-items: stretch;
      margin-bottom: 48px;
    }

    @media (max-width: 1040px) {
      .layout-02-blueprint-grid { grid-template-columns: 1fr; }
    }

    .layout-02-blueprint-grid .project-art-frame {
      aspect-ratio: 380 / 680;
      min-height: 520px;
    }

    .blueprint-spec-table {
      background: rgba(255, 0, 127, 0.04);
      border: 1px solid rgba(255, 0, 127, 0.25);
      padding: 24px;
      margin-top: 24px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .blueprint-row {
      display: flex;
      justify-content: space-between;
      font-size: 12px;
      font-weight: 700;
      padding-bottom: 8px;
      border-bottom: 1px dashed rgba(255, 255, 255, 0.15);
    }
    .blueprint-row span:first-child { color: #888888; text-transform: uppercase; font-size: 10px; letter-spacing: 0.15em; }
    .blueprint-row span:last-child { color: #ffffff; font-weight: 900; }

    /* SPECIFIC LAYOUT 03: DIAGONAL CHECKERBOARD (CHAISE SUSPENDUE) */
    .layout-03-checkerboard {
      display: flex;
      flex-direction: column;
      gap: 40px;
      margin-bottom: 48px;
    }

    .checkerboard-row-1 {
      display: grid;
      grid-template-columns: 1fr 1.3fr;
      gap: clamp(32px, 4vw, 64px);
      align-items: center;
    }

    .checkerboard-row-2 {
      display: grid;
      grid-template-columns: 1.3fr 1fr;
      gap: clamp(32px, 4vw, 64px);
      align-items: center;
      padding-top: 36px;
      border-top: 1px solid rgba(255, 255, 255, 0.12);
    }

    @media (max-width: 900px) {
      .checkerboard-row-1, .checkerboard-row-2 { grid-template-columns: 1fr; }
    }

    .layout-03-checkerboard .project-art-frame {
      aspect-ratio: 1 / 1;
      min-height: 420px;
    }

    .checkerboard-tech-card {
      background: rgba(0, 245, 255, 0.05);
      border: 1px solid rgba(0, 245, 255, 0.25);
      padding: 28px;
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 18px;
    }

    @media (max-width: 600px) {
      .checkerboard-tech-card { grid-template-columns: 1fr; }
    }

    /* SPECIFIC LAYOUT 04: MONUMENTAL LANDSCAPE HERO + TRIPTYCH (CANAPÉ GALET) */
    .layout-04-landscape-frame {
      width: 100%;
      aspect-ratio: 21 / 9;
      min-height: 380px;
      max-height: 520px;
      margin-bottom: 48px;
    }

    @media (max-width: 768px) {
      .layout-04-landscape-frame { aspect-ratio: 16 / 9; }
    }

    .layout-04-triptych {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 36px;
      padding-top: 36px;
      border-top: 1px solid rgba(255, 255, 255, 0.15);
      margin-bottom: 48px;
    }

    @media (max-width: 860px) {
      .layout-04-triptych { grid-template-columns: 1fr; }
    }

    .triptych-col {
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    /* SPECIFIC LAYOUT 05: ART CATALOG SPREAD (VASE COROLLE) */
    .layout-05-spread {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: clamp(36px, 5vw, 72px);
      align-items: start;
      margin-bottom: 48px;
    }

    @media (max-width: 900px) {
      .layout-05-spread { grid-template-columns: 1fr; }
    }

    .layout-05-spread .project-art-frame {
      aspect-ratio: 400 / 520;
      min-height: 460px;
    }

    .catalog-certif-box {
      background: rgba(200, 75, 255, 0.05);
      border: 1px solid rgba(200, 75, 255, 0.3);
      padding: 24px;
      margin-top: 24px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    /* SPECIFIC LAYOUT 06: SWISS BRUTALIST POSTER (ARCHE RADIALE) */
    .layout-06-brutalist-wrap {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-bottom: 48px;
    }

    .layout-06-hero-frame {
      width: 100%;
      aspect-ratio: 16 / 10;
      min-height: 440px;
      max-height: 580px;
      margin-bottom: 44px;
    }

    .layout-06-modular-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 28px;
      width: 100%;
      padding-top: 36px;
      border-top: 2px solid #ffeb00;
    }

    @media (max-width: 960px) {
      .layout-06-modular-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 580px) {
      .layout-06-modular-grid { grid-template-columns: 1fr; }
    }

    /* Bottom next-project teaser & return button */
    .project-footer-card {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 24px;
      padding: 28px 36px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.12);
      margin-top: 60px;
      transition: background 250ms ease, border-color 250ms ease;
    }

    .project-footer-card:hover {
      background: rgba(255, 255, 255, 0.07);
      border-color: rgba(255, 255, 255, 0.25);
    }

    .next-teaser-info {
      display: flex;
      align-items: center;
      gap: 20px;
    }

    .next-teaser-swatch {
      width: 44px;
      height: 44px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
    }

    .next-teaser-swatch::before {
      content: "";
      position: absolute;
      inset: 0;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 250 250' width='250' height='250'%3E%3Cfilter id='paperFibers' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.62' numOctaves='4' result='noise' stitchTiles='stitch'/%3E%3CfeColorMatrix type='matrix' values='3.5 0 0 0 -1.2  0 3.5 0 0 -1.2  0 0 3.5 0 -1.2  0 0 0 1 0' in='noise' result='contrasted'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23paperFibers)'/%3E%3C/svg%3E");
      background-size: 100px 100px;
      mix-blend-mode: multiply;
      opacity: 0.5;
    }
"""

# Insert CSS right before /* Accessibility focus */
css_target = "    /* Accessibility focus */"
if css_target in content:
    content = content.replace(css_target, css_block + "\n" + css_target)
    print("CSS successfully inserted.")
else:
    print("Warning: css_target not found!")

# 3. Build HTML for 6 projects
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

# Project 01 HTML
p1 = pdata['project-01']
html_p1 = f"""    <!-- VIEW DETAIL: PROJET 01 (FAUTEUIL NUAGE - STAGGERED ASYMMETRIC) -->
    <section id="view-project-01" class="view-panel project-detail-section">
{make_top_bar(0)}

      <div class="editorial-tag-row">
        <span class="editorial-tag">01 // Mobilier Éditorial</span>
        <span class="chroma-badge" style="background: rgba(204, 255, 0, 0.2); color: #ccff00; border: 1px solid rgba(204, 255, 0, 0.4);">
          * ÉDITION LIMITÉE 12 EXEMPLAIRES *
        </span>
      </div>

      <h1 class="editorial-h1" style="margin-bottom: 20px;">Fauteuil Nuage</h1>
      <p class="editorial-lead" style="max-width: 880px; margin-bottom: 48px;">
        Une assise monolithique en apesanteur, explorant la densité d'un volume gonflé d'air et la radicalité chromatique du vert acide.
      </p>

      <!-- GRILLE ASYMÉTRIQUE 62% / 38% -->
      <div class="layout-01-grid">
        <div>
          <div class="project-art-frame" style="background-color: {p1['bg_color']};">
            <div class="frame-illustration">
              <svg {p1['svg_attrs']}>
                {p1['svg_inner']}
              </svg>
            </div>
            <div class="project-detail-cartouche">
              <div class="detail-cartouche-tag">01 — Architecture d'Assise // Paris 2025</div>
              <h2 class="detail-cartouche-title">* FAUTEUIL NUAGE *</h2>
              <div class="detail-cartouche-meta">
                <span>PROTOTYPE N°01</span>
                <span style="font-size: 13px;">*</span>
                <span>TIRAGE NUMÉROTÉ D'ART</span>
              </div>
            </div>
          </div>
        </div>

        <div>
          <div class="editorial-col-heading">
            <span class="mini-swatch" style="background-color: {p1['bg_color']};"></span>
            Genèse &amp; Anatomie de la Forme
          </div>
          <div class="editorial-text" style="margin-bottom: 24px;">
            <p>
              Né d'un dessin spontané en atelier, le Fauteuil Nuage rompt avec l'austérité géométrique traditionnelle. Sa silhouette organique semble flotter au-dessus du plancher, défiant la rigidité de la structure interne par un capitonnage continu sans couture apparente.
            </p>
            <p>
              Chaque courbe a été modelée pour offrir une prise tactile généreuse tout en affirmant une présence sculpturale forte dans l'espace contemporain.
            </p>
          </div>

          <div class="layout-01-card-spec">
            <div class="editorial-col-heading" style="color: #ffffff; margin-bottom: 12px;">
              Fiche Matériaux &amp; Procédés
            </div>
            <ul class="editorial-ul" style="font-size: 13px; line-height: 1.7; color: #cccccc;">
              <li>&bull; Mousse polyuréthane multi-densité (35 à 50 kg/m³) injectée</li>
              <li>&bull; Velours de laine bouclée texturé sur mesure (teinte Acid Lime)</li>
              <li>&bull; Châssis tubulaire en acier électrosoudé masqué</li>
              <li>&bull; Dimensions : 94 &times; 102 &times; H 82 cm (assise 41 cm)</li>
              <li>&bull; Poids net : 28 kg &mdash; Fabriqué à la main en Île-de-France</li>
            </ul>
          </div>
        </div>
      </div>

      <blockquote class="editorial-quote-card" style="border-left-color: {p1['bg_color']};">
        <p class="quote-text">
          « Morgan Janot réinvente le fauteuil d'apparat contemporain en lui injectant une insolence chromatique électrisante et un confort enveloppant. »
        </p>
        <cite class="quote-author">&mdash; Gazette du Design &amp; Architecture, Milan (2025)</cite>
      </blockquote>

      <div class="layout-01-bottom-stats">
        <div class="stat-pill-box">
          <span style="color: {p1['bg_color']};">&bull;</span>
          <span>12 EX. NUMÉROTÉS</span>
        </div>
        <div class="stat-pill-box">
          <span style="color: {p1['bg_color']};">&bull;</span>
          <span>ACQUISITION MOBILIER NATIONAL</span>
        </div>
        <div class="stat-pill-box">
          <span style="color: {p1['bg_color']};">&bull;</span>
          <span>SÉLECTION SALONE MILAN 2025</span>
        </div>
      </div>

{make_footer(0)}
    </section>"""

# Project 02 HTML
p2 = pdata['project-02']
html_p2 = f"""    <!-- VIEW DETAIL: PROJET 02 (LAMPADAIRE ARTICULÉ - 3-COLUMN BLUEPRINT) -->
    <section id="view-project-02" class="view-panel project-detail-section">
{make_top_bar(1)}

      <div class="editorial-tag-row">
        <span class="editorial-tag">02 // Design d'Espace</span>
        <span class="chroma-badge" style="background: rgba(255, 0, 127, 0.2); color: #ff55a3; border: 1px solid rgba(255, 0, 127, 0.4);">
          * PROTOTYPE CINÉTIQUE BREVETÉ *
        </span>
      </div>

      <h1 class="editorial-h1" style="margin-bottom: 20px;">Lampadaire Articulé</h1>
      <p class="editorial-lead" style="max-width: 880px; margin-bottom: 48px;">
        Un équilibre mécanique parfait entre bras télescopiques en porte-à-faux et faisceau lumineux directionnel haute fidélité.
      </p>

      <!-- GRILLE 3 COLONNES D'INGÉNIERIE : 28% / 44% / 28% -->
      <div class="layout-02-blueprint-grid">
        <!-- Col 1 : Cinématique & Balancier -->
        <div>
          <div class="editorial-col-heading">
            <span class="mini-swatch" style="background-color: {p2['bg_color']};"></span>
            Mécanique du Balancier
          </div>
          <div class="editorial-text" style="font-size: 14px; margin-bottom: 16px;">
            <p>
              Le système d'articulation repose sur deux pivots à friction sèche usinés en laiton massif. Le contrepoids cylindrique compense exactement la portée du bras supérieur de 180 cm sans aucun ressort visible.
            </p>
          </div>

          <div class="blueprint-spec-table">
            <div class="blueprint-row">
              <span>Portée max</span>
              <span>220 cm</span>
            </div>
            <div class="blueprint-row">
              <span>Rotation mât</span>
              <span>360&deg; continue</span>
            </div>
            <div class="blueprint-row">
              <span>Débattement</span>
              <span>110 à 240 cm</span>
            </div>
            <div class="blueprint-row">
              <span>Contrepoids laiton</span>
              <span>8.4 kg usiné CNC</span>
            </div>
            <div class="blueprint-row">
              <span>Finition</span>
              <span>Laque époxy Cyber Magenta</span>
            </div>
          </div>
        </div>

        <!-- Col 2 : Estampe Totem Verticale au centre -->
        <div>
          <div class="project-art-frame" style="background-color: {p2['bg_color']};">
            <div class="frame-illustration">
              <svg {p2['svg_attrs']}>
                {p2['svg_inner']}
              </svg>
            </div>
            <div class="project-detail-cartouche">
              <div class="detail-cartouche-tag">02 — Cinétique &amp; Lumière // Studio 2025</div>
              <h2 class="detail-cartouche-title">* LAMPADAIRE ARTICULÉ *</h2>
              <div class="detail-cartouche-meta">
                <span>PIVOT À FRICTION SÈCHE</span>
                <span style="font-size: 13px;">*</span>
                <span>ROTATION 360&deg;</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Col 3 : Philosophie & Optique -->
        <div>
          <div class="editorial-col-heading">
            <span class="mini-swatch" style="background-color: {p2['bg_color']};"></span>
            Philosophie de l'Éclairage
          </div>
          <div class="editorial-text" style="font-size: 14px; margin-bottom: 16px;">
            <p>
              L'intention est de sculpter l'obscurité. La tête lumineuse intègre une lentille collimatrice micro-prismatique diffusant un cône de lumière douce et précis de 38&deg;, sans éblouissement latéral.
            </p>
          </div>

          <div class="blueprint-spec-table" style="border-color: rgba(255, 255, 255, 0.15); background: rgba(255, 255, 255, 0.04);">
            <div class="blueprint-row">
              <span>Source lumineuse</span>
              <span>Module LED COB 2700K</span>
            </div>
            <div class="blueprint-row">
              <span>Indice de rendu</span>
              <span>CRI Ra &gt; 98</span>
            </div>
            <div class="blueprint-row">
              <span>Flux utile</span>
              <span>2 400 lumens</span>
            </div>
            <div class="blueprint-row">
              <span>Contrôle</span>
              <span>Variateur tactile capacitif</span>
            </div>
            <div class="blueprint-row">
              <span>Câblage</span>
              <span>Tressé soie noire intégrée</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Frise des 3 configurations d'usage -->
      <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 24px 32px; display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px;">
        <div>
          <div style="font-size: 11px; font-weight: 900; letter-spacing: 0.18em; text-transform: uppercase; color: {p2['bg_color']}; margin-bottom: 6px;">
            01 &bull; Lecture Basse (45&deg;)
          </div>
          <p style="font-size: 13px; color: #aaaaaa; margin: 0; line-height: 1.5;">
            Faisceau concentré au-dessus d'une assise ou d'un bureau de travail, sans fuite parasite.
          </p>
        </div>
        <div>
          <div style="font-size: 11px; font-weight: 900; letter-spacing: 0.18em; text-transform: uppercase; color: {p2['bg_color']}; margin-bottom: 6px;">
            02 &bull; Zénithal Central (90&deg;)
          </div>
          <p style="font-size: 13px; color: #aaaaaa; margin: 0; line-height: 1.5;">
            Portée de 220 cm remplaçant une suspension de plafond sans perçage de dalle.
          </p>
        </div>
        <div>
          <div style="font-size: 11px; font-weight: 900; letter-spacing: 0.18em; text-transform: uppercase; color: {p2['bg_color']}; margin-bottom: 6px;">
            03 &bull; Sculpture Réfléchie (135&deg;)
          </div>
          <p style="font-size: 13px; color: #aaaaaa; margin: 0; line-height: 1.5;">
            Éclairage indirect dirigé vers une paroi ou un mur d'exposition pour un bain de lumière diffuse.
          </p>
        </div>
      </div>

{make_footer(1)}
    </section>"""

# Project 03 HTML
p3 = pdata['project-03']
html_p3 = f"""    <!-- VIEW DETAIL: PROJET 03 (CHAISE SUSPENDUE - DIAGONAL CHECKERBOARD) -->
    <section id="view-project-03" class="view-panel project-detail-section">
{make_top_bar(2)}

      <div class="editorial-tag-row">
        <span class="editorial-tag">03 // Structure Géométrique</span>
        <span class="chroma-badge" style="background: rgba(0, 245, 255, 0.2); color: #00f0ff; border: 1px solid rgba(0, 245, 255, 0.4);">
          * ÉTUDE TENSIONNELLE EN APESANTEUR *
        </span>
      </div>

      <h1 class="editorial-h1" style="margin-bottom: 20px;">Chaise Suspendue</h1>
      <p class="editorial-lead" style="max-width: 880px; margin-bottom: 48px;">
        L'abolition des pieds traditionnels au profit d'un treillis géométrique autoportant ancré au plafond par des liens invisibles.
      </p>

      <!-- GRILLE EN DAMIER / CHECKERBOARD -->
      <div class="layout-03-checkerboard">
        <!-- Rangée 1 : Texte gauche + Estampe carrée droite -->
        <div class="checkerboard-row-1">
          <div>
            <div class="editorial-col-heading">
              <span class="mini-swatch" style="background-color: {p3['bg_color']};"></span>
              Le Vide Comme Matériau
            </div>
            <div class="editorial-text">
              <p>
                En éliminant tout contact direct avec le sol, la Chaise Suspendue libère la surface habitable et crée une sensation d'apesanteur immédiate. La structure triangulée répartit les forces de traction le long de câbles tressés invisibles à l'œil nu.
              </p>
              <p>
                L'assise se comporte comme une membrane en suspension dynamique qui réagit subtilement aux mouvements du corps.
              </p>
            </div>
          </div>

          <div>
            <div class="project-art-frame" style="background-color: {p3['bg_color']};">
              <div class="frame-illustration">
                <svg {p3['svg_attrs']}>
                  {p3['svg_inner']}
                </svg>
              </div>
              <div class="project-detail-cartouche">
                <div class="detail-cartouche-tag">03 — Structure Géométrique // Paris 2026</div>
                <h2 class="detail-cartouche-title">* CHAISE SUSPENDUE *</h2>
                <div class="detail-cartouche-meta">
                  <span>ANCRAGE MONOPHONIQUE</span>
                  <span style="font-size: 13px;">*</span>
                  <span>DYNEEMA &amp; TITANE</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Rangée 2 : Cartouche technique 4 modules gauche + Citation droite -->
        <div class="checkerboard-row-2">
          <div class="checkerboard-tech-card">
            <div>
              <div style="font-size: 11px; font-weight: 900; letter-spacing: 0.16em; text-transform: uppercase; color: {p3['bg_color']}; margin-bottom: 6px;">
                Suspension
              </div>
              <p style="font-size: 13px; color: #ffffff; margin: 0; line-height: 1.4;">
                Corde synthétique Dyneema SK78 tressée 4mm (rupture &gt; 1 800 kg).
              </p>
            </div>
            <div>
              <div style="font-size: 11px; font-weight: 900; letter-spacing: 0.16em; text-transform: uppercase; color: {p3['bg_color']}; margin-bottom: 6px;">
                Armature
              </div>
              <p style="font-size: 13px; color: #ffffff; margin: 0; line-height: 1.4;">
                Profilés cintrés en titane Ti-6Al-4V microbillé haute rigidité.
              </p>
            </div>
            <div>
              <div style="font-size: 11px; font-weight: 900; letter-spacing: 0.16em; text-transform: uppercase; color: {p3['bg_color']}; margin-bottom: 6px;">
                Membrane
              </div>
              <p style="font-size: 13px; color: #ffffff; margin: 0; line-height: 1.4;">
                Toile composite aramide thermocollée découpée laser sans effilochage.
              </p>
            </div>
            <div>
              <div style="font-size: 11px; font-weight: 900; letter-spacing: 0.16em; text-transform: uppercase; color: {p3['bg_color']}; margin-bottom: 6px;">
                Charge Certifiée
              </div>
              <p style="font-size: 13px; color: #ffffff; margin: 0; line-height: 1.4;">
                Éprouvée à 260 kg en charge dynamique (Bureau Veritas).
              </p>
            </div>
          </div>

          <div>
            <blockquote class="editorial-quote-card" style="border-left-color: {p3['bg_color']}; margin: 0;">
              <p class="quote-text">
                « Une expérience quasi-méditative où le corps épouse les oscillations imperceptibles de l'air ambiant. »
              </p>
              <cite class="quote-author">&mdash; Exposition Pavillon de l'Arsenal (2024)</cite>
            </blockquote>
          </div>
        </div>
      </div>

{make_footer(2)}
    </section>"""

# Project 04 HTML
p4 = pdata['project-04']
html_p4 = f"""    <!-- VIEW DETAIL: PROJET 04 (CANAPÉ GALET - MONUMENTAL LANDSCAPE) -->
    <section id="view-project-04" class="view-panel project-detail-section">
{make_top_bar(3)}

      <div class="editorial-tag-row">
        <span class="editorial-tag">04 // Recherche Formelle</span>
        <span class="chroma-badge" style="background: rgba(255, 94, 0, 0.2); color: #ff904d; border: 1px solid rgba(255, 94, 0, 0.4);">
          * MONOLITHE SCULPTURAL &amp; CUIR PATINÉ *
        </span>
      </div>

      <h1 class="editorial-h1" style="margin-bottom: 20px;">Canapé Galet</h1>
      <p class="editorial-lead" style="max-width: 880px; margin-bottom: 40px;">
        Une masse rocheuse adoucie par l'érosion géologique du temps, accueillant un orbe sphérique mobile en cuir naturel ciré.
      </p>

      <!-- IMMENSE ESTAMPE PANORAMIQUE PAYSAGE 21:9 -->
      <div class="project-art-frame layout-04-landscape-frame" style="background-color: {p4['bg_color']};">
        <div class="frame-illustration">
          <svg {p4['svg_attrs']}>
            {p4['svg_inner']}
          </svg>
        </div>
        <div class="project-detail-cartouche">
          <div class="detail-cartouche-tag">04 — Recherche Formelle // Atelier Janot</div>
          <h2 class="detail-cartouche-title">* CANAPÉ GALET *</h2>
          <div class="detail-cartouche-meta">
            <span>VOLUME MONOBLOC</span>
            <span style="font-size: 13px;">*</span>
            <span>ORBE EN CUIR PLEINE FLEUR</span>
          </div>
        </div>
      </div>

      <!-- TRIPTYQUE INFÉRIEUR (3 COLONNES DISTINCTES) -->
      <div class="layout-04-triptych">
        <div class="triptych-col">
          <div class="editorial-col-heading">
            <span class="mini-swatch" style="background-color: {p4['bg_color']};"></span>
            01 &bull; Érosion &amp; Géologie
          </div>
          <div class="editorial-text" style="font-size: 14px; margin: 0;">
            <p>
              Inspiré par les galets de granit polis par les marées de l'Atlantique, ce canapé élimine tout angle saillant. Sa silhouette asymétrique permet trois postures d'assise distinctes : assise formelle à droite, lounge décontracté au centre, et méridienne de repos à gauche.
            </p>
          </div>
        </div>

        <div class="triptych-col">
          <div class="editorial-col-heading">
            <span class="mini-swatch" style="background-color: {p4['bg_color']};"></span>
            02 &bull; Cuir &amp; Sellerie d'Art
          </div>
          <div class="editorial-text" style="font-size: 14px; margin: 0;">
            <p>
              La sphère d'appoint mobile de 42 cm est confectionnée en cuir de taurillon pleine fleur patiné manuellement à la cire d'abeille et pigments minéraux. Elle fait office d'accoudoir déplaçable, de cale-dos ou d'objet sculptural indépendant.
            </p>
          </div>
        </div>

        <div class="triptych-col">
          <div class="editorial-col-heading">
            <span class="mini-swatch" style="background-color: {p4['bg_color']};"></span>
            03 &bull; Données d'Atelier
          </div>
          <ul class="editorial-ul" style="font-size: 13px; line-height: 1.8; color: #cccccc;">
            <li>&bull; L 285 &times; P 138 &times; H 76 cm (assise 38 cm)</li>
            <li>&bull; Poids total : 115 kg (monobloc indéformable)</li>
            <li>&bull; Structure en multiplis de hêtre durable français</li>
            <li>&bull; Mousse végétale à base d'huile de ricin</li>
            <li>&bull; Fabrication artisanale sur commande (8 semaines)</li>
          </ul>
        </div>
      </div>

{make_footer(3)}
    </section>"""

# Project 05 HTML
p5 = pdata['project-05']
html_p5 = f"""    <!-- VIEW DETAIL: PROJET 05 (VASE COROLLE - ART CATALOG SPREAD) -->
    <section id="view-project-05" class="view-panel project-detail-section">
{make_top_bar(4)}

      <div class="editorial-tag-row">
        <span class="editorial-tag">05 // Édition Limitée</span>
        <span class="chroma-badge" style="background: rgba(200, 75, 255, 0.2); color: #d97dff; border: 1px solid rgba(200, 75, 255, 0.4);">
          * CRISTAL DE MURANO SOUFFLÉ BOUCHE *
        </span>
      </div>

      <h1 class="editorial-h1" style="margin-bottom: 20px;">Vase Corolle</h1>
      <p class="editorial-lead" style="max-width: 880px; margin-bottom: 48px;">
        La capture instantanée d'un mouvement de rotation liquide figé pour l'éternité dans le cristal incandescent.
      </p>

      <!-- DOUBLE-PAGE CATALOGUE D'ART 50% / 50% -->
      <div class="layout-05-spread">
        <!-- Volet Gauche : L'Estampe et le Certificat de Galerie -->
        <div>
          <div class="project-art-frame" style="background-color: {p5['bg_color']};">
            <div class="frame-illustration">
              <svg {p5['svg_attrs']}>
                {p5['svg_inner']}
              </svg>
            </div>
            <div class="project-detail-cartouche">
              <div class="detail-cartouche-tag">05 — Cristal Soufflé // Édition Limitée 08 Ex.</div>
              <h2 class="detail-cartouche-title">* VASE COROLLE *</h2>
              <div class="detail-cartouche-meta">
                <span>SOUFFLÉ À LA VOLÉE</span>
                <span style="font-size: 13px;">*</span>
                <span>MURANO &mdash; PARIS</span>
              </div>
            </div>
          </div>

          <div class="catalog-certif-box">
            <div style="font-size: 10px; font-weight: 900; letter-spacing: 0.22em; text-transform: uppercase; color: {p5['bg_color']};">
              Certificat d'Authenticité d'Atelier
            </div>
            <div style="font-size: 13px; font-weight: 700; color: #ffffff;">
              Tirage d'Art Numéroté &mdash; Pièce 01 / 08
            </div>
            <p style="font-size: 12px; color: #aaaaaa; margin: 0; line-height: 1.5;">
              Signature gravée à la pointe diamant sous la base : <em>« M. Janot &mdash; Murano 2026 »</em>. Livré dans un coffret en noyer massif gainé de velours noir.
            </p>
          </div>
        </div>

        <!-- Volet Droit : Récit & Chromatique -->
        <div>
          <div class="editorial-col-heading">
            <span class="mini-swatch" style="background-color: {p5['bg_color']};"></span>
            Le Feu et le Souffle
          </div>
          <div class="editorial-text" style="margin-bottom: 32px;">
            <p>
              Réalisée à Venise en collaboration étroite avec les maîtres verriers de Murano, chaque corolle est façonnée à la canne sans moule restrictif. La force centrifuge appliquée lors de la rotation manuelle dicte l'évasement asymétrique des lèvres du vase.
            </p>
            <p>
              Le passage brutal de 1 250&deg;C à l'air libre impose une maîtrise gestuelle millimétrée : le verrier dispose de moins de 45 secondes avant que le verre ne commence à figer sa courbe.
            </p>
          </div>

          <div class="editorial-col-heading">
            <span class="mini-swatch" style="background-color: {p5['bg_color']};"></span>
            Spectre Chromatique Ultraviolet
          </div>
          <div class="editorial-text" style="margin-bottom: 32px;">
            <p>
              La nuance ultraviolette provient d'un dosage précis d'oxydes de manganèse et de traces de cobalt incorporés en bain de fusion. La matière vivante diffracte la lumière naturelle : violet profond sous ciel couvert, reflets fuchsia électriques en plein soleil.
            </p>
          </div>

          <div style="background: rgba(255, 255, 255, 0.04); border-left: 3px solid {p5['bg_color']}; padding: 20px 24px;">
            <div style="font-size: 12px; font-weight: 900; letter-spacing: 0.16em; text-transform: uppercase; color: #ffffff; margin-bottom: 8px;">
              Dimensions &amp; Métrologie
            </div>
            <div style="font-size: 13px; color: #bbbbbb; line-height: 1.6;">
              Hauteur : 48 cm &bull; Diamètre max : 36 cm &bull; Poids net : 9.2 kg de cristal pur à 24% PbO. Pièce unique non reproductible à l'identique.
            </div>
          </div>
        </div>
      </div>

{make_footer(4)}
    </section>"""

# Project 06 HTML
p6 = pdata['project-06']
html_p6 = f"""    <!-- VIEW DETAIL: PROJET 06 (ARCHE RADIALE - SWISS BRUTALIST POSTER) -->
    <section id="view-project-06" class="view-panel project-detail-section">
{make_top_bar(5)}

      <div class="editorial-tag-row" style="justify-content: center;">
        <span class="editorial-tag">06 // Manifesto &amp; Archive</span>
        <span class="chroma-badge" style="background: rgba(255, 235, 0, 0.2); color: #ffeb00; border: 1px solid rgba(255, 235, 0, 0.4);">
          * BIENNALE DE MILAN 2025 *
        </span>
      </div>

      <div style="text-align: center; max-width: 960px; margin: 0 auto 40px auto;">
        <h1 class="editorial-h1" style="font-size: clamp(42px, 7vw, 92px); margin-bottom: 16px;">* ARCHE RADIALE *</h1>
        <p class="editorial-lead" style="margin: 0 auto;">
          Une installation monumentale en 42 arches concentriques d'aluminium jaune solaire, créant une onde optique et sonore immersive.
        </p>
      </div>

      <!-- MONOLITHE HERO CENTRÉ -->
      <div class="layout-06-brutalist-wrap">
        <div class="project-art-frame layout-06-hero-frame" style="background-color: {p6['bg_color']};">
          <div class="frame-illustration">
            <svg {p6['svg_attrs']}>
              {p6['svg_inner']}
            </svg>
          </div>
          <div class="project-detail-cartouche">
            <div class="detail-cartouche-tag">06 — Manifeste &amp; Archive // Biennale de Milan</div>
            <h2 class="detail-cartouche-title">* ARCHE RADIALE *</h2>
            <div class="detail-cartouche-meta">
              <span>INSTALLATION 4.80M DE HAUT</span>
              <span style="font-size: 13px;">*</span>
              <span>42 ARCS EN ALUMINIUM ANODISÉ</span>
            </div>
          </div>
        </div>

        <!-- GRILLE 4 COLONNES MODULAIRE BRUTALISTE -->
        <div class="layout-06-modular-grid">
          <div>
            <div class="editorial-col-heading" style="color: {p6['bg_color']};">
              01 &bull; Moiré Optique
            </div>
            <p style="font-size: 13px; line-height: 1.6; color: #aaaaaa; margin: 0;">
              En circulant sous et autour de l'arche, le décalage angulaire de 2.5&deg; entre chaque arceau engendre un effet de moiré cinétique. La matière semble palpiter sous l'œil du visiteur.
            </p>
          </div>

          <div>
            <div class="editorial-col-heading" style="color: {p6['bg_color']};">
              02 &bull; Aluminium 6061
            </div>
            <p style="font-size: 13px; line-height: 1.6; color: #aaaaaa; margin: 0;">
              Profilés cintrés à froid par mandrin rotatif à commande numérique. Assemblage par clavetage conique invisible sans aucun point de soudure apparent.
            </p>
          </div>

          <div>
            <div class="editorial-col-heading" style="color: {p6['bg_color']};">
              03 &bull; Acoustique du Dôme
            </div>
            <p style="font-size: 13px; line-height: 1.6; color: #aaaaaa; margin: 0;">
              La géométrie parabolique concentre l'onde sonore à un foyer situé à 1.40 m du sol, produisant un chuchotement amplifié pour toute personne debout au centre.
            </p>
          </div>

          <div>
            <div class="editorial-col-heading" style="color: {p6['bg_color']};">
              04 &bull; Fiche Biennale
            </div>
            <ul class="editorial-ul" style="font-size: 12px; line-height: 1.7; color: #cccccc;">
              <li>&bull; Envergure : 6.40 m</li>
              <li>&bull; Hauteur : 4.80 m</li>
              <li>&bull; Finition : Anodisation 25&mu;m</li>
              <li>&bull; Poids structurel : 340 kg</li>
            </ul>
          </div>
        </div>
      </div>

{make_footer(5)}
    </section>"""

all_projects_html = "\n\n".join([html_p1, html_p2, html_p3, html_p4, html_p5, html_p6])

# Insert HTML right before <!-- VIEW 2: ABOUT (ACCESSIBLE VIA ROULETTE WITH * ABOUT *) -->
html_target = "    <!-- VIEW 2: ABOUT (ACCESSIBLE VIA ROULETTE WITH * ABOUT *) -->"
if html_target in content:
    content = content.replace(html_target, all_projects_html + "\n\n" + html_target)
    print("Project HTML views successfully inserted.")
else:
    print("Warning: html_target not found!")

# 4. Update JS panels dictionary and add showProjectDetail
# In JS:
js_panels_target = """      const panels = {
        portfolio: document.getElementById('view-portfolio'),
        about: document.getElementById('view-about'),
        contact: document.getElementById('view-contact')
      };"""

js_panels_replacement = """      const panels = {
        portfolio: document.getElementById('view-portfolio'),
        about: document.getElementById('view-about'),
        contact: document.getElementById('view-contact'),
        'project-01': document.getElementById('view-project-01'),
        'project-02': document.getElementById('view-project-02'),
        'project-03': document.getElementById('view-project-03'),
        'project-04': document.getElementById('view-project-04'),
        'project-05': document.getElementById('view-project-05'),
        'project-06': document.getElementById('view-project-06')
      };

      const projectTitles = {
        'project-01': 'Fauteuil Nuage',
        'project-02': 'Lampadaire Articulé',
        'project-03': 'Chaise Suspendue',
        'project-04': 'Canapé Galet',
        'project-05': 'Vase Corolle',
        'project-06': 'Arche Radiale'
      };

      function showProjectDetail(projectId) {
        if (!panels[projectId]) return;
        revealPanel(projectId);
        if (stickyTitle && projectTitles[projectId]) {
          stickyTitle.textContent = '* ' + projectTitles[projectId].toUpperCase() + ' *';
        }
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }"""

if js_panels_target in content:
    content = content.replace(js_panels_target, js_panels_replacement)
    print("JS panels dictionary successfully updated.")
else:
    print("Warning: js_panels_target not found!")

# 5. Update drawer link click handler and card click handlers
js_drawer_target = """      document.querySelectorAll('.drawer-project-link').forEach(function(link) {
        link.addEventListener('click', function(e) {
          e.preventDefault();
          const targetId = link.getAttribute('data-project-id');
          if (targetId) {
            navigateToProject(targetId);
          }
        });
      });"""

js_drawer_replacement = """      // CLIC SUR LES PROJETS DU TIROIR LATÉRAL -> OUVRIR LA PAGE DÉTAIL DU PROJET
      document.querySelectorAll('.drawer-project-link').forEach(function(link) {
        link.addEventListener('click', function(e) {
          e.preventDefault();
          const targetId = link.getAttribute('data-project-id');
          closeDrawer();
          if (targetId) {
            showProjectDetail(targetId);
          }
        });
      });

      // CLIC SUR LES CARTES DE PROJETS DE LA GRILLE PRINCIPALE -> OUVRIR LA PAGE DU PROJET
      document.querySelectorAll('.project-card').forEach(function(card) {
        card.style.cursor = 'pointer';
        card.addEventListener('click', function(e) {
          showProjectDetail(card.id);
        });
        card.addEventListener('keydown', function(e) {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            showProjectDetail(card.id);
          }
        });
      });

      // BOUTONS DE NAVIGATION INTER-PROJETS (PRÉCÉDENT / SUIVANT)
      document.querySelectorAll('.btn-switch-project').forEach(function(btn) {
        btn.addEventListener('click', function() {
          const target = btn.getAttribute('data-target-project');
          if (target) {
            showProjectDetail(target);
          }
        });
      });"""

if js_drawer_target in content:
    content = content.replace(js_drawer_target, js_drawer_replacement)
    print("JS drawer and card click handlers successfully updated.")
else:
    print("Warning: js_drawer_target not found!")

# 6. Update handleHash to support #project-01 ... #project-06
js_hash_target = """      // SYNCHRONISATION DU HASH DANS L'URL
      function handleHash() {
        const hash = (window.location.hash || '').replace('#', '').toLowerCase();
        const foundIdx = cycle.indexOf(hash);
        if (foundIdx !== -1) {
          activeIdx = foundIdx;
        } else {
          activeIdx = 0;
        }
        committedIdx = activeIdx;
        updateDrumLabels();
        revealPanel(cycle[committedIdx]);
      }"""

js_hash_replacement = """      // SYNCHRONISATION DU HASH DANS L'URL
      function handleHash() {
        const rawHash = (window.location.hash || '').replace('#', '').toLowerCase();
        if (rawHash.startsWith('project-') && panels[rawHash]) {
          showProjectDetail(rawHash);
          return;
        }
        const foundIdx = cycle.indexOf(rawHash);
        if (foundIdx !== -1) {
          activeIdx = foundIdx;
        } else {
          activeIdx = 0;
        }
        committedIdx = activeIdx;
        updateDrumLabels();
        revealPanel(cycle[committedIdx]);
      }"""

if js_hash_target in content:
    content = content.replace(js_hash_target, js_hash_replacement)
    print("JS handleHash successfully updated.")
else:
    print("Warning: js_hash_target not found!")

with open('standalone.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved standalone.html successfully, new size:", len(content))
