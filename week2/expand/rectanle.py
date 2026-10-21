
import cv2
img = cv2.imread("expand/444.png")

if img is None:
    print("图片读取失败")
else:
    x, y, w, h = cv2.selectROI("Select Person", img, False, False)

    if w > 0 and h > 0:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imwrite("expand/person_box.png", img)
        print("矩形框已保存！")
        person = img[y:y+h, x:x+w]
        cv2.imwrite("expand/person_crop.png", person)
    cv2.destroyAllWindows()
