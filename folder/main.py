import cv2

# 1: connect camera via USB , 0: connect camera installed in your computer
cap = cv2.VideoCapture("yedi2.avi")

count = 0
name = 0
while (cap.isOpened()):
    # ret返回布尔值
    ret, frame = cap.read()
    count = count + 1
    print("ret", ret)
    if count % 30 == 0:
        name = name + 1
        cv2.imwrite("data/"+str(name)+".jpg", frame)
    # 展示读取到的视频矩阵
    cv2.imshow('image', frame)
    cv2.waitKey(1)
    # # q键退出
    # if cv2.waitKey(10) & 0xFF == ord('q'):
    #     break
# 释放资源
cap.release()
# 关闭窗口
cv2.destroyAllWindows()