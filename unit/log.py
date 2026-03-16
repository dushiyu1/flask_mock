import logging
import os

class Logger:
    @classmethod

    def info(self,msg):
        # ========== 关键：正确配置日志（确保输出到控制台） ==========
        # 1. 获取根日志器
        log_dir = './log'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)  # 设置全局日志级别为INFO

        # 2. 清除默认处理器（避免Flask默认配置覆盖）
        logger.handlers.clear()

        # 3. 添加控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)  # 控制台日志级别

        # 4. 设置日志格式
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(formatter)

        # 5. 将处理器添加到日志器
        logger.addHandler(console_handler)
        file_handler = logging.FileHandler(f"{log_dir}/flask_mock.log", encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        logger.info(msg)

