#!/usr/bin/env python3
"""
Renames:
- Project 2: 'Lampadaire Articulé' -> 'Lampe Burma'
- Project 4: 'Chaise Suspendue' -> 'Satsu Chair'
Across portfolio.html and synchronizes index.html
"""

import sys
import shutil

replacements = [
    # CSS comments
    ('/* SPECIFIC LAYOUT 02: 3-COLUMN BLUEPRINT (LAMPADAIRE ARTICULÉ) */',
     '/* SPECIFIC LAYOUT 02: 3-COLUMN BLUEPRINT (LAMPE BURMA) */'),
    ('/* SPECIFIC LAYOUT 03: DIAGONAL CHECKERBOARD (CHAISE SUSPENDUE) */',
     '/* SPECIFIC LAYOUT 03: DIAGONAL CHECKERBOARD (SATSU CHAIR) */'),
    ('PROJET 02 (LAMPADAIRE ARTICULÉ) — COMPOSITION SELON MODÈLE DE RÉFÉRENCE',
     'PROJET 02 (LAMPE BURMA) — COMPOSITION SELON MODÈLE DE RÉFÉRENCE'),
    ('/* RANGÉE 4 : NŒUD GÉOMÉTRIQUE & TEXTE (GAUCHE) + ÉLÉVATION LAMPADAIRE AGRANDIE (DROITE) */',
     '/* RANGÉE 4 : NŒUD GÉOMÉTRIQUE & TEXTE (GAUCHE) + ÉLÉVATION LAMPE BURMA AGRANDIE (DROITE) */'),
    ('PROJET 04 (CHAISE SUSPENDUE) — MISE EN PAGE RIGOUREUSE SELON MODÈLE DE RÉFÉRENCE',
     'PROJET 04 (SATSU CHAIR) — MISE EN PAGE RIGOUREUSE SELON MODÈLE DE RÉFÉRENCE'),

    # Drawer
    ('<span class="drawer-project-name" data-i18n="title_p2">Lampadaire Articulé</span>',
     '<span class="drawer-project-name" data-i18n="title_p2">Lampe Burma</span>'),
    ('<span class="drawer-project-name" data-i18n="title_p4">Chaise Suspendue</span>',
     '<span class="drawer-project-name" data-i18n="title_p4">Satsu Chair</span>'),

    # Cards in frames-grid (portfolio squares)
    ('<h3 class="mosaic-cartouche-title" data-i18n="card2_title">* LAMPADAIRE ARTICULÉ *</h3>',
     '<h3 class="mosaic-cartouche-title" data-i18n="card2_title">* LAMPE BURMA *</h3>'),
    ('<p data-i18n="card2_desc">Lampadaire articulé à rotules géométriques et contrepoids béton.</p>',
     '<p data-i18n="card2_desc">Lampe articulée à rotules géométriques et contrepoids béton.</p>'),
    ('<h3 class="mosaic-cartouche-title" data-i18n="card4_title">* CHAISE SUSPENDUE *</h3>',
     '<h3 class="mosaic-cartouche-title" data-i18n="card4_title">* SATSU CHAIR *</h3>'),

    # Project 1 footer nav to project 2
    ('data-target-project="project-02" aria-label="Projet suivant : Lampadaire Articulé">',
     'data-target-project="project-02" aria-label="Projet suivant : Lampe Burma">'),
    ('<span data-i18n="next_p1">Projet suivant &bull; 02 (Lampadaire Articulé)</span>',
     '<span data-i18n="next_p1">Projet suivant &bull; 02 (Lampe Burma)</span>'),

    # Project 2 detail view
    ('<!-- VIEW DETAIL: PROJET 02 (LAMPADAIRE ARTICULÉ) -->',
     '<!-- VIEW DETAIL: PROJET 02 (LAMPE BURMA) -->'),
    ('<h1 class="proj-vertical-title" data-i18n="title_p2">Lampadaire Articulé</h1>',
     '<h1 class="proj-vertical-title" data-i18n="title_p2">Lampe Burma</h1>'),
    ('alt="Lampadaire allumé dans un salon intimiste"',
     'alt="Lampe Burma allumée dans un salon intimiste"'),
    ('<!-- SECTION 4 : NŒUD GÉOMÉTRIQUE + TEXTE CENTRÉS VERTICALEMENT (5 COL) + ÉLÉVATION LAMPADAIRE (7 COL) -->',
     '<!-- SECTION 4 : NŒUD GÉOMÉTRIQUE + TEXTE CENTRÉS VERTICALEMENT (5 COL) + ÉLÉVATION LAMPE BURMA (7 COL) -->'),
    ('alt="Élévation complète du lampadaire articulé"',
     'alt="Élévation complète de la Lampe Burma"'),

    # Project 3 footer nav
    ('data-target-project="project-02" aria-label="Projet précédent : Lampadaire Articulé">',
     'data-target-project="project-02" aria-label="Projet précédent : Lampe Burma">'),
    ('data-target-project="project-04" aria-label="Projet suivant : Chaise Suspendue">',
     'data-target-project="project-04" aria-label="Projet suivant : Satsu Chair">'),
    ('<span data-i18n="next_p3">Projet suivant &bull; 04 (Chaise Suspendue)</span>',
     '<span data-i18n="next_p3">Projet suivant &bull; 04 (Satsu Chair)</span>'),

    # Project 4 detail view
    ('<!-- VIEW DETAIL: PROJET 04 (CHAISE SUSPENDUE) -->',
     '<!-- VIEW DETAIL: PROJET 04 (SATSU CHAIR) -->'),
    ('<h1 class="proj-vertical-title" data-i18n="title_p4">Chaise Suspendue</h1>',
     '<h1 class="proj-vertical-title" data-i18n="title_p4">Satsu Chair</h1>'),
    ('alt="Chaise Suspendue - Vue en lévitation"', 'alt="Satsu Chair - Vue en lévitation"'),
    ('alt="Chaise Suspendue - Rendu 3D studio"', 'alt="Satsu Chair - Rendu 3D studio"'),
    ('alt="Chaise Suspendue - Recherches graphiques et croquis"', 'alt="Satsu Chair - Recherches graphiques et croquis"'),
    ('alt="Chaise Suspendue - Référence biomécanique manga"', 'alt="Satsu Chair - Référence biomécanique manga"'),
    ('alt="Chaise Suspendue - Modélisation CAO de l\'ossature"', 'alt="Satsu Chair - Modélisation CAO de l\'ossature"'),
    ('alt="Chaise Suspendue - Plan 2D d\'usinage vectoriel"', 'alt="Satsu Chair - Plan 2D d\'usinage vectoriel"'),
    ('alt="Chaise Suspendue - Découpe laser des membrures"', 'alt="Satsu Chair - Découpe laser des membrures"'),
    ('alt="Chaise Suspendue - Gabarit à plat sur plan de coupe"', 'alt="Satsu Chair - Gabarit à plat sur plan de coupe"'),
    ('alt="Chaise Suspendue - Maquette d\'étude en volume"', 'alt="Satsu Chair - Maquette d\'étude en volume"'),

    # JS projectTitles & comments
    ("'project-02': 'Lampadaire Articulé',", "'project-02': 'Lampe Burma',"),
    ("'project-04': 'Chaise Suspendue',", "'project-04': 'Satsu Chair',"),
    ("'project-02'  // 5: Lampadaire articulé (Gris)", "'project-02'  // 5: Lampe Burma (Gris)"),

    # I18N FR
    ('card2_title: "* LAMPADAIRE ARTICULÉ *",', 'card2_title: "* LAMPE BURMA *",'),
    ('card2_desc: "Lampadaire articulé à rotules géométriques et contrepoids béton.",',
     'card2_desc: "Lampe articulée à rotules géométriques et contrepoids béton.",'),
    ('card4_title: "* CHAISE SUSPENDUE *",', 'card4_title: "* SATSU CHAIR *",'),
    ('title_p2: "Lampadaire Articulé",', 'title_p2: "Lampe Burma",'),
    ('title_p4: "Chaise Suspendue",', 'title_p4: "Satsu Chair",'),
    ('next_p1: "Projet suivant &bull; 02 (Lampadaire Articulé)",',
     'next_p1: "Projet suivant &bull; 02 (Lampe Burma)",'),
    ('next_p3: "Projet suivant &bull; 04 (Chaise Suspendue)",',
     'next_p3: "Projet suivant &bull; 04 (Satsu Chair)",'),

    # I18N EN
    ('card2_title: "* ARTICULATED FLOOR LAMP *",', 'card2_title: "* LAMPE BURMA *",'),
    ('card2_desc: "Articulated floor lamp with geometric swivels and concrete counterweight.",',
     'card2_desc: "Articulated lamp with geometric swivels and concrete counterweight.",'),
    ('card4_title: "* SUSPENDED CHAIR *",', 'card4_title: "* SATSU CHAIR *",'),
    ('title_p2: "Articulated Floor Lamp",', 'title_p2: "Lampe Burma",'),
    ('title_p4: "Suspended Chair",', 'title_p4: "Satsu Chair",'),
    ('next_p1: "Next project &bull; 02 (Articulated Floor Lamp)",',
     'next_p1: "Next project &bull; 02 (Lampe Burma)",'),
    ('next_p3: "Next project &bull; 04 (Suspended Chair)",',
     'next_p3: "Next project &bull; 04 (Satsu Chair)",')
]

with open('portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

for old, new in replacements:
    if old not in content:
        print(f"FAILED TO FIND: {old}")
        sys.exit(1)
    content = content.replace(old, new)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated portfolio.html successfully.")

# Also sync to index.html so python -m http.server 8000 serves the fresh version
shutil.copyfile('portfolio.html', 'index.html')
print("Synchronized portfolio.html -> index.html.")
