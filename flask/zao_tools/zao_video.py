import cv2
import subprocess


# RTMP 推送函数
def push_rtmp_stream(rtmp_url):
    # 打开视频文件（或者摄像头）
    cap = cv2.VideoCapture(0)

    # 获取视频的基本信息
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # 创建 FFmpeg 进程来推送 RTMP 流
    command = [
        r'C:\ProgramData\chocolatey\bin\ffmpeg',
        '-y',  # 自动覆盖输出文件
        '-f', 'rawvideo',  # 输入格式为原始视频流
        '-vcodec', 'rawvideo',  # 输入视频编码为原始数据
        '-pix_fmt', 'bgr24',  # 输入视频的像素格式（OpenCV 默认）
        '-s', f'{frame_width}x{frame_height}',  # 设置视频尺寸
        '-r', str(fps),  # 设置帧率
        '-i', '-',  # 从标准输入读取视频流
        '-c:v', 'libx264',  # 使用 x264 编码
        '-preset', 'fast',  # 编码预设
        '-f', 'flv',  # 输出为 FLV 格式
        rtmp_url  # RTMP 推送的目标地址
    ]

    # 启动 FFmpeg 子进程
    ffmpeg_process = subprocess.Popen(command, stdin=subprocess.PIPE)

    while cap.isOpened():
        ret, frame = cap.read()  # 读取视频帧

        if not ret:
            break  # 如果视频读取失败，结束循环

        # 对每一帧进行处理（例如转为灰度图像）
        processed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 将每帧转为灰度图像
        processed_frame = cv2.cvtColor(processed_frame, cv2.COLOR_GRAY2BGR)  # 转回到BGR格式
        print(processed_frame.shape)
        # 将处理后的帧发送到 FFmpeg
        ffmpeg_process.stdin.write(processed_frame.tobytes())

    # 释放资源
    cap.release()
    ffmpeg_process.stdin.close()
    ffmpeg_process.wait()
