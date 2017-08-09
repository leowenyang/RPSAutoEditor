#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import json
import subprocess

from ffmpegwrapper.videoautoeditor import *
from ffmpegwrapper.timerCounter import *

from clipData import *

def test():
    # handle = ['splitAudio', '04.mp4', '04.mp3']
    # editor = VideoAutoEditor()
    # editor.splitAudio(handle)
    
    # 'contrast', 'brightness', 'saturation'
    # handle = ['videoCBS', '04.mp4', '1', '0', '1', '04_color.mp4']
    # editor = VideoAutoEditor()
    # editor.videoCBS(handle)

    # handle = ['outputFormat', 'H:/2017-05-27-延河杯 延八 延九/等级3/[2上半场0.01.34][等级3][进球]/11.主相机.MP4', 'test.mp4']
    # editor = VideoAutoEditor()
    # editor.outputFormat(handle)

    # handle = ['addNullAudio', 'clip_fadein.mp4', 'null.mp3', 'clip_fadein_out.mp4']
    # editor = VideoAutoEditor()
    # editor.addNullAudio(handle)

    # handle = ['merge', 'clip_fadein_out.mp4', 'test.mp4', 'outFile.mp4']
    # editor = VideoAutoEditor()
    # editor.videoMerge(handle)

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

    handle = ['PIP_imgOnVideo', 'clip.mp4', 'header.png', '1', '2', 'clip_subtitle.mp4']
    editor = VideoAutoEditor()
    editor.PIP_imgOnVideo(handle)

    handle = ['PIP_imgOnVideo', 'clip.mp4', 'header.png', '2', '3', 'clip_subtitle.mp4']
    editor = VideoAutoEditor()
    editor.PIP_imgOnVideo(handle)
    handle = ['PIP_imgOnVideo', 'clip.mp4', 'header.png', '3', '4', 'clip_subtitle.mp4']
    editor = VideoAutoEditor()
    editor.PIP_imgOnVideo(handle)
    handle = ['PIP_imgOnVideo', 'clip.mp4', 'header.png', '4', '5', 'clip_subtitle.mp4']
    editor = VideoAutoEditor()
    editor.PIP_imgOnVideo(handle)
    handle = ['PIP_imgOnVideo', 'clip.mp4', 'header.png', '5', '6', 'clip_subtitle.mp4']
    editor = VideoAutoEditor()
    editor.PIP_imgOnVideo(handle)
    handle = ['PIP_imgOnVideo', 'clip.mp4', 'header.png', '6', '7', 'clip_subtitle.mp4']
    editor = VideoAutoEditor()
    editor.PIP_imgOnVideo(handle)
    handle = ['PIP_imgOnVideo', 'clip.mp4', 'header.png', '7', '8', 'clip_subtitle.mp4']
    editor = VideoAutoEditor()
    editor.PIP_imgOnVideo(handle)
    handle = ['PIP_imgOnVideo', 'clip.mp4', 'header.png', '8', '9', 'clip_subtitle.mp4']
    editor = VideoAutoEditor()
    editor.PIP_imgOnVideo(handle)
    handle = ['PIP_imgOnVideo', 'clip.mp4', 'header.png', '9', '10', 'clip_subtitle.mp4']
    editor = VideoAutoEditor()
    editor.PIP_imgOnVideo(handle)
    handle = ['PIP_imgOnVideo', 'clip.mp4', 'header.png', '10', '11', 'clip_subtitle.mp4']
    editor = VideoAutoEditor()
    editor.PIP_imgOnVideo(handle)

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
    resultFile = ''
    config = getJson(strategyFile, "config")
    isHasAudio = config.get('audio', "")

    ouputFolder = os.path.realpath(config['ouputFolder'])
    musicFolder = os.path.realpath(config['musicFolder'])
    titleText = config.get('title_text', "")

    videoType = config.get('videoType', "")
    if videoType == "1":
        # xiaopian
        if len(titleText) == 0:
            titleText = "product_music"
        resultFile = ouputFolder+'/../'+titleText+'.mp4'

    elif videoType == "2":
        # jijinsucai
        # create temp fold
        tmpSaveFolder = ouputFolder+'/../../集锦'
        if not os.path.exists(tmpSaveFolder):
            os.mkdir(tmpSaveFolder)
        # copy file
        # print(ouputFolder.split('\\')[-2])
        tmpFileName = os.path.join(tmpSaveFolder, ouputFolder.split('\\')[-2]+'.mp4')
        shutil.copyfile(os.path.join(ouputFolder, 'product.mp4'), tmpFileName)
    elif videoType == "3":
        # jijin
        resultFile = ouputFolder+'/../'+'全场集锦.mp4'
    else:
        return

    if not ('musicFolder' in config.keys())  or '' == config['musicFolder']:
        return

    # 1. get video length
    videoTime = getAVDuration(ouputFolder+"/product.mp4")
    # 2. find musstrategyFileic
    musicFile = matchVideoTime(musicFolder, videoTime)

    # Add music
    if musicFile == None:
        return

    if isHasAudio == '' :
        listParam = ['addMusic', ouputFolder+'/product.mp4', musicFile, resultFile]
        editor = VideoAutoEditor()
        editor.addMusic(listParam)
    else:
        listParam = ['addMergeMusic', ouputFolder+'/product.mp4', musicFile, resultFile]
        editor = VideoAutoEditor()
        editor.addMergeMusic(listParam)

    if videoType == "1":
        # Save other folder
        tmpSaveFolder = ouputFolder+'/../../小片'
        if not os.path.exists(tmpSaveFolder):
            os.mkdir(tmpSaveFolder)
        # copy file
        shutil.copyfile(resultFile, os.path.join(tmpSaveFolder, os.path.basename(resultFile)))

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

