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

def test_getFrameRate():
    inFile = os.path.join(os.path.abspath('.'), 'unitTest', 'data','testVideo.mp4')
    editor = VideoAutoEditor()
    result = editor.getFrameRate(inFile)
    assert(result == '30')

def test_checkVideoMute():
    inFile = os.path.join(os.path.abspath('.'), 'unitTest', 'data','testVideo.mp4')
    editor = VideoAutoEditor()
    result = editor.checkVideoMute(inFile)
    assert(result == False)

def test_getVideoLen():
    inFile = os.path.join(os.path.abspath('.'), 'unitTest', 'data','testVideo.mp4')
    editor = VideoAutoEditor()
    result = editor.getVideoLen(inFile)
    assert(result == 10)

def test_videoCut():
    inFile = os.path.join(os.path.abspath('.'), 'unitTest', 'data','testVideo.mp4')
    outFile = os.path.join(os.path.abspath('.'), 'unitTest', 'data','testVideo_x.mp4')
    handle = ['videoCut', inFile, 3, 5, outFile]
    editor = VideoAutoEditor()
    editor.videoCut(handle)
    assert os.path.exists(outFile)
    os.remove(outFile)

def test_videoCut_a():
    inFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo.mp4')
    outFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo_x_a.mp4')
    handle = ['videoCut_a', inFile, 3, 5, outFile]
    editor = VideoAutoEditor()
    editor.videoCut_a(handle)
    assert os.path.exists(outFile)
    os.remove(outFile)

def test_audioMute():
    inFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo.mp4')
    outFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo_mute.mp4')
    handle = ['audioMute', inFile, outFile]
    editor = VideoAutoEditor()
    editor.audioMute(handle)
    assert os.path.exists(outFile)
    os.remove(outFile)

def test_creatMuteAudio():
    inFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo.mp4')
    outFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo_createmute.mp4')
    handle = ['creatMuteAudio', inFile, outFile]
    editor = VideoAutoEditor()
    editor.creatMuteAudio(handle)
    assert os.path.exists(outFile)
    os.remove(outFile)
# def test_eachVideoMerge(self, listParam):
# def test_videoMerge(self, listParam):
# def test_videoOverlayVideo(self, listParam):
# def test_videoCBS(self, listParam):
# def test_videoToOneImg(self, listParam):
# def test_videoEndToOneImg(self, listParam):
# def test_oneImgToVideo(self, listParam):
# def test_PIP_videoOnImg(self, listParam):
# def test_PIP_imgOnVideo(self, listParam):
# def test_PIP_imgOnVideo_2(self, listParam):
# def test_videoLogo(self, listParam):
# def test_cameraMove(self, listParam):
# def test_cameraWalk(self, listParam):
# def test_addSubtitle(self, listParam):
# def test_videoScale(self, listParam):
# def test_videoFade(self, listParam):
# def test_videoRotate(self, listParam):
# def test_videoSpeed(self, listParam):
# def test_outputFormat(self, listParam):
# def test_addFilter(self, listParam):
# def test_addVoice(self, listParam):
# def test_showTime(self, listParam):
# def test_formatTime(self, time):
# def test_imgMoveScale(self, listParam):
# def test_mergeAudio(self, listParam):
# def test_addMusic(self, listParam):
# def test_transVideoRate(self, listParam):
# def test_addMergeMusic(self, listParam):
# def test_splitAudio(self, listParam):
# def test_addNullAudio(self, listParam):
# def test_videoToGif(self, listParam):
# def test_rmShaky(self, listParam):


def test_videoReverse():
    inFile = os.path.join(os.path.abspath('.'), 'unitTest', 'data','testVideo.mp4')
    outFile = os.path.join(os.path.abspath('.'), 'unitTest', 'data','testVideo_reverse.mp4')
    handle = ['videoReverse', inFile, outFile]
    editor = VideoAutoEditor()
    editor.videoReverse(handle)
    assert os.path.exists(outFile)
    os.remove(outFile)





