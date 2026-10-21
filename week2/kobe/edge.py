import cv2
img=cv2.imread("kobe/kobe.png")

if img is None:
    print("没找到图片")
else:
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    sober_x=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
    sober_y=cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)
    sober_x=cv2.convertScaleAbs(sober_x)
    sober_y=cv2.convertScaleAbs(sober_y)
    cv2.imwrite("kobe/sober_x.png",sober_x)
    cv2.imwrite("kobe/sober_y.png",sober_y)
    gray1=cv2.GaussianBlur(gray,(5,5),0)#不用这个全是乱码，这图噪声太多了
    canny1=cv2.Canny(gray1,50,100)
    cv2.imwrite("kobe/canny1.png",canny1)
    canny2=cv2.Canny(gray1,100,200)
    cv2.imwrite("kobe/canny2.png",canny2)
    canny3=cv2.Canny(gray1,150,250)
    cv2.imwrite("kobe/canny3.png",canny3)

    
