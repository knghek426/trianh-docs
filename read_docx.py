import zipfile
import xml.etree.ElementTree as ET
import glob
import sys

def read_docx(path):
    text_content = f"\n\n=================================\n--- Reading {path} ---\n=================================\n\n"
    try:
        with zipfile.ZipFile(path) as docx:
            xml_content = docx.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            text = []
            for p in tree.iterfind('.//w:p', ns):
                p_text = ''.join(node.text for node in p.iterfind('.//w:t', ns) if node.text)
                if p_text:
                    text.append(p_text)
            text_content += '\n'.join(text)
    except Exception as e:
        text_content += f'Error reading {path}: {e}'
    return text_content
    
with open('extracted_docs.txt', 'w', encoding='utf-8') as f:
    for file in glob.glob('*.docx'):
        f.write(read_docx(file))
print("Extraction complete.")