def findClipDataByhash(hash, clipData):
    for clip in clipData:
        if hash == clip['inVideoFileHash']:
            return clip
    return False

def diffAutoEditorFile(newFile, oldFile):
    # new diff json file
    if os.path.exists(os.path.join(os.path.dirname(newFile),"autoEditor_diff.json")):
        os.remove(os.path.join(os.path.dirname(newFile),"autoEditor_diff.json"))

    diffJson = getJson(os.path.join(os.path.dirname(newFile),"autoEditor.json"))
    oldJson = getJson(oldFile, "clips_handle")

    for clip in diffJson['clips_handle']:
        oldClip = findClipDataByhash(clip['inVideoFileHash'], oldJson)

        if not oldClip:
            continue
        if ((oldClip['actionsHash'] == clip['actionsHash']) 
           and (clip['isMerge'] == '0')
           and (os.path.exists(clip['outVideoFile']))):
            # set no handle
            diffJson['clips_handle'][diffJson['clips_handle'].index(clip)]['noChange'] = '1'

    with open(os.path.join(os.path.dirname(newFile),"autoEditor_diff.json"), "w", encoding='utf-8') as f:
        json.dump(diffJson, f, indent=4, ensure_ascii=False)
    return os.path.join(os.path.dirname(newFile),"autoEditor_diff.json")

def handleAutoEdit_new(strategyFile):
    # counter time
    timerCounter = CountingTimer()
    timerCounter.begin()

    # handle config
    config = getJson(strategyFile, "config")
    ouputFolder = os.path.realpath(config['ouputFolder'])

    # check autoEditor file
    if os.path.exists(ouputFolder + "/autoEditor_old.json"):
        handleAEFile = diffAutoEditorFile(ouputFolder+"/autoEditor.json", ouputFolder + "/autoEditor_old.json")
    else:
        handleAEFile = ouputFolder+"/autoEditor.json"

    editor = VideoAutoEditor()
    clips = getJson(handleAEFile, "clips_handle")
    for clip in clips:
        if clip['noChange'] == '1':
            continue
        for action in clip['actions']:
            editor.handleCmd(action)

    # counter time
    timerCounter.end()
    print("total spend %s s" % (timerCounter.diff()[0]))

