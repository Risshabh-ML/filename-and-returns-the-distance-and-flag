import cv2 as cv
import ntpath
import matplotlib.pyplot as plt
import sys
import os
path = r'C:\Users\Rishab\Desktop\intership\Images'

files = os.listdir(path)
def midpoint(image):
    a = image.shape
    y = int((a[0])/2)
    x = int((a[1])/2)
    return (x,y)


# function takes full file path
def get_filename(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


# find contours in the image
def findContr(edgeImg):
    _, contours, _  = cv.findContours(edgeImg.copy(), cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    return contours


# check if the midpoint pixel is on a contour line, if so, return a list of distances to nearest contours
def checkfence(image):
    distances_fence = []
    for i in findContr(image):
        check = cv.pointPolygonTest((i),midpoint(image),False)
        distances = abs(int(cv.pointPolygonTest((i),midpoint(image),True)))
        if check == 0:
            distances_fence.append(distances)
    fence = (distances_fence)
    return fence


# check if the midpoint pixel is outside a contour, if so, return a list of distances to nearest contours
def checkoutside(image):
    distances_out = []
    for i in findContr(image):
        check = cv.pointPolygonTest((i),midpoint(image),False)
        distances = abs(int(cv.pointPolygonTest((i),midpoint(image),True)))
        if check == -1:
            distances_out.append(distances)
    outside = (distances_out)
    return outside


# check if the midpoint pixel is inside a contour, if so, return distance to nearest contour wall
def checkinside(image):
    for i in findContr(image):
        check = cv.pointPolygonTest((i),midpoint(image),False)
        if check == 1:
            distance = abs(int(cv.pointPolygonTest((i),midpoint(image),True)))
            if distance is not []:
                return distance


# function to create image with edges defined using Laplacian algorithm
def edgedetect(image):
    # given image is converted to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # performs edge detection, then perform a dilation + erosion to
    # close gaps in between object edges
    edged = cv.Laplacian(src=gray, ddepth=cv.CV_8U, ksize=5)
    edged = cv.dilate(edged, None, iterations=1)
    edged = cv.erode(edged, None, iterations=1)
    return edged



if __name__ == "__main__":

    for file in files:
        print('enter 1 if you want more image distance or aenter any no you dont want more img1')
        num = int(input("Enter a number: "))
        if (num==1):
            fn = input("Enter Filename: ")
            img = cv.imread(fn)
            plt.imshow(img)
            plt.show()
            edges = edgedetect(img)
            plt.imshow(edges)
            plt.show()
            name = get_filename(fn)
            print(name)
            # if statements to check distances
            if checkinside(edges) is not None:
                print(f'\n Filename: {name} | flag: wall : ', checkinside(edges))
            elif checkoutside(edges) is not None:
                print(f'\n Filename: {name} | flag: building: ', min(checkoutside(edges)))
            else:
                print(f'\n Filename: {name} | flag: road : ', min(checkfence(edges)))

        else:
            exit()
