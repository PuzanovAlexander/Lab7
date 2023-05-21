from PIL import Image

filename = "helltaker.jpeg"
with Image.open(filename) as img:
    img.load()

new_img = img.resize((img.width // 3, img.height // 3))

new_img.save("resized_helltaker.jpeg")

converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
converted_img.save("image_fliphelltaker_top.jpeg")
converted_img = img.transpose(Image.FLIP_LEFT_RIGHT)
converted_img.save("image_flip_helltaker.jpeg")