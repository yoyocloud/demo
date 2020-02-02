# coding=utf-8
import os
import time
# 当前路径
abs_path = os.path.realpath(__file__)
# 项目路径
tv_path = os.path.split(os.path.split(abs_path)[0])[0]
# 配置文件
conf_path = os.path.join(tv_path, "test_data", "config.conf")
# 日志
log_path = os.path.join(tv_path, "test_result", "logs", "log")




