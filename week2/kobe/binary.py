#二值化
import cv2
img=cv2.imread("kobe/kobe.png")

if img is None:
    print("无照片")
else:
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    cv2.imwrite("kobe/binary.png",binary)
    print("实际使用的阈值是:",ret)