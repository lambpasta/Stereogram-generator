# Importing Image from PIL package
from PIL import Image
from numpy import interp

blackoffset = 340 # define the pixel width of the background
whiteoffset = 230 # define the pixel width of the foreground

fullhd = (1920, 1080)
OUTPUT_SIZE = fullhd

# creating a image object
stereo = Image.open(r"Assets\train.jpg").resize(OUTPUT_SIZE)
reference = Image.open(r"Assets\noise.jpg").resize(OUTPUT_SIZE)
edit = reference.load()


print("\n\nWelcome to Stereogram maker")
print("output image size: "+str(OUTPUT_SIZE)+"\n")

xoffset = (reference.width-stereo.width)/2
yoffset = (reference.height-stereo.height)/2


for row in range(stereo.height):
    if (row%(round(stereo.height/10))==0):
        print("Generating... "+str(round(row/stereo.height*100))+"%")
    for col in range(stereo.width):
            redValue = stereo.getpixel((col, row))[0]
            depthoffset = round(interp(redValue,[0,255],[blackoffset, whiteoffset]))
            edit[col, row] = reference.getpixel((col+xoffset-depthoffset, row+yoffset))

print("Stereogram complete!")

reference.show()