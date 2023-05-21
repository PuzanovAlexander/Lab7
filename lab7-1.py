from PIL import Image

filename = "helltaker.jpeg"
with Image.open(filename) as img:
    img.load()

img.show()
width, height = img.size

format = img.format

mode = img.mode

print("Ширина: ", width)
print("Высота:  ", height)
print("Формат: ", format)
print("Цветовая модель:", mode)