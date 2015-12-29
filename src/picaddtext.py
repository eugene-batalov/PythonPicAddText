from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
#from os import os
from glob import glob

"""img = Image.open("z1_p01_c1_i.jpg")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("MyriadPro-Bold.otf", 42)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((40, 35),"1",(255,255,255),font=font)
img.save('z1_p01_c1_i-out.jpg')"""

for filename in glob('*.jpg'):
    img = Image.open(filename)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("MyriadPro-Bold.otf", 42)
    draw.text((17, 35),"0"+filename[4:6],(0,0,0),font=font)#(255,255,255),font=font)
    img.save(filename[4:6]+'.jpg')