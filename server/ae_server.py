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

SERVER_VERSION = "1.0.4"

def save2File(file, content):
    with open(file, "a", encoding='utf-8') as f:
        f.write(content)
        f.close()

class ServerServicer(wxrpcauth_pb2.wxAuthServicer):

    def CallAutoEditor(self, request, context):
        # start
        content = "%s %s START\n" % (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), request.name)
        save2File("log.txt", content)
        parseStrategy(request.name)
        handleAutoEdit(request.name)
        addMusic(request.name)
        # end
        content = "%s %s END\n" % (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), request.name)
        save2File("log.txt", content)
        return wxrpcauth_pb2.AuthReply(message=request.name)

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
            raise e

    def checkVersion(self, version):
        response = self.stub.checkServerVersion(wxrpcauth_pb2.AuthRequest(name=version))
        if response.message == "OK":
            return "OK"
        else:
            return response.message


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

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    wxrpcauth_pb2.add_wxAuthServicer_to_server(ServerServicer(), server)
    server.add_insecure_port('[::]:'+port)
    server.start()
    print('current version is %s' %(SERVER_VERSION))
    print('AE server is running ...')
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
       server.stop(0)

if __name__ == '__main__':
    main()
