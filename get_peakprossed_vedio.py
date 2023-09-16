import cv2
import numpy as np

def   get_peak(or_image):
    


    # 读取图像为灰度图
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype(np.uint8)


    # 使用自适应阈值化来检测对比度高的区域
    # 参数：输入图像，最大像素值，自适应阈值算法（ADAPTIVE_THRESH_GAUSSIAN_C或ADAPTIVE_THRESH_MEAN_C），阈值类型，邻域大小，C常数
    adaptive_threshold = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 18)

    black_pixels = (adaptive_threshold == 0)
    pass
    # 定义膨胀核的大小
    kernel_size = 2  # 可以根据需要调整范围的大小
    kernel = np.ones((kernel_size, kernel_size), np.uint8)  
    # 使用cv2.dilate对黑色区域进行膨胀
    expanded_black_pixels = cv2.dilate(black_pixels.astype(np.uint8), kernel, iterations=1)
   
    expanded_black_pixels = (expanded_black_pixels == 1)  # 将整数0和1转换回布尔值True和False


    or_image[expanded_black_pixels] = [0, 0, 255]  # 将黑色区域替换为红色
    return or_image






cap = cv2.VideoCapture(0)
# 检查摄像头是否成功打开
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

while True:
    # 从摄像头读取一帧图像
    ret, frame = cap.read()

    # 检查是否成功读取图像
    if not ret:
        print("无法读取图像")
        break

    # 显示实时视频流
    cv2.imshow("original", frame)
    cv2.imshow("peaked", get_peak(frame))
    
    # 按下'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源
cap.release()

# 关闭所有窗口
cv2.destroyAllWindows()