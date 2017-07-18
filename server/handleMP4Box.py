#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import json
import subprocess

from mp4boxwrapper.mp4boxhandle import *

def test():
    handle = ['videoCrypt', 'out.mp4', 'drm_file.xml', 'out_encryp.mp4']
    editor = MP4boxHandle()
    editor.videoCrypt(handle)

    handle = ['videoCrypt', 'out_encryp.mp4', 'drm_file.xml', 'out_clear.mp4']
    editor.videoDecrypt(handle)

def buildCmd(cmd, param, inFile, outFile):
    cmdList = []
    cmdList.append(cmd)
    if len(inFile) != 0:
        cmdList.append(inFile)
    for item in param:
        cmdList.append(item)
    cmdList.append(outFile)

    return cmdList

def getFileByPath(path):
    '''
    get full path file 
    '''
    files = os.listdir(path)
    fileList = []
    for fileName in files:
        fullFileName = os.path.join(path, fileName)
        fileList.append(fullFileName)
 
    return fileList


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

def levelJson(jsonData, objLevel, curLevel=0):
    if objLevel == curLevel:
        return jsonData

    if (isinstance(jsonData, dict)):
        for item in jsonData:
            if (isinstance(jsonData[item], dict)):
                levelJson(jsonData[item], objLevel, curLevel=curLevel+1)
    else:
        print("Is not json object!")
        
if __name__ == '__main__':
    test()
