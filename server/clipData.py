#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import hashlib
import urllib.request

class ClipData(object):
    """docstring for ClipData"""
    def __init__(self, inFile):
        super(ClipData, self).__init__()
        self.inVideoFile = inFile
        self.inVideoFileHash = self.setVideoFileHash(inFile)
        self.outVideoFile = ''
        self.outAudioFile = ''
        self.actions = []
        self.actionsHash = ''
        self.idType = '0'
        self.noChange = '0'
        self.isMerge = '0'

    def checkFileExists(self, url):
        if url.find('http://') == -1:
            return os.path.exists(url)
        
        status = urllib.request.urlopen(url).code
        print(status)
        if status == 200:
            return True
        else:
            return False

    def setVideoFileHash(self, videoFile, salt=''):
        # self.inVideoFileHash = hashlib.md5(bytes(videoFile,encoding='utf-8')).hexdigest()
        if videoFile.find('http://') == -1:
            md5Result = self.md5sum(videoFile)
        else:
            md5Result = self.md5hex(videoFile)
        self.inVideoFileHash = self.md5hex(videoFile+md5Result+salt)
        return self.inVideoFileHash

    def addAction(self, action):
        self.actions.append(action)

    def setOutVideoFile(self, outFile):
        self.outVideoFile = outFile

    def setOutAudioFile(self, outFile):
        self.outAudioFile = outFile

    def setMergeFlag(self):
        self.isMerge = '1'

    def setIdType(self, idType):
        self.idType = idType

    def setActionsHash(self):
        # self.actionsHash = hash(''.join(self.actions))
        outData = ''
        for action in self.actions:
            if action[0] == 'PIP_imgOnVideo':
                outData += self.md5sum(action[2])
            if action[0] == 'PIP_imgOnVideo_2':
                outData += self.md5sum(action[2])
            if action[0] == 'videoLogo':
                outData += self.md5sum(action[2])
            for item in action:
                outData += str(item)
        self.actionsHash = hashlib.md5(bytes(outData, encoding='utf-8')).hexdigest()
        print(self.actionsHash)

    def md5hex(self, word):  
        """ MD5加密算法，返回32位小写16进制符号 """   
        if isinstance(word, str):  
            word = word.encode("utf-8")  
        elif not isinstance(word, str):  
            word = str(word)  
        m = hashlib.md5()  
        m.update(word)  
        return m.hexdigest()  
   
    def md5sum(self, fname):  
        """ 计算文件的MD5值"""  
        def read_chunks(fh):  
            fh.seek(0)  
            chunk = fh.read(8096)  
            while chunk:  
                yield chunk  
                chunk = fh.read(8096)  
            else: #最后要将游标放回文件开头  
                fh.seek(0)  
        m = hashlib.md5()  
        if isinstance(fname, str) \
                and self.checkFileExists(fname):  
            with open(fname, "rb") as fh:  
                for chunk in read_chunks(fh):  
                    m.update(chunk)  
        #上传的文件缓存 或 已打开的文件流  
        elif fname.__class__.__name__ in ["StringIO", "StringO"] : 
            for chunk in read_chunks(fname):  
                m.update(chunk)  
        else:  
            return ""
        return m.hexdigest()  

def main():
    clip = ClipData("H:/2017-05-27-延河杯 延八 延九/等级3/[2上半场0.01.34][等级3][进球]\\11.主相机.MP4")
    print(clip.setVideoFileHash("H:/2017-05-27-延河杯 延八 延九/等级3/[2上半场0.01.34][等级3][进球]\\11.主相机.MP4"))
    # clip = ClipData("\\\\Yiball-server\\忆球工具\\自动化剪辑素材\\header.mp4")
    # print(clip.inVideoFileHash)
    # clip = ClipData("\\\\Yiball-server\\忆球工具\\自动化剪辑素材\\header.mp4")
    # print(clip.inVideoFileHash)


if __name__ == '__main__':
    main()
