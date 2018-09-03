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

def test_outputSarDar():
    inFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo.mp4')
    outFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo_sar_dar.mp4')
    ffmpeg = FFMpegFactory(inFile, outFile)
    ffmpeg.outputSarDar()
    result = ffmpeg.run()
    assert os.path.exists(outFile)
    os.remove(outFile)

def test_outputFormat():
    inFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo.mp4')
    outFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo_format.mp4')
    ffmpeg = FFMpegFactory(inFile, outFile)
    ffmpeg.outputFormat()
    result = ffmpeg.run()
    assert os.path.exists(outFile)
    os.remove(outFile)

def test_mp4Format_2():
    inFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo.mp4')
    outFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo_mp4_2.mp4')
    ffmpeg = FFMpegFactory(inFile, outFile)
    ffmpeg.mp4Format_2("30")
    result = ffmpeg.run()
    assert os.path.exists(outFile)
    os.remove(outFile)

def test_mp4Format():
    inFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo.mp4')
    outFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo_mp4.mp4')
    ffmpeg = FFMpegFactory(inFile, outFile)
    ffmpeg.mp4Format()
    result = ffmpeg.run()
    assert os.path.exists(outFile)
    os.remove(outFile)

def test_videFormat():
    inFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo.mp4')
    outFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo_format.mp4')
    ffmpeg = FFMpegFactory(inFile, outFile)
    ffmpeg.videFormat()
    result = ffmpeg.run()
    assert os.path.exists(outFile)
    os.remove(outFile)

def test_videoCut():
    inFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo.mp4')
    outFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo_cut.mp4')
    ffmpeg = FFMpegFactory(inFile, outFile)
    ffmpeg.videoCut(1, 3)
    result = ffmpeg.run()
    assert os.path.exists(outFile)
    os.remove(outFile)

def test_videoCut_2():
    inFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo.mp4')
    outFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo_cut_2.mp4')
    ffmpeg = FFMpegFactory(inFile, outFile)
    ffmpeg.videoCut_2(1, 3)
    result = ffmpeg.run()
    assert os.path.exists(outFile)
    os.remove(outFile)

def test_addFilter():
    inFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo.mp4')
    outFile = os.path.join(os.path.abspath('.'),
        'unitTest',
        'data',
        'testVideo_cut_2.mp4')
    ffmpeg = FFMpegFactory(inFile, outFile)
    ffmpeg.addFilter('trim=1:3')
    result = ffmpeg.run()
    assert os.path.exists(outFile)
    os.remove(outFile)

# def test_showTime(self, frameRate, time ,startTime, endTime, posX=351, posY=117, fontSize=35, fontcolor='#FFFFFF'):
# def test_videoMerge(self):
# def test_twoVideoMerge(self, videoLen, videFile, overlayDuring):
# def test_videoScale(self, x, y, width, height):
# def test_videoRotate(self, angle):
# def test_videoReverse(self):
# def test_videoCBS(self, contrast=1, brightness=0, saturation=1):
# def test_videoLogo(self, imgFile):
# def test_videoToOneImg(self, time):
# def test_videoEndToOneImg(self, time):
# def test_oneImgToVideo(self, time):
# def test_videoOverlayVideo(self, file):
# def test_PIP_videoOnImg(self, videoFile):
# def test_PIP_imgOnVideo(self, imgFile, start, end):
# def test_PIP_imgOnVideo_2(self, imgFile, start, end):
# def test_videoFadeIn(self, during):
# def test_videoFadeOut(self, start):
# def test_videoSpeed(self, videoStart, videoEnd, slowStart, slowEnd, speed):
# def test_imgMoveScale(self, during):
# def test_videoMoveScale(self, w1, w2, frame, frameRate):
# def test_videoMoveScale_yb(self, x1, y1, w1, h1, x2, y2, w2, h2, frame, frameRate):
# def test_cameraMove(self, x, y, frameRate):
# def test_cameraWalk(self, srcX, srcY, dstX, dstY, width, height, frames):
# def test_vidstabdetect(self):
# def test_vidstabtransform(self):
# def test_palettegen(self):
# def test_paletteuse(self, file):
# def test_addMergeMusic(self, music):
# def test_splitAudio(self):
# def test_mergeAudio(self, file):
# def test_addMusic(self, music):
# def test_addNullAudio(self, nullFile):
# def test_creatMuteAudio(self, during):
# def test_audioMute(self):
# def test_audioMix(self, audioFile):
# def test_transVideoRate(self, rate):
# def test_addSubtitle(self, txtFile):
