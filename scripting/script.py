from PIL import Image, ImageFilter

img = Image.open("./img/nov_22.jpeg")
# filtered_img = img.filter(ImageFilter.BLUR)
print(img.size, img.format, img.mode)
filtered_img.save("./img/blur.png", "png")
