#! /usr/bin/python
# -*- coding: utf-8 -*-

import hashlib

class ClipData(object):
    """docstring for ClipData"""
    def __init__(self, inFile):
        super(ClipData, self).__init__()
        self.inVideoFile = inFile
        self.inVideoFileHash = hashlib.md5(bytes(inFile,encoding='utf-8')).hexdigest()
        self.outVideoFile = ''
        self.outAudioFile = ''
        self.actions = []
        self.actionsHash = ''
        self.noChange = '0'
        self.isMerge = '0'

    def setVideoFileHash(self, videoFile):
        self.inVideoFileHash = hashlib.md5(bytes(videoFile,encoding='utf-8')).hexdigest()

    def addAction(self, action):
        self.actions.append(action)

    def setOutVideoFile(self, outFile):
        self.outVideoFile = outFile

    def setOutAudioFile(self, outFile):
        self.outAudioFile = outFile

    def setMergeFlag(self):
        self.isMerge = '1'

    def setActionsHash(self):
        # self.actionsHash = hash(''.join(self.actions))
        outData = ''
        for action in self.actions:
            for item in action:
                outData += str(item)
        self.actionsHash = hashlib.md5(bytes(outData, encoding='utf-8')).hexdigest()

def main():
    clip = ClipData("H:/2017-05-27-延河杯 延八 延九/等级3/[2上半场0.01.34][等级3][进球]\\11.主相机.MP4")
    print(clip.inVideoFileHash)
    clip = ClipData("\\\\Yiball-server\\忆球工具\\自动化剪辑素材\\header.mp4")
    print(clip.inVideoFileHash)
    clip = ClipData("\\\\Yiball-server\\忆球工具\\自动化剪辑素材\\header.mp4")
    print(clip.inVideoFileHash)


if __name__ == '__main__':
    main()
