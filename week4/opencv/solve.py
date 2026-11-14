import glob
from collections import defaultdict, deque

import cv2
import numpy as np


# 1. 选择素材并读取图片
choice = input("请输入素材名称 A、B 或 C：").strip().upper()

folders = {
    "A": "01_素材A",
    "B": "02_素材B",
    "C": "03_素材C"
}

if choice not in folders:
    raise SystemExit("输入错误，请输入 A、B 或 C")

folder = "/home/lyp/NEXUS/week4/course_data/" + folders[choice] + "/碎片"
files = sorted(glob.glob(folder + "/*.png"))

if not files:
    raise SystemExit("没有找到图片，请检查文件夹路径")

images = []

for file in files:
    image = cv2.imread(file)

    if image is None or image.shape != (64, 64, 3):
        raise SystemExit("图片读取失败或尺寸不对：" + file)

    images.append(image)

print("读取的图片数量：", len(images))


# 2. 为每张图片准备四个方向
rotations = []

for image in images:
    directions = [image]

    for _ in range(3):
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        directions.append(image)

    rotations.append(directions)


# 3. 建立索引：记录每张图片的左、右、上、下边缘
# 边缘宽度取 32 像素，之后用它快速找到可能匹配的碎片
edges = [defaultdict(list) for _ in range(4)]

for index, directions in enumerate(rotations):
    for turn, image in enumerate(directions):
        parts = [
            image[:, :32],    # 左半边
            image[:, 32:],    # 右半边
            image[:32, :],    # 上半边
            image[32:, :]     # 下半边
        ]

        for side in range(4):
            key = parts[side].tobytes()
            edges[side][key].append((index, turn))


# 4. 检查两张图片重叠的所有像素
def overlap_same(image1, image2, dx, dy):
    # image2 相对于 image1 移动了 dx、dy
    x1 = max(0, dx)
    x2 = min(64, dx + 64)
    y1 = max(0, dy)
    y2 = min(64, dy + 64)

    if x1 >= x2 or y1 >= y2:
        return False

    part1 = image1[y1:y2, x1:x2]
    part2 = image2[y1-dy:y2-dy, x1-dx:x2-dx]

    return np.array_equal(part1, part2)


# 5. 从第 0 张碎片开始，向四周寻找邻居
# placed 的格式：碎片编号 → (x 坐标, y 坐标, 旋转次数)
placed = {0: (0, 0, 0)}
occupied = {(0, 0)}
queue = deque([0])

while queue:
    current = queue.popleft()
    x, y, turn = placed[current]
    image = rotations[current][turn]

    # 通常移动 32 像素；也尝试较小移动，处理边缘重叠
    for shift in range(32, 0, -1):

        # 依次检查右、左、下、上四个方向
        checks = [
            (image[:, shift:shift+32], 0, shift, 0),
            (image[:, 32-shift:64-shift], 1, -shift, 0),
            (image[shift:shift+32, :], 2, 0, shift),
            (image[32-shift:64-shift, :], 3, 0, -shift)
        ]

        for part, side, dx, dy in checks:
            position = (x + dx, y + dy)

            if position in occupied:
                continue

            # 找出边缘一致的候选碎片
            candidates = edges[side].get(part.tobytes(), [])
            valid = []

            for index, next_turn in candidates:
                if index in placed:
                    continue

                candidate = rotations[index][next_turn]

                if not overlap_same(image, candidate, dx, dy):
                    continue

                # 检查它是否与其他已放置的碎片发生冲突
                conflict = False

                for other, (ox, oy, other_turn) in placed.items():
                    relative_x = position[0] - ox
                    relative_y = position[1] - oy

                    if abs(relative_x) < 64 and abs(relative_y) < 64:
                        other_image = rotations[other][other_turn]

                        if not overlap_same(
                            other_image, candidate, relative_x, relative_y
                        ):
                            conflict = True
                            break

                if not conflict:
                    valid.append((index, next_turn))

            # 只有一个候选时才放入，避免随便选择
            if len(valid) == 1:
                index, next_turn = valid[0]

                placed[index] = (position[0], position[1], next_turn)
                occupied.add(position)
                queue.append(index)

    print(f"\r已放置：{len(placed)} / {len(images)}", end="", flush=True)

print()


# 6. 根据碎片坐标创建画布
min_x = min(x for x, y, turn in placed.values())
min_y = min(y for x, y, turn in placed.values())
max_x = max(x + 64 for x, y, turn in placed.values())
max_y = max(y + 64 for x, y, turn in placed.values())

width = max_x - min_x
height = max_y - min_y

result = np.zeros((height, width, 3), dtype=np.uint8)
covered = np.zeros((height, width), dtype=bool)

for index, (x, y, turn) in placed.items():
    x = x - min_x
    y = y - min_y

    result[y:y+64, x:x+64] = rotations[index][turn]
    covered[y:y+64, x:x+64] = True


# 7. 保存图片并输出检查结果
output = f"/home/lyp/NEXUS/week4/opencv/result_{choice}.png"

if cv2.imwrite(output, result):
    print("结果已保存到：", output)
else:
    print("保存失败，请检查输出路径")

print("结果尺寸：", width, "×", height)
print("已放置碎片：", len(placed), "/", len(images))
print("未放置碎片：", len(images) - len(placed))
print("未覆盖的像素数：", np.count_nonzero(~covered))

if len(placed) < len(images) or not np.all(covered):
    print("结果可能不完整，需要继续检查。")
else:
    print("所有碎片已放置，请打开结果图检查画面。")