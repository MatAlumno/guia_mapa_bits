from PIL import Image

def add_watermark(base_image_path, watermark_image_path, position):
    base_image = Image.open(base_image_path).convert("RGBA")
    watermark = Image.open(watermark_image_path).convert("RGBA")

    base_width, base_height = base_image.size
    watermark_width, watermark_height = watermark.size

    if position == 'Superior izquierda':
        position = (50, 50)
    elif position == 'Superior derecha':
        position = (base_width - watermark_width - 50, 50)
    elif position == 'Inferior izquierda':
        position = (50, base_height - watermark_height - 50)
    elif position == 'Inferior derecha':
        position = (base_width - watermark_width - 50, base_height - watermark_height - 50)
    else:
        raise ValueError("Posición no válida")

    base_image.paste(watermark, position, watermark)
    
    output_path = "imagen_marcada.png"
    base_image.save(output_path, "PNG")

    print(f"Imagen guardada en: {output_path}")

base_image_path = input("Introduce la ruta de la imagen base: ")
watermark_image_path = input("Introduce la ruta de la imagen de la marca de agua: ")
print("Opciones de posición: Superior izquierda, Superior derecha, Inferior izquierda, Inferior derecha")
position = input("Introduce la posición de la marca de agua: ")

add_watermark(base_image_path, watermark_image_path, position)