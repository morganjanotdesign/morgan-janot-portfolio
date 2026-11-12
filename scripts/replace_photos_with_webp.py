import os
import shutil
import base64
import re

webp_src_dir = 'src/assets/images_webp'
target_dirs = [
    'src/assets/images',
    'images',
    '/Users/morganjanot/.gemini/antigravity/brain/df18ad40-ac30-4b7a-b04f-f3de4961c66b/images'
]

# 1. Copy webp images to target directories and clean up old png/jpg
for target_dir in target_dirs:
    if not os.path.exists(target_dir):
        continue
    print(f"Updating photos in {target_dir}...")
    for root, dirs, files in os.walk(webp_src_dir):
        for f in files:
            if f.endswith('.webp'):
                src_file = os.path.join(root, f)
                rel_path = os.path.relpath(src_file, webp_src_dir)
                dest_file = os.path.join(target_dir, rel_path)
                os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                shutil.copyfile(src_file, dest_file)
                
                # Check for corresponding old png/jpg and remove them
                base_no_ext, _ = os.path.splitext(dest_file)
                for old_ext in ['.png', '.jpg', '.jpeg']:
                    old_path = base_no_ext + old_ext
                    if os.path.exists(old_path):
                        os.remove(old_path)
                        print(f"  Removed old file: {old_path}")

print("Images copied to destination directories and old formats replaced with .webp.")

# 2. Update standalone.html with new WebP base64 data URIs
standalone_path = 'standalone.html'
portfolio_artifact_path = '/Users/morganjanot/.gemini/antigravity/brain/df18ad40-ac30-4b7a-b04f-f3de4961c66b/portfolio.html'

with open(standalone_path, 'r', encoding='utf-8') as f:
    html = f.read()

def get_webp_b64(rel_path):
    full_path = os.path.join(webp_src_dir, rel_path)
    with open(full_path, 'rb') as fp:
        data = fp.read()
    b64 = base64.b64encode(data).decode('ascii')
    return f'data:image/webp;base64,{b64}'

mapping = [
    ('Fog Chair Modèle 001 - Vue perspective isométrique', 'project-01/15.webp'),
    ('Fog Chair Modèle 001 - Vue trois-quarts en élévation', 'project-01/12.webp'),
    ('Fog Chair Modèle 001 - Trio de chaises en équilibre', 'project-01/13.webp'),
    ('Lampadaire articulé avec socle en béton brut', 'project-02/Gemini_Generated_Image_hpc2n0hpc2n0hpc2.webp'),
    ('Détail macro rotule sphérique chromée usinée', 'project-02/usm-creative-since-1965-keyvisual-04-5mch2z.webp'),
    ('Bras articulé télescopique et passage de câble orange', 'project-02/Gemini_Generated_Image_ntm565ntm565ntm5.webp'),
    ('Gros plan sur la rotule à facettes et l\'anneau passe-câble', 'project-02/Gemini_Generated_Image_np88z9np88z9np88.webp'),
    ('Cube connecteur géométrique à facettes usiné avec filetages', 'project-02/Gemini_Genemage_45c55i45c55i45c5.webp'),
    ('Chaise géométrique minimale et assise en tension textile', 'project-04/Gemini_Generated_Image_bbgjp7bbgjp7bbgj.webp'),
    ('Détail vue éclatée de la traverse et des vis d\'assemblage', 'project-04/Gemini_Generated_Image_thwtruthwtruthwt.webp'),
    ('Enceintes acoustiques stéréophoniques, vue trois-quarts', 'project-05/enceinte1.webp'),
    ('Enceintes acoustiques en situation réelle sur table basse', 'project-05/Untitled.webp'),
    ('Détail du geste ergonomique réglant les commandes analogiques', 'project-05/main.webp'),
    ('Roues en uréthane bleu cobalt translucide 70mm 78A', 'project-05/wheels_transparent.webp'),
    ('Enceintes acoustiques, grande vue arrière connectique', 'project-05/enceinte3.webp'),
    ('Gros plan macro sur les membranes des haut-parleurs', 'project-05/enceinte4.webp'),
    ('Enceintes acoustiques, grande vue de face en contre-plongée', 'project-05/enceinte2bis.webp'),
    ('LEO-11 - Luminaire d\'ambiance, vue perspective en suspension', 'project-06/f.webp'),
    ('LEO-11 - Luminaire d\'ambiance en situation in situ sur bloc', 'project-06/fi.webp'),
]

# We will iterate through all <img> tags and match against mapping
img_tag_regex = re.compile(r'(<img\s+[^>]*?>)', re.DOTALL)

def replace_img_src(match):
    tag = match.group(1)
    alt_m = re.search(r'alt=\"([^\"]*)\"', tag)
    if not alt_m:
        return tag
    alt_val = alt_m.group(1)
    
    # Find matching mapping
    matched_rel = None
    for alt_sub, rel_webp in mapping:
        if alt_sub in alt_val:
            matched_rel = rel_webp
            break
            
    if not matched_rel:
        print(f"Warning: No mapping found for img with alt: {alt_val[:40]}")
        return tag
        
    new_src = get_webp_b64(matched_rel)
    # Replace src="..." with new_src
    updated_tag = re.sub(r'src=\"[^\"]*\"', f'src="{new_src}"', tag)
    print(f"Updated img ({matched_rel}): old tag len {len(tag):,} -> new tag len {len(updated_tag):,}")
    return updated_tag

updated_html, count = img_tag_regex.subn(replace_img_src, html)
print(f"\nTotal <img> tags replaced: {count} of {len(mapping)}")
assert count == len(mapping), f"Expected {len(mapping)} replacements, got {count}"

# Verify updated HTML
assert updated_html.strip().endswith('</html>'), "HTML does not end properly"
orig_sz = len(html)
new_sz = len(updated_html)
print(f"Standalone HTML size: {orig_sz:,} chars -> {new_sz:,} chars (saved {orig_sz - new_sz:,} chars, {(1 - new_sz/orig_sz)*100:.1f}% reduction)")

with open(standalone_path, 'w', encoding='utf-8') as f:
    f.write(updated_html)
print("Updated standalone.html successfully.")

if os.path.exists(os.path.dirname(portfolio_artifact_path)):
    shutil.copyfile(standalone_path, portfolio_artifact_path)
    print(f"Copied to artifact {portfolio_artifact_path} ({os.path.getsize(portfolio_artifact_path):,} bytes)")

