import cv2
import numpy as np

def grayscale_resize(imge, new_height, new_width):
    newresize = np.empty([new_width, new_height], dtype=np.uint8)  #resize image with type unint8
    x_neighbor = (new_width/imge.shape[0]) #resize ratio to find nearest neighbor pixel for width
    y_neighbor = (new_height/imge.shape[1]) #resize ratio for height
   
#   print(x_neighbor, y_neighbor, new_height )
    for i in range(new_width):
        for j in range(new_height):

            newresize[i, j, ] = imge[(int(i / x_neighbor)), (int(j / y_neighbor)), ] # with making the values an int - we get the nearest neighbor by the value rounded from the float
            
    return newresize


def grayscale_dither(img, threshold):
    print(img.shape[0])
    width = img.shape[0] - 5
    print(width)
    height = img.shape[1] -5
    dither = img
    for a in range(img.shape[0] -3):
        for b in range(img.shape[1] -3):
            i = a + 1 # to avoid initial edges
            j =  b + 1
            x = img[i,j]
            if x  < threshold:
                error =  img[i, j]
                dither[i, j] = 0
                dither[i, j+1] = (img[i, j+1] + error * 7 / 16)                    
                dither[i+1, j-1] = (img[i + 1, j- 1] + error * 3 / 16)
                dither[i+1, j] = (img[i+1, j] + error * 5 / 16)
                dither[i-1, j+1] = (img[i-1, j+1] + error * 1 / 16)
            else:
                error = 255 - img[i,j]
                dither[i,j] = 255
                dither[i, j+1] = (dither[i, j+1] - error * 7 / 16)
                dither[i+1, j-1] = (dither[i + 1, j- 1] - error * 3 / 16)
                dither[i+1, j] = (dither[i, j+1] - error * 5 / 16)
                dither[i-1, j+1] = (dither[i, j+1] - error * 1 / 16)

    return dither

def grayscale_dither_multilevel(img, levels):
    print(img.shape[0])
    width = img.shape[0] - 5
    print(width)
    height = img.shape[1] -5
    dither = img
    for a in range(img.shape[0] -3):
        for b in range(img.shape[1] -3):
            i = a + 1 # to avoid initial edges
            j =  b + 1
            x = img[i,j]
            lvl_min = levels[min(range(len(levels)), key=lambda i: abs(levels[i]- x))] #inline fnction to find the closest value of pixel value to the list
            dither[i, j] = lvl_min
            if x  < lvl_min:
                error =  lvl_min - img[i, j] 
                dither[i, j+1] = (img[i, j+1] + error * 7 / 16)                    
                dither[i+1, j-1] = (img[i + 1, j- 1] + error * 3 / 16)
                dither[i+1, j] = (img[i+1, j] + error * 5 / 16)
                dither[i-1, j+1] = (img[i-1, j+1] + error * 1 / 16)
            else:
                error = img[i,j] - lvl_min
                dither[i, j+1] = (dither[i, j+1] - error * 7 / 16)
                dither[i+1, j-1] = (dither[i + 1, j- 1] - error * 3 / 16)
                dither[i+1, j] = (dither[i, j+1] - error * 5 / 16)
                dither[i-1, j+1] = (dither[i, j+1] - error * 1 / 16)

    return dither
    




#GREY_IMAGE1 = cv2.imread('C:/Users/matth/Pictures/Art/Grayscale_Cat.jpg') #474 x 710 pixels
#GREY_IMAGE1 = cv2.imread('C:/Users/matth/Pictures/Art/junger_cat.png')

#cv2.imshow('yes', grayscale_resize(GREY_IMAGE1, 300, 300))


#gray = cv2.cvtColor(GREY_IMAGE1, cv2.COLOR_BGR2GRAY)

#cv2.imshow('yes', grayscale_dither_multilevel(gray, [100, 50, 25, 200, 255, 160, 199, 70, 78, 40, 30, 55, 1, 6]))
#cv2.waitKey()
