import numpy as np
import cv2
import matplotlib.pyplot as plt
from vektor import Vektor
blur_radius = 15
edge_cut = 30
left_cut = 0
right_cut = 0
top_cut = 0
bottom_cut = 0
nicoles_radius = 1


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
    # dat = img[minLoc[1]][:]
    
    # dat = [c[minLoc[0]] for c in img]
    dat = [min(k) for k in img] # horizontal bars
    saveable = []
    # TODO: make this iterable loop instead of setting the var
    i = 0
    lowest = 0
    for eachList in img:
        eachList = list(eachList)
        saveable += [[eachList.index(min(eachList)), i, min(eachList)]]
        if(saveable[lowest][2] > min(eachList)):
            lowest = i
        i += 1
    i = 0
    darkest = Vektor(saveable[lowest][0], saveable[lowest][1])
    for eachitem in saveable:
        v = Vektor(eachitem[0], eachitem[1])
        eachitem.append(v.nicolesAngle(darkest, nicoles_radius))
    print(minVal)

    plt.plot([k[3] for k in saveable], [k[2] for k in saveable])
    plt.ylabel('Greyscale')
    plt.xlabel('Angle')
    plt.show()
    fil = open("data.csv", "w")
    i = 0
    fil.write(str(minLoc) + "\n")
    for eachpoint in saveable:
        fil.write(str(eachpoint)[1:-1] + "\n")
        i+=1
    fil.close()
    cv2.circle(img, minLoc, 3 * radius, (255, 0, 0), 2)
    return img

def autocrop_edges(img):
    im8 = (img/256).astype('uint8')
    """Crops the black edges of the image"""
    im8 = (255 - im8)
    (_,thresh) = cv2.threshold(im8, 80, 150, cv2.THRESH_BINARY)
    (contours,high) = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    (x,y,w,h) = cv2.boundingRect(cnt)
    crop = img[y + top_cut : y + h - bottom_cut, x + left_cut : x + w - right_cut]
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
