# coding=utf-8
import logging
from common import do_path
from common import do_conf
from logging.handlers import TimedRotatingFileHandler


class Logging:
    def __init__(self, name="qingke_tv"):
        self.tv_logger = logging.getLogger(name)

    def get_log(self, level, msg):
        # 日志搜集器及等级
        self.tv_logger.setLevel(level)
        tv_formatter = logging.Formatter(do_conf.ReadConfig(do_path.conf_path).get_str("LOGGING", "logging_formatter"))


        # console渠道
        # console_handle = logging.StreamHandler()
        # console_handle.setLevel(level)
        # console_handle.setFormatter(tv_formatter)
        # self.tv_logger.addHandler(console_handle)

        # 日志文件渠道
        # file_handle = logging.FileHandler(do_path.log_path)
        file_handle = TimedRotatingFileHandler(filename=do_path.log_path, when="S", interval=1, backupCount=5)
        # file_handle.suffix = "%Y%m%d-%H%M.log"
        file_handle.setLevel(level)
        file_handle.setFormatter(tv_formatter)
        self.tv_logger.addHandler(file_handle)

        if level == "DEBUG":
            self.tv_logger.debug(msg)
        elif level == "INFO":
            self.tv_logger.info(msg)
        elif level == "WARNING":
            self.tv_logger.warning(msg)
        elif level == "ERROR":
            self.tv_logger.error(msg)
        elif level == "CRITICAL":
            self.tv_logger.critical(msg)

        self.tv_logger.removeHandler(file_handle)
        # self.tv_logger.removeHandler(console_handle)

    def debug(self, msg):
        self.get_log("DEBUG", msg)

    def info(self, msg):
        self.get_log("INFO", msg)

    def warning(self, msg):
        self.get_log("WARNING", msg)

    def error(self, msg):
        self.get_log("ERROR", msg)

    def critical(self, msg):
        self.get_log("CRITICAL", msg)


if __name__ == '__main__':
    ml = Logging()
    ml.info("info")











