import os
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

def create_voc_xml(json_path, output_dir):
    """LabelMe JSON'dan Pascal VOC XML oluşturur"""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # XML kök elementi
    root = ET.Element("annotation")
    
    # Görsel bilgileri
    ET.SubElement(root, "filename").text = os.path.basename(data["imagePath"])
    size = ET.SubElement(root, "size")
    ET.SubElement(size, "width").text = str(data["imageWidth"])
    ET.SubElement(size, "height").text = str(data["imageHeight"])
    ET.SubElement(size, "depth").text = "3"  # RGB varsayılan
    
    # Her nesne için bbox
    for shape in data["shapes"]:
        obj = ET.SubElement(root, "object")
        ET.SubElement(obj, "name").text = shape["label"]
        ET.SubElement(obj, "pose").text = "Unspecified"
        ET.SubElement(obj, "truncated").text = "0"
        ET.SubElement(obj, "difficult").text = "0"
        
        points = shape["points"]
        bbox = ET.SubElement(obj, "bndbox")
        ET.SubElement(bbox, "xmin").text = str(min(p[0] for p in points))
        ET.SubElement(bbox, "ymin").text = str(min(p[1] for p in points))
        ET.SubElement(bbox, "xmax").text = str(max(p[0] for p in points))
        ET.SubElement(bbox, "ymax").text = str(max(p[1] for p in points))
    
    # XML'i formatla ve kaydet
    xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ", encoding='utf-8')
    xml_file = os.path.join(output_dir, os.path.splitext(os.path.basename(json_path))[0] + ".xml")
    with open(xml_file, 'wb') as f:  # Binary modda yaz
        f.write(xml_str)

def convert_to_voc(json_dir, output_dir):
    """Tüm JSON'ları VOC'ye dönüştürür"""
    os.makedirs(output_dir, exist_ok=True)
    for json_file in os.listdir(json_dir):
        if json_file.endswith('.json'):
            create_voc_xml(
                json_path=os.path.join(json_dir, json_file),
                output_dir=output_dir
            )

if __name__ == "__main__":
    # Klasör yolları (Masaüstü/proje'ye göre ayarlayın)
    BASE_DIR = os.path.join(os.path.expanduser("~"), "Desktop", "proje")
    
    # Instance-based (polygon) dönüşümü
    convert_to_voc(
        json_dir=os.path.join(BASE_DIR, "apple_instance"),
        output_dir=os.path.join(BASE_DIR, "voc_instance")
    )
    
    # Semantic (rectangle) dönüşümü
    convert_to_voc(
        json_dir=os.path.join(BASE_DIR, "apple_semantic"),
        output_dir=os.path.join(BASE_DIR, "voc_semantic")
    )
    
    print("✅ Pascal VOC dönüşümü tamamlandı!")
    print(f"Çıktılar: {os.path.join(BASE_DIR, 'voc_instance')} ve {os.path.join(BASE_DIR, 'voc_semantic')}")