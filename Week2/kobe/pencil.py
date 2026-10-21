import cv2
img=cv2.imread("kobe/kobe.png")

if img is None:
    print("没找到图片")
else:
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray1=cv2.GaussianBlur(gray,(5,5),0)
    edges=cv2.Canny(gray1,100,200)
    pencil=cv2.bitwise_not(edges)
    cv2.imwrite("kobe/pencil.png",pencil)