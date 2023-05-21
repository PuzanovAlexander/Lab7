from PIL import Image, ImageFilter

filenames = ["1.jpeg", "2.jpg", "3.jpg", "4.jpg", "5.jpeg"]

for file in filenames:
    with Image.open(file) as img:
        img.load()
        new_img = img.filter(ImageFilter.CONTOUR)
        # new_img.show()
        new_img.save(f"new_{file}")