import numpy as np
import cv2
blur_radius = 15

def load_image_as_grayscale(filepath):
    """load an image as grayscale at the specified location and return it."""
    img = cv2.imread(filepath, 0)
    return img

def apply_blur(img):
    """Blurs the image that is passed to it by the global blur_radius variable"""
    radius = blur_radius
    gray = img.copy()
    gray = cv2.GaussianBlur(gray, (radius, radius), 0)
    return gray

def circle_darkest(img):
    """Circles the darkest point in an image."""
    radius = blur_radius
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(img)
    cv2.circle(img, minLoc, 3 * radius, (255, 0, 0), 2)
    return img

def autocrop_edges(img):
    """Crops the black edges of the image"""
    _,thresh = cv2.threshold(img, 1, 255, cv2.THRESH_BINARY)
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    x,y,w,h = cv2.boundingRect(cnt)
    crop = img[y : y + h, x : x + w]
    return crop

#x = load_image_as_grayscale('warn.jpg')
#x = apply_blur(x)
#x = autocrop_edges(x)
#x = circle_darkest(x)
#cv2.imshow("Circled Darkest", x)
#cv2.waitKey(0)
