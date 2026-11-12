import re

def main():
    with open('portfolio.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Section 1
    target_sec1 = """          <!-- SECTION 1 : INTRODUCTION BÂCHE RECYCLÉE & STRUCTURE ALU (5 COL) + PHOTO (7 COL) -->
          <div class="proj-section">
            <div class="proj-span-5 proj-align-center">
              <div class="proj-text-block">
                <p class="proj-text-lead">Les immenses bâches publicitaires qui habillent nos bâtiments finissent souvent jetées une fois les campagnes terminées. Ce projet propose de leur offrir une seconde vie en les transformant en mobilier. L'idée repose sur un contraste fort : une structure profilée et sobre en aluminium sur laquelle vient se tendre un fragment de bâche recyclée. Confrontant la rigueur industrielle du métal à l'esthétique aléatoire et colorée de la publicité, chaque chaise devient une pièce unique.</p>
              </div>
            </div>"""

    replace_sec1 = """          <!-- SECTION 1 : LE MOBILIER ÉVÉNEMENTIEL 100% NATUREL & MATIÈRES BRUTES (5 COL) + PHOTO (7 COL) -->
          <div class="proj-section">
            <div class="proj-span-5 proj-align-center">
              <div class="proj-text-block">
                <p class="proj-text-lead">Les festivals et les événements en plein air exigent des aménagements temporaires qui posent souvent un défi écologique et logistique majeur. Le transport, l'installation et le stockage du mobilier traditionnel génèrent une empreinte carbone importante et finissent parfois en déchets. Pour répondre à cette problématique, ce projet repense intégralement la conception de l'assise événementielle avec une approche radicale : un mobilier 100 % naturel, fabriqué sur place et conçu pour disparaître sans laisser de trace.</p>
                <p>Plutôt que d'importer des matériaux industriels, le projet s'appuie sur ce que la nature offre déjà. Le mobilier est constitué exclusivement de matières organiques brutes : de la terre, du chanvre et de la paille. Ces éléments sont assemblés et compressés à froid dans un moule spécialement conçu pour l'assise.</p>
              </div>
            </div>"""

    assert target_sec1 in content, "Section 1 target not found"
    content = content.replace(target_sec1, replace_sec1, 1)

    # 2. Update Section 3
    sec3_pattern = r'''(\s*<!-- SECTION 3 :[^\n]*-->\s*<div class="proj-section">\s*<div class="proj-span-7 proj-align-center">\s*<div class="proj-media proj-ratio-auto">\s*<img [^>]*alt="KOMPRESS — Modélisation CAO de la matrice et du moule de compression"[^>]*>\s*</div>\s*</div>\s*)<div class="proj-span-5 proj-align-center">\s*<div class="proj-text-block">\s*<p>L'identité de cette assise s'exprime également[^<]*</p>\s*<p>En transposant l'énergie visuelle[^<]*</p>\s*</div>\s*</div>(\s*</div>)'''

    sec3_match = re.search(sec3_pattern, content)
    assert sec3_match is not None, "Section 3 pattern not found"

    def sec3_replacement(m):
        header = m.group(1).replace("RHINO CAO À GAUCHE (7 COL) + 2 PARAGRAPHES TECHNIQUES À DROITE (5 COL)", "MOULE DE COMPRESSION CAO (7 COL) + PRODUCTION IN SITU & CYCLE ÉPHÉMÈRE (5 COL)")
        body = """<div class="proj-span-5 proj-align-center">
              <div class="proj-text-block">
                <p>L'innovation majeure réside dans le processus de production. Le mobilier n'est pas fabriqué en usine pour être ensuite acheminé par camion. Il est moulé et compressé directement sur le lieu de l'événement. Cette méthode supprime les contraintes de transport et de logistique, tout en permettant au design de s'imprégner de l'essence même du site qui l'accueille.</p>
                <p>L'essence de ce mobilier est son caractère éphémère. Une fois le festival ou l'événement terminé, il n'y a rien à démonter, à transporter ou à jeter à la poubelle. Conçue pour être friable, l'assise peut simplement être brisée et émiettée sur place. La terre, la paille et le chanvre se décomposent naturellement et retournent à leur état d'origine. C'est un cycle de vie en boucle fermée qui ne génère absolument aucune pollution visuelle ou matérielle pour l'environnement.</p>
              </div>
            </div>"""
        return header + body + m.group(2)

    content = re.sub(sec3_pattern, sec3_replacement, content, count=1)

    # 3. Update I18N.fr.projects['project-03']
    fr_pattern = r'''('project-03':\s*\[)\s*"Les immenses bâches publicitaires[^"]*",\s*"L'identité de cette assise[^"]*",\s*"En transposant l'énergie visuelle[^"]*"(\s*\])'''

    fr_match = re.search(fr_pattern, content)
    assert fr_match is not None, "I18N FR project-03 pattern not found"

    fr_replacement = r'''\1
              "Les festivals et les événements en plein air exigent des aménagements temporaires qui posent souvent un défi écologique et logistique majeur. Le transport, l'installation et le stockage du mobilier traditionnel génèrent une empreinte carbone importante et finissent parfois en déchets. Pour répondre à cette problématique, ce projet repense intégralement la conception de l'assise événementielle avec une approche radicale : un mobilier 100 % naturel, fabriqué sur place et conçu pour disparaître sans laisser de trace.",
              "Plutôt que d'importer des matériaux industriels, le projet s'appuie sur ce que la nature offre déjà. Le mobilier est constitué exclusivement de matières organiques brutes : de la terre, du chanvre et de la paille. Ces éléments sont assemblés et compressés à froid dans un moule spécialement conçu pour l'assise.",
              "L'innovation majeure réside dans le processus de production. Le mobilier n'est pas fabriqué en usine pour être ensuite acheminé par camion. Il est moulé et compressé directement sur le lieu de l'événement. Cette méthode supprime les contraintes de transport et de logistique, tout en permettant au design de s'imprégner de l'essence même du site qui l'accueille.",
              "L'essence de ce mobilier est son caractère éphémère. Une fois le festival ou l'événement terminé, il n'y a rien à démonter, à transporter ou à jeter à la poubelle. Conçue pour être friable, l'assise peut simplement être brisée et émiettée sur place. La terre, la paille et le chanvre se décomposent naturellement et retournent à leur état d'origine. C'est un cycle de vie en boucle fermée qui ne génère absolument aucune pollution visuelle ou matérielle pour l'environnement."\2'''

    content = re.sub(fr_pattern, fr_replacement, content, count=1)

    # 4. Update I18N.en.projects['project-03']
    en_pattern = r'''('project-03':\s*\[)\s*"The huge advertising banners[^"]*",\s*"The seat's identity is further[^"]*",\s*"By translating the visual kinetic[^"]*"(\s*\])'''

    en_match = re.search(en_pattern, content)
    assert en_match is not None, "I18N EN project-03 pattern not found"

    en_replacement = r'''\1
              "Outdoor festivals and events require temporary fixtures that often present a major ecological and logistical challenge. The transportation, installation, and storage of conventional furniture generate a significant carbon footprint and frequently result in waste. In response, this project fundamentally rethinks event seating through a radical approach: 100% natural furniture, produced directly on site and designed to vanish without leaving a trace.",
              "Rather than importing industrial materials, the project relies on what nature readily provides. The seating is composed exclusively of raw organic materials: earth, hemp, and straw. These elements are combined and cold-compressed within a mold custom-engineered for the seat.",
              "The central innovation lies in the production process. The furniture is not manufactured in a factory to be hauled by truck; it is molded and compressed directly at the event venue. This on-site approach eliminates transport and logistics constraints while allowing the design to absorb the true essence of its host site.",
              "The core identity of this furniture lies in its ephemeral nature. Once the festival or event concludes, there is nothing to dismantle, transport, or discard. Engineered to be friable, the seat can simply be broken down and crumbled on site. The earth, straw, and hemp decompose naturally, returning to their original state. It is a closed-loop lifecycle that leaves behind zero visual or material pollution for the environment."\2'''

    content = re.sub(en_pattern, en_replacement, content, count=1)

    with open('portfolio.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("SUCCESS: portfolio.html updated cleanly for KOMPRESS (project-03)!")

if __name__ == '__main__':
    main()
