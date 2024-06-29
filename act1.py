from PIL import Image
import os

ruta_imagen = input("Ingrese la ruta de la imagen: ")

if os.path.isfile(ruta_imagen):
    Img = Image.open(ruta_imagen)
    
    width, height = Img.size
    print('_____________________________________________')
    print(f'nombre      |   {Img.filename.split('\\')[-1]}')
    print('_____________________________________________')
    print(f'extension   |   {Img.format}')
    print('_____________________________________________')
    print(f'resulucion  |   {Img.size}')
    print('_____________________________________________')
    print(f'pixeles     |   {width * height}')
    print('_____________________________________________')
    print(f'ruta        |   {Img.filename}')
    print('_____________________________________________')

    Img.show()
else:
    print("La ruta no es valida")