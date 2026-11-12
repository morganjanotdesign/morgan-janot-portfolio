import re

def main():
    with open('portfolio.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Section 1
    target_sec1 = """            <div class="proj-span-4 proj-align-end">
              <div class="proj-text-block">
                <p class="proj-text-lead">L'abolition des pieds traditionnels au profit d'un treillis autoportant ancré au plafond par des liens invisibles. &mdash; Ancrage Monophonique &bull; Imperial Red</p>
                <p>Pourquoi cette recherche ? Pour libérer complètement la surface au sol et éprouver le vide comme matériau structural. En suspendant l'assise au plafond par des filins en fibre Dyneema ultra-résistante, l'objet s'affranchit des contraintes d'appui et réagit aux oscillations du corps pour une sensation de lévitation intégrale.</p>
                <p>L'arceau triangulé en titane microbillé distribue les tensions mécaniques de manière isotrope. La membrane textile thermoformée épouse la posture sans point dur, rappelant l'aéronautique et le gréement nautique de haute mer.</p>
              </div>
            </div>"""

    replace_sec1 = """            <div class="proj-span-4 proj-align-end">
              <div class="proj-text-block">
                <p class="proj-text-lead">Les immenses bâches publicitaires qui habillent nos bâtiments finissent souvent jetées une fois les campagnes terminées. Ce projet propose de leur offrir une seconde vie en les transformant en mobilier. L'idée repose sur un contraste fort : une structure profilée et sobre en aluminium sur laquelle vient se tendre un fragment de bâche recyclée. Confrontant la rigueur industrielle du métal à l'esthétique aléatoire et colorée de la publicité, chaque chaise devient une pièce unique.</p>
              </div>
            </div>"""

    assert target_sec1 in content, "Section 1 target not found"
    content = content.replace(target_sec1, replace_sec1, 1)

    # 2. Update Section 2
    target_sec2 = """            <div class="proj-span-6 proj-align-end">
              <div class="proj-text-block">
                <p>Un pont suspendu à l'échelle du corps : le dessin découle de la tension pure. Les profilés en aluminium microbillé forment un compas géométrique qui guide le câble sans frottement. La membrane textile tendue crée une surface continue, soulignant le vide sous l'assise pour magnifier la sensation d'apesanteur.</p>
              </div>
            </div>"""

    replace_sec2 = """            <div class="proj-span-6 proj-align-end">
              <div class="proj-text-block">
                <p>L'identité de cette assise s'exprime également à travers sa silhouette atypique, directement inspirée de la pop culture japonaise. Le profil de la structure métallique reprend les lignes nerveuses d'une onomatopée extraite du manga Evangelion.</p>
              </div>
            </div>"""

    assert target_sec2 in content, "Section 2 target not found"
    content = content.replace(target_sec2, replace_sec2, 1)

    # 3. Update Section 3
    target_sec3 = """            <div class="proj-span-4 proj-align-end">
              <div class="proj-text-block">
                <p>L’énergie biomécanique des structures animées japonaises a nourri la silhouette : tension angulaire des montants, nervures brutes et sensation d'une ossature vivante prête à se déployer dans l'espace.</p>
              </div>
            </div>"""

    replace_sec3 = """            <div class="proj-span-4 proj-align-end">
              <div class="proj-text-block">
                <p>En transposant l'énergie visuelle d'un son dessiné en une forme physique tridimensionnelle, le projet crée un mobilier hybride, à la croisée du recyclage urbain et de l'hommage culturel.</p>
              </div>
            </div>"""

    assert target_sec3 in content, "Section 3 target not found"
    content = content.replace(target_sec3, replace_sec3, 1)

    # 4. Update Section 4
    sec4_pattern = r'''(\s*<!-- SECTION 4 :[^\n]*-->\s*<div class="proj-section">\s*)<div class="proj-span-5 proj-align-end">\s*<div class="proj-text-block">\s*<p>Modélisation paramétrique des sections[^<]*</p>\s*</div>\s*</div>\s*<div class="proj-span-7">\s*(<div class="proj-media proj-ratio-4-3">\s*<img [^>]*alt="Chaise Suspendue - Modélisation CAO de l'ossature" class="proj-img )is-cover("[^>]*>\s*</div>)\s*</div>(\s*</div>)'''

    sec4_match = re.search(sec4_pattern, content)
    assert sec4_match is not None, "Section 4 pattern not found"

    def sec4_replacement(m):
        return (
            m.group(1).replace("TEXTE CAO ALIGNÉ EN BAS (5 COL) + MODÉLISATION 3D VIOLETTE (7 COL)", "MODÉLISATION 3D (12 COL)")
            + '<div class="proj-span-12">\n            '
            + m.group(2).replace("proj-ratio-4-3", "proj-ratio-16-9")
            + "is-contain"
            + m.group(3)
            + '\n          </div>'
            + m.group(4)
        )

    content = re.sub(sec4_pattern, sec4_replacement, content, count=1)

    # 5. Update I18N.fr.projects['project-04']
    fr_pattern = r'''('project-04':\s*\[)\s*"L'abolition des pieds traditionnels[^"]*",\s*"Pourquoi cette recherche \?[^"]*",\s*"L'arceau triangulé en titane[^"]*",\s*"Un pont suspendu à l'échelle[^"]*",\s*"L’énergie biomécanique des structures[^"]*",\s*"Modélisation paramétrique des sections[^"]*"(\s*\])'''

    fr_match = re.search(fr_pattern, content)
    assert fr_match is not None, "I18N FR pattern not found"

    fr_replacement = r'''\1
              "Les immenses bâches publicitaires qui habillent nos bâtiments finissent souvent jetées une fois les campagnes terminées. Ce projet propose de leur offrir une seconde vie en les transformant en mobilier. L'idée repose sur un contraste fort : une structure profilée et sobre en aluminium sur laquelle vient se tendre un fragment de bâche recyclée. Confrontant la rigueur industrielle du métal à l'esthétique aléatoire et colorée de la publicité, chaque chaise devient une pièce unique.",
              "L'identité de cette assise s'exprime également à travers sa silhouette atypique, directement inspirée de la pop culture japonaise. Le profil de la structure métallique reprend les lignes nerveuses d'une onomatopée extraite du manga Evangelion.",
              "En transposant l'énergie visuelle d'un son dessiné en une forme physique tridimensionnelle, le projet crée un mobilier hybride, à la croisée du recyclage urbain et de l'hommage culturel."\2'''

    content = re.sub(fr_pattern, fr_replacement, content, count=1)

    # 6. Update I18N.en.projects['project-04']
    en_pattern = r'''('project-04':\s*\[)\s*"Abolishing traditional legs[^"]*",\s*"Why this research\?[^"]*",\s*"The triangulated bead-blasted[^"]*",\s*"A suspension bridge tailored[^"]*",\s*"The biomechanical energy of Japanese[^"]*",\s*"Parametric section modeling[^"]*"(\s*\])'''

    en_match = re.search(en_pattern, content)
    assert en_match is not None, "I18N EN pattern not found"

    en_replacement = r'''\1
              "The huge advertising banners that wrap our buildings often end up discarded once campaigns conclude. This project gives them a second life by turning them into furniture. The concept hinges on a striking contrast: a sleek, minimalist aluminum profile over which a fragment of recycled banner is stretched. By confronting the industrial rigor of metal with the colorful, unpredictable graphics of advertising, each chair becomes a unique piece.",
              "The seat's identity is further articulated through its distinctive silhouette, directly inspired by Japanese pop culture. The metal frame's profile echoes the dynamic, sharp lines of an onomatopoeia drawn from the manga Evangelion.",
              "By translating the visual kinetic energy of drawn sound into a physical three-dimensional form, the project creates a hybrid piece of furniture at the intersection of urban upcycling and cultural homage."\2'''

    content = re.sub(en_pattern, en_replacement, content, count=1)

    with open('portfolio.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("SUCCESS: portfolio.html updated cleanly!")

if __name__ == '__main__':
    main()
