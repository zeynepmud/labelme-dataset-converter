# Labelme Dataset Converter (COCO, Pascal VOC, YOLO)

Bu repo, **Labelme** görsel etiketleme aracı kullanılarak oluşturulan özel veri setlerinin popüler derin öğrenme formatlarına (**COCO**, **Pascal VOC** ve **YOLO**) dönüştürülmesi amacıyla geliştirilmiştir.

Proje kapsamında kullanılan veri seti **tarafımca oluşturulmuş ve Labelme kullanılarak poligon (segmentasyon) formatında etiketlenmiştir.**

Proje hem **Instance Segmentation** (nesne ayrımı) hem de **Semantic Segmentation** (anlamsal bölütleme) görevlerini desteklemektedir.

---

## 📁 Proje Yapısı

```text
labelme-dataset-converter/
├── apple_instance/           # Oluşturulan Instance Segmentation veri seti
│   ├── *.jpg
│   └── *.json
│
├── apple_semantic/           # Oluşturulan Semantic Segmentation veri seti
│   ├── *.jpg
│   └── *.json
│
├── labelme_to_coco.py        # Labelme → COCO dönüştürücü
├── labelme_to_voc.py         # Labelme → Pascal VOC dönüştürücü
├── labelme_to_yolo.py        # Labelme → YOLO dönüştürücü
└── README.md
