import cv2
import numpy as np

def emptyFunction():
    pass

cam = cv2.VideoCapture(0)

windowsname = "TestTestTest"
cv2.namedWindow(windowsname)
cv2.createTrackbar("h", windowsname,0,179,emptyFunction)
cv2.createTrackbar("s", windowsname,0,255,emptyFunction)
cv2.createTrackbar("v", windowsname,0,255,emptyFunction)
cv2.createTrackbar("H", windowsname,0,179,emptyFunction)
cv2.createTrackbar("S", windowsname,0,255,emptyFunction)
cv2.createTrackbar("V", windowsname,0,255,emptyFunction)

while(1):
    _,frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h = cv2.getTrackbarPos("h", windowsname)
    s = cv2.getTrackbarPos("s", windowsname)
    v = cv2.getTrackbarPos("v", windowsname)
    H = cv2.getTrackbarPos("H", windowsname)
    S = cv2.getTrackbarPos("S", windowsname)
    V = cv2.getTrackbarPos("V", windowsname)
    
    lower_red = np.array([h,s,v], dtype = np.uint8)
    upper_red = np.array([H,S,V], dtype = np.uint8)

    lower_green = np.array([40,44,0], dtype = np.uint8)
    upper_green = np.array([69,255,255], dtype = np.uint8)
    
    lower_cyan = np.array([81,71,100], dtype = np.uint8)
    upper_cyan = np.array([112,255,255], dtype = np.uint8)

    lower_blue = np.array([81,0,100], dtype = np.uint8)
    upper_blue = np.array([132,255,255], dtype = np.uint8)
    
    
    
    red = cv2.inRange(hsv, lower_red, upper_red)
    green = cv2.inRange(hsv, lower_green, upper_green)
    blue = cv2.inRange(hsv, lower_blue, upper_blue)
    cyan = cv2.inRange(hsv, lower_cyan, upper_cyan)
    
    
    mask = cv2.bitwise_or(red,green)
    mask1 = cv2.bitwise_or(blue,mask)
    fmask = cv2.bitwise_or(mask,mask1)
    median = cv2.medianBlur(red, 31)
    
    cv2.imshow("HELLA", median)
    
    if cv2.waitKey(5)==27:
        break
    
cv2.destroyAllWindows()
cam.release()