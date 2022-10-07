import warnings
import cv2
import numpy as np

"""
视频另存工具
"""
class VideoWriterUtil:
    '''
        @description: 写视频的工具类，两个方法，写入和关闭文件
    '''
    def __init__(self, name, width, height, fps=25):
        # type: (str, int, int, int) -> None
        if not name.endswith('.mp4'):  # 保证文件名的后缀是.mp4
            name += '.mp4'
            warnings.warn('video name should ends with ".avi"')
        self.__name = name          # 文件名
        self.__height = height      # 高
        self.__width = width        # 宽
        # fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # 如果是avi视频，编码需要为MJPG

        self.__writer = cv2.VideoWriter(name, fourcc, fps, (int(width), int(height)))

    def write(self, frame):
        if frame.dtype != np.uint8:  # 检查frame的类型
            raise ValueError('frame.dtype should be np.uint8')
        # 检查frame的大小
        row, col, _ = frame.shape
        if row != self.__height or col != self.__width:
            warnings.warn('长和宽不等于创建视频写入时的设置，此frame不会被写入视频')
            return
        self.__writer.write(frame)

    def close(self):
        self.__writer.release()


def create_videoWriter(capture, new_name: str) -> VideoWriterUtil:
    """
        构建视频写入工具，如果 capture 未打开，那么返回 None
        @capture:   cv2.VideoCapture 返回值
        @new_name:  新视频的文件名
        @return:    VideoWriterUtil
    """
    if capture.isOpened():                                  # VideoCaputre对象是否成功打开
        fps = capture.get(cv2.CAP_PROP_FPS)                 # 返回视频的fps--帧率
        width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)       # 返回视频的宽
        height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)     # 返回视频的高
        print('>>> 原始视频信息：', 'fps:', fps,'width:', width,'height:', height)

        return VideoWriterUtil(new_name, width, height, fps), width, height
    
    return None



if __name__=="__main__":
    """
        测试使用方法
    """
    cam=cv2.VideoCapture(0)

    if cam.isOpened():                                  # VideoCaputre对象是否成功打开
        fps = cam.get(cv2.CAP_PROP_FPS)                 # 返回视频的fps--帧率
        width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)       # 返回视频的宽
        height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)     # 返回视频的高
        print('fps:', fps,'width:',width,'height:',height)

        vw = VideoWriterUtil('./camare.mp4', width, height, fps)

        while(True):
            # 读取一帧视频
            readStatus, frame = cam.read()  
            frame_count = 0

            if(not readStatus):     # 视频读取完毕
                print('视频已处理完成')
                if vw != None:
                    vw.close()
                break
            else:                   # 视频还未处理完
                vw.write(frame)         
                frame_count += 1