# -----------------------------------------------------------------------#
#   predict.py将单张图片预测、摄像头检测、FPS测试和目录遍历检测等功能
#   整合到了一个py文件中，通过指定mode进行模式的修改。
# -----------------------------------------------------------------------#
import time

import cv2
import numpy as np
from PIL import Image

from yolo_cell import YOLO_CELL
from yolo_small import YOLO_SMALL


if __name__ == "__main__":
    # 实例化细胞检测网络
    yolo_c = YOLO_CELL()
    # 实例化单细胞检测网络
    yolo_s = YOLO_SMALL()
    # 读取视频
    # capture = cv2.VideoCapture('4000lu1cun1000zhen.avi')
    # video = cv2.VideoCapture('4000lu1cun1000zhen.avi')
    capture = cv2.VideoCapture('1000lu50cunPFPE-TEIS.avi')
    video = cv2.VideoCapture('1000lu50cunPFPE-TEIS.avi')
    #crop  检测单细胞的窗口
    cv2.namedWindow("crop", 0)
    # ori_crop 扣细胞的窗口
    cv2.namedWindow("ori_crop", 0)
    while (True):
        t1 = time.time()

        frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

        print(frame_count)
        # 读取某一帧 frame是读取的图片
        ref, frame = capture.read()
        # 原始图像
        frame_ori = frame.copy()
        # 展示图像
        show_frame = frame.copy()
        ###  检测细胞网络
        # 格式转变，BGRtoRGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # 转变成Image
        frame = Image.fromarray(np.uint8(frame))
        # 进行检测， box就是检测出来的细胞坐标
        frame, save_frame, box = yolo_c.detect_image(frame)

        if len(box) > 0:
            for i in range(len(box)):
                #x1, y1 表示细胞的左上角坐标，x2,y2 表示的是右下角坐标
                x1, y1, x2, y2 = box[i]
                # 抠图，从原始图像中把细胞图像扣出来
                crop_image = frame_ori[x1:x2, y1:y2]
                #  cv2.rectangle(show_frame, (y1, x1), (y2, x2), (0, 0, 255), 1)
                show_crop_image = crop_image.copy()
                ori_crop_image = crop_image.copy()
                crop_image = cv2.cvtColor(crop_image, cv2.COLOR_BGR2RGB)
                crop_image = Image.fromarray(np.uint8(crop_image))
                # 进行检测， box_small 是单细胞坐标
                crop_image, _, box_small = yolo_s.detect_image(crop_image)
                for bs in box_small:
                    # x1_s, y1_s 表示细胞的左上角坐标，x2_s,y2_s 表示的是右下角坐标
                    x1_s, y1_s, x2_s, y2_s = bs
                    cv2.rectangle(show_crop_image, (y1_s, x1_s), (y2_s, x2_s), (0, 0, 255), 1)
                if len(box_small) == 1:
                    cv2.rectangle(show_frame, (y1, x1), (y2, x2), (0, 0, 255), 1)
                cv2.imshow("ori_crop", ori_crop_image)
                # cv2.imshow("crop", show_crop_image)
                cv2.imwrite("crop/%s.png" % i, show_crop_image)
                cv2.imshow("frame_ori", show_frame)
                cv2.waitKey(1)
                # if len(box_small) == 1:
                #     time.sleep(1)


