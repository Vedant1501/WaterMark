
# To add a watermark to an image

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
     

# PIL - Python Imaging Library  
    
# Creating a function
def watermark(input_image_path,output_image_path,text, pos,text_color, size):
    ''' We take input image and watermark it positioning it
         according to our wish and save it with a new filename'''
    # open image to be watermarked
    photo = Image.open(input_image_path)

    # make the image editable
    drawing = ImageDraw.Draw(photo)
    font = ImageFont.truetype("arial.ttf", size = 100)       #ttf = True Type Format
    drawing.text(pos, text, text_color, font=font)
    photo.show()
    photo.save(output_image_path)

    
if __name__ == '__main__':
    watermark(input_image_path='E:\Wallpaper\Rick & Morty Dark.jpg',
                   output_image_path='E:\Wallpaper\edited.jpg',
                   text='THIS IS A WATERMARK',
                   size = 100,
                   pos=(500, 150),      # x and y co-ordinates of the watermark
                   text_color = 'yellow')
