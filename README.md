# 🔗 Generador de Código QR

Un generador simple de códigos QR en Python. Convierte cualquier URL en una imagen PNG con código QR.

## 📋 Requisitos

- Python 3.11+
- pip (gestor de paquetes de Python)

## 🚀 Instalación y uso

1. **Clona o descarga el proyecto:**
```bash
git clone https://github.com/sebitabravo/qrgen.git
cd qrgen
```

2. **Instala las dependencias:**
```bash
pip install -r requirements.txt
```

3. **Ejecuta el programa:**
```bash
python main.py
```

4. **¡Úsalo!**
   - Ingresa la URL que quieres convertir
   - Dale un nombre al archivo (sin extensión)
   - El QR se guardará automáticamente en la carpeta `assets/`

## 📁 Estructura del proyecto

```
qrgen/
├── main.py          # Programa principal
├── requirements.txt # Dependencias
├── assets/          # Carpeta donde se guardan los QRs
└── README.md        # Este archivo
```

## 🛠️ Dependencias

- `qrcode[pil]` - Para generar códigos QR

## 📄 Licencia

Este proyecto es de código abierto. ¡Úsalo como quieras!
