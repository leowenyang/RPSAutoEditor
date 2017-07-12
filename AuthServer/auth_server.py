#! /usr/bin/python
# -*- coding: utf-8 -*-

import time
from concurrent import futures
from pkg_resources import *

import grpc

import wxrpcauth_pb2

from wxlogin import *
import json

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

AUTHSERVER_VERSION = "1.0.0"
CLIENT_VERSION = ""
CLIENT2_VERSION = ""
SERVER_VERSION = ""
# get version
with open("config.conf", encoding='utf-8') as f:
    json_object = json.load(f)
    CLIENT_VERSION = json_object['clientVersion']
    CLIENT2_VERSION = json_object['client2Version']
    SERVER_VERSION = json_object['serverVersion']


class ServerServicer(wxrpcauth_pb2.wxAuthServicer):

    def checkClientVersion(self, request, context):
        if request.name == CLIENT_VERSION:
            return wxrpcauth_pb2.AuthReply(message="OK")
        return wxrpcauth_pb2.AuthReply(message=CLIENT_VERSION)

    def checkClient2Version(self, request, context):
        if request.name == CLIENT2_VERSION:
            return wxrpcauth_pb2.AuthReply(message="OK")
        return wxrpcauth_pb2.AuthReply(message=CLIENT2_VERSION)

    def checkServerVersion(self, request, context):
        if request.name == SERVER_VERSION:
            return wxrpcauth_pb2.AuthReply(message="OK")
        return wxrpcauth_pb2.AuthReply(message=SERVER_VERSION)

    def getWxBotKey(self, request, context):
        wxBotInfo = getWxBotKey('yiball.pkl')
        return wxrpcauth_pb2.ByteReplay(message=wxBotInfo)

    def checkWxBot(self, request, context):
        if isValidMember(request.name):
            return wxrpcauth_pb2.AuthReply(message="OK")
        return wxrpcauth_pb2.AuthReply(message="NOK") 

    def wxRPCAuth(self, request, context):
        return wxrpcauth_pb2.AuthReply(message="OK")


def main():
    port = '1338'

    with open('server.key') as f:
        private_key = bytes(f.read(), encoding = "utf8")
        print(private_key)
    with open('server.crt') as f:
        certificate_chain = bytes(f.read(), encoding = "utf8")
        print(certificate_chain)

    server_credentials = grpc.ssl_server_credentials(
      ((private_key, certificate_chain,),))

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    wxrpcauth_pb2.add_wxAuthServicer_to_server(ServerServicer(), server)

    server.add_secure_port('[::]:'+port, server_credentials)


    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        pass
    server.stop(0)
	
def serve():
    port = '1338'


    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    wxrpcauth_pb2.add_wxAuthServicer_to_server(ServerServicer(), server)
    server.add_insecure_port('[::]:'+port)
    server.start()

    print('current version is %s' %(AUTHSERVER_VERSION))
    print('Auth server is running ...')

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
       server.stop(0)

if __name__ == '__main__':
    serve()
