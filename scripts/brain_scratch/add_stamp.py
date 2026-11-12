standalone_path = '/Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/standalone.html'
portfolio_path = '/Users/morganjanot/.gemini/antigravity/brain/04838ef3-4249-4209-97cb-1440ffec4bcd/portfolio.html'

with open(standalone_path, 'r', encoding='utf-8') as f:
    content = f.read()

# CSS to inject
css_stamp = """
    /* =============================================================
       PERSISTENT BOTTOM-RIGHT MARGIN HALLMARK STAMP: LYON 2026®
       ============================================================= */
    .margin-stamp-lyon {
      position: fixed;
      right: clamp(16px, 2.2vw, 32px);
      bottom: clamp(32px, 5vh, 52px);
      z-index: 150;
      pointer-events: none;
      user-select: none;
      transform: rotate(90deg);
      transform-origin: 100% 100%;
      white-space: nowrap;
      font-family: "Playfair Display", "Didot", "Bodoni MT", "Times New Roman", serif;
      font-size: clamp(10px, 0.95vw, 12px);
      font-weight: 500;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: rgba(255, 255, 255, 0.72);
      line-height: 1;
      display: inline-flex;
      align-items: baseline;
      opacity: 0.75;
      transition: opacity 300ms ease;
    }

    .margin-stamp-lyon .stamp-r {
      font-size: 0.58em;
      line-height: 0;
      vertical-align: super;
      margin-left: 3px;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-weight: 700;
      opacity: 0.85;
    }
  </style>"""

content = content.replace('  </style>', css_stamp, 1)

# HTML markup to inject inside body
html_stamp = """<body id="page-body">

  <!-- PERSISTENT BOTTOM-RIGHT MARGIN HALLMARK STAMP: LYON 2026® -->
  <aside class="margin-stamp-lyon" aria-hidden="true">
    <span>LYON 2026</span><sup class="stamp-r">&reg;</sup>
  </aside>"""

content = content.replace('<body id="page-body">', html_stamp, 1)

with open(standalone_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated standalone.html successfully")

with open(portfolio_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated portfolio.html successfully")
