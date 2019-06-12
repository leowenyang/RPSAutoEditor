#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import json
import subprocess
import random

from ffmpegwrapper.videoautoeditor import *
from ffmpegwrapper.timerCounter import *


def specialEffect():
    # editor = VideoAutoEditor()
    # during = editor.creatMuteAudio("clip.mp4")
    # print(during)

    # probe = FFProbeFactory("E:\\work\\创业之路\\音视频技术\\并行计算\\自动化剪辑\\server\\clip.mp4")
    # len = probe.getVideoFrameRate()
    # print(1)
    # print(len)
    # print(2)

    handle = ['videoReverse', 'E:\\work\\创业之路\\音视频技术\\并行计算\\自动化剪辑\\server\\clip.mp4', 'E:\\work\\创业之路\\音视频技术\\并行计算\\自动化剪辑\\server\\clip_reverse.mp4']
    editor = VideoAutoEditor()
    editor.videoReverse(handle)

def musicHoldOn(picList, music):
    """ According to Music < Hold On (Radio Edit) by Moguai / Cheat Codes >
    to generate video, this song has the follow feature:
    - 2s to start
    - 0.5s to change tempo

    so, we need to the follow element
    - 22 pictures
    - 2s video to start
    - other video is the same 0.5s
    -
    """

    if len(picList) != 22:
        return
    # 1. generate 2s video

    # 2. generate 0.5s video (21)
    # ffmpeg.exe -f lavfi -i color=black:s=1920x1080 -loop 1 -i .\2.jpg -filter_complex "[1:v]scale=-1:1080[pic];[0:v][pic] overlay=x=(W-w)/2:y=(H-h)/2[out]" -t 0.5 -y 2.mp4
    # 3. merge all video
    # ffmpeg.exe -f concat -safe 0 -i .\file.txt -c copy -y output.mp4
    # 4. add music
    # ffmpeg.exe -i .\output.mp4 -i .\holdon.mp3 -c copy -map 0:v -map 1:a -y shark.mp4




if __name__ == '__main__':
    specialEffect()

