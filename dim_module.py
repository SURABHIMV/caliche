# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 12:19:02 2023

@author: hp
"""


import cv2
import os
#from google.colab.patches import cv2_imshow
 
# Load the JPG image                                                           
                            
def imag(image):
    image1 = cv2.imread('C:/Users/hp/Pictures/dimension_measurement/images/'+image)
 
    # Convert the image to grayscale
    gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    # Apply thresholding to create a binary mask image using otsu's thresholding
    _, binary_mask = cv2.threshold(blurred, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    # Apply thresholding to create a binary mask image using simple thresholding
    #_, binary_mask = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    #saving the binary_mask image in .png format
    destination_dir = 'C:/Users/hp/Pictures/dimension_measurement/images/upload'
    os.makedirs(destination_dir, exist_ok=True)  # Create directory if it doesn't exist
    destination = os.path.join(destination_dir, image + '.png')
    cv2.imwrite(destination, binary_mask)
    
    #reading the saved .png image
    im = cv2.imread(destination)
    img = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    #Finding edges of the image
    #edge_image = cv2.Canny(img,250,200)
    contours, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #Reverting the original image back to BGR so we can draw in colors
    img_c = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    img_c1=cv2.drawContours(img_c, contours, -1, (0, 255, 0), 3)
    
    for contour in contours:
      # Calculate contour dimensions
       x, y, width, height = cv2.boundingRect(contour)
       #perimeter = cv2.arcLength(contour, True)

       # Display the measured dimensions
       #print("Width: {} pixel".format(width))
       w=width*0.0264583333
       print("Width in cm: {} cm".format(w))
       #print("Height: {} pixels".format(height))
       h=height*0.0264583333
       print("Height in cm: {} cm".format(h))
       # Draw the contour and bounding box on the image (optional)
       cv2.drawContours(img_c, [contour], 0, (0, 255, 0), 2)
       v=cv2.rectangle(img_c, (x, y), (x + width, y + height), (0, 0, 255), 2)
    
    return v
