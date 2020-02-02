# coding=utf-8
from configparser import ConfigParser
from common import do_path


class ReadConfig:
    def __init__(self, filename):
        """
        :param filename: 文件名
        """
        self.cf = ConfigParser()
        self.cf.read(filename, encoding="utf-8")

    def get_int(self, section, option):
        """
        :param section: 片区
        :param option: 选项
        :return: 选项的的值
        """
        value = self.cf.getint(section, option)
        return value

    def get_float(self, section, option):
        value = self.cf.getfloat(section, option)
        return value

    def get_bool(self, section, option):
        value = self.cf.getboolean(section, option)
        return value

    def get_str(self, section, option):
        value = self.cf.get(section, option)
        return value


if __name__ == '__main__':
    rc = ReadConfig(do_path.conf_path)
    res = rc.get_str("LOGGING", "logging_formatter")
    print(res, type(res))
