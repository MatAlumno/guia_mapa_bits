from PIL import Image
import os

def pixel(x1,y1,color):
    for y in range(y1, min(y1+pix, height)):
        for x in range(x1, min(x1+pix, width)):
            img.putpixel((x,y),color)

ruta_imagen = input("Ingrese la ruta de la imagen: ")
while not os.path.isfile(ruta_imagen):
    ruta_imagen = input("La ruta es incorrecta, reingresela: ")
    
pix = input("Ingrese la pixelacion de la imagen: ")
while int(pix)<2 or pix == '':
    ruta_imagen = input("La pixelacion es incorrecta, reingrese el numero: ")
pix = int(pix)
    
img = Image.open(ruta_imagen)
width, height = img.size

for y in range(0, height, pix):
    for x in range(0, width,  pix):
        color = img.getpixel((x,y))
        pixel(x,y,color)
        
img.save('imagenesFiltradas/imagePixelated.png')