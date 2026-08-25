import os
import json
import numpy as np
from datetime import datetime

def convert_to_coco(json_dir, output_file):
    """LabelMe JSON'larını COCO formatına dönüştürür."""
    coco = {
        "info": {"description": "COCO Dataset", "date_created": datetime.now().strftime("%Y-%m-%d")},
        "licenses": [],
        "images": [],
        "annotations": [],
        "categories": [{"id": 0, "name": "apple"}]  # Tek sınıf: apple
    }
    
    image_id = 1
    annotation_id = 1
    
    for json_file in os.listdir(json_dir):
        if not json_file.endswith('.json'):
            continue
            
        json_path = os.path.join(json_dir, json_file)
        with open(json_path, 'r') as f:
            data = json.load(f)
        
        # Görsel bilgisi (JSON ile aynı isimde .jpg/.png olduğunu varsayar)
        image_file = json_file.replace('.json', '.jpg')  # .png de olabilir
        coco["images"].append({
            "id": image_id,
            "file_name": image_file,
            "width": data["imageWidth"],
            "height": data["imageHeight"]
        })
        
        # Etiketleri işle
        for shape in data["shapes"]:
            points = np.array(shape["points"])
            x_min, y_min = np.min(points, axis=0)
            x_max, y_max = np.max(points, axis=0)
            width = x_max - x_min
            height = y_max - y_min
            
            coco["annotations"].append({
                "id": annotation_id,
                "image_id": image_id,
                "category_id": 0,  # apple sınıfı
                "bbox": [x_min, y_min, width, height],
                "area": width * height,
                "iscrowd": 0
            })
            annotation_id += 1
        
        image_id += 1
    
    with open(output_file, 'w') as f:
        json.dump(coco, f, indent=2)

if __name__ == "__main__":
    # Instance-based (polygon) dönüşümü
    convert_to_coco(
        json_dir="apple_instance",
        output_file="coco_instance.json"
    )
    
    # Semantic (rectangle) dönüşümü
    convert_to_coco(
        json_dir="apple_semantic",
        output_file="coco_semantic.json"
    )
    
    print("Dönüşüm tamamlandı! Çıktılar:")
    print("- coco_instance.json (polygon etiketler)")
    print("- coco_semantic.json (rectangle etiketler)")