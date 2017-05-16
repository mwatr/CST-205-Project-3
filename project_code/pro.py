#Project 3
#Alejandro Casillas, Michael Waters, Conrado Aguilar
from PIL import Image, ImageFilter              # This imports a specific section of a library
from PIL import ImageFont, ImageDraw            # This imports a specific section of a library
#Alejandro did this part (5-10)
im = Image.open( '1.png' )                     #This reads the image to allow the program to change it
                              
im.show()                                      #This displays the image 
safe = 1                                       
image = Image.open('1.png')                    #This reads the image to allow the program to change it
t,a = image.size                               #Get the cordinates of the image
#Michael did this part(12-27)
while safe == 1:                               # this is a while loop
    print 'There is five filters which you can chose from.'            #print displays thinks on the screen
    print 'Type 1 for a SHARPEN filter.'
    print 'Type 2 for a BLUR filter.'
    print 'Type 3 for a EDGE_ENHANCE filter.'
    print 'Type 4 for a SMOOTH filter.'
    print 'Type 5 for a CONTOUR filter.'
    print 'Type 6 for putting words on your picture.'
    print 'Type 7 for rotating the pic'
    print 'Type 0 to exit the program.'
    print 'Your x-coordinate of the pic is:',t
    print 'Your y-coordinate of the pic is:',a  
    number = input('Enter a number: ')             #lets the user input a number

    if number == 0:                                   # this are if statement for what the user enters
        safe = 0                                #gets out of the while loop
#Conrado did this part(29-40)
    if number == 1:
        im_sharp = im.filter( ImageFilter.SHARPEN )                  #changes the images     
        im_sharp.save( 'image_sharpened.jpg', 'JPEG' )         #It creates the image with the new filter
    elif number == 2:
        rad = int(raw_input('Enter how much blur do you want on your pic(1 to 50): '))    # Enter a number
        im_blur = im.filter(ImageFilter.GaussianBlur(radius= rad))              #  applys the filter
        im_blur.save('image_Gaublur.jpg', 'JPEG')            # saves the pic 

    elif number == 3:
        im_edge = im.filter(ImageFilter.EDGE_ENHANCE)         #  applys the filter
        im_edge.save('image_edge.jpg', 'JPEG')          #creates a new image
# Michael did this part(41-57)
    elif number == 4:
        im_smooth = im.filter(ImageFilter.SMOOTH)          #  applys the filter
        im_smooth.save('image_smooth.jpg', 'JPEG')            #creates a new image
    elif number == 5:
        im_contour = im.filter(ImageFilter.CONTOUR)           #  applys the filter
        im_contour.save('image_contour.jpg', 'JPEG')             #creates a new image

    elif number == 6:
        
        w = input('The x cordinate for the placement of words: ')            # Enter a number
        h = input('The y cordinate for the placement of words: ')               # Enter a number
        word = raw_input('Enter your text: ')                      # Enter a word
        big = input('Enter the size of your font(1 - 50): ')              # Enter a number
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("font.ttf", big)
        draw.text((w, h), word, font=font)               
        image.save('pic_with_word.jpg', "JPEG")                   #creates a new image
#Alejandro did the this part(58-68)
    elif number == 7:
        print 'Type 1 to rotate to the left.'              # displays the words on the screen
        print 'Type 2 to rotate to the right.'
        print 'Type 3 to turn the picture upside-down'
        spin = input('Enter the number to which you would want to rotate the pic: ')       # Enter a number
        if spin == 1:
            img2 = image.rotate(90)             # rotates the picture to the left
        if spin == 2:                   
            img2 = image.rotate(-90)              # rotates the picture to the right
        if spin == 3:
            img2 = image.rotate(180)            # rotates the picture upside down
        img2.save("rotated_pic.jpg", "JPEG")             #creates a new image