from PIL import Image

with Image.open(r"D:\parth\dev\python-programming\data\image1.jpg") as img:
    img.load()

print(img.size)
# img.show()

img_cropped = img.crop((100, 50, 250, 350))
print(img_cropped.size)
# img_cropped.show()

img_low_res = img.resize((img.height // 4, img.width // 2))
print(img_low_res.size)
# img_low_res.show()

img_low_equal_res = img.reduce(4)
print(img_low_equal_res.size)
img_low_equal_res.show()