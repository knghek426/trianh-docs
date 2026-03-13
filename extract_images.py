import zipfile
import os
import glob
import shutil

def extract_images_from_docx(docx_path, output_folder):
    # Ensure raw output folder exists
    base_name = os.path.splitext(os.path.basename(docx_path))[0]
    target_dir = os.path.join(output_folder, base_name)
    os.makedirs(target_dir, exist_ok=True)
    
    # Open docx as zip
    print(f"Extracting images from: {docx_path}")
    count = 0
    try:
        with zipfile.ZipFile(docx_path, 'r') as docx:
            for item in docx.namelist():
                if item.startswith('word/media/'):
                    filename = os.path.basename(item)
                    if filename:
                        # Trích xuất nội dung file thay vì dùng extract() để tránh lỗi thư mục
                        source = docx.read(item)
                        target_path = os.path.join(target_dir, filename)
                        with open(target_path, 'wb') as f:
                            f.write(source)
                        count += 1
        print(f" -> Extracted {count} images to {target_dir}")
    except Exception as e:
        print(f" -> Error reading {docx_path}: {e}")

# Chạy cho tất cả file docx trong thư mục hiện tại
output_base_folder = 'assets/extracted_images'
os.makedirs(output_base_folder, exist_ok=True)

for file in glob.glob('*.docx'):
    extract_images_from_docx(file, output_base_folder)
    
print("\\nAll Done!")