def parseStrategy_new(strategyFile):
    clipDataList = []
    # handle config
    config = getJson(strategyFile, "config")
    logoFile = config.get('logo', "")
    titlePng = config.get('title', "")
    isHasAudio = config.get('audio', "")
    ouputFolder = os.path.realpath(config['ouputFolder'])

    # handle video clips
    clips = getJson(strategyFile, "video_clips")
    nClip = 0
    for clip in clips:
        nClip = nClip + 1
        # get info from JSON file
        file = clip.get('file', "")
        actions = clip.get('actions', "")
        baseName = os.path.basename(file)

        # new clipData
        clipData = ClipData(file)
        outputFile = ''
        finalOutputFile = file

        nAction = 0
        isCutWithAudio = True
        muteAduioFile = ''
        for action in actions:
            nAction = nAction + 1
            # get action info
            cmd = action.get('action', "")
            param = action.get('parameter', "")

            if 'join' == cmd:
                # get audio
                clipData.setOutAudioFile(file)
                clipData.setOutVideoFile(file)
            if 'cut' == cmd:
                # videoCut
                outputFile = os.path.join(ouputFolder, baseName[:-4]+"_cut"+str(nClip)+str(nAction)+baseName[-4:])
                param[1] = round(param[1] - param[0], 3)
                clipData.addAction(actionCut(finalOutputFile, outputFile, param))
                clipData.setOutVideoFile(outputFile)
                # clipData.setOutAudioFile()
                clipData.setVideoFileHash(file, str(param[0])+str(param[1]))
                finalOutputFile = outputFile

                # outputFormat
                outputFile = os.path.join(ouputFolder, baseName[:-4]+"_format"+str(nClip)+str(nAction)+baseName[-4:])
                clipData.addAction(actionFormat(finalOutputFile, outputFile, param))
                clipData.setOutVideoFile(outputFile)
                clipData.setOutAudioFile(outputFile)
                finalOutputFile = outputFile

                # no Audio
                isCutWithAudio = False
            if 'cut_a' == cmd:
                # videoCut
                outputFile = os.path.join(ouputFolder, baseName[:-4]+"_cut_a"+str(nClip)+str(nAction)+baseName[-4:])
                param[1] = round(param[1] - param[0], 3)
                clipData.addAction(actionCut_a(finalOutputFile, outputFile, param))
                clipData.setOutVideoFile(outputFile)
                # clipData.setOutAudioFile()
                clipData.setVideoFileHash(file, str(param[0])+str(param[1]))
                finalOutputFile = outputFile

                # outputFormat
                outputFile = os.path.join(ouputFolder, baseName[:-4]+"_format"+str(nClip)+str(nAction)+baseName[-4:])
                clipData.addAction(actionFormat(finalOutputFile, outputFile, param))
                clipData.setOutVideoFile(outputFile)
                clipData.setOutAudioFile(outputFile)
                finalOutputFile = outputFile

                # have Audio
                isCutWithAudio = True
            if 'format' == cmd:
                # outputFormat
                outputFile = os.path.join(ouputFolder, baseName[:-4]+"_format"+str(nClip)+str(nAction)+baseName[-4:])
                clipData.addAction(actionFormat(finalOutputFile, outputFile, param))
                clipData.setOutVideoFile(outputFile)
                # clipData.setOutAudioFile()
                finalOutputFile = outputFile
            if 'addstar' == cmd:
                lastOutputFile = finalOutputFile

                # videoToOneImg
                param = []
                param.append('-0.1')
                outputFile = os.path.join(ouputFolder, "clip_"+str(nClip)+".png")
                print(ouputFolder)
                clipData.addAction(actionVideoEndOnImg(clipDataList[-1].outVideoFile, outputFile, param))
                clipData.setOutVideoFile(outputFile)
                # clipData.setOutAudioFile()
                finalOutputFile = outputFile

                # PIP_videoOnImg
                outputFile = os.path.join(ouputFolder, baseName[:-4]+"_pip"+str(nClip)+str(nAction)+baseName[-4:])
                clipData.addAction(actionVideoOnImg(finalOutputFile, outputFile, [lastOutputFile]))
                clipData.setOutVideoFile(outputFile)
                # clipData.setOutAudioFile()
                finalOutputFile = outputFile
            if 'rotate' == cmd:
                # videoRotate
                if param[0] == 0:
                    continue
                outputFile = os.path.join(ouputFolder, baseName[:-4]+"_rotate"+str(nClip)+str(nAction)+baseName[-4:])
                clipData.addAction(actionRotate(finalOutputFile, outputFile, param))
                clipData.setOutVideoFile(outputFile)
                # clipData.setOutAudioFile()
                finalOutputFile = outputFile
            if 'select_range' == cmd:
                # videoScale
                if param[0] == 0 and param[1] == 0 and param[2] == 1920 and param[3] == 1080:
                    continue
                outputFile = os.path.join(ouputFolder, baseName[:-4]+"_range"+str(nClip)+str(nAction)+baseName[-4:])
                clipData.addAction(actionScale(finalOutputFile, outputFile, param))
                clipData.setOutVideoFile(outputFile)
                # clipData.setOutAudioFile()
                finalOutputFile = outputFile
            if 'camera_move' == cmd:
                # cameraMove
                outputFile = os.path.join(ouputFolder, baseName[:-4]+"_camera"+str(nClip)+str(nAction)+baseName[-4:])
                clipData.addAction(actionCameraMove(finalOutputFile, outputFile, param))
                clipData.setOutVideoFile(outputFile)
                # clipData.setOutAudioFile()
                finalOutputFile = outputFile

                # rmShaky
                outputFile = os.path.join(ouputFolder, baseName[:-4]+"_rmshaky"+str(nClip)+str(nAction)+baseName[-4:])
                clipData.addAction(actionRmShaky(finalOutputFile, outputFile, param))
                clipData.setOutVideoFile(outputFile)
                # clipData.setOutAudioFile()
                finalOutputFile = outputFile
            if 'slow_motion' == cmd:
                # videoSpeed
                if param[4] == 1:
                    continue
                outputFile = os.path.join(ouputFolder, baseName[:-4]+"_slow"+str(nClip)+str(nAction)+baseName[-4:])
                clipData.addAction(actionSpeed(finalOutputFile, outputFile, param))
                clipData.setOutVideoFile(outputFile)
                # clipData.setOutAudioFile()
                finalOutputFile = outputFile
            if 'add_subtitle' == cmd:
                # add subtitle
                if param[0] != 1:
                    continue
                outputFile = os.path.join(ouputFolder, baseName[:-4]+"_subtitle"+str(nClip)+str(nAction)+baseName[-4:])
                param = []
                param.append(titlePng)
                param.append('1')
                param.append('3')
                clipData.addAction(actionImgOnVideo(finalOutputFile, outputFile, param))
                clipData.setOutVideoFile(outputFile)
                # clipData.setOutAudioFile()
                finalOutputFile = outputFile
            if 'add_pic' == cmd:
                # add picture
                if param[0] == '':
                    continue
                outputFile = os.path.join(ouputFolder, baseName[:-4]+"_pic"+str(nClip)+str(nAction)+baseName[-4:])
                clipData.addAction(actionImgOnVideo(finalOutputFile, outputFile, param))
                clipData.setOutVideoFile(outputFile)
                # clipData.setOutAudioFile()
                finalOutputFile = outputFile
            if 'fade_inout' == cmd:
                # videoFade
                outputFile = os.path.join(ouputFolder, baseName[:-4]+"_fadeinout"+str(nClip)+str(nAction)+baseName[-4:])
                clipData.addAction(actionFade(finalOutputFile, outputFile, param))
                clipData.setOutVideoFile(outputFile)
                # clipData.setOutAudioFile()
                finalOutputFile = outputFile

        if logoFile != '':
            # videoLogo
            outputFile = os.path.join(ouputFolder, baseName[:-4]+"_logo"+str(nClip)+baseName[-4:])
            clipData.addAction(actionLogo(finalOutputFile, outputFile, [logoFile, '100']))
            clipData.setOutVideoFile(outputFile)
            # clipData.setOutAudioFile()
            finalOutputFile = outputFile

        # get audio file
        if isHasAudio != '' :
            audioOutputFile = os.path.join(ouputFolder, baseName[:-4]+str(nClip)+"_audio.mp3")
            if checkVideoMute(file) or not isCutWithAudio:
                clipData.addAction(actionCreateMuteAudio(clipData.outAudioFile, audioOutputFile, []))
            else:
                clipData.addAction(actionSplitAudio(clipData.outAudioFile, audioOutputFile, []))  
            clipData.setOutAudioFile(audioOutputFile)

        # append list
        clipData.setActionsHash()
        clipDataList.append(clipData)

    # general merge file
    if isHasAudio != '' :
        # gen product
        mergeList = ["videoMerge"]
        outputFile = os.path.join(ouputFolder, "product_video.mp4")
        clipData = ClipData(outputFile)
        for clip in clipDataList:
            mergeList.append(clip.outVideoFile)
        mergeList.append(outputFile)
        clipData.addAction(mergeList)
        clipData.setOutVideoFile(outputFile)
        clipData.setActionsHash()
        clipData.setMergeFlag()
        clipDataList.append(clipData)
        finalOutputFile = outputFile


        # gen product audio
        mergeList = ["videoMerge"]
        outputFile = os.path.join(ouputFolder, "product_audio.mp3")
        clipData = ClipData(outputFile)
        for clip in clipDataList:
            if clip.outAudioFile == '':
                continue
            mergeList.append(clip.outAudioFile)
        mergeList.append(outputFile)
        clipData.addAction(mergeList)
        clipData.setOutVideoFile(outputFile)
        clipData.setActionsHash()
        clipData.setMergeFlag()
        clipDataList.append(clipData)
        audioOutputFile = outputFile

        # merge product video and audio
        outputFile = os.path.join(ouputFolder, "product.mp4")
        clipData = ClipData(outputFile)
        clipData.addAction(actionMergeAudio(finalOutputFile, outputFile, [audioOutputFile]))
        clipData.setOutVideoFile(outputFile)
        clipData.setMergeFlag()
        clipDataList.append(clipData)
    else:
        mergeList = ["videoMerge"]
        outputFile = os.path.join(ouputFolder, "product.mp4")
        clipData = ClipData(outputFile)
        for clip in clipDataList:
            mergeList.append(clip.outVideoFile)
        mergeList.append(outputFile)
        clipData.addAction(mergeList)
        clipData.setOutVideoFile(outputFile)
        clipData.setActionsHash()
        clipDataList.append(clipData)
        # clipData.setOutAudioFile()
        clipData.setMergeFlag()
        finalOutputFile = outputFile

    # save JSON file
    json_object = {}
    json_object["clips_handle"] = []
    for clip in clipDataList:
        json_object["clips_handle"].append(clip.__dict__)

    if os.path.exists(ouputFolder + "/autoEditor.json"):
        if os.path.exists(ouputFolder + "/autoEditor_old.json"):
            os.remove(ouputFolder + "/autoEditor_old.json")
        os.rename(ouputFolder + "/autoEditor.json", ouputFolder + "/autoEditor_old.json")
 
    with open(ouputFolder + "/autoEditor.json", "w", encoding='utf-8') as f:
        json.dump(json_object, f, indent=4, ensure_ascii=False)

