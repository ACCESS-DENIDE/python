from PIL import Image, ImageFilter


with Image.open("resourses/sobaken.jpg") as img:
        img.load()

def Ex1():
 
    img.show()
    print("Ширина: ", img.size[0])
    print("Высота:  ", img.size[1])
    print("Формат: ", img.format)
    print("Цветовая модель:", img.mode)

def Ex2():
    compressed_img = img.resize((img.width // 3, img.height // 3))
    compressed_img.save("compressed_sobaken.jpg")

    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    flipped_img.save("image_flipLR_sobaken.jpg")
    flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    flipped_img.save("image_flipTop_sobaken.jpg")

def Ex3():
     for i in range(1, 6):
       f_name="resourses/"+str(i)+".jpg"
       with Image.open(f_name) as img:
            img.load()
            new_img = img.filter(ImageFilter.FIND_EDGES)
            new_img.save("new_" +str(i)+".jpg")
            img.close()

def Ex4():
    with Image.open("resourses/watermark.png") as img_water:
        img_water.load()
    img_water=img_water.convert('RGBA')
    
    for i in range(1, 6):
        f_name="resourses/"+str(i)+".jpg"
        with Image.open(f_name) as img:
            img.load()
        img=img.convert('RGBA')
        
        layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
        img_water=img_water.resize(img.size)
        layer.paste(img_water)
        layer2 = layer.copy()
        layer2.putalpha(128)
        layer.paste(layer2, layer)

        outp=Image.alpha_composite(img, layer)

        outp=outp.convert('RGB')
        outp.save("marked_"+str(i)+".jpg")
        img.close()
        
    img_water.close()

Ex1()