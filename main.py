import qrcode
import os

carpeta_qrs = "assets"


def generar_qr(url: str, archivo: str = "qr_generado.png"):
    """Genera un código QR a partir de una URL y lo guarda en un archivo"""
    try:
        os.makedirs(carpeta_qrs, exist_ok=True)
        archivo = os.path.join(carpeta_qrs, archivo)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )

        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(archivo)
        print(f"✅ QR guardado como '{archivo}'")
        return True
    except Exception as e:
        print(f"❌ Error al generar el QR: {e}")
        return False


if __name__ == "__main__":
    print("🔗 Generador de Código QR")
    url_usuario = input(
        "👉 Ingresa la URL que quieres convertir en QR: ").strip()

    if url_usuario:
        archivo = input(
            "📁 Ingresa un nombre para el archivo (sin extensión): ").strip()
        if not archivo:
            archivo = "qr_generado"
        # Asegurar que termine en .png
        if not archivo.endswith('.png'):
            archivo += ".png"

        exito = generar_qr(url_usuario, archivo)
        if exito:
            print(f"🎉 ¡Listo! Tu QR está en la carpeta '{carpeta_qrs}'")
    else:
        print("⚠️ No ingresaste una URL válida.")
