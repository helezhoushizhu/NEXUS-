import cv2
import numpy as np

binary=cv2.imread("kobe/binary.png")

if binary is None:
    print("没找到图片")
else:
    kernel=np.ones((3,3),np.uint8)
    erosion1=cv2.erode(binary,kernel,iterations=1)
    erosion3=cv2.erode(binary,kernel,iterations=3)

    dilation1=cv2.dilate(binary,kernel,iterations=1)
    dilation3=cv2.dilate(binary,kernel,iterations=3)
    cv2.imwrite("kobe/erosion1.png",erosion1)
    cv2.imwrite("kobe/erosion3.png",erosion3)
    cv2.imwrite("kobe/dilation1.png",dilation1)
    cv2.imwrite("kobe/dilation3.png",dilation1)
    