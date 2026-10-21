import cv2
#通过拉普拉斯响应方差计算清晰程度
img1=cv2.imread("expand/111.png")
img2=cv2.imread("expand/222.png")
img3=cv2.imread("expand/333.png")
img4=cv2.imread("expand/444.png")
img5=cv2.imread("expand/555.png")

gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
gray4=cv2.cvtColor(img4,cv2.COLOR_BGR2GRAY)
gray5=cv2.cvtColor(img5,cv2.COLOR_BGR2GRAY)

score1=cv2.Laplacian(gray1,cv2.CV_64F).var()
score2=cv2.Laplacian(gray2,cv2.CV_64F).var()
score3=cv2.Laplacian(gray3,cv2.CV_64F).var()
print("第一张照片的清晰程度是：",score1)
print("第二张照片的清晰程度是：",score2)
print("第三张照片的清晰程度是：",score3)

median_555=cv2.medianBlur(gray5,3)
cv2.imwrite("expand/555_median_denoising.png",median_555)