def actionCreateMuteAudio(inFile, outFile, param):
    return buildCmd("creatMuteAudio", param, inFile, outFile)

def actionSplitAudio(inFile, outFile, param):
    return buildCmd("splitAudio", param, inFile, outFile)

def actionMergeAudio(inFile, outFile, param):
    return buildCmd("mergeAudio", param, inFile, outFile)

def actionCut(inFile, outFile, param):
    # videoCut
    return buildCmd("videoCut", param, inFile, outFile)

def actionCut_a(inFile, outFile, param):
    # videoCut
    return buildCmd("videoCut_a", param, inFile, outFile)

def actionRotate(inFile, outFile, param):
    return buildCmd("videoRotate", param, inFile, outFile)

def actionFormat(inFile, outFile, param):
    return buildCmd("outputFormat", [], inFile, outFile)

def actionScale(inFile, outFile, param):
    return buildCmd("videoScale", param, inFile, outFile)

def actionCameraMove(inFile, outFile, param):
    return buildCmd("cameraMove", param, inFile, outFile)

def actionRmShaky(inFile, outFile, param):
    return buildCmd("rmShaky", [], inFile, outFile)

def actionSpeed(inFile, outFile, param):
    return buildCmd("videoSpeed", param, inFile, outFile);

def actionImgOnVideo(inFile, outFile, param):
    return buildCmd("PIP_imgOnVideo", param, inFile, outFile)

