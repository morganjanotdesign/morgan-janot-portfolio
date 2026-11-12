#!/usr/bin/env python3
import re
import os
import shutil

with open("portfolio.html", "r", encoding="utf-8") as f:
    html = f.read()

# Clean up any stray slash inside <img> tags from self-closing tags
html = re.sub(r'(<img\b[^>]*?)\s*/\s*(decoding="async"|width="\d+"|loading="lazy")', r'\1 \2', html)
html = re.sub(r'(<img\b[^>]*?)\s*/\s*(decoding="async"|width="\d+"|loading="lazy")', r'\1 \2', html)

# Lock legacy portfolio DOM elements with hidden + inline display:none !important
legacy_open_tags = [
    (r'<div class="portfolio-bg-year" id="portfolio-bg-year"[^>]*>',
     '<div class="portfolio-bg-year" id="portfolio-bg-year" aria-hidden="true" hidden style="display:none !important;visibility:hidden !important;">'),
    (r'<aside class="margin-stamp-lyon"[^>]*>',
     '<aside class="margin-stamp-lyon" aria-hidden="true" hidden style="display:none !important;visibility:hidden !important;">'),
    (r'<aside class="project-hover-desc desc-left" id="project-hover-desc-left"[^>]*>',
     '<aside class="project-hover-desc desc-left" id="project-hover-desc-left" aria-hidden="true" hidden style="display:none !important;visibility:hidden !important;">'),
    (r'<aside class="project-hover-desc desc-right" id="project-hover-desc-right"[^>]*>',
     '<aside class="project-hover-desc desc-right" id="project-hover-desc-right" aria-hidden="true" hidden style="display:none !important;visibility:hidden !important;">'),
    (r'<div class="site-intro-curtain" id="intro-curtain"[^>]*>',
     '<div class="site-intro-curtain" id="intro-curtain" role="banner" aria-label="Introduction Morgan Janot" hidden style="display:none !important;visibility:hidden !important;">'),
    (r'<header class="top-bar" id="top-bar"[^>]*>',
     '<header class="top-bar" id="top-bar" aria-hidden="true" hidden style="display:none !important;visibility:hidden !important;">'),
    (r'<div class="drawer-overlay" id="drawer-overlay"[^>]*>',
     '<div class="drawer-overlay" id="drawer-overlay" aria-hidden="true" hidden style="display:none !important;visibility:hidden !important;">'),
    (r'<aside class="projects-drawer" id="projects-drawer"[^>]*>',
     '<aside class="projects-drawer" id="projects-drawer" role="dialog" aria-modal="true" aria-label="Liste des projets" aria-hidden="true" hidden style="display:none !important;visibility:hidden !important;">'),
    (r'<div class="portfolio-mobile-desc" id="portfolio-mobile-desc"[^>]*>',
     '<div class="portfolio-mobile-desc" id="portfolio-mobile-desc" aria-live="polite" hidden style="display:none !important;visibility:hidden !important;">'),
]

for pat, repl in legacy_open_tags:
    html = re.sub(pat, repl, html, count=1)

responsive_css_marker_start = "/* === SPEED & COMPLETE RESPONSIVE ZERO-OVERLAP OPTIMIZATION START === */"
responsive_css_marker_end = "/* === SPEED & COMPLETE RESPONSIVE ZERO-OVERLAP OPTIMIZATION END === */"

html = re.sub(
    re.escape(responsive_css_marker_start) + r".*?" + re.escape(responsive_css_marker_end),
    "",
    html,
    flags=re.S
)

responsive_css = f"""
    {responsive_css_marker_start}
    /* ==========================================================================
       1. SUPPRESSION GLOBALE ET DÉFINITIVE DE TOUS LES ÉLÉMENTS DE L'ANCIEN PORTFOLIO
          (Empêche #top-bar, le logo dragon, * ABOUT * / * CONTACT *, le tiroir //,
           le filigrane 2026, le rideau d'intro et les bannières d'apparaître où que ce soit)
       ========================================================================== */
    #top-bar,
    .top-bar,
    #hero-banner,
    .hero-banner,
    #portfolio-bg-year,
    .portfolio-bg-year,
    .margin-stamp-lyon,
    .project-hover-desc,
    #project-hover-desc-left,
    #project-hover-desc-right,
    #intro-curtain,
    .site-intro-curtain,
    #projects-drawer,
    .projects-drawer,
    #drawer-overlay,
    .drawer-overlay,
    #sticky-roulette-dropdown,
    .sticky-roulette-dropdown,
    #sticky-center-wrapper,
    .sticky-center-wrapper,
    #portfolio-mobile-desc,
    .portfolio-mobile-desc {{
      display: none !important;
      visibility: hidden !important;
      opacity: 0 !important;
      pointer-events: none !important;
      width: 0 !important;
      height: 0 !important;
      overflow: hidden !important;
    }}

    /* Garantir le fond blanc pur et texte noir sur ABOUT et CONTACT comme sur HOME et WORK */
    html:has(body.view-is-about),
    body.view-is-about,
    html:has(body.view-is-contact),
    body.view-is-contact {{
      background: #ffffff !important;
      background-color: #ffffff !important;
      color: #000000 !important;
    }}

    /* ==========================================================================
       2. NAVIGATION SUPÉRIEURE (TONAJ / WORK / ABOUT / CONTACT) — ZÉRO COLLISION
       ========================================================================== */
    @media (max-width: 900px) {{
      .tonaj-home-nav,
      .tonaj-about-view .tonaj-home-nav,
      .tonaj-contact-view .tonaj-home-nav,
      .project-detail-section .proj-top-nav {{
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 48px !important;
        padding: 0 clamp(16px, 4.5vw, 32px) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        background: rgba(255, 255, 255, 0.94) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        z-index: 2600 !important;
        box-sizing: border-box !important;
        pointer-events: auto !important;
      }}

      #tonaj-home-page .tonaj-home-nav,
      #view-portfolio .tonaj-home-nav {{
        background: transparent !important;
        backdrop-filter: none !important;
        -webkit-backdrop-filter: none !important;
      }}

      .tonaj-home-link,
      .project-detail-section .proj-top-nav .tonaj-home-link,
      .tonaj-home-link.is-active,
      .tonaj-home-link[aria-current="page"] {{
        position: relative !important;
        left: auto !important;
        top: auto !important;
        transform: none !important;
        font-size: clamp(12px, 3.2vw, 15px) !important;
      }}
    }}

    /* ==========================================================================
       3. PAGE D'ACCUEIL (#tonaj-home-page) — ADAPTATION ÉCRANS COURTS & MOBILES
       ========================================================================== */
    .tonaj-home-center-box {{
      max-height: calc(100dvh - 140px) !important;
    }}

    @media (max-width: 680px) {{
      .tonaj-home-center-box {{
        width: min(82vw, 360px, calc(44dvh * 433 / 168)) !important;
      }}
    }}

    /* ==========================================================================
       4. PAGE WORK / PORTFOLIO (#view-portfolio) — RESPONSIVE TABLETTE & MOBILE
       ========================================================================== */
    @media (max-width: 680px) {{
      #view-portfolio .portfolio-section {{
        --carousel-card-size: min(52vw, 210px, 29dvh) !important;
        --carousel-stage-w: calc(var(--carousel-card-size) * 501 / 166) !important;
        top: 35% !important;
        left: 50% !important;
        transform: translate(-50%, -50%) !important;
      }}

      #view-portfolio .frames-grid .mosaic-cartouche {{
        padding: 7px 9px !important;
      }}

      #view-portfolio .frames-grid .mosaic-cartouche-tag {{
        font-size: clamp(7px, 2vw, 8.5px) !important;
      }}

      #view-portfolio .frames-grid .mosaic-cartouche-title {{
        font-size: clamp(11px, 3.2vw, 13.5px) !important;
      }}

      #view-portfolio .frames-grid .mosaic-cartouche-meta {{
        font-size: clamp(6.5px, 1.8vw, 7.5px) !important;
      }}

      .tonaj-work-active-desc {{
        position: absolute !important;
        top: 54.5% !important;
        bottom: auto !important;
        left: 20px !important;
        right: 20px !important;
        width: auto !important;
        max-width: 420px !important;
      }}

      .tonaj-work-active-desc-text {{
        font-size: clamp(11px, 3.1vw, 12.5px) !important;
        line-height: 1.4 !important;
      }}

      .tonaj-work-heading {{
        top: auto !important;
        bottom: 54px !important;
        left: 18px !important;
        font-size: min(12dvh, 18.5vw) !important;
        line-height: 0.82 !important;
      }}

      #view-portfolio .tonaj-home-lang {{
        left: 20px !important;
        bottom: 16px !important;
      }}

      #view-portfolio .tonaj-home-city {{
        left: auto !important;
        right: 20px !important;
        bottom: 16px !important;
      }}
    }}

    /* ==========================================================================
       5. PAGES ABOUT (#view-about) & CONTACT (#view-contact)
          Fidélité stricte à la maquette sur Desktop (> 960px) + Ordre propre sur Mobile (<= 960px)
       ========================================================================== */
    @media (min-width: 961px) {{
      /* Empêcher l'email et le téléphone de se toucher sur les écrans intermédiaires (961px - 1200px) */
      .tonaj-contact-huge-link {{
        font-size: clamp(17.5px, 2.95vw, 36px) !important;
      }}

      /* Sur écrans très peu hauts (< 680px de hauteur), ajuster le padding-top du formulaire Contact */
      @media (max-height: 680px) {{
        .tonaj-contact-green-block {{
          padding-top: clamp(70px, 16vh, 130px) !important;
        }}
        .tonaj-form-textarea {{
          height: clamp(54px, 10vh, 84px) !important;
        }}
      }}
    }}

    @media (max-width: 960px) {{
      /* Ordre logique sur Mobile/Tablette dans About : 1. Manifeste vert -> 2. Nom & Photo -> 3. Titre ABOUT */
      .tonaj-about-manifesto {{
        order: 1 !important;
      }}
      .tonaj-about-right-col {{
        order: 2 !important;
      }}
      .tonaj-about-giant-title-wrapper {{
        order: 3 !important;
      }}
    }}

    /* ==========================================================================
       6. PAGES PROJETS (#view-project-01..06) — RESPONSIVE TABLETTE & MOBILE
       ========================================================================== */
    @media (min-width: 821px) {{
      .proj-vertical-title {{
        font-size: clamp(42px, min(8.2vw, 11.5vh), 124px) !important;
      }}
    }}

    @media (max-width: 820px) {{
      :root {{
        --proj-margin-x: 4.5vw;
        --proj-content-width: 91vw;
        --proj-gap: 16px;
        --proj-section-gap: 38px;
        --proj-text-gap: 10px;
        --proj-top-offset: 72px;
        --proj-bottom-offset: 48px;
      }}

      .proj-title-rail {{
        position: relative !important;
        top: auto !important;
        left: auto !important;
        margin-bottom: 20px !important;
      }}

      .proj-vertical-title {{
        writing-mode: horizontal-tb !important;
        text-orientation: initial !important;
        font-size: clamp(34px, 10.5vw, 56px) !important;
        line-height: 0.96 !important;
        white-space: normal !important;
      }}

      .proj-content-grid {{
        width: 100% !important;
        max-width: 100% !important;
      }}

      .proj-span-3,
      .proj-span-4,
      .proj-span-5,
      .proj-span-6,
      .proj-span-7,
      .proj-span-8,
      .proj-span-12 {{
        grid-column: 1 / -1 !important;
      }}

      .proj-subcol-right {{
        width: 100% !important;
        align-self: stretch !important;
      }}

      .proj-fill-height {{
        height: auto !important;
        aspect-ratio: 4 / 3 !important;
      }}

      .proj-fill-height .proj-img {{
        position: relative !important;
      }}

      .proj-triptych-row {{
        grid-template-columns: 1fr !important;
      }}

      .proj-ratio-triptych-left {{
        aspect-ratio: 4 / 3 !important;
      }}

      .proj-footer-bar {{
        flex-direction: column !important;
        align-items: flex-start !important;
        gap: 12px !important;
      }}
    }}
    {responsive_css_marker_end}
"""

html = html.replace("  </style>", responsive_css + "\n  </style>", 1)

with open("portfolio.html", "w", encoding="utf-8") as f:
    f.write(html)

shutil.copyfile("portfolio.html", "index.html")
print(f"Updated portfolio.html and index.html ({os.path.getsize('portfolio.html')/1024:.1f} KB)")
