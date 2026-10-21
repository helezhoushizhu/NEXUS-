import cv2
img=cv2.imread("666.png")
if img is None:
    print("没找到图片")
else:
    mean=cv2.blur(img,(9,9))
    cv2.imwrite("mean.png",mean)
    print("完成均值")
    box=cv2.boxFilter(img,-1,(9,9),normalize=True)
    cv2.imwrite("box.png",box)
    diff=cv2.absdiff(mean,box)
    print("biggest difference:",diff.max())
    gaussian=cv2.GaussianBlur(img,(9,9),0)
    cv2.imwrite("gaussian.png",gaussian)
    median=cv2.medianBlur(img,5)
    cv2.imwrite("median.png",median)