import logging
import os
import time

log_time = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))

class Logger:
    def __init__(self, logs_root_path='./logs', module_name="audio", level=logging.INFO, type_file=True, type_terminal=True):
        '''
        Args:
            logs_root_path: 日志存放的根目录，一般在项目目录的根位置
            module_name:    日志的输出模块，比如在处理音频的模块中输出的信息，应该带有此信息，分开目录存放

        Usage:
            >>> logger = Logger()

                logger.info('sdsadsadsds')
                logger.info('thyjyj fgfdgfdg')
                logger.error('thyjyj fgfdgfdg')
                logger.warn('thyjyj fgfdgfdg')
                logger.exception('thyjyj fgfdgfdg')
        '''
        super().__init__()
        self.logs_root_path = logs_root_path
        self.module_name = module_name
        # 设置日志文件的存放位置
        joined_path = os.path.join(self.logs_root_path, module_name)
        Logger.mkdir(joined_path)
        self.log_file = os.path.join(joined_path, '{}.log'.format(log_time))
        
        # 初始化日志记录器
        self.logger = logging.getLogger(module_name)
        # 设置日志等级
        self.level = level
        self.logger.setLevel(self.level)

        if not self.logger.handlers:
            # 同时设置文件输出和终端输出
            fh = logging.FileHandler(self.log_file, encoding='utf-8')
            fh.setLevel(self.level)

            ch = logging.StreamHandler()
            ch.setLevel(self.level)
            # 设置格式
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            ch.setFormatter(formatter)
            fh.setFormatter(formatter)
            if type_file:
                self.logger.addHandler(fh)
            if type_terminal:
                self.logger.addHandler(ch)


    def error(self, msg, *args, **kwargs):
        if self.logger is not None:
            self.logger.error(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        if self.logger is not None:
            self.logger.info(msg, *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        if self.logger is not None:
            self.logger.warning(msg, *args, **kwargs)

    def exception(self, msg, *args, exc_info=True, **kwargs):
        if self.logger is not None:
            self.logger.exception(msg, *args, exc_info=True, **kwargs)


    @staticmethod
    def mkdir(path):
        path.strip()
        path.rstrip('\\')
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)

if __name__=='__main__':
    logger = Logger()

    logger.info('sdsadsadsds')
    logger.info('thyjyj fgfdgfdg')
    logger.error('thyjyj fgfdgfdg')
    logger.warn('thyjyj fgfdgfdg')
    logger.exception('thyjyj fgfdgfdg')
