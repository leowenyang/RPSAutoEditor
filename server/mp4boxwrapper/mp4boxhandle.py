#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json
import shutil

from .mp4box import *
from .parameters import *

class MP4boxFactory(object):
    """docstring for MP4boxFactory"""
    def __init__(self, inFile, outFile):
        self.input = Input('"'+inFile+'"')
        self.output = Output('"'+outFile+'"')
  
    """
    Video Handle
    """
    def videoCrypt(self, drm_file):
        # Input 
        self.input.add_formatparam('-crypt', '"'+drm_file+'"')

    def videoDecrypt(self, drm_file):
        # Input 
        self.input.add_formatparam('-decrypt', '"'+drm_file+'"')

    """
    Other Handle
    """
    def run(self):
        MP4box(os.path.join(os.path.abspath('.'), 'bin','mp4box.exe'), self.input, self.output).run()

class MP4boxHandle():
    """docstring for VideoAutoEditor"""
    def __init__(self):
        pass

    def getVideoLen(self, file):
        '''
        Get Video/Audio total time (s)
        :param file: video/audio file
        '''
        item_list = None
        cmd = '%s -i "%s"' % (os.path.join(os.path.abspath('.'), 'bin','ffmpeg.exe'),file)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        p.wait()
        item_list = p.stdout.read().splitlines()

        duration = None
        for i in range(len(item_list)):
            try:
                item = item_list[i].decode('utf-8')
            except:
                item = str(item_list[i])

            if "Duration" in item:
                begin_index = item.find(":")
                end_index = item.find(",")
                duration = item[begin_index + 1: end_index].strip()
                microTime = duration[duration.find(".") :]
                duration = duration[ : duration.find(".")]
                duration = duration.split(':')
                duration = int(duration[0])*3600 + int(duration[1])*60 + int(duration[2])+float(microTime)
           
        return duration

    def videoCrypt(self, listParam):
        """
        handle : ['videoCrypt', 'inFile', 'drmFile', outFile']
        """

        # check Param
        if len(listParam) != 4:
            print(listParam)
            print("COMMAND: videoCrypt -> param format invalid")
            print("['videoCrypt', 'inFile', 'drmFile', 'outFile']")
            return
        
        # handle
        mp4boxHandler = MP4boxFactory(listParam[1], listParam[-1])
        mp4boxHandler.videoCrypt(listParam[2])
        mp4boxHandler.run()

    def videoDecrypt(self, listParam):
        """
        handle : ['videoDecrypt', 'inFile', 'drmFile', outFile']
        """

        # check Param
        if len(listParam) != 4:
            print(listParam)
            print("COMMAND: videoDecrypt -> param format invalid")
            print("['videoDecrypt', 'inFile', 'drmFile', 'outFile']")
            return
        
        # handle
        mp4boxHandler = MP4boxFactory(listParam[1], listParam[-1])
        mp4boxHandler.videoDecrypt(listParam[2])
        mp4boxHandler.run()

    def handleCmd(self, listParam):
        if not len(listParam):
            print("cmd error")
            return

        # counter time
        self.timerCounter.begin()

        # handle 
        print(listParam)
        eval("self."+listParam[0])(listParam)

        # counter time
        self.timerCounter.end()
        print("%s spend %s s" % (listParam[0], self.timerCounter.diff()))

    def run(self):
        handle = ['videoCrypt', 'demo.mp4', '2', 'output.mp4']
        self.videoSpeed(handle)

def main():
    handler = MP4boxHandle()
    handler.run()
        
if __name__ == '__main__':
    main()