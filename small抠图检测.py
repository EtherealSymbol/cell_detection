# -----------------------------------------------------------------------#
#   predict.py将单张图片预测、摄像头检测、FPS测试和目录遍历检测等功能
#   整合到了一个py文件中，通过指定mode进行模式的修改。
# -----------------------------------------------------------------------#
import time

import cv2
import numpy as np
from PIL import Image
import os
from yolo_cell import YOLO_CELL

if __name__ == "__main__":
    yolo = YOLO_CELL()
    filename = os.listdir("data/")
    count = 0
    cv2.namedWindow("ff", 0)
    for i in filename:
        print(i)
        path = "data/" + i

        frame = cv2.imread(path)
        frame_ori = frame.copy()
        frame_show = frame.copy()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # 转变成Image
        frame = Image.fromarray(np.uint8(frame))
        # 进行检测
        frame, save_frame, box = yolo.detect_image(frame)
        if len(box) > 0:
            for i in range(len(box)):
                count = count + 1

                x1, y1, x2, y2 = box[i]
                small_cell = frame_ori[x1:x2, y1:y2, :]
                print("small", small_cell.shape)
                cv2.rectangle(frame_ori, (y1, x1), (y2, x2), (0, 0, 255), 2)
                cv2.imwrite("crop_img/" + str(count) + '.jpg', small_cell)
                cv2.imshow("ff", frame_ori)
                cv2.imshow("small_cell", small_cell)

                cv2.waitKey(0)
        # cv2.imshow("ff", frame_ori)
        # cv2.imshow("shsshs", frame_show)
    # cv2.waitKey(0)

