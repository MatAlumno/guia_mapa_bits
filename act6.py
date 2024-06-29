from PIL import Image
import os

def reSize(rute, width, height):
    img = Image.open(rute)
    resizedImg = img.resize((width,height))
    return(resizedImg)
    
    
ruta_carpeta = input("Ingrese la ruta de la carpeta que contiene las imágenes: ")
while not os.path.isdir(ruta_carpeta):
    ruta_carpeta = input("La ruta es incorrecta, reingresela: ")

imagenes = []
for archivo in os.listdir(ruta_carpeta):
    if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        ruta_completa = os.path.join(ruta_carpeta, archivo)
        imagenes.append(ruta_completa)
print(imagenes)

#WIDTH
collageW = input('Ingrese el ancho del collage: ')
while int(collageW) < 10 or collageW == '':
    X1 = int(input('ingrese un valor mayor: '))
collageW = int(collageW)
#HEIGHT
collageH = input('Ingrese el alto del collage: ')
while int(collageH) < 10 or collageH == '':
    X1 = int(input('ingrese un alto mayor: '))
collageH = int(collageH)

count = 0
resImg = Image.new('RGBA', (collageW, collageH))
for y in range(0,collageH,round(collageH/3)):
    for x in range(0,collageW,round(collageW/3)):
        if count < 9:
            resImg.paste(reSize(imagenes[count],round(collageW/3),round(collageH/3)),(x,y))
        count += 1
resImg.save('collage.png')