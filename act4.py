from PIL import Image

img = Image.open('pwnitent.jpg')
width, height = img.size

print(width, height)

X1 = int(input('Ingrese la posición X donde iniciará el recorte: '))
while X1 > width:
    X1 = int(input('Su posición X es mayor que el ancho de la imagen. Ingrese nuevamente: '))
Y1 = int(input('Ingrese la posición Y donde iniciará el recorte: '))
while Y1 > height:
    Y1 = int(input('Su posición Y es mayor que la altura de la imagen. Ingrese nuevamente: '))

widthImg = int(input('Ingrese el ancho del recorte: '))
while widthImg + X1 > width:
    widthImg = int(input('El ancho del recorte más la posición X superan el ancho de la imagen. Ingrese nuevamente: '))
heightImg = int(input('Ingrese la altura del recorte: '))
while heightImg + Y1 > height:
    heightImg = int(input('La altura del recorte más la posición Y superan la altura de la imagen. Ingrese nuevamente: '))

croppedNerd = img.crop((X1, Y1, X1 + widthImg, Y1 + heightImg))

croppedNerd.save('croppedPenit.jpg')
croppedNerd.show()
