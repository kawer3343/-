from PIL import Image
import os


image = Image.open("photo_0.jpg")

print("штука картинки ну да я не знаю:", image.mode)
print(image.height, image.width)
print(image.format)
print(image.size)

inst = image.resize((1080,1080))
print(inst.size)
inst.save("photo_inst.png", format="PNG")

vk = image.resize((1400,1000))
print(vk.size)
vk.save("photo_vk.png", format="PNG")

fb = image.resize((1200,628))
print(fb.size)
fb.save("photo_fb.png", format="PNG")
