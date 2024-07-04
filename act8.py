from PIL import Image
import os

#kernelS
kernel_3x3 = [
    [1/16, 2/16, 1/16],
    [2/16, 4/16, 2/16],
    [1/16, 2/16, 1/16]
]
kernel_5x5 = [
    [1/256,  4/256,  6/256,  4/256,  1/256],
    [4/256, 16/256, 24/256, 16/256,  4/256],
    [6/256, 24/256, 36/256, 24/256,  6/256],
    [4/256, 16/256, 24/256, 16/256,  4/256],
    [1/256,  4/256,  6/256,  4/256,  1/256]
]
kernel_7x7 = [
    [0.000036, 0.000363, 0.001446, 0.002289, 0.001446, 0.000363, 0.000036],
    [0.000363, 0.003676, 0.014832, 0.023287, 0.014832, 0.003676, 0.000363],
    [0.001446, 0.014832, 0.059635, 0.093013, 0.059635, 0.014832, 0.001446],
    [0.002289, 0.023287, 0.093013, 0.145688, 0.093013, 0.023287, 0.002289],
    [0.001446, 0.014832, 0.059635, 0.093013, 0.059635, 0.014832, 0.001446],
    [0.000363, 0.003676, 0.014832, 0.023287, 0.014832, 0.003676, 0.000363],
    [0.000036, 0.000363, 0.001446, 0.002289, 0.001446, 0.000363, 0.000036]
]

def apply_filter(image, kernel):
    img_width, img_height = image.size
    pixels = image.load()
    #agarra el pixel
    for y in range(img_height):
        for x in range(img_width):
            red, green, blue = 0, 0, 0
            #agarra los pixeles de alrededor
            for ky in range(len(kernel)):
                for kx in range(len(kernel[0])):
                    pixelX = x + kx - len(kernel[0]) // 2
                    pixelY = y + ky - len(kernel) // 2
                    #aplicar filtro con kernel
                    if 0 <= pixelX < img_width and 0 <= pixelY < img_height:
                        r, g, b = pixels[pixelX, pixelY]
                        red += int(r * kernel[ky][kx])
                        green += int(g * kernel[ky][kx])
                        blue += int(b * kernel[ky][kx])
                        
            pixels[x, y] = (red, green, blue)
    
    return image

ruta_imagen = input("Ingrese la ruta de la imagen: ")
while not os.path.isfile(ruta_imagen):
    ruta_imagen = input("La ruta es incorrecta, reingresela: ")

img = Image.open(ruta_imagen)

img_filtrada_3x3 = apply_filter(img, kernel_3x3)
img_filtrada_5x5 = apply_filter(img, kernel_5x5)
img_filtrada_7x7 = apply_filter(img, kernel_7x7)

img_filtrada_3x3.save('imagenesFiltradas/imageGaus3x3.png')
img_filtrada_5x5.save('imagenesFiltradas/imageGaus5x5.png')
img_filtrada_7x7.save('imagenesFiltradas/imageGaus7x7.png')

print("GUARDADO")
