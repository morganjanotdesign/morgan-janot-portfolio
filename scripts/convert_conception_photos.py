import os
import io
import shutil
from PIL import Image

src_dir = '/Users/morganjanot/Desktop/perso/portfolio /portfolio/PROJET /01'
target_dirs = [
    'src/assets/images/project-01',
    'src/assets/images_webp/project-01',
    'images/project-01',
    'images_webp/project-01',
    '/Users/morganjanot/Desktop/perso/portfolio /portfolio/PROJET /01',
    '/Users/morganjanot/.gemini/antigravity/brain/df18ad40-ac30-4b7a-b04f-f3de4961c66b/images/project-01',
    '/Users/morganjanot/.gemini/antigravity/brain/df18ad40-ac30-4b7a-b04f-f3de4961c66b/images_webp/project-01'
]

for d in target_dirs:
    os.makedirs(d, exist_ok=True)

converted = {}

for i in range(1, 6):
    src_file = os.path.join(src_dir, f'{i}.jpg')
    assert os.path.exists(src_file), f"Source file not found: {src_file}"
    im = Image.open(src_file)
    buf = io.BytesIO()
    # Save as high quality WebP
    im.save(buf, format='WEBP', quality=92, method=5)
    data = buf.getvalue()
    converted[i] = data
    orig_sz = os.path.getsize(src_file)
    webp_sz = len(data)
    print(f"Converted {i}.jpg: {orig_sz:,} B -> {webp_sz:,} B ({(1 - webp_sz/orig_sz)*100:.1f}% reduction)")
    
    # Save to all target directories
    for d in target_dirs:
        out_path = os.path.join(d, f'{i}.webp')
        with open(out_path, 'wb') as fp:
            fp.write(data)

print("All 5 conception photos converted and saved to all target locations successfully!")
