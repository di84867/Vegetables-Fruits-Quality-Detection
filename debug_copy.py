import shutil
import os

source_dir = r"C:\Users\singh\.gemini\antigravity\brain\299770e0-16c7-4897-a01b-f7e4f92036a6"
dest_dir = r"c:\Users\singh\Desktop\Vegetables-Fruits-Quality-Detection\assets"

files = {
    "project_banner_1775659334916.png": "banner.png",
    "web_app_mockup_1775659465592.png": "web_app.png",
    "gui_app_mockup_1775659582631.png": "gui_app.png"
}

for src, dst in files.items():
    src_path = os.path.join(source_dir, src)
    dst_path = os.path.join(dest_dir, dst)
    print(f"Copying {src_path} to {dst_path}")
    if os.path.exists(src_path):
        shutil.copyfile(src_path, dst_path)
        print("Success")
    else:
        print("Source not found")