def actionVideoOnImg(inFile, outFile, param):
    return buildCmd("PIP_videoOnImg", param, inFile, outFile)

def actionVideoEndOnImg(inFile, outFile, param):
    return buildCmd("videoEndToOneImg", param, inFile, outFile)

def actionFade(inFile, outFile, param):
    return buildCmd("videoFade", param, inFile, outFile)

def actionLogo(inFile, outFile, param):
    return buildCmd("videoLogo", param, inFile, outFile)

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
        isCutWithAudio = False
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

                # get audio from file
                muteAduioFile = finalOutputFile
                isCutWithAudio = True

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
                isCutWithAudio = False

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
                isCutWithAudio = True

            if 'format' == cmd:
                param = action["parameter"]

                # outputFormat
                outputFile = ouputFolder + "/clip_"+str(nClip)+"_mp4format.mp4"
                actionList.append(buildCmd("outputFormat", [], finalOutputFile, outputFile))
                finalOutputFile = outputFile

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
                # param[2] = param[1] + param[2]
                outputFile = ouputFolder + "/clip_"+str(nClip)+"_pic_"+str(nAction)+".mp4"
                actionList.append(buildCmd("PIP_imgOnVideo", param, finalOutputFile, outputFile))
                finalOutputFile = outputFile

            if 'fade_inout' == cmd:
                param = action["parameter"]

                outputFile = ouputFolder + "/clip_"+str(nClip)+"_fade_"+str(nAction)+".mp4"
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
            if checkVideoMute(file) or not isCutWithAudio:
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
                

def checkVideoMute(file):
    item_list = None
    cmd = '%s -i "%s"' % (os.path.join(os.path.abspath('.'), 'bin','ffmpeg.exe'),file)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    p.wait()
    item_list = p.stdout.read().splitlines()

    for i in range(len(item_list)):
        try:
            item = item_list[i].decode('utf-8')
        except:
            item = str(item_list[i])

        if "Audio" in item:
            return False
    return True

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
        print(os.path.basename(audioFile))
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
    # parseStrategy("G:/视频剪辑/2017-07-08-财政局/切片目录/特写相机/集锦/strategy.json")
    # handleAutoEdit("G:/视频剪辑/2017-07-08-财政局/切片目录/特写相机/集锦/strategy.json")
    parseStrategy_new("H:/2017-05-27-延河杯 延八 延九/等级3/[2上半场0.08.22][等级3][进球]/strategy.json")
    handleAutoEdit_new("H:/2017-05-27-延河杯 延八 延九/等级3/[2上半场0.08.22][等级3][进球]/strategy.json")
    # addMusic("H:/八喜/strategy.json")
    # test()
    # print(checkVideoMute("H:/auto_tool_test/output/"))

