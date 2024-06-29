from PIL import Image
import os

ruta_imagen = input("Ingrese la ruta de la imagen: ")
while not os.path.isfile(ruta_imagen):
    ruta_imagen = input("La ruta es incorrecta, reingresela: ")

img = Image.open(ruta_imagen)
width, height = img.size

for y in range(height):
    for x in range(width):
        color = img.getpixel((x,y))
        gray = round((color[0]+color[1]+color[2])/3)
        img.putpixel((x,y),(gray,gray,gray))
        
img.save('imagenesFiltradas/imageGray.png')