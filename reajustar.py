from PIL import Image


img = Image.open('imc.png')
width =  1052 // 3
height = 113 // 3
img_resized = img.resize((width, height))
img_resized.save('Capa Redimensionada.png')