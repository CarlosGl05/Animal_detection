# Detección y Clasificación de Fauna Marina en Video 🐢🐬🦈

Este proyecto implementa y contrasta dos enfoques de visión computacional para la detección y clasificación automática de especies marinas (delfines, tortugas y tiburones gata) en grabaciones de video subacuáticas.

## 📋 Descripción del Proyecto

El monitoreo de especies marinas presenta desafíos únicos debido a la distorsión del agua, los cambios de iluminación y el camuflaje natural. Este repositorio aborda el problema con dos metodologías:

1. **Visión Clásica (`Mask_detection`):** Utiliza OpenCV para la segmentación de imágenes basada en el espacio de color HSV, desenfoque Gaussiano y operaciones morfológicas para detectar siluetas por contraste.
2. **Deep Learning (`YOLO_detection`):** Emplea una red neuronal convolucional (YOLOv8) entrenada específicamente para realizar detección y clasificación taxonómica simultáneas en tiempo real, demostrando mayor robustez ante los cambios del entorno subacuático.

## 📂 Estructura del Repositorio

```text
ANIMAL_DETECTION/
├── Mask_detection/
│   ├── MaskDetection.py       # Script de detección por segmentación de color y contornos
│   ├── delfines.mp4
│   ├── tiburon.mp4
│   └── tortugas.mp4
├── YOLO_detection/
│   ├── train/
│   │   ├── best.pt            # Pesos finales del modelo YOLOv8 entrenado
│   │   ├── best2.pt
│   │   └── Train_Yolo_sea_animal_detection.ipynb  # Notebook de entrenamiento (Google Colab)
│   ├── Videos/
│   │   ├── delfines.mp4
│   │   ├── tiburon.mp4
│   │   └── tortugas.mp4
│   └── detection.py           # Script de inferencia usando YOLOv8
└── README.md
```

## ⚙️ Requisitos e Instalación

Se recomienda ejecutar este proyecto dentro de un entorno virtual de Python (probado en Python 3.12.7) para evitar conflictos de dependencias.

### 1. Clonar el repositorio

```bash
git clone <https://github.com/CarlosGl05/Animal_detection.git>
cd ANIMAL_DETECTION
```

### 2. Crear y activar el entorno virtual

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install opencv-python ultralytics numpy
```

## 🚀 Uso

### Enfoque Clásico (Máscaras de Color)

Procesa los videos secuencialmente aplicando filtros morfológicos para detectar movimiento y siluetas.

```bash
cd Mask_detection
python MaskDetection.py
```

> **Controles:** Presiona `q` para cerrar el video actual y avanzar al siguiente.

### Enfoque Deep Learning (YOLOv8)

Carga los pesos entrenados del modelo para dibujar cajas delimitadoras y etiquetas de clasificación sobre los animales detectados.

```bash
cd YOLO_detection
python detection.py
```

> **Controles:** Presiona `q` para cerrar el video actual y avanzar al siguiente.

## 🧠 Tecnologías Utilizadas

| Categoría | Herramientas |
|---|---|
| Lenguaje | Python 3.x |
| Visión Clásica | OpenCV (`cv2`), NumPy |
| Deep Learning | Ultralytics (YOLOv8) |
| Entrenamiento | Google Colab (GPU T4) |
| Gestión de Datasets | Roboflow |

## 👤 Autor

**Carlos Andrés Gloria Cortés**  
Estudiante de Ingeniería en Tecnologías Computacionales  
Tecnológico de Monterrey