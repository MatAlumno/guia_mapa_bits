from PIL import Image
import os

ruta_imagen = input("Ingrese la ruta de la imagen: ")

if os.path.isfile(ruta_imagen):
    nerdImg = Image.open(ruta_imagen)
    width, height = nerdImg.size
    print('_____________________________________________')
    print(f'nombre      |   {nerdImg.filename.split('\\')[-1]}')
    print('_____________________________________________')
    print(f'extension   |   {nerdImg.format}')
    print('_____________________________________________')
    print(f'resulucion  |   {nerdImg.size}')
    print('_____________________________________________')
    print(f'pixeles     |   {width * height}')
    print('_____________________________________________')
    print(f'ruta        |   {nerdImg.filename}')
    print('_____________________________________________')
    # Muestra la imagen
    nerdImg.show()
else:
    print("La ruta ingresada no es válida o el archivo no existe.")ñ