from PIL import Image

water = "watermark.png"
with Image.open(water) as img_water:
    img_water.load()

img_water = Image.open(water)
img_water = img_water.resize((img_water.width // 2, img_water.height // 2))


filename = "helltaker.jpeg"
with Image.open(filename) as img:
    img.load()


img.paste(img_water, (10, 440), img_water)
img.save("watermark_helltaker.jpeg")