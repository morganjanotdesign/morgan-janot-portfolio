import base64
import os
import re

# 1. Load base64 for images in Project 01, 04, 06
b64_p1 = {}
for i in [1, 2, 3, 4, 5]:
    p = f'src/assets/images/project-01/{i}.webp'
    with open(p, 'rb') as fp:
        b64_p1[f'{i}.webp'] = base64.b64encode(fp.read()).decode('utf-8')

b64_p4 = {}
for f in ['IMG_7196.webp', 'IMG_7205.webp', 'IMG_7215.webp', 'IMG_7229.webp', 'IMG_7233.webp']:
    p = f'src/assets/images/project-04/{f}'
    with open(p, 'rb') as fp:
        b64_p4[f] = base64.b64encode(fp.read()).decode('utf-8')

b64_p6 = {}
for f in ['Capture d’écran 2026-09-30 à 22.46.10.webp', 'Capture d’écran 2026-09-30 à 22.46.58.webp']:
    p = f'src/assets/images/project-06/{f}'
    with open(p, 'rb') as fp:
        b64_p6[f] = base64.b64encode(fp.read()).decode('utf-8')

print("All image base64s loaded successfully!")

# Define CSS for Accordion Conception with Scattered Photos & Light/Dark Mode
theme_and_scatter_css = """
    /* ==========================================================================
       CONCEPTION ACCORDION MORPH & SCATTERED PHOTOS
       ========================================================================== */
    .conception-accordion-block {
      max-width: 1440px;
      margin: clamp(80px, 10vw, 150px) auto clamp(60px, 8vw, 120px) auto;
      padding: 0 clamp(16px, 4vw, 48px);
      box-sizing: border-box;
    }

    /* Accordion Trigger Header Button */
    .conception-tab-trigger {
      width: 100%;
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 8px;
      padding: clamp(28px, 4vw, 56px) clamp(20px, 3.5vw, 48px);
      text-align: left;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      gap: 16px;
      transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      overflow: hidden;
      box-sizing: border-box;
      color: inherit;
    }
    .conception-tab-trigger:hover {
      background: rgba(255, 255, 255, 0.045);
      border-color: rgba(255, 255, 255, 0.28);
      transform: translateY(-2px);
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.4);
    }
    .conception-tab-trigger::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 2px;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
      opacity: 0;
      transition: opacity 0.4s ease;
    }
    .conception-tab-trigger:hover::before {
      opacity: 1;
    }

    /* Category Tag */
    .conception-trigger-tag {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 11px;
      font-weight: 900;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: #888888;
      transition: color 0.4s ease;
    }
    .conception-trigger-tag .tag-dot {
      width: 8px;
      height: 8px;
      border-radius: 2px;
    }

    /* Title Row with Morphing Title & Pill Button */
    .conception-title-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
      flex-wrap: wrap;
    }

    /* Le Titre Conception Morphing : Gros de base, puis se transforme à l'ouverture */
    .conception-morph-title {
      margin: 0;
      padding: 0;
      font-size: clamp(48px, 6.5vw, 92px);
      font-weight: 900;
      letter-spacing: -0.03em;
      line-height: 1.0;
      color: #ffffff;
      transition: font-size 0.5s cubic-bezier(0.16, 1, 0.3, 1), transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), color 0.4s ease;
      will-change: font-size, transform;
    }

    /* Action Pill [ + Ouvrir le dossier ] / [ − Replier le dossier ] */
    .conception-action-pill {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 10px 22px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.2);
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: #ffffff;
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      flex-shrink: 0;
    }
    .conception-action-pill .pill-symbol {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.15);
      font-size: 14px;
      font-weight: 900;
      line-height: 1;
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .conception-action-pill .pill-count {
      color: #888888;
      font-size: 11px;
    }

    /* Subtitle description preview */
    .conception-desc-preview {
      margin: 0;
      font-size: clamp(14px, 1.15vw, 17px);
      font-weight: 300;
      line-height: 1.65;
      color: #bbbbbb;
      max-width: 720px;
      transition: opacity 0.4s ease, max-height 0.4s ease;
    }

    /* ÉTAT OUVERT (.is-open) */
    .conception-accordion-block.is-open .conception-tab-trigger {
      padding: clamp(20px, 3vw, 36px) clamp(20px, 3.5vw, 48px);
      background: rgba(255, 255, 255, 0.035);
      border-bottom-left-radius: 0;
      border-bottom-right-radius: 0;
      border-bottom-color: transparent;
    }
    .conception-accordion-block.is-open .conception-morph-title {
      font-size: clamp(26px, 3.2vw, 38px);
      letter-spacing: -0.01em;
    }
    .conception-accordion-block.is-open .conception-action-pill {
      background: rgba(255, 255, 255, 0.16);
      border-color: rgba(255, 255, 255, 0.38);
    }
    .conception-accordion-block.is-open .conception-action-pill .pill-symbol {
      transform: rotate(45deg);
    }

    /* Corps Dépliable */
    .conception-collapsible-body {
      max-height: 0;
      opacity: 0;
      overflow: hidden;
      pointer-events: none;
      transition: max-height 0.7s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), padding 0.5s ease;
      background: rgba(255, 255, 255, 0.015);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-top: none;
      border-bottom-left-radius: 8px;
      border-bottom-right-radius: 8px;
      box-sizing: border-box;
      padding: 0 clamp(20px, 3.5vw, 48px);
    }
    .conception-accordion-block.is-open .conception-collapsible-body {
      max-height: 3500px;
      opacity: 1;
      pointer-events: auto;
      padding: clamp(32px, 4.5vw, 64px) clamp(20px, 3.5vw, 48px);
    }

    /* SCATTERED DISPERSED STAGE : Disposition Aléatoire & Vivante */
    .conception-scatter-stage {
      display: grid;
      gap: clamp(24px, 3vw, 42px);
      align-items: center;
      position: relative;
      box-sizing: border-box;
      padding: clamp(16px, 2vw, 32px) 0;
    }
    .conception-scatter-stage.scatter-5 {
      grid-template-columns: 1fr 1fr 1.05fr;
    }
    .conception-scatter-stage.scatter-2 {
      grid-template-columns: 1fr 1fr;
    }
    .scatter-col {
      display: flex;
      flex-direction: column;
      gap: clamp(24px, 3vw, 38px);
    }

    /* Carte Photo Dispersée Individuelle */
    .scatter-photo-card {
      position: relative;
      border-radius: 6px;
      overflow: hidden;
      background-color: #121214;
      border: 1px solid rgba(255, 255, 255, 0.12);
      box-shadow: 0 16px 45px rgba(0, 0, 0, 0.75);
      transition: transform 0.45s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.45s ease, z-index 0s, border-color 0.4s ease;
      cursor: pointer;
      will-change: transform;
    }
    .scatter-photo-card.aspect-4-3 {
      aspect-ratio: 4 / 3;
    }
    .scatter-photo-card.tall-fill {
      height: 100%;
      min-height: 380px;
    }
    .scatter-photo-card img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* Effet tactile au survol : la photo se redresse, s'agrandit et s'élève vers l'utilisateur */
    .scatter-photo-card:hover {
      transform: rotate(0deg) scale(1.07) translateY(-14px) !important;
      z-index: 40 !important;
      border-color: rgba(255, 255, 255, 0.4) !important;
      box-shadow: 0 35px 80px rgba(0, 0, 0, 0.95), 0 0 0 1px rgba(255, 255, 255, 0.2) !important;
    }
    .scatter-photo-card:hover img {
      transform: scale(1.02);
    }

    /* DISPERSION ORGANIQUE POUR PROJET 01 (5 PHOTOS) */
    .scatter-p01-1 { transform: rotate(-3.2deg) translateY(-8px); }
    .scatter-p01-2 { transform: rotate(2.8deg) translateY(14px); }
    .scatter-p01-3 { transform: rotate(-2.2deg) translateY(-12px); }
    .scatter-p01-4 { transform: rotate(3.5deg) translateY(10px); }
    .scatter-p01-5 { transform: rotate(-1.5deg) translateY(-4px); }

    /* DISPERSION ORGANIQUE POUR PROJET 04 (5 PHOTOS) */
    .scatter-p04-1 { transform: rotate(-2.8deg) translateY(-6px); }
    .scatter-p04-2 { transform: rotate(3.2deg) translateY(16px); }
    .scatter-p04-3 { transform: rotate(-3.6deg) translateY(6px); }
    .scatter-p04-4 { transform: rotate(2.2deg) translateY(-10px); }
    .scatter-p04-5 { transform: rotate(-1.2deg) translateY(2px); }

    /* DISPERSION ORGANIQUE POUR PROJET 06 (2 PHOTOS) */
    .scatter-p06-1 { transform: rotate(-2.6deg) translateY(-6px); }
    .scatter-p06-2 { transform: rotate(2.8deg) translateY(12px); }

    /* Animation d'éclosion dispersée à l'ouverture */
    @keyframes scatterBurst {
      0% {
        opacity: 0;
        transform: scale(0.8) translate(0, 30px) rotate(0deg);
      }
      100% {
        opacity: 1;
      }
    }
    .conception-accordion-block.is-open .scatter-photo-card {
      animation: scatterBurst 0.65s cubic-bezier(0.16, 1, 0.3, 1) backwards;
    }
    .conception-accordion-block.is-open .scatter-item-1 { animation-delay: 0.05s; }
    .conception-accordion-block.is-open .scatter-item-2 { animation-delay: 0.12s; }
    .conception-accordion-block.is-open .scatter-item-3 { animation-delay: 0.18s; }
    .conception-accordion-block.is-open .scatter-item-4 { animation-delay: 0.24s; }
    .conception-accordion-block.is-open .scatter-item-5 { animation-delay: 0.30s; }

    @media (max-width: 900px) {
      .conception-scatter-stage.scatter-5 {
        grid-template-columns: 1fr !important;
      }
      .conception-scatter-stage.scatter-2 {
        grid-template-columns: 1fr !important;
      }
      .scatter-photo-card {
        transform: none !important;
      }
      .scatter-photo-card:hover {
        transform: scale(1.02) !important;
      }
    }

    /* ==========================================================================
       THEME CLAIR / SOMBRE (INVERSION NOIR ET BLANC)
       ========================================================================== */
    body.light-mode {
      background-color: #f7f7f9 !important;
      color: #0d0d11 !important;
    }
    body.light-mode .top-bar {
      background: rgba(247, 247, 249, 0.92) !important;
      border-bottom-color: rgba(0, 0, 0, 0.08) !important;
    }
    body.light-mode .brand-title {
      color: #0d0d11 !important;
    }
    body.light-mode .sticky-center-title {
      color: #0d0d11 !important;
    }
    body.light-mode .slash-mark {
      background-color: #0d0d11 !important;
    }
    body.light-mode .margin-stamp-lyon {
      color: rgba(0, 0, 0, 0.35) !important;
    }

    body.light-mode .drum-slot-center {
      color: #0d0d11 !important;
    }
    body.light-mode .drum-slot-btn {
      color: rgba(0, 0, 0, 0.45) !important;
    }
    body.light-mode .sticky-roulette-dropdown {
      background: rgba(255, 255, 255, 0.96) !important;
      border-color: rgba(0, 0, 0, 0.1) !important;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.12) !important;
    }

    /* Panneau latéral des projets */
    body.light-mode .projects-drawer {
      background: #ffffff !important;
      color: #0d0d11 !important;
      border-left-color: rgba(0, 0, 0, 0.1) !important;
      box-shadow: -24px 0 80px rgba(0, 0, 0, 0.15) !important;
    }
    body.light-mode .drawer-header {
      border-bottom-color: rgba(0, 0, 0, 0.08) !important;
    }
    body.light-mode .drawer-title {
      color: #0d0d11 !important;
    }
    body.light-mode .drawer-subtitle {
      color: #555560 !important;
    }
    body.light-mode .drawer-project-link {
      background: rgba(0, 0, 0, 0.03) !important;
      border-color: rgba(0, 0, 0, 0.07) !important;
      color: #0d0d11 !important;
    }
    body.light-mode .drawer-project-link:hover {
      background: rgba(0, 0, 0, 0.06) !important;
      border-color: rgba(0, 0, 0, 0.2) !important;
    }
    body.light-mode .drawer-project-title {
      color: #0d0d11 !important;
    }
    body.light-mode .drawer-arrow {
      background: rgba(0, 0, 0, 0.05) !important;
      border-color: rgba(0, 0, 0, 0.1) !important;
      color: #0d0d11 !important;
    }
    body.light-mode .drawer-footer {
      background: #f7f7f9 !important;
      border-top-color: rgba(0, 0, 0, 0.08) !important;
    }
    body.light-mode .drawer-footer-btn {
      background: rgba(0, 0, 0, 0.05) !important;
      border-color: rgba(0, 0, 0, 0.1) !important;
      color: #0d0d11 !important;
    }

    /* Contrôle de thème dans le panneau latéral droit */
    .drawer-theme-section {
      padding: 18px 24px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      display: flex;
      flex-direction: column;
      gap: 12px;
      background: rgba(255, 255, 255, 0.02);
    }
    body.light-mode .drawer-theme-section {
      border-bottom-color: rgba(0, 0, 0, 0.08) !important;
      background: rgba(0, 0, 0, 0.015) !important;
    }
    .drawer-theme-meta {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.18em;
      color: rgba(255, 255, 255, 0.5);
    }
    body.light-mode .drawer-theme-meta {
      color: #666670 !important;
    }
    .drawer-theme-val {
      font-weight: 900;
      color: #ffffff;
    }
    body.light-mode .drawer-theme-val {
      color: #0d0d11 !important;
    }
    .drawer-theme-toggle-wrap {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px;
      background: rgba(255, 255, 255, 0.06);
      padding: 4px;
      border-radius: 12px;
      border: 1px solid rgba(255, 255, 255, 0.1);
    }
    body.light-mode .drawer-theme-toggle-wrap {
      background: rgba(0, 0, 0, 0.05) !important;
      border-color: rgba(0, 0, 0, 0.1) !important;
    }
    .theme-switch-btn {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 9px 12px;
      border-radius: 9px;
      border: none;
      background: transparent;
      color: rgba(255, 255, 255, 0.5);
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.08em;
      cursor: pointer;
      transition: all 0.25s ease;
    }
    body.light-mode .theme-switch-btn {
      color: #666670 !important;
    }
    .theme-switch-btn.active {
      background: rgba(255, 255, 255, 0.18);
      color: #ffffff;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
    }
    body.light-mode .theme-switch-btn.active {
      background: #ffffff !important;
      color: #0d0d11 !important;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1) !important;
    }

    /* Bouton d'accès rapide dans la top-bar */
    .top-theme-quick-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #ffffff;
      cursor: pointer;
      transition: all 0.3s ease;
      margin-right: 12px;
    }
    .top-theme-quick-btn:hover {
      background: rgba(255, 255, 255, 0.16);
      transform: scale(1.08);
    }
    body.light-mode .top-theme-quick-btn {
      background: rgba(0, 0, 0, 0.05) !important;
      border-color: rgba(0, 0, 0, 0.12) !important;
      color: #0d0d11 !important;
    }
    body.light-mode .top-theme-quick-btn:hover {
      background: rgba(0, 0, 0, 0.1) !important;
    }

    /* Vues Projets et Textes en Light Mode */
    body.light-mode .view-panel {
      background-color: #f7f7f9 !important;
      color: #0d0d11 !important;
    }
    body.light-mode .project-header-title,
    body.light-mode .hero-concept-title {
      color: #0d0d11 !important;
    }
    body.light-mode .project-header-desc,
    body.light-mode .hero-concept-thesis {
      color: #2b2b32 !important;
    }
    body.light-mode .project-desc {
      color: #2b2b32 !important;
    }
    body.light-mode .p1-showcase-text p {
      color: #2b2b32 !important;
    }
    body.light-mode .project-specs-bar {
      background: rgba(0, 0, 0, 0.04) !important;
      border-color: rgba(0, 0, 0, 0.08) !important;
      color: #555560 !important;
    }
    body.light-mode .project-specs-bar .spec-val {
      color: #0d0d11 !important;
    }
    body.light-mode .project-nav-btn {
      color: #0d0d11 !important;
      border-color: rgba(0, 0, 0, 0.15) !important;
    }
    body.light-mode .project-counter-pill {
      background: rgba(0, 0, 0, 0.05) !important;
      border-color: rgba(0, 0, 0, 0.12) !important;
      color: #555560 !important;
    }
    body.light-mode .project-footer-card {
      background: rgba(0, 0, 0, 0.03) !important;
      border-color: rgba(0, 0, 0, 0.08) !important;
    }
    body.light-mode .next-teaser-info div > div:last-child {
      color: #0d0d11 !important;
    }

    /* Accordion Conception en Light Mode */
    body.light-mode .conception-tab-trigger {
      background: rgba(0, 0, 0, 0.02) !important;
      border-color: rgba(0, 0, 0, 0.1) !important;
    }
    body.light-mode .conception-tab-trigger:hover {
      background: rgba(0, 0, 0, 0.04) !important;
      border-color: rgba(0, 0, 0, 0.2) !important;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.08) !important;
    }
    body.light-mode .conception-morph-title {
      color: #0d0d11 !important;
    }
    body.light-mode .conception-desc-preview {
      color: #555560 !important;
    }
    body.light-mode .conception-action-pill {
      background: rgba(0, 0, 0, 0.05) !important;
      border-color: rgba(0, 0, 0, 0.12) !important;
      color: #0d0d11 !important;
    }
    body.light-mode .conception-action-pill .pill-symbol {
      background: rgba(0, 0, 0, 0.08) !important;
      color: #0d0d11 !important;
    }
    body.light-mode .conception-collapsible-body {
      background: rgba(0, 0, 0, 0.015) !important;
      border-color: rgba(0, 0, 0, 0.1) !important;
    }
    body.light-mode .scatter-photo-card {
      background-color: #ffffff !important;
      border-color: rgba(0, 0, 0, 0.12) !important;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.12) !important;
    }
    body.light-mode .scatter-photo-card:hover {
      border-color: rgba(0, 0, 0, 0.3) !important;
      box-shadow: 0 32px 75px rgba(0, 0, 0, 0.22) !important;
    }

    /* About & Contact views en Light Mode */
    body.light-mode .about-editorial-title,
    body.light-mode .contact-title {
      color: #0d0d11 !important;
    }
    body.light-mode .about-body,
    body.light-mode .contact-body {
      color: #2b2b32 !important;
    }
"""

# HTML Template for Project 01 Conception (5 photos dispersées)
p1_conception_accordion = f"""      <!-- 5. SECTION CONCEPTION : DOSSIER DÉPLIABLE & PHOTOS DISPERSÉES -->
      <div class="conception-accordion-block" id="conception-accordion-p01">
        <button type="button" class="conception-tab-trigger btn-conception-toggle" aria-expanded="false" aria-controls="conception-body-p01">
          <div class="conception-trigger-tag">
            <span class="tag-dot" style="background: rgba(255, 255, 255, 0.8);"></span>
            <span>01 // PROCESSUS &amp; RECHERCHES</span>
          </div>
          <div class="conception-title-row">
            <h2 class="conception-morph-title">Conception</h2>
            <span class="conception-action-pill">
              <span class="pill-symbol">+</span>
              <span class="pill-label">Ouvrir le dossier</span>
              <span class="pill-count">[ 05 photos ]</span>
            </span>
          </div>
          <p class="conception-desc-preview">
            Recherches de formes, exploration des principes d’assemblage et maquettes d’atelier. Décomposition des modules et expérimentation de la modularité à l'échelle.
          </p>
        </button>

        <div class="conception-collapsible-body" id="conception-body-p01">
          <div class="conception-scatter-stage scatter-5">
            <!-- Colonne 1 : Photos 01 & 03 -->
            <div class="scatter-col">
              <div class="scatter-photo-card aspect-4-3 scatter-p01-1 scatter-item-1">
                <img src="data:image/webp;base64,{b64_p1['1.webp']}" alt="Conception Fog Chair - Exploration maquette 01" loading="lazy">
              </div>
              <div class="scatter-photo-card aspect-4-3 scatter-p01-3 scatter-item-3">
                <img src="data:image/webp;base64,{b64_p1['3.webp']}" alt="Conception Fog Chair - Exploration maquette 03" loading="lazy">
              </div>
            </div>

            <!-- Colonne 2 : Photos 02 & 04 -->
            <div class="scatter-col">
              <div class="scatter-photo-card aspect-4-3 scatter-p01-2 scatter-item-2">
                <img src="data:image/webp;base64,{b64_p1['2.webp']}" alt="Conception Fog Chair - Exploration maquette 02" loading="lazy">
              </div>
              <div class="scatter-photo-card aspect-4-3 scatter-p01-4 scatter-item-4">
                <img src="data:image/webp;base64,{b64_p1['4.webp']}" alt="Conception Fog Chair - Exploration maquette 04" loading="lazy">
              </div>
            </div>

            <!-- Colonne 3 : Photo 05 (Portrait vertical) -->
            <div class="scatter-photo-card tall-fill scatter-p01-5 scatter-item-5">
              <img src="data:image/webp;base64,{b64_p1['5.webp']}" alt="Conception Fog Chair - Exploration maquette 05" loading="lazy">
            </div>
          </div>
        </div>
      </div>
"""

# HTML Template for Project 04 Conception (5 photos dispersées)
p4_conception_accordion = f"""      <!-- 4. SECTION CONCEPTION : DOSSIER DÉPLIABLE & PHOTOS DISPERSÉES -->
      <div class="conception-accordion-block" id="conception-accordion-p04">
        <button type="button" class="conception-tab-trigger btn-conception-toggle" aria-expanded="false" aria-controls="conception-body-p04">
          <div class="conception-trigger-tag">
            <span class="tag-dot" style="background: rgba(227, 6, 19, 0.85);"></span>
            <span>04 // PROCESSUS &amp; RECHERCHES</span>
          </div>
          <div class="conception-title-row">
            <h2 class="conception-morph-title">Conception</h2>
            <span class="conception-action-pill">
              <span class="pill-symbol">+</span>
              <span class="pill-label">Ouvrir le dossier</span>
              <span class="pill-count">[ 05 photos ]</span>
            </span>
          </div>
          <p class="conception-desc-preview">
            Recherches de formes, exploration des principes d’assemblage et maquettes d’atelier. Expérimentations sur la géométrie et la résistance des éléments structurels.
          </p>
        </button>

        <div class="conception-collapsible-body" id="conception-body-p04">
          <div class="conception-scatter-stage scatter-5">
            <!-- Colonne 1 : Photos 01 & 03 -->
            <div class="scatter-col">
              <div class="scatter-photo-card aspect-4-3 scatter-p04-1 scatter-item-1">
                <img src="data:image/webp;base64,{b64_p4['IMG_7196.webp']}" alt="Conception Chaise Suspendue - Maquette atelier 01" loading="lazy">
              </div>
              <div class="scatter-photo-card aspect-4-3 scatter-p04-3 scatter-item-3">
                <img src="data:image/webp;base64,{b64_p4['IMG_7215.webp']}" alt="Conception Chaise Suspendue - Exploration géométrique 03" loading="lazy">
              </div>
            </div>

            <!-- Colonne 2 : Photos 02 & 04 -->
            <div class="scatter-col">
              <div class="scatter-photo-card aspect-4-3 scatter-p04-2 scatter-item-2">
                <img src="data:image/webp;base64,{b64_p4['IMG_7205.webp']}" alt="Conception Chaise Suspendue - Maquette atelier 02" loading="lazy">
              </div>
              <div class="scatter-photo-card aspect-4-3 scatter-p04-4 scatter-item-4">
                <img src="data:image/webp;base64,{b64_p4['IMG_7229.webp']}" alt="Conception Chaise Suspendue - Exploration géométrique 04" loading="lazy">
              </div>
            </div>

            <!-- Colonne 3 : Photo 05 (Portrait vertical) -->
            <div class="scatter-photo-card tall-fill scatter-p04-5 scatter-item-5">
              <img src="data:image/webp;base64,{b64_p4['IMG_7233.webp']}" alt="Conception Chaise Suspendue - Prototype en situation 05" loading="lazy">
            </div>
          </div>
        </div>
      </div>
"""

# HTML Template for Project 06 Conception (2 photos dispersées)
p6_conception_accordion = f"""      <!-- 4. SECTION CONCEPTION : DOSSIER DÉPLIABLE & PHOTOS DISPERSÉES -->
      <div class="conception-accordion-block" id="conception-accordion-p06">
        <button type="button" class="conception-tab-trigger btn-conception-toggle" aria-expanded="false" aria-controls="conception-body-p06">
          <div class="conception-trigger-tag">
            <span class="tag-dot" style="background: rgba(255, 235, 0, 0.9);"></span>
            <span>06 // PROCESSUS &amp; MODÉLISATION 3D</span>
          </div>
          <div class="conception-title-row">
            <h2 class="conception-morph-title">Conception</h2>
            <span class="conception-action-pill">
              <span class="pill-symbol">+</span>
              <span class="pill-label">Ouvrir le dossier</span>
              <span class="pill-count">[ 02 photos ]</span>
            </span>
          </div>
          <p class="conception-desc-preview">
            Études de structure filaire, modélisation volumétrique 3D et calage des proportions de la cage en acier.
          </p>
        </button>

        <div class="conception-collapsible-body" id="conception-body-p06">
          <div class="conception-scatter-stage scatter-2">
            <div class="scatter-photo-card scatter-p06-1 scatter-item-1" style="aspect-ratio: 16/10;">
              <img src="data:image/webp;base64,{b64_p6['Capture d’écran 2026-09-30 à 22.46.10.webp']}" alt="Conception LEO-11 - Vue CAO filaire 3D 01" loading="lazy">
            </div>
            <div class="scatter-photo-card scatter-p06-2 scatter-item-2" style="aspect-ratio: 16/10;">
              <img src="data:image/webp;base64,{b64_p6['Capture d’écran 2026-09-30 à 22.46.58.webp']}" alt="Conception LEO-11 - Vue CAO filaire 3D 02" loading="lazy">
            </div>
          </div>
        </div>
      </div>
"""

# HTML for Drawer Theme Switcher & Top Bar Quick Toggle
drawer_theme_html = """      <!-- SÉLECTEUR DE THÈME D'AFFICHAGE (MENU DE DROITE) -->
      <div class="drawer-theme-section">
        <div class="drawer-theme-meta">
          <span class="drawer-theme-label"><span class="drawer-pulse-dot" style="background: currentColor;"></span> MODE D'AFFICHAGE</span>
          <span class="drawer-theme-val" id="drawer-theme-status">SOMBRE</span>
        </div>
        <div class="drawer-theme-toggle-wrap">
          <button type="button" class="theme-switch-btn active" id="btn-theme-dark" aria-label="Activer le mode sombre">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
            </svg>
            <span>Sombre</span>
          </button>
          <button type="button" class="theme-switch-btn" id="btn-theme-light" aria-label="Activer le mode clair">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="5"></circle>
              <line x1="12" y1="1" x2="12" y2="3"></line>
              <line x1="12" y1="21" x2="12" y2="23"></line>
              <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
              <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
              <line x1="1" y1="12" x2="3" y2="12"></line>
              <line x1="21" y1="12" x2="23" y2="12"></line>
              <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
              <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
            </svg>
            <span>Clair</span>
          </button>
        </div>
      </div>
"""

top_bar_quick_theme_html = """    <!-- Bouton Accès Rapide Thème (Sombre / Clair) -->
    <div style="display: flex; align-items: center;">
      <button type="button" class="top-theme-quick-btn" id="top-theme-quick-btn" aria-label="Basculer le mode sombre / clair" title="Basculer le mode clair / sombre">
        <svg id="theme-icon-moon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
        </svg>
        <svg id="theme-icon-sun" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: none;">
          <circle cx="12" cy="12" r="5"></circle>
          <line x1="12" y1="1" x2="12" y2="3"></line>
          <line x1="12" y1="21" x2="12" y2="23"></line>
          <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
          <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
          <line x1="1" y1="12" x2="3" y2="12"></line>
          <line x1="21" y1="12" x2="23" y2="12"></line>
          <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
          <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
        </svg>
      </button>
"""

# JavaScript for Accordion Toggle & Theme Switching
js_logic = """
      // =========================================================================
      // GESTION DU THÈME CLAIR / SOMBRE (INVERSION NOIR & BLANC)
      // =========================================================================
      const btnThemeDark = document.getElementById('btn-theme-dark');
      const btnThemeLight = document.getElementById('btn-theme-light');
      const drawerThemeStatus = document.getElementById('drawer-theme-status');
      const topThemeQuickBtn = document.getElementById('top-theme-quick-btn');
      const themeIconMoon = document.getElementById('theme-icon-moon');
      const themeIconSun = document.getElementById('theme-icon-sun');

      function applyTheme(theme) {
        if (theme === 'light') {
          pageBody.classList.add('light-mode');
          if (btnThemeDark) btnThemeDark.classList.remove('active');
          if (btnThemeLight) btnThemeLight.classList.add('active');
          if (drawerThemeStatus) drawerThemeStatus.textContent = 'CLAIR';
          if (themeIconMoon) themeIconMoon.style.display = 'none';
          if (themeIconSun) themeIconSun.style.display = 'block';
        } else {
          pageBody.classList.remove('light-mode');
          if (btnThemeDark) btnThemeDark.classList.add('active');
          if (btnThemeLight) btnThemeLight.classList.remove('active');
          if (drawerThemeStatus) drawerThemeStatus.textContent = 'SOMBRE';
          if (themeIconMoon) themeIconMoon.style.display = 'block';
          if (themeIconSun) themeIconSun.style.display = 'none';
        }
        try {
          localStorage.setItem('mj_theme', theme);
        } catch(e) {}
      }

      function toggleTheme() {
        const isLight = pageBody.classList.contains('light-mode');
        applyTheme(isLight ? 'dark' : 'light');
      }

      if (btnThemeDark) btnThemeDark.addEventListener('click', function() { applyTheme('dark'); });
      if (btnThemeLight) btnThemeLight.addEventListener('click', function() { applyTheme('light'); });
      if (topThemeQuickBtn) topThemeQuickBtn.addEventListener('click', toggleTheme);

      // Restaurer le thème sauvegardé
      try {
        const savedTheme = localStorage.getItem('mj_theme');
        if (savedTheme === 'light') {
          applyTheme('light');
        } else {
          applyTheme('dark');
        }
      } catch(e) {}

      // =========================================================================
      // GESTION DES ONGLETS DE CONCEPTION (DÉPLIAGE, TITRE MORPHING & PHOTOS DISPERSÉES)
      // =========================================================================
      document.querySelectorAll('.btn-conception-toggle').forEach(function(btn) {
        btn.addEventListener('click', function(e) {
          e.preventDefault();
          const block = btn.closest('.conception-accordion-block');
          if (!block) return;
          const isOpen = block.classList.contains('is-open');
          
          if (isOpen) {
            block.classList.remove('is-open');
            btn.setAttribute('aria-expanded', 'false');
            const label = btn.querySelector('.pill-label');
            const sym = btn.querySelector('.pill-symbol');
            if (label) label.textContent = 'Ouvrir le dossier';
            if (sym) sym.textContent = '+';
          } else {
            block.classList.add('is-open');
            btn.setAttribute('aria-expanded', 'true');
            const label = btn.querySelector('.pill-label');
            const sym = btn.querySelector('.pill-symbol');
            if (label) label.textContent = 'Replier le dossier';
            if (sym) sym.textContent = '−';
          }
        });
      });
"""

files_to_update = [
    'standalone.html',
    'portfolio.html',
    '/Users/morganjanot/.gemini/antigravity/brain/df18ad40-ac30-4b7a-b04f-f3de4961c66b/portfolio.html'
]

for path in files_to_update:
    if not os.path.exists(path):
        continue

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add CSS
    if '.conception-accordion-block' not in content:
        style_close = content.find('</style>')
        assert style_close != -1
        content = content[:style_close] + theme_and_scatter_css + content[style_close:]

    # 2. Add Drawer Theme Switcher if not present
    if 'drawer-theme-section' not in content:
        drawer_header_idx = content.find('<div class="drawer-header">')
        assert drawer_header_idx != -1
        # Insert after <div class="drawer-header">
        close_header_div = content.find('</div>', drawer_header_idx + len('<div class="drawer-header">') + 200) # after title-group
        assert close_header_div != -1
        # Find where drawer-header ends
        # In fact, right after <div class="drawer-title-group"> ... </div></div>
        header_end = content.find('</div>\n\n    <!-- Corps du panneau', drawer_header_idx)
        if header_end == -1:
            header_end = content.find('</div>\n    <!-- Corps du panneau', drawer_header_idx)
        assert header_end != -1
        content = content[:header_end] + '\n' + drawer_theme_html + content[header_end:]

    # 3. Add Top Bar Quick Toggle if not present
    if 'top-theme-quick-btn' not in content:
        menu_btn_marker = '<div class="top-icon-menu" id="top-menu-btn"'
        idx_menu = content.find(menu_btn_marker)
        assert idx_menu != -1
        # wrap with flex or insert before
        content = content[:idx_menu] + top_bar_quick_theme_html + content[idx_menu:]
        # close the flex wrapper right after top-menu-btn
        close_menu = content.find('</div>\n  </header>', idx_menu)
        if close_menu == -1:
            close_menu = content.find('</div>\n    </div>\n  </header>', idx_menu)
        assert close_menu != -1
        content = content[:close_menu+6] + '\n    </div>' + content[close_menu+6:]

    # 4. Replace Conception section in Project 01
    p1_old_start = content.find('<!-- 5. SECTION CONCEPTION : RECHERCHES & MAQUETTES')
    if p1_old_start != -1:
        p1_old_end = content.find('<!-- 5. Universal Next Project Teaser Footer -->', p1_old_start)
        assert p1_old_end != -1
        content = content[:p1_old_start] + p1_conception_accordion + '\n      ' + content[p1_old_end:]

    # 5. Replace Conception section in Project 04
    p4_old_start = content.find('<!-- 4. SECTION CONCEPTION : RECHERCHES & MAQUETTES')
    if p4_old_start == -1:
        p4_old_start = content.find('<!-- SECTION CONCEPTION : RECHERCHES & MAQUETTES (PHOTOS 01 À 05 DU DOSSIER 04)')
    if p4_old_start != -1:
        p4_old_end = content.find('<!-- 4. Universal Next Project Teaser Footer -->', p4_old_start)
        assert p4_old_end != -1
        content = content[:p4_old_start] + p4_conception_accordion + '\n      ' + content[p4_old_end:]

    # 6. Replace Conception section in Project 06
    p6_old_start = content.find('<!-- 4. SECTION CONCEPTION : RECHERCHES & MODÉLISATION 3D')
    if p6_old_start == -1:
        p6_old_start = content.find('<!-- SECTION CONCEPTION : RECHERCHES & MODÉLISATION 3D')
    if p6_old_start != -1:
        p6_old_end = content.find('<!-- 4. Universal Next Project Teaser Footer -->', p6_old_start)
        assert p6_old_end != -1
        content = content[:p6_old_start] + p6_conception_accordion + '\n      ' + content[p6_old_end:]

    # 7. Add JS logic before </script>
    if 'applyTheme' not in content:
        script_close = content.rfind('})();\n  </script>')
        if script_close == -1:
            script_close = content.rfind('})();\n</script>')
        assert script_close != -1
        content = content[:script_close] + js_logic + '\n      ' + content[script_close:]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {path} successfully!")

print("All HTML files processed!")
