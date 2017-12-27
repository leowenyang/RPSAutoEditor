#! /usr/bin/python
# -*- coding: utf-8 -*-

import grpc

# import wxrpcauth_pb2
import client.wxrpcauth_pb2 as wxrpcauth_pb2
from client.wxlogin_client import *
from client.taskqueue.taskqueue import Queue, Task
import os
import json

from pkg_resources import *

from time import time, sleep

class AEClient(object):
  """docstring for AEClient"""
  def __init__(self, parent, host):
    super(AEClient, self).__init__()
    self.parentWin = parent
    self.port = '1337'
    self.host = host
    # new threads
    self.queue = Queue(workers=1)
    # http connect
    try:
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.port))
        self.stub = wxrpcauth_pb2.wxAuthStub(self.channel)
    except Exception as e:
        print("RPC error")
        raise e

  def callAutoEditor(self, file):
    try:
        response = self.stub.CallAutoEditor(wxrpcauth_pb2.AuthRequest(name=file))
        print(eval(response.message))
        # self.parentWin.refresh_task_status_completed(response.message)
    except Exception as e:
        print("===========gRPC error=============")
        # self.parentWin.refresh_status_bar("无法连接到服务器，请检查服务器是否启动！")
        raise

  def run(self, file):
    # threading is stop, new one
    if self.queue.dying:
        self.queue = Queue(workers=1)

    try:
        return self.queue.add(self.callAutoEditor, file)
    except Exception as e:
        raise e;

  def cancelWaiting(self, file):
    return self.queue.cancelTask(self.callAutoEditor, file)

  def waitFinished(self):
    for task in self.queue.finished:
        print (task.result)

class wxClient(object):
    """docstring for wxClient"""
    def __init__(self, host):
        super(wxClient, self).__init__()
        self.port = '1338'

        # http connect
        try:
            self.channel = grpc.insecure_channel('{}:{}'.format(host, self.port))
            self.stub = wxrpcauth_pb2.wxAuthStub(self.channel)
        except Exception as e:
            raise e

    def checkVersion(self, version):
        response = self.stub.checkClientVersion(wxrpcauth_pb2.AuthRequest(name=version))
        if response.message == "OK":
            return "OK"
        else:
            return response.message

    def checkVersion_2(self, version):
        response = self.stub.checkClient2Version(wxrpcauth_pb2.AuthRequest(name=version))
        if response.message == "OK":
            return "OK"
        else:
            return response.message

    def checkWxUser(self):
        response = self.stub.getWxBotKey(wxrpcauth_pb2.AuthRequest(name=''))
        # print(response.message)
        with open('yiball123.pkl','wb') as f:
           f.write(response.message)

        # wxBotID = getWxBotID('yiball123.pkl')
        # response = self.stub.checkWxBot(wxrpcauth_pb2.AuthRequest(name=wxBotID))
        # return response.message

        wxBotMsg = getWxBotMsg('yiball123.pkl')
        response = self.stub.checkWxBot(wxrpcauth_pb2.AuthRequest(name=wxBotMsg[0]))
        return wxBotMsg[1], response.message

	
if __name__ == '__main__':
    client = AEClient('127.0.0.1')
    client.callAutoEditor("G:/视频剪辑/等级3/PIC_0035_进球/strategy.json")
    # print("first one")
    # sleep(10)
    # client.run("G:/视频剪辑/等级3/PIC_0038_射门/strategy.json")
    # print("second one")
    # client = wxClient('127.0.0.1')
    # print(client.checkWxUser())
    # print(client.checkVersion("1.01"))