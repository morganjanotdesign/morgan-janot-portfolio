#!/usr/bin/env python3
import re
import os
import shutil

with open("portfolio.html", "r", encoding="utf-8") as f:
    html = f.read()

# Clean up any stray slash inside <img> tags from self-closing tags
html = re.sub(r'(<img\b[^>]*?)\s*/\s*(decoding="async"|width="\d+"|loading="lazy")', r'\1 \2', html)
html = re.sub(r'(<img\b[^>]*?)\s*/\s*(decoding="async"|width="\d+"|loading="lazy")', r'\1 \2', html)

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
       OPTIMISATION RESPONSIVE COMPLÈTE & ZÉRO SUPERPOSITION (TOUS ÉCRANS)
       Couvre Desktop Large, Laptop 13"/14", Tablette Portrait/Paysage et Mobile
       ========================================================================== */

    /* 1. NAVIGATION SUPÉRIEURE (TONAJ / WORK / ABOUT / CONTACT) — ZÉRO COLLISION */
    @media (max-width: 900px) {{
      .tonaj-home-nav,
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

    /* 2. PAGE D'ACCUEIL (#tonaj-home-page) — ADAPTATION ÉCRANS COURTS & MOBILES */
    .tonaj-home-center-box {{
      max-height: calc(100dvh - 140px) !important;
    }}

    @media (max-width: 680px) {{
      .tonaj-home-center-box {{
        width: min(82vw, 360px, calc(44dvh * 433 / 168)) !important;
      }}
    }}

    /* 3. PAGE WORK / PORTFOLIO (#view-portfolio) — ZÉRO SUPERPOSITION SUR TOUS ÉCRANS */
    @media (min-width: 961px) {{
      #view-portfolio .portfolio-section {{
        top: 46% !important;
      }}

      .tonaj-work-heading {{
        top: auto !important;
        bottom: clamp(54px, 7.6vh, 84px) !important;
        left: 2.65% !important;
        font-size: min(19.5vh, 14.6vw) !important;
        line-height: 0.8 !important;
      }}

      .tonaj-work-active-desc {{
        top: auto !important;
        bottom: clamp(58px, 8.2vh, 90px) !important;
        right: clamp(24px, 4.8vw, 65px) !important;
        width: clamp(220px, 24vw, 320px) !important;
      }}

      #view-portfolio .tonaj-home-lang,
      #view-portfolio .tonaj-home-city {{
        bottom: clamp(14px, 2.4vh, 24px) !important;
      }}
    }}

    /* Tablette (681px - 960px) */
    @media (max-width: 960px) and (min-width: 681px) {{
      #view-portfolio .portfolio-section {{
        --carousel-stage-w: min(76vw, calc(30vh * 501 / 166)) !important;
        --carousel-card-size: calc(var(--carousel-stage-w) * 166 / 501) !important;
        top: 44% !important;
      }}

      .tonaj-work-heading {{
        top: auto !important;
        bottom: clamp(54px, 7.2vh, 76px) !important;
        left: 3.2vw !important;
        font-size: min(15.5vh, 14.5vw) !important;
        line-height: 0.82 !important;
      }}

      .tonaj-work-active-desc {{
        top: auto !important;
        bottom: clamp(58px, 7.8vh, 82px) !important;
        right: 3.5vw !important;
        width: clamp(200px, 34vw, 290px) !important;
      }}

      #view-portfolio .tonaj-home-lang {{
        left: 3.2vw !important;
        bottom: 18px !important;
      }}

      #view-portfolio .tonaj-home-city {{
        left: auto !important;
        right: 3.5vw !important;
        bottom: 18px !important;
      }}
    }}

    /* Mobile (<= 680px) : Carrousel agrandi + Description dessous + Titre WORK + Pied de page */
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

    /* 4. PAGE ABOUT (#view-about) — ZÉRO SUPERPOSITION DESKTOP, LAPTOP, TABLETTE & MOBILE */
    @media (min-width: 1025px) and (min-height: 720px) {{
      .tonaj-about-green-block {{
        top: 10.2vh !important;
        height: clamp(60px, 9.2vh, 88px) !important;
      }}

      .tonaj-about-manifesto {{
        top: 21.8vh !important;
        left: 3.25% !important;
        width: clamp(340px, 52vw, 560px) !important;
        font-size: clamp(11px, min(0.95vw, 1.42vh), 13.8px) !important;
        line-height: 1.4 !important;
        gap: clamp(7px, 1.2vh, 13px) !important;
      }}

      .tonaj-about-right-col {{
        top: 10.2vh !important;
        left: 63.5% !important;
        width: 30% !important;
        gap: clamp(10px, 1.8vh, 20px) !important;
      }}

      .tonaj-about-photo-frame {{
        max-height: clamp(190px, 37vh, 350px) !important;
        width: auto !important;
        max-width: min(100%, 330px) !important;
      }}

      .tonaj-about-giant-title-wrapper {{
        top: auto !important;
        bottom: clamp(52px, 7vh, 72px) !important;
        left: 2.65% !important;
      }}

      .tonaj-about-giant-title {{
        font-size: min(18.5vh, 14.8vw) !important;
        line-height: 0.82 !important;
      }}

      .tonaj-about-view .tonaj-home-lang,
      .tonaj-about-view .tonaj-home-city {{
        bottom: clamp(14px, 2.2vh, 22px) !important;
      }}
    }}

    /* Flux vertical fluide pour About sur Tablette, Mobile ou écrans peu hauts */
    @media (max-width: 1024px), (max-height: 719px) {{
      html:has(body.view-is-about),
      body.view-is-about {{
        overflow-y: auto !important;
        overflow-x: hidden !important;
        height: auto !important;
      }}

      #view-about.view-panel.is-active {{
        position: relative !important;
        inset: auto !important;
        height: auto !important;
        min-height: 100vh !important;
        min-height: 100dvh !important;
        overflow-y: visible !important;
        overflow-x: hidden !important;
      }}

      .tonaj-about-view .tonaj-home-nav {{
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 48px !important;
        background: rgba(255, 255, 255, 0.94) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        z-index: 2600 !important;
      }}

      .tonaj-about-stage {{
        height: auto !important;
        min-height: auto !important;
        padding-top: 64px !important;
        padding-bottom: 16px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: stretch !important;
        gap: 0 !important;
      }}

      .tonaj-about-green-block {{
        display: none !important;
      }}

      .tonaj-about-manifesto {{
        order: 1 !important;
        position: relative !important;
        top: auto !important;
        left: auto !important;
        width: 92vw !important;
        max-width: none !important;
        background-color: #1bff00 !important;
        padding: 24px 20px !important;
        border-radius: 4px !important;
        margin: 8px 4vw 28px 4vw !important;
        font-size: clamp(12.5px, 3.2vw, 14.5px) !important;
        line-height: 1.5 !important;
        gap: 12px !important;
        box-sizing: border-box !important;
      }}

      .tonaj-about-right-col {{
        order: 2 !important;
        position: relative !important;
        top: auto !important;
        left: auto !important;
        width: 100% !important;
        padding: 0 4vw !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-start !important;
        gap: 14px !important;
        margin-bottom: 28px !important;
        box-sizing: border-box !important;
      }}

      .tonaj-about-name {{
        margin: 0 !important;
      }}

      .tonaj-about-photo-frame {{
        width: min(68vw, 260px) !important;
        max-height: none !important;
        margin: 0 !important;
      }}

      .tonaj-about-giant-title-wrapper {{
        order: 3 !important;
        position: relative !important;
        top: auto !important;
        bottom: auto !important;
        left: auto !important;
        padding: 4px 4vw 0 4vw !important;
        margin-top: 4px !important;
      }}

      .tonaj-about-giant-title {{
        font-size: clamp(54px, 15vw, 104px) !important;
        line-height: 0.88 !important;
      }}

      .tonaj-about-view .tonaj-home-lang {{
        position: relative !important;
        left: auto !important;
        bottom: auto !important;
        margin: 12px 0 8px 4vw !important;
        display: inline-flex !important;
        align-self: flex-start !important;
      }}

      .tonaj-about-view .tonaj-home-city {{
        position: relative !important;
        left: auto !important;
        right: auto !important;
        bottom: auto !important;
        margin: 0 0 24px 4vw !important;
        display: block !important;
      }}
    }}

    /* 5. PAGE CONTACT (#view-contact) — ZÉRO SUPERPOSITION DESKTOP, LAPTOP, TABLETTE & MOBILE */
    @media (min-width: 1025px) and (min-height: 720px) {{
      .tonaj-contact-green-block {{
        top: 10.2vh !important;
        left: 2.65% !important;
        width: 94.7% !important;
        padding: clamp(28px, 6.2vh, 68px) clamp(24px, 3.8vw, 52px) clamp(16px, 2.6vh, 28px) !important;
      }}

      .tonaj-form-textarea {{
        height: clamp(46px, 7.2vh, 70px) !important;
      }}

      .tonaj-contact-huge-link {{
        top: 56.5vh !important;
        font-size: clamp(16px, min(2.35vw, 3.6vh), 32px) !important;
      }}

      .tonaj-contact-email {{
        left: 2.65% !important;
      }}

      .tonaj-contact-phone {{
        left: auto !important;
        right: 2.65% !important;
      }}

      .tonaj-contact-giant-title-wrapper {{
        top: auto !important;
        bottom: clamp(52px, 7vh, 72px) !important;
        left: 2.65% !important;
      }}

      .tonaj-contact-giant-title {{
        font-size: min(18.5vh, 13.8vw) !important;
        line-height: 0.82 !important;
      }}

      .tonaj-contact-social-links {{
        top: auto !important;
        bottom: clamp(58px, 8vh, 82px) !important;
        left: auto !important;
        right: 2.65% !important;
        font-size: clamp(20px, min(2.5vw, 3.6vh), 32px) !important;
      }}

      .tonaj-contact-view .tonaj-home-lang,
      .tonaj-contact-view .tonaj-home-city {{
        bottom: clamp(14px, 2.2vh, 22px) !important;
      }}
    }}

    /* Flux vertical fluide pour Contact sur Tablette, Mobile ou écrans peu hauts */
    @media (max-width: 1024px), (max-height: 719px) {{
      html:has(body.view-is-contact),
      body.view-is-contact {{
        overflow-y: auto !important;
        overflow-x: hidden !important;
        height: auto !important;
      }}

      #view-contact.view-panel.is-active {{
        position: relative !important;
        inset: auto !important;
        height: auto !important;
        min-height: 100vh !important;
        min-height: 100dvh !important;
        overflow-y: visible !important;
        overflow-x: hidden !important;
      }}

      .tonaj-contact-view .tonaj-home-nav {{
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 48px !important;
        background: rgba(255, 255, 255, 0.94) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        z-index: 2600 !important;
      }}

      .tonaj-contact-stage {{
        height: auto !important;
        min-height: 100vh !important;
        padding-top: 68px !important;
        padding-bottom: 36px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: stretch !important;
      }}

      .tonaj-contact-green-block {{
        position: relative !important;
        top: auto !important;
        left: 4vw !important;
        width: 92vw !important;
        height: auto !important;
        padding: 28px 5vw 32px 5vw !important;
        border-radius: 4px !important;
        flex-shrink: 0 !important;
      }}

      .tonaj-contact-huge-link {{
        position: relative !important;
        top: auto !important;
        left: auto !important;
        right: auto !important;
        display: block !important;
        padding: 0 4vw !important;
        font-size: clamp(17px, 4.8vw, 26px) !important;
        white-space: normal !important;
        word-break: break-word !important;
      }}

      .tonaj-contact-email {{
        margin-top: 28px !important;
      }}

      .tonaj-contact-phone {{
        margin-top: 10px !important;
      }}

      .tonaj-contact-giant-title-wrapper {{
        position: relative !important;
        top: auto !important;
        bottom: auto !important;
        left: auto !important;
        padding: 24px 4vw 0 4vw !important;
        margin-top: auto !important;
      }}

      .tonaj-contact-giant-title {{
        font-size: clamp(48px, 14.5vw, 96px) !important;
        line-height: 0.88 !important;
      }}

      .tonaj-contact-social-links {{
        position: relative !important;
        top: auto !important;
        bottom: auto !important;
        left: auto !important;
        right: auto !important;
        padding: 18px 4vw 12px 4vw !important;
        gap: 24px !important;
      }}

      .tonaj-contact-view .tonaj-home-lang {{
        position: relative !important;
        left: auto !important;
        bottom: auto !important;
        margin: 14px 0 8px 4vw !important;
        display: inline-flex !important;
        align-self: flex-start !important;
      }}

      .tonaj-contact-view .tonaj-home-city {{
        position: relative !important;
        left: auto !important;
        right: auto !important;
        bottom: auto !important;
        margin: 0 0 16px 4vw !important;
        display: block !important;
      }}
    }}

    /* 6. PAGES PROJETS (#view-project-01..06) — RESPONSIVE TABLETTE & MOBILE */
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
