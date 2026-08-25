import os
import json
import numpy as np
from collections import defaultdict

def get_all_labels(json_dir):
    """JSON dosyalarındaki tüm etiketleri otomatik toplar"""
    labels = set()
    for json_file in os.listdir(json_dir):
        if json_file.endswith('.json'):
            with open(os.path.join(json_dir, json_file), 'r') as f:
                data = json.load(f)
                for shape in data['shapes']:
                    labels.add(shape['label'])
    return sorted(list(labels))

def labelme_to_yolo(json_dir, output_dir, class_list):
    os.makedirs(output_dir, exist_ok=True)
    
    for json_file in os.listdir(json_dir):
        if not json_file.endswith('.json'):
            continue
            
        json_path = os.path.join(json_dir, json_file)
        txt_path = os.path.join(output_dir, json_file.replace('.json', '.txt'))
        
        with open(json_path, 'r') as f_json, open(txt_path, 'w') as f_txt:
            data = json.load(f_json)
            
            for shape in data['shapes']:
                try:
                    class_id = class_list.index(shape['label'])
                except ValueError:
                    print(f"Uyarı: {shape['label']} etiketi class_list'te yok. Atlandı.")
                    continue
                
                points = np.array(shape['points'])
                x_min, y_min = np.min(points, axis=0)
                x_max, y_max = np.max(points, axis=0)
                
                x_center = (x_min + x_max) / (2 * data['imageWidth'])
                y_center = (y_min + y_max) / (2 * data['imageHeight'])
                width = (x_max - x_min) / data['imageWidth']
                height = (y_max - y_min) / data['imageHeight']
                
                f_txt.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")

if __name__ == "__main__":
    DESKTOP_PATH = os.path.join(os.path.expanduser("~"), "Desktop")
    PROJECT_PATH = os.path.join(DESKTOP_PATH, "proje")
    
    # KLASÖR İSİMLERİNİZİ BURAYA YAZIN
    INSTANCE_DIR = "apple_instance"      # Polygon etiketli klasör
    SEMANTIC_DIR = "apple_semantic"      # Rectangle etiketli klasör
    
    # Otomatik etiket toplama
    all_labels = get_all_labels(os.path.join(PROJECT_PATH, INSTANCE_DIR))
    all_labels += get_all_labels(os.path.join(PROJECT_PATH, SEMANTIC_DIR))
    class_list = sorted(list(set(all_labels)))
    
    print(f"Bulunan etiketler: {class_list}")
    
    # Instance-based dönüşüm
    labelme_to_yolo(
        json_dir=os.path.join(PROJECT_PATH, INSTANCE_DIR),
        output_dir=os.path.join(PROJECT_PATH, "yolo_instance"),
        class_list=class_list
    )
    
    # Semantic dönüşüm
    labelme_to_yolo(
        json_dir=os.path.join(PROJECT_PATH, SEMANTIC_DIR),
        output_dir=os.path.join(PROJECT_PATH, "yolo_semantic"),
        class_list=class_list
    )