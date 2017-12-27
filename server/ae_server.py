#! /usr/bin/python
# -*- coding: utf-8 -*-

import time
from concurrent import futures
from pkg_resources import *

import grpc

import wxrpcauth_pb2

from handleAutoEdit import *
import json

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

SERVER_VERSION = "1.0.32"

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
                resultDict['info'] = []
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


class wxClient(object):
    """docstring for wxClient"""
    def __init__(self, host):
        super(wxClient, self).__init__()
        self.port = '1338'

        # http connect
        try:
            channel = grpc.insecure_channel('{}:{}'.format(host, self.port))
            self.stub = wxrpcauth_pb2.wxAuthStub(channel)
        except Exception as e:
            print(e)
            input('无法连接到验证服务器，请联系开发人员，按回车键退出。。。')
            return

    def checkVersion(self, version):
        response = self.stub.checkServerVersion(wxrpcauth_pb2.AuthRequest(name=version))
        if response.message == "OK":
            return "OK"
        else:
            return response.message

    def callAutoEditor(self, file):
        try:
            response = self.stub.CallAutoEditor(wxrpcauth_pb2.AuthRequest(name=file))
            print(eval(response.message))
            # self.parentWin.refresh_task_status_completed(response.message)
        except Exception as e:
            print("===========gRPC error=============")
            # self.parentWin.refresh_status_bar("无法连接到服务器，请检查服务器是否启动！")
            raise


def main():
    # get IP
    with open("config.conf", encoding='utf-8') as f:
        json_object = json.load(f)
        authIP = json_object['authIP']

    # check verison
    client = wxClient(authIP)
    result = client.checkVersion(SERVER_VERSION)
    if "OK" == result:
        serve()
    else:
        tips= "ERROR!!! Please upgrade program to %s" % result
        input(tips)

    
def serve():
    port = '1337'
    
    try:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
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
    main()
