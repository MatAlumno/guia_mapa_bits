from PIL import Image
import os

ruta_imagen = input("Ingrese la ruta de la imagen: ")
while not os.path.isfile(ruta_carpeta):
    ruta_carpeta = input("La ruta es incorrecta, reingresela: ")
    
img = Image.open(ruta_imagen)
rot = input(f'ingrese los grados de rotacion: ')
while 0 > int(rot) > 360:
    rot = input(f'ingrese un numero entre 0 y 360: ')
img.rotate(int(rot), expand=True).save('rotation.jpg')
img = Image.open('rotation.jpg')
img.show()