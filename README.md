# Portfolio Morgan Janot (MJ) — Landing Page Expérimentale

Landing page de portfolio minimaliste, éditoriale et hautement graphique conçue d'après la maquette de référence.

## ✨ Caractéristiques & Système Graphique

- **Grille 2 × 3 plein écran (6 blocs jointifs) :**
  - Sans gouttière, sans bordure superflue, reproduisant fidèlement l'aspect d'une grande affiche contemporaine.
- **Palette Chromatique Exacte :**
  - **Bloc 01 (Orange vif) :** `#e9722b` — Tracé fauteuil biomorphique `#eb6209`
  - **Bloc 02 (Violet profond) :** `#914792` — Tracé luminaire architectural `#812383`
  - **Bloc 03 (Vert chartreuse) :** `#68b42d` — Tracé fauteuil cantilever `#2c8934`
  - **Bloc 04 (Brun chaud) :** `#775732` — Tracé assise modulaire `#724b10`
  - **Bloc 05 (Bleu céruléen) :** `#46a0d1` — Tracé sculpture florale / sablier `#27629f`
  - **Bloc 06 (Rouge vermillon) :** `#d83d46` — Composition volontairement épurée et minimaliste
- **Comportement Hover Physique :**
  - Chaque bloc agit comme un panneau graphique que l'utilisateur soulève (`translateY(-9px) scale(1.024)` avec ombre portée diffuse `shadow-2xl`).
  - L'illustration vectorielle réagit avec un déplacement organique subtil (`translate(8px, -4px) scale(1.03)`).
  - La flèche glisse vers la droite (`translateX(14px) scale(1.04)`).
  - Les blocs voisins réduisent subtilement leur contraste et luminosité pour renforcer la profondeur du bloc actif.
  - La typographie émerge progressivement depuis le bas à gauche avec un étagement soigné (Catégorie &rarr; Titre &rarr; Description).
- **Header Éditorial Minimaliste :**
  - Monogramme central **"MJ"** chevauchant l'arête verticale séparant les colonnes 1 et 2.
  - Liens **About** & **Contact** calés en haut à droite en typographie sans-serif bold à fort contraste.
- **Responsive & Tactile :**
  - Desktop / Tablette : Grille 2 colonnes × 3 lignes.
  - Mobile : 1 colonne verticale de 6 panneaux plein format.
  - Support tactile : tap pour activer / soulever le bloc, second tap ou tap extérieur pour fermer.
- **Accessibilité :**
  - Navigation complète au clavier (`Tab`, `Shift-Tab`, `Entrée`, `Espace`, `Échap`).
  - Focus visible haute visibilité.
  - Respect strict de `prefers-reduced-motion`.

---

## 📁 Architecture du Code

```text
mj-portfolio/
├── index.html                  # Point d'entrée Vite
├── standalone.html             # Version autonome autonome immédiate (zéro dépendance)
├── package.json                # Dépendances & scripts React/Vite/Tailwind
├── vite.config.js              # Configuration Vite
├── tailwind.config.js          # Configuration Tailwind
├── postcss.config.js           # Plugins PostCSS
└── src/
    ├── main.jsx                # Montage React
    ├── App.jsx                 # Composition globale
    ├── style.css               # Styles de base, resets & règles d'accessibilité
    ├── data/
    │   └── projectsData.js     # Données centralisées des 6 projets (titres, catégories, etc.)
    └── components/
        ├── Header.jsx          # Header flottant avec logo MJ et navigation
        ├── PortfolioGrid.jsx   # Grille 2x3 et gestion réciproque des états
        ├── PortfolioTile.jsx   # Bloc interactif unitaire
        └── Illustrations.jsx   # Tracés vectoriels SVG haute fidélité
```

---

## 🚀 Comment Lancer et Prévisualiser

### 1. Prévisualisation directe instantanée
Ouvrez simplement le fichier `standalone.html` dans n'importe quel navigateur (double-cliquez dessus ou glissez-le dans Safari/Chrome/Firefox).

### 2. Avec serveur local intégré (sans installation)
Dans le terminal :
```bash
cd /Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio
ruby -run -e httpd . -p 3000
```
Puis ouvrez [http://localhost:3000/standalone.html](http://localhost:3000/standalone.html).

### 3. En mode développement Node / React (si Node.js est configuré)
```bash
npm install
npm run dev
```

---

## ✏️ Personnalisation des Projets
Pour modifier le nom des projets, les descriptions, les catégories ou les liens, éditez simplement le fichier [`src/data/projectsData.js`](file:///Users/morganjanot/.gemini/antigravity/scratch/mj-portfolio/src/data/projectsData.js).
