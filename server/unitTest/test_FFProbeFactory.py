#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append('../')
from ffmpegwrapper.videoautoeditor import *

##########################################
def init():
    currPath = '.'
    #获取当前工作目录
    currPath = os.getcwd()
    #更改当前工作目录
    if currPath.endswith('unitTest'):
        os.chdir(os.path.join(currPath, '..'))

# init all funtion
init()
##########################################

def test_getVideoLen():
    inFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo.mp4')
    probe = FFProbeFactory(inFile)
    result = probe.getVideoLen()
    assert result == 10

def test_getVideoSize():
    inFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo.mp4')
    probe = FFProbeFactory(inFile)
    result = probe.getVideoSize()
    assert result == 16589937

def test_getVideoWidth():
    inFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo.mp4')
    probe = FFProbeFactory(inFile)
    result = probe.getVideoWidth()
    assert result == 1920

def test_getVideoHeight():
    inFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo.mp4')
    probe = FFProbeFactory(inFile)
    result = probe.getVideoHeight()
    assert result == 1080

def test_getVideoFrameRate():
    inFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo.mp4')
    probe = FFProbeFactory(inFile)
    result = probe.getVideoFrameRate()
    assert result == 30.0

def test_getVideoFrames():
    inFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo.mp4')
    probe = FFProbeFactory(inFile)
    result = probe.getVideoFrames()
    assert result == 300
