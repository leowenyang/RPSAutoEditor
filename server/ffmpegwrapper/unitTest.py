#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json
import shutil

from .videoautoeditor import *

def test_videoReverse():
    handle = ['videoReverse', 'E:\\work\\创业之路\\音视频技术\\并行计算\\自动化剪辑\\server\\clip.mp4', 'E:\\work\\创业之路\\音视频技术\\并行计算\\自动化剪辑\\server\\clip_reverse.mp4']
    editor = VideoAutoEditor()
    editor.videoReverse(handle)
