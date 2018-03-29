import numpy as np
import cv2
import matplotlib.pyplot as plt
blur_radius = 15
edge_cut = 30
def load_image_as_grayscale(filepath):
    """load an image as grayscale at the specified location and return it."""
    img = cv2.imread(filepath, -1)
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
    print(minLoc)

    # dat = img[minLoc[1]][:] # horizontal line
    # dat = [c[minLoc[0]] for c in img] # vertical line
    dat = [min(k) for k in img] # horizontal bars
    # dat = [min(k) for k in zip(*img)] # vertical bars
    # dat = [list(k).index(min(k)) for k in img] # index

    print(minVal)
    print(len(dat))
    print(len(img))
    plt.plot(dat)
    plt.ylabel('Greyscale')
    plt.xlabel('Distance in pixels')
    plt.show()
    fil = open("data.csv", "w")
    i = 0
    fil.write(str(minLoc) + "\n")
    for eachpoint in dat:
        fil.write(str(i) + "," + str(eachpoint) + "\n")
        i+=1
    fil.close()
    cv2.circle(img, minLoc, 3 * radius, (255, 0, 0), 2)
    return img

def autocrop_edges(img):
    im8 = (img/256).astype('uint8')
    """Crops the black edges of the image"""
    im8 = (255 - im8)
    _,thresh = cv2.threshold(im8, 80, 150, cv2.THRESH_BINARY)
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    x,y,w,h = cv2.boundingRect(cnt)
    crop = img[y + edge_cut : y + h - edge_cut, x + edge_cut : x + w - edge_cut]
    return crop

def cutFromTop(img,n):
    crop = img[:,n:]
    return crop

def cutFromBot(img,n):
    crop = img[:,:-n]
    return crop

def cutFromLeft(img,n):
    crop = img[n:,:]
    return crop

def cutFromRight(img,n):
    crop = img[:-n,:]
    return crop



def save_image(filename, img):
    cv2.imwrite(filename+"proc.tif", img)