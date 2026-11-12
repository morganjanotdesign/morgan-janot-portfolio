import os
import shutil
from PIL import Image

src_img_dir = 'src/assets/images'
dest_dirs = [
    'src/assets/images_webp',
    'images_webp',
    '/Users/morganjanot/.gemini/antigravity/brain/df18ad40-ac30-4b7a-b04f-f3de4961c66b/images_webp'
]

# Ensure destination directories exist
for d in dest_dirs:
    os.makedirs(d, exist_ok=True)

converted_files = []

for root, dirs, files in os.walk(src_img_dir):
    for f in sorted(files):
        ext = os.path.splitext(f)[1].lower()
        if ext in ['.png', '.jpg', '.jpeg', '.webp']:
            full_src = os.path.join(root, f)
            rel_path = os.path.relpath(full_src, src_img_dir)
            base_name, _ = os.path.splitext(rel_path)
            webp_rel_path = base_name + '.webp'

            print(f"Converting: {rel_path} -> {webp_rel_path}")

            if ext == '.webp':
                # Already webp, read directly
                with open(full_src, 'rb') as fp:
                    data = fp.read()
            else:
                im = Image.open(full_src)
                # Save to memory first
                import io
                buf = io.BytesIO()
                im.save(buf, format='WEBP', quality=95, method=5)
                data = buf.getvalue()

            orig_sz = os.path.getsize(full_src)
            webp_sz = len(data)
            reduction = (1 - webp_sz / orig_sz) * 100 if orig_sz > 0 else 0
            print(f"  {orig_sz:,} B -> {webp_sz:,} B ({reduction:.1f}% reduction)")

            # Write to all destination directories
            for dest_base in dest_dirs:
                dest_file = os.path.join(dest_base, webp_rel_path)
                os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                with open(dest_file, 'wb') as fp:
                    fp.write(data)

            converted_files.append((rel_path, webp_rel_path, data))

print(f"\nSuccessfully converted and copied {len(converted_files)} images to all webp folders!")
