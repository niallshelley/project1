# By Niall Shelley
from PIL import Image

def median(list):
    #Sort list, find median, return median
    listLen = len(list)
    sortedVals = sorted(list)
    middleIn = ((listLen+1)//2)-1
    return sortedVals[middleIn]

#Where the given images for the project are stored
imageList = []
#Put the images in the list
for i in range(1,9):
    imageList.append(Image.open(str(i)+'.png'))

#Establish the dimensions of the picture using the first image
picWid, picHigh = imageList[0].size

#Establish the output image
newIm = Image.new("RGB",(picWid, picHigh))

#Establish the pixel lists that will go through the median function for each color
redPix = []
bluePix = []
greenPix = []

#Iterate through each pixel
for w in range(picWid):
    for h in range(picHigh):
        #Iterate through all images for the given pixel
        for anImage in imageList:
            #Get the data of the given pixel and put it into the pixel lists
            r, g, b = anImage.getpixel((w,h))
            redPix.append(r)
            bluePix.append(b)
            greenPix.append(g)
        
        #Calculate the medians of each pixel
        medianRed = median(redPix)
        medianBlue = median(bluePix)
        medianGreen = median(greenPix)
        #Purge the lists for the next iteration
        redPix = [] 
        bluePix = []
        greenPix = []
        #Establish the RGB of the given pixel onto the output image
        newIm.putpixel((w,h), (medianRed,medianGreen,medianBlue))

#Output the image
newIm.save('projImage.png')