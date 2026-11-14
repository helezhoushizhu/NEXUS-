import glob
import cv2
import numpy as np
folder="/home/lyp/NEXUS/week4/course_data/01_素材A/碎片"
files=glob.glob(folder+"/*.png")
print("文件数量为：",len(files))
print("第一张图片的路径是：",files[0])

image=cv2.imread(files[0])
if image is None:
    print("图片路径不对")
else:
    print("图片读取成功！")
    print("图片形状为：",image.shape)
    left_half=image[:,0:32]
    right_half=image[:,32:64]
    print("左半边的形状：", left_half.shape)
    print("右半边的形状：", right_half.shape)
    print("左半边和右半边一样吗？", np.array_equal(left_half, right_half))

    image2 = cv2.imread(files[1])

    if image2 is None:
        print("第二张图片读取失败")
    else:
        right1 = image[:, 32:64]
        left2 = image2[:, 0:32]

        same = np.array_equal(right1, left2)

        print("第一张右半边和第二张左半边相同吗？", same)
        rotated=cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)
        print("原图形状：", image.shape)
        print("旋转后形状：", rotated.shape)
        print("左转一下右转一下是不是一样的：",np.array_equal(image,cv2.rotate(rotated,cv2.ROTATE_90_COUNTERCLOCKWISE)))
        for i in range(4):
            right1 = image[:, 32:64]
            left2 = image2[:, 0:32]

            same = np.array_equal(right1, left2)
            print("第二张旋转", i * 90, "度，匹配结果：", same)

            image2 = cv2.rotate(image2, cv2.ROTATE_90_CLOCKWISE)