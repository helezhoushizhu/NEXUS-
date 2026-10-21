import cv2
img=cv2.imread("666.png")

if img is None:
    print("Error: Could not load image")
else:
    print(type(img))
    print(img.shape)
pixel=img[200,200]
"""print(pixel)
print("blue",pixel[0])
print("green",pixel[1])
print("red",pixel[2])
crop=img[100:200,100:200]
cv2.imwrite("crop.png",crop)
print("crop shape",crop.shape)
"""
b,g,r=cv2.split(img)
cv2.imwrite("blue.png",b)
cv2.imwrite("green.png",g)
cv2.imwrite("red.png",r)
merge=cv2.merge((b,g,r))
cv2.imwrite("merge.png",merge)
h,w=img.shape[:2]
img2=cv2.resize(img,(w//2,h//2))
cv2.imwrite("img2.png",img2)
print(img2.shape)
"""img3=cv2.addWeighted(b,0.3,img,0.7,0)
cv.imwrite("img3.png",img3)
这种写法不匹配，一个单通道，一个三通道
"""
gray_bgr = cv2.cvtColor(b, cv2.COLOR_GRAY2BGR)
blend = cv2.addWeighted(img, 0.1, gray_bgr, 0.9, 0)
cv2.imwrite("blend.jpg", blend)
print("图像融合完成！")