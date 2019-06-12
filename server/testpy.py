# -*- coding: utf-8 -*-

import os

def test():
    str = "E:/work/创业之路/音视频技术/并行计算/自动化剪辑/server/bin/ffmpeg.exe -i out.mp4 11.mp4"
    ret = os.system(str)
    print(ret)
    return ret

def formatTime(time):
    # 00:00 -> 00\:00\:00\:00
    time = time.replace(':', '\:')
    time = '00\:'+time+'\:00'
    return time

if __name__ == '__main__':
    # test()
    print(formatTime('00:04'))