# -*- coding: UTF-8 -*-
"""
@Author ：WangJie
@Date   ：2020/12/23 13:07 
@Desc   ：
"""
import random
import ctypes
import time
import os

if __name__ == '__main__':
    path = "E:\PythonDemo\自动更换壁纸\壁纸"
    while True:
        file = os.listdir(path)  # 打开存储图片文件夹中的图片目录
        filepath = os.path.join(path, random.choice(file))  # 随机选取某张图片，建立绝对地址
        print(filepath)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)  # 设置桌面壁纸
        time.sleep(30 * 60);  # 睡眠半个小时