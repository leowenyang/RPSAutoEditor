#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import json
import subprocess

from ffmpegwrapper.videoautoeditor import *
from ffmpegwrapper.timerCounter import *

def test():
    handle = ['outputFormat', 'H:/2017-05-27-延河杯 延八 延九/等级3/[2上半场0.01.34][等级3][进球]/11.主相机.MP4', 'test.mp4']
    editor = VideoAutoEditor()
    editor.outputFormat(handle)

    handle = ['addNullAudio', 'clip_fadein.mp4', 'null.mp3', 'clip_fadein_out.mp4']
    editor = VideoAutoEditor()
    editor.addNullAudio(handle)

    handle = ['merge', 'clip_fadein_out.mp4', 'test.mp4', 'outFile.mp4']
    editor = VideoAutoEditor()
    editor.videoMerge(handle)

    # editor = VideoAutoEditor()
    # editor.getVideoLen('11.MP4')

    # handle = ['videoFade', 'clip.mp4', '2', 'clip_fadeout.mp4']
    # editor = VideoAutoEditor()
    # editor.videoFade(handle)

    # handle = ['videoFade', 'clip_2.mp4', '1', 'clip_fadein.mp4']
    # editor = VideoAutoEditor()
    # editor.videoFade(handle)

    # handle = ['merge', 'clip_fadeout.mp4', 'clip_fadein.mp4', 'outFile.mp4']
    # editor = VideoAutoEditor()
    # editor.videoMerge(handle)

    # handle = ['imgMoveScale', 'football.jpg', '5', 'output.mp4']
    # editor = VideoAutoEditor()
    # editor.imgMoveScale(handle)

    # handle = ['videoSpeed', 'clip_3_logo.mp4', '0', '25', '0', '25', '1.5', 'output.mp4']
    # editor = VideoAutoEditor()
    # editor.videoSpeed(handle)

    # handle = ['videoRotate', 'match.mp4', '2', 'output.mp4']
    # editor = VideoAutoEditor()
    # editor.videoRotate(handle)

    # handle = ['videoScale', 'match.mp4', '100', '100', '640', '360', 'output.mp4']
    # editor = VideoAutoEditor()
    # editor.videoScale(handle)

    # handle = ['outputFormat', 'test.mp4', 'clip.mp4']
    # editor = VideoAutoEditor()
    # editor.outputFormat(handle)

    # handle = ['cameraMove', 'clip.mp4', '960', '540', 'outFile.mp4']
    # editor = VideoAutoEditor()
    # editor.cameraMove(handle)

    # handle = ['rmShaky', 'outFile.mp4', 'outFile_rmshaky.mp4']
    # editor = VideoAutoEditor()
    # editor.rmShaky(handle)

    # handle = ['PIP_imgOnVideo', 'clip.mp4', 'header.png', '3', '6', 'clip_subtitle.mp4']
    # editor = VideoAutoEditor()
    # editor.PIP_imgOnVideo(handle)

    # handle = ['PIP_videoOnImg', 'header.png', 'clip.mp4', 'clip_pip.mp4']
    # editor = VideoAutoEditor()
    # editor.PIP_videoOnImg(handle)

    # handle = ['eachVideoMerge', [['./temp/header.mp4', '0'],
    #                             ['clip.mp4','-1'],
    #                             ['transfer.mp4', '1'],
    #                             ['clip.mp4', '-1']], './temp/outFile.mp4']
    # handle = ['eachVideoMerge', [['./header.mp4', '0'],
    #                              ['clip.mp4','1']], './outFile.mp4']
    # editor = VideoAutoEditor()
    # editor.eachVideoMerge(handle)

    # probe = FFProbeFactory('clip.mp4')
    # probe.getVideoLen()

def addMusic(strategyFile):
    # handle config
    config = getJson(strategyFile, "config")
    isHasAudio = config.get('audio', "")

    if not ('musicFolder' in config.keys())  or '' == config['musicFolder']:
        return

    ouputFolder = os.path.realpath(config['ouputFolder'])
    musicFolder = os.path.realpath(config['musicFolder'])
    titleText = config['title_text']
    if len(titleText) == 0:
        titleText = "product_music"

    # 1. get video length
    videoTime = getAVDuration(ouputFolder+"/product.mp4")
    # 2. find musstrategyFileic
    musicFile = matchVideoTime(musicFolder, videoTime)

    # Add music
    if musicFile == None:
        return

    if isHasAudio == '' :
        listParam = ['addMusic', ouputFolder+'/product.mp4', musicFile, ouputFolder+'/../'+titleText+'.mp4']
        editor = VideoAutoEditor()
        editor.addMusic(listParam)
    else:
        listParam = ['addMergeMusic', ouputFolder+'/product.mp4', musicFile, ouputFolder+'/../'+titleText+'.mp4']
        editor = VideoAutoEditor()
        editor.addMergeMusic(listParam)

def buildCmd(cmd, param, inFile, outFile):
    cmdList = []
    cmdList.append(cmd)
    if len(inFile) != 0:
        cmdList.append(inFile)
    for item in param:
        cmdList.append(item)
    cmdList.append(outFile)

    return cmdList

def handleAutoEdit(strategyFile):
    # counter time
    timerCounter = CountingTimer()
    timerCounter.begin()

    # handle config
    config = getJson(strategyFile, "config")
    ouputFolder = os.path.realpath(config['ouputFolder'])

    editor = VideoAutoEditor()
    actions = getJson(ouputFolder+"/autoEditor.json", "action")
    for cmd in actions:
        editor.handleCmd(cmd)

    # counter time
    timerCounter.end()
    print("total spend %s s" % (timerCounter.diff()[0]))

def parseStrategy(strategyFile):
    mergeList = ["videoMerge"]
    mergeAudioList = ["videoMerge"]
    videoAudioList = []
    muteAduioFile = ''
    # mergeList = ["eachVideoMerge"]
    clipMergeList = []
    actionList = []
    cmdList = []
    logoFile = ''
    titlePng = ''
    ouputFolder = ''
    isHasAudio = ''

    # handle config
    config = getJson(strategyFile, "config")
    logoFile = config['logo']
    titlePng = config['title']
    isHasAudio = config.get('audio', "")
    ouputFolder = os.path.realpath(config['ouputFolder'])


    # handle video clips
    strategy = getJson(strategyFile, "video_clips")
    nClip = 0
    nLastClip = len(strategy)
    for clip in strategy:
        # some temp var
        nClip = nClip + 1
        finalOutputFile = ''
        outputFile = ''

        # get info from JSON file
        file = clip['file']
        actions = clip['actions']

        isAddLogo = False
        muteAduioFile = ''
        nAction = 0
        for action in actions:
            # some temp var
            nAction = nAction + 1
            cmd = action["action"]
            if 'join' == cmd:
                finalOutputFile = file
                # check if add logo
                param = action["parameter"]
                mergeTime = param[0]
                if mergeTime > 0 or nClip == 1:
                    isAddLogo = False
                else:
                    isAddLogo = True

            if 'cut' == cmd:
                param = action["parameter"]

                # videoCut
                outputFile = ouputFolder + "/clip_"+str(nClip)+file[-4:]
                param[1] = round(param[1] - param[0], 3)
                actionList.append(buildCmd("videoCut", param, file, outputFile))
                finalOutputFile = outputFile

                # outputFormat
                outputFile = ouputFolder + "/clip_"+str(nClip)+"_format.mp4"
                actionList.append(buildCmd("outputFormat", [], finalOutputFile, outputFile))
                finalOutputFile = outputFile

                # get audio from file
                muteAduioFile = finalOutputFile

            if 'cut_a' == cmd:
                param = action["parameter"]

                # videoCut
                outputFile = ouputFolder + "/clip_"+str(nClip)+file[-4:]
                param[1] = round(param[1] - param[0], 3)
                actionList.append(buildCmd("videoCut_a", param, file, outputFile))
                finalOutputFile = outputFile

                # outputFormat
                outputFile = ouputFolder + "/clip_"+str(nClip)+"_format.mp4"
                actionList.append(buildCmd("outputFormat", [], finalOutputFile, outputFile))
                finalOutputFile = outputFile

                # get audio from file
                muteAduioFile = finalOutputFile

            if 'addstar' == cmd:
                param = action["parameter"]

                lastOutputFile = finalOutputFile

                # videoToOneImg
                param = []
                param.append(mergeList[-1])
                param.append('-0.1')
                outputFile = ouputFolder + "/clip_"+str(nClip)+".png"
                actionList.append(buildCmd("videoEndToOneImg", param, '', outputFile))
                finalOutputFile = outputFile

                # PIP_videoOnImg
                outputFile = ouputFolder + "/clip_"+str(nClip)+"_pip.mp4"
                actionList.append(buildCmd("PIP_videoOnImg", [lastOutputFile], finalOutputFile, outputFile))
                finalOutputFile = outputFile

            if 'rotate' == cmd:
                param = action["parameter"]

                # videoRotate
                if param[0] == 0:
                    continue
                outputFile = ouputFolder + "/clip_"+str(nClip)+"_rotate.mp4"
                actionList.append(buildCmd("videoRotate", param, finalOutputFile, outputFile))
                finalOutputFile = outputFile

            if 'select_range' == cmd:
                param = action["parameter"]

                # videoScale
                if param[0] == 0 and param[1] == 0 and param[2] == 1920 and param[3] == 1080:
                    continue
                outputFile = ouputFolder + "/clip_"+str(nClip)+"_range.mp4"
                actionList.append(buildCmd("videoScale", param, finalOutputFile, outputFile))
                finalOutputFile = outputFile

            if 'camera_move' == cmd:
                param = action["parameter"]

                # cameraMove
                outputFile = ouputFolder + "/clip_"+str(nClip)+"_camera.mp4"
                actionList.append(buildCmd("cameraMove", param, finalOutputFile, outputFile))
                finalOutputFile = outputFile

                # rmShaky
                outputFile = ouputFolder + "/clip_"+str(nClip)+"_rmshaky.mp4"
                actionList.append(buildCmd("rmShaky", [], finalOutputFile, outputFile))
                finalOutputFile = outputFile

            if 'slow_motion' == cmd:
                param = action["parameter"]

                # videoSpeed
                if param[4] == 1:
                    continue
                outputFile = ouputFolder + "/clip_"+str(nClip)+"_slow.mp4"
                actionList.append(buildCmd("videoSpeed", param, finalOutputFile, outputFile))
                finalOutputFile = outputFile

            if 'add_subtitle' == cmd:
                param = action["parameter"]

                # add subtitle
                if param[0] != 1:
                    continue
                outputFile = ouputFolder + "/clip_"+str(nClip)+"_subtitle.mp4"
                param = []
                param.append(titlePng)
                param.append('1')
                param.append('3')
                actionList.append(buildCmd("PIP_imgOnVideo", param, finalOutputFile, outputFile))
                finalOutputFile = outputFile

            if 'add_pic' == cmd:
                param = action["parameter"]

                # add picture
                if param[0] == '':
                    continue
                param[2] = param[1] + param[2]
                outputFile = ouputFolder + "/clip_"+str(nClip)+"_pic_"+str(nAction)+".mp4"
                actionList.append(buildCmd("PIP_imgOnVideo", param, finalOutputFile, outputFile))
                finalOutputFile = outputFile

            if 'fade_inout' == cmd:
                param = action["parameter"]

                outputFile = ouputFolder + "/clip_"+str(nClip)+"_fade.mp4"
                actionList.append(buildCmd("videoFade", param, finalOutputFile, outputFile))
                finalOutputFile = outputFile

        if isAddLogo and logoFile != '':
            # videoLogo
            outputFile = ouputFolder + "/clip_"+str(nClip)+"_logo.mp4"
            actionList.append(buildCmd("videoLogo", [logoFile, '100'], finalOutputFile, outputFile))
            finalOutputFile = outputFile

        # get audio file
        if isHasAudio != '' :
            audioOutputFile = ouputFolder + "/clip_"+str(nClip)+"_audio.mp3"
            if muteAduioFile == '' :
                actionList.append(buildCmd("creatMuteAudio", [], finalOutputFile, audioOutputFile))
            else:
                actionList.append(buildCmd("splitAudio", [], muteAduioFile, audioOutputFile))  
            mergeAudioList.append(audioOutputFile)
        
        # clip finished, merge file
        # clipMergeList.append([finalOutputFile, mergeTime])
        # clipMergeList.append(finalOutputFile)
        # merge clip
        mergeList.append(finalOutputFile)

    if isHasAudio != '' :
        # gen product
        finalOutputFile = ouputFolder + "/product_video.mp4"
        mergeList.append(finalOutputFile)

        # gen product audio
        audioOutputFile = ouputFolder + "/product_audio.mp3"
        mergeAudioList.append(audioOutputFile)

        # merge product video and audio
        outputFile = ouputFolder + "/product.mp4"
        videoAudioList = buildCmd("mergeAudio", [audioOutputFile], finalOutputFile, outputFile)
    else :
        # gen product
        finalOutputFile = ouputFolder + "/product.mp4"
        mergeList.append(finalOutputFile)

    # save JSON file
    json_object = {}
    json_object["action"] = []
    for item in actionList:
        json_object["action"].append(item)
    json_object["action"].append(mergeList)
    if isHasAudio != '' :
        json_object["action"].append(mergeAudioList)
        json_object["action"].append(videoAudioList)

    with open(ouputFolder + "/autoEditor.json", "w", encoding='utf-8') as f:
        json.dump(json_object, f, indent=4, ensure_ascii=False)
                

def getAVDuration(file):
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
            duration = duration[ : duration.find(".")]
            duration = duration.split(':')
            duration = int(duration[0])*3600 + int(duration[1])*60 + int(duration[2])
       
    return duration

def matchVideoTime(audioLibPath, videoTime):
    # get all audio file
    if os.path.exists(audioLibPath):
        audioFileList = getFileByPath(audioLibPath)          
    else:
        print("no this %s folder" % audioLibPath)
        return None

    # travel all file
    for audioFile in audioFileList:
        if (audioFile[-4:].upper() != ".MP3"):
            continue
        audioTime = getAVDuration(audioFile)
        if matchTime(videoTime, audioTime):
            return audioFile
    # not found
    return None

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

def matchTime(videoTime, audioTime):
    # if abs(outTime-inTime) < 2:
    #     return True
    # else:
    #     return False

    if (videoTime > audioTime) and (videoTime - audioTime <= 2):
        return True
    else:
        return False

def saveJson():
    pass

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
    # parseStrategy("E:/work/创业之路/音视频技术/科大讯飞/FFmpeg特效库/dev/strategy.json")
    parseStrategy("//Yiball-server/延十八比赛/等级3/[2上半场0.05.28][等级3][进球]/strategy.json")
    handleAutoEdit("//Yiball-server/延十八比赛/等级3/[2上半场0.05.28][等级3][进球]/strategy.json")
    addMusic("//Yiball-server/延十八比赛/等级3/[2上半场0.05.28][等级3][进球]/strategy.json")
    # test()

