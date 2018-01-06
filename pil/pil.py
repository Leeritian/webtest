import PIL.Image as Image
import os, sys

img_width=170
img_height=60
target_width=6
target_height=11

path='d:\\fff\\pil\\img\\'
images=[]
for file in os.listdir(path):
    f=os.path.join(path,file)
    images.append(f)
img=[]
for im in images:
    im=Image.open(im)
    im = im.resize((170,60),Image.NEAREST)
    img.append(im)

target=Image.new('RGB',(img_width*target_width,img_height*target_height))
for i in range(0,target_height):
    for j in range(0,target_width):
        try:
            target.paste(img[target_height*j+i],(j*img_width,i*img_height))
        except IndexError:
            break

target.show()
target.save('d:\\fff\\pil\\target.png')
