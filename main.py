from PIL import Image
import os


for number in range(5):
    image = Image.open(f"photo_{number}.jpg")
    file_path = f"photo_end_{number}"
    if not os.path.isdir(file_path):
        os.mkdir(file_path)
        
    inst_image = image.resize((1080, 1080))
    coordinates = (10, 0, inst_image.width-10, inst_image.height)
    inst_image = inst_image.crop(coordinates)
    inst_image.save(f"{file_path}/photo_inst.png", "PNG")
    
    vk_image = image.resize((1400, 1000))
    vk_image.save(f"{file_path}/photo_vk.png", "PNG")
    
    fb_image = image.resize((1200, 628))
    fb_image.save(f"{file_path}/photo_fb.png", "PNG")
