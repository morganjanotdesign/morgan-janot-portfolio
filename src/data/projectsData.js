/**
 * Portfolio Projects Data
 * Centralized data source for the 6 portfolio grid frames.
 * Couleurs FLUO haute intensité concordant avec les projets présentés :
 * - 01 : Orange Fluo / Tangerine (Fog Chair en laine & laque orange)
 * - 02 : Gris Minéral / Béton Brut Architectural (Lampadaire Articulé)
 * - 03 : Vert Studio Profond / Émeraude Foncé (Canapé Galet)
 * - 04 : Rouge Suisse / Swiss Red (Chaise Suspendue)
 * - 05 : Bleu Cobalt Fluo / Laser Blue (Enceinte DAA-DAA en bleu cobalt)
 * - 06 : Jaune Fluo / Neon Lemon (Arche Radiale)
 */

export const projects = [
  {
    id: 1,
    number: "01",
    title: "Fog Chair",
    category: "01 — Architecture d'assise",
    description: "Comment réintégrer le jeu dans notre quotidien grâce au mobilier modulable ?",
    bgColor: "rgb(255, 94, 0)", // Orange Fluo / Tangerine Électrique
    strokeColor: "rgb(180, 50, 0)", // Orange plus foncé
    link: "/project-01",
    illustrationKey: "chair_orange"
  },
  {
    id: 2,
    number: "02",
    title: "Lampadaire Articulé",
    category: "02 — Design d'espace",
    description: "Officiate molesequam ullorerum nestem se et et pella sed ut occaborat magnitis et que pelenihil iust omnihictae. Et eturiatem.",
    bgColor: "rgb(180, 185, 192)", // Gris Minéral / Béton Brut Architectural
    strokeColor: "rgb(80, 85, 95)", // Gris graphite plus foncé
    link: "/project-02",
    illustrationKey: "lamp_purple"
  },
  {
    id: 3,
    number: "03",
    title: "Canapé Galet",
    category: "03 — Recherche formelle",
    description: "Assise monobloc sculpturale et coussin sphérique en cuir patiné. Recherche formelle et cinétique.",
    bgColor: "rgb(0, 140, 70)", // Vert Studio Profond (plus foncé)
    strokeColor: "rgb(0, 85, 42)", // Vert foncé accentué
    link: "/project-03",
    illustrationKey: "sofa_brown"
  },
  {
    id: 4,
    number: "04",
    title: "Chaise Suspendue",
    category: "04 — Structure géométrique",
    description: "Structure géométrique minimale et assise en tension textile. Équilibre architectural contemporain.",
    bgColor: "rgb(227, 6, 19)", // Rouge Suisse / Swiss Red
    strokeColor: "rgb(150, 4, 13)", // Rouge Suisse profond
    link: "/project-04",
    illustrationKey: "chair_green"
  },
  {
    id: 5,
    number: "05",
    title: "DAA-DAA",
    category: "05 — Enceinte Acoustique",
    description: "Système stéréophonique sculptural à cylindres découplés en aluminium brossé et uréthane bleu cobalt.",
    bgColor: "rgb(0, 130, 255)", // Bleu Cobalt Fluo / Laser Blue
    strokeColor: "rgb(0, 70, 190)", // Bleu cobalt plus foncé
    link: "/project-05",
    illustrationKey: "vase_blue"
  },
  {
    id: 6,
    number: "06",
    title: "LEO-11",
    category: "06 — Luminaire d'ambiance",
    description: "Lampe d'ambiance sculpturale : tension entre ossature filaire en acier et diffusion graphique texturée.",
    bgColor: "rgb(255, 235, 0)", // Jaune Fluo / Neon Lemon Highlighter
    strokeColor: "rgb(168, 150, 0)", // Jaune plus foncé
    link: "/project-06",
    illustrationKey: "leo_11"
  }
];
