#! /usr/bin/python
# -*- coding: utf-8 -*-

import time
import requests
import traceback
import argparse
from concurrent import futures
from pkg_resources import *

import grpc

import wxrpcauth_pb2

from handleAutoEdit import *
import json

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
YUN_ADMIN_SERVER_URL = 'http://180.76.189.114:4545'

SERVER_VERSION = "2.01.02"
SERVER_NAME = "ae_server"
SERVER_KEY  = "yiballserver"
SERVER_DESCRIPTION = '''
*************************
*    忆球云剪辑服务器    *
*************************
'''

def postByCurl(url, data):
    try:
        output = requests.post(url, data)
        return output.text
    except Exception as e:
        print(e)
        print(traceback.format_exec())

def getToolsVersion(name, version):
    url = YUN_ADMIN_SERVER_URL+'/yunadmin/toolsversion/checkversion'
    data = {"name": name, "version": version}
    output = postByCurl(url, data)
    return json.loads(output)

def save2File(file, content):
    with open(file, "a", encoding='utf-8') as f:
        f.write(content)
        f.close()

class ServerServicer(wxrpcauth_pb2.wxAuthServicer):

    def CallAutoEditor(self, request, context):
        file = request.name
        resultDict = {}
        resultDict['task'] = file
        # start
        content = "%s %s START\n" % (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), request.name)
        save2File("log.txt", content)
        result = parseStrategy_new(file)
        print("handle strategy file", result)
        if len(result) == 0:
            aeScript = diffAutoEditFile_new(file)
            print(aeScript)
            if (handleAutoEdit_new(aeScript) == 0):
                addMusic(file)
                resultDict['result'] = 'OK'
                resultDict['info'] = []
            else:
                resultDict['result'] = 'NOK'
                resultDict['info'] = ['ffmpeg command run error']
        else:
            noFoundFile = {}
            if len(result[0]) == 0:
                noFoundFile['nofile'] = ['some file no found']
            else:
                noFoundFile['nofile'] = result
            resultDict['result'] = 'NOK'
            resultDict['info'] = noFoundFile
        # end
        content = "%s %s END\n" % (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), file)
        save2File("log.txt", content)
        # return wxrpcauth_pb2.AuthReply(message=request.name)
        return wxrpcauth_pb2.AuthReply(message=str(resultDict))

    def runAEScript(self, request, context):
        file = request.name
        resultDict = {}
        resultDict['task'] = file

        if (handleAutoEdit_new(file) == 0):
            resultDict['result'] = 'OK'
            resultDict['info'] = []
        else:
            resultDict['result'] = 'NOK'
            resultDict['info'] = []

        return wxrpcauth_pb2.AuthReply(message=str(resultDict))

    def connectServer(self, host, port, file, idType):
        try:
            channel = grpc.insecure_channel('{}:{}'.format(host, port))
            stub = wxrpcauth_pb2.wxAuthStub(channel)
            response = stub.runAEScript(wxrpcauth_pb2.AuthRequest(name=file))
            print(eval(response.message))
        except Exception as e:
            print(e)
            input('无法连接到验证服务器，请联系开发人员，按回车键退出。。。')
            return

def usage():
    parser = argparse.ArgumentParser(description=SERVER_DESCRIPTION)
    parser.add_argument("--version", help='显示版本信息', action="store_true")
    args = parser.parse_args()
    if args.version:
        print(SERVER_VERSION)
        return
    print(SERVER_DESCRIPTION)
    main()

def main():
    result = getToolsVersion(SERVER_NAME, SERVER_VERSION)
    if result['success']:
        if (SERVER_KEY == result['data']):
            serve()
        else:
            tips= "ERROR!!! your tools is valid, pls ask for yiball"
            input(tips)
    else:
        tips= "ERROR!!! message is  %s" % result['message']
        input(tips)

def serve():
    port = '1337'

    try:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
        wxrpcauth_pb2.add_wxAuthServicer_to_server(ServerServicer(), server)
        server.add_insecure_port('[::]:'+port)
        server.start()
    except Exception as e:
        print(e)
        input('无法连接到验证服务器，请联系开发人员，按回车键退出。。。')
        return

    print('current version is %s' %(SERVER_VERSION))
    print('AE server is running ...')

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
       server.stop(0)

if __name__ == '__main__':
    usage()
