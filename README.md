# Labelme Dataset Converter (COCO, Pascal VOC, YOLO)

Bu repo, Labelme görsel etiketleme aracı kullanılarak poligon (segmentasyon) formatında etiketlenmiş özel veri setlerini popüler derin öğrenme formatlarına (**COCO**, **Pascal VOC** ve **YOLO**) dönüştürmek için kullanılan Python betiklerini içerir.

Proje hem **Instance Segmentation** (nesne ayrımı) hem de **Semantic Segmentation** (anlamsal bölütleme) görevlerini desteklemektedir.

---

## 📁 Proje Yapısı

```text
labelme-dataset-converter/
├── apple_instance/           # Örnek Instance Segmentation girdi verisi (.jpg ve .json)
├── apple_semantic/           # Örnek Semantic Segmentation girdi verisi (.jpg ve .json)
├── labelme_to_coco.py        # Labelme -> COCO formatı dönüştürücü (.json)
├── labelme_to_voc.py         # Labelme -> Pascal VOC formatı dönüştürücü (Maskeler / XML)
├── labelme_to_yolo.py        # Labelme -> YOLO formatı dönüştürücü (.txt poligon/kutu)
```

---

##  Desteklenen Formatlar

1. **COCO Formatı (`labelme_to_coco.py`)**:
   - Standart `coco_instance.json` ve `coco_semantic.json` formatlarında toplu etiket dosyası üretir.

2. **Pascal VOC Formatı (`labelme_to_voc.py`)**:
   - Segmentasyon maskeleri (PNG indeks/renkli maskeler) ve sınıf haritaları oluşturur.

3. **YOLO Formatı (`labelme_to_yolo.py`)**:
   - Normalize edilmiş poligon koordinatlarını içeren `.txt` etiket dosyaları üretir.

---

##  Kurulum

Gereksinimleri yükleyin:

```bash
pip install numpy pillow opencv-python labelme
```

---

##  Kullanım

İlgili dönüştürücü scripti çalıştırmak için terminalden aşağıdaki komutları kullanabilirsiniz:

### 1. COCO Formatına Dönüştürme:
```bash
python labelme_to_coco.py
```

### 2. Pascal VOC Formatına Dönüştürme:
```bash
python labelme_to_voc.py
```

### 3. YOLO Formatına Dönüştürme:
```bash
python labelme_to_yolo.py
```

*Not: Scriptler varsayılan olarak `apple_instance/` ve `apple_semantic/` klasörlerindeki görselleri ve JSON etiketlerini okuyup çıktı klasörlerini (`voc_*`, `yolo_*`, `coco_*.json`) otomatik oluşturur.*
