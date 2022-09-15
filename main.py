import cv2 as cv

img = cv.imread('colors.jpg', 1)

#Resize
width = int(img.shape[1] * 60/100)
height = int(img.shape[0] * 60/100)
dim = (width, height)
img = cv.resize(img, dim, interpolation = cv.INTER_AREA)

r = g = b = x = y = 0

def color_code(event,x,y,flags,params):
    if event == cv.EVENT_LBUTTONDBLCLK:
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
        cv.imshow('Color Code Detector', img)
        cv.rectangle(img, (20,20), (400,60), (b,g,r), -1)
        text =' RGB = ('+str(r) +","+str(g)+","+str(b)+")"
        cv.putText(img,text,(50,50),2,0.8,(0,0,0),1,cv.LINE_AA)
        
cv.imshow('Color Code Detector', img)
cv.setMouseCallback('Color Code Detector',color_code)
cv.waitKey(0)
cv.destroyAllWindows()