#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import json
import subprocess
import random

from ffmpegwrapper.videoautoeditor import *
from ffmpegwrapper.timerCounter import *


def specialEffect():
    openEye()
    # musicHoldOn(['E:/work/视频测试/儿子毕业了/1.jpg',
    #     'E:/work/视频测试/儿子毕业了/2.jpg',
    #     'E:/work/视频测试/儿子毕业了/3.jpg',
    #     'E:/work/视频测试/儿子毕业了/4.jpg',
    #     'E:/work/视频测试/儿子毕业了/5.jpg',
    #     'E:/work/视频测试/儿子毕业了/6.jpg',
    #     'E:/work/视频测试/儿子毕业了/7.jpg',
    #     'E:/work/视频测试/儿子毕业了/8.jpg',
    #     'E:/work/视频测试/儿子毕业了/9.jpg',
    #     'E:/work/视频测试/儿子毕业了/10.jpg',
    #     'E:/work/视频测试/儿子毕业了/11.jpg',
    #     'E:/work/视频测试/儿子毕业了/12.jpg',
    #     'E:/work/视频测试/儿子毕业了/13.jpg',
    #     'E:/work/视频测试/儿子毕业了/14.jpg',
    #     'E:/work/视频测试/儿子毕业了/15.jpg',
    #     'E:/work/视频测试/儿子毕业了/16.jpg',
    #     'E:/work/视频测试/儿子毕业了/17.jpg',
    #     'E:/work/视频测试/儿子毕业了/18.jpg',
    #     'E:/work/视频测试/儿子毕业了/19.jpg',
    #     'E:/work/视频测试/儿子毕业了/20.jpg',
    #     'E:/work/视频测试/儿子毕业了/21.jpg',
    #     'E:/work/视频测试/儿子毕业了/22.jpg'],
    #     'E:/work/视频测试/儿子毕业了/holdon.mp3')

    # cardVideo(['E:/work/视频测试/儿子毕业了/1.jpg',
    #     'E:/work/视频测试/儿子毕业了/2.jpg',
    #     'E:/work/视频测试/儿子毕业了/3.jpg',
    #     'E:/work/视频测试/儿子毕业了/4.jpg',
    #     'E:/work/视频测试/儿子毕业了/5.jpg',
    #     'E:/work/视频测试/儿子毕业了/6.jpg',
    #     'E:/work/视频测试/儿子毕业了/7.jpg',
    #     'E:/work/视频测试/儿子毕业了/8.jpg',
    #     'E:/work/视频测试/儿子毕业了/9.jpg',
    #     'E:/work/视频测试/儿子毕业了/10.jpg',
    #     'E:/work/视频测试/儿子毕业了/11.jpg',
    #     'E:/work/视频测试/儿子毕业了/12.jpg',
    #     'E:/work/视频测试/儿子毕业了/13.jpg',
    #     'E:/work/视频测试/儿子毕业了/14.jpg',
    #     'E:/work/视频测试/儿子毕业了/15.jpg',
    #     'E:/work/视频测试/儿子毕业了/16.jpg',
    #     'E:/work/视频测试/儿子毕业了/17.jpg',
    #     'E:/work/视频测试/儿子毕业了/18.jpg',
    #     'E:/work/视频测试/儿子毕业了/19.jpg',
    #     'E:/work/视频测试/儿子毕业了/20.jpg',
    #     'E:/work/视频测试/儿子毕业了/21.jpg',
    #     'E:/work/视频测试/儿子毕业了/22.jpg'], 'dayang')

def openEye():
    handle = []
    handle.append('openEye')
    handle.append('E:/work/视频测试/out.mp4')
    handle.append('E:/work/视频测试/output.mp4')
    editor = VideoAutoEditor()
    editor.openEye(handle)


def cardVideo(picList, effectName):
    if effectName == "holdon":
        effectConf = os.path.join(os.path.abspath('.'), 'template', 'cardvideo', 'holdon.conf')
    elif effectName == "dayang":
        effectConf = os.path.join(os.path.abspath('.'), 'template', 'cardvideo', 'dayang.conf')
    else:
        return

    print(effectConf)
    common = getJson(effectConf, 'common')
    cardVideoNum = int(common.get('number', '0'))
    cardVideoFile = common.get('file', '')
    cardVideoFile = os.path.join(os.path.abspath('.'), 'template', 'cardvideo', cardVideoFile)

    cards = getJson(effectConf, 'cards')
    mergeFileList = []
    mergeFileList.append('videoMerge')

    for i in range(0, cardVideoNum):
        # 1. generate 2s video
        handle = []
        handle.append('oneImgToVideo')
        handle.append(picList[i])
        handle.append(cards[i].get('time'))
        handle.append('1920')
        handle.append('1080')
        handle.append('black')
        outputFile = os.path.join(os.path.dirname(picList[i]), os.path.basename(picList[i])[:-4]+'.mp4')
        handle.append(outputFile)
        editor = VideoAutoEditor()
        editor.oneImgToVideo(handle)

        mergeFileList.append(outputFile)

    # 3. merge all video
    outputFile = os.path.join(os.path.dirname(picList[0]), 'output.mp4')
    mergeFileList.append(outputFile)
    editor = VideoAutoEditor()
    editor.videoMerge(mergeFileList)

    # 4. add music
    handle = []
    handle.append('addMusic')
    handle.append(outputFile)
    handle.append(cardVideoFile)
    outputFile = os.path.join(os.path.dirname(picList[0]), 'shark.mp4')
    handle.append(outputFile)
    editor = VideoAutoEditor()
    editor.addMusic(handle)

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
    mergeFileList = []
    mergeFileList.append('videoMerge')
    # 1. generate 2s video
    handle = []
    handle.append('oneImgToVideo')
    handle.append(picList[0])
    handle.append('2')
    handle.append('1920')
    handle.append('1080')
    handle.append('black')
    outputFile = os.path.join(os.path.dirname(picList[0]),os.path.basename(picList[0])[:-4]+'.mp4')
    handle.append(outputFile)
    editor = VideoAutoEditor()
    editor.oneImgToVideo(handle)

    mergeFileList.append(outputFile)

    # 2. generate 0.5s video (21)
    for i in range(1,len(picList)):
        print(i)
        handle = []
        handle.append('oneImgToVideo')
        handle.append(picList[i])
        handle.append('0.4999')
        handle.append('1920')
        handle.append('1080')
        handle.append('black')
        outputFile = os.path.join(os.path.dirname(picList[i]),os.path.basename(picList[i])[:-4]+'.mp4')
        handle.append(outputFile)
        editor = VideoAutoEditor()
        editor.oneImgToVideo(handle)

        mergeFileList.append(outputFile)

    outputFile = os.path.join(os.path.dirname(picList[0]), 'output.mp4')
    mergeFileList.append(outputFile)

    # 3. merge all video
    editor = VideoAutoEditor()
    editor.videoMerge(mergeFileList)

    # 4. add music
    handle = []
    handle.append('addMusic')
    handle.append(outputFile)
    handle.append(music)
    outputFile = os.path.join(os.path.dirname(picList[0]), 'shark.mp4')
    handle.append(outputFile)
    editor = VideoAutoEditor()
    editor.addMusic(handle)

def getJson(file, key=None):
    """
    :param file: Json file
    :param key: Json file first level key
    """
    with open(file, encoding='utf-8') as f:
        json_object = json.load(f)
        if key == None:
            keyValue = json_object
        else:
            keyValue = json_object[key]
        return keyValue

if __name__ == '__main__':
    specialEffect()

