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
  def __init__(self, host):
    super(AEClient, self).__init__()
    self.port = '1337'
    self.host = host
    # new threads
    self.queue = Queue(workers=1)
    # http connect
    try:
        channel = grpc.insecure_channel('{}:{}'.format(self.host, self.port))
        self.stub = wxrpcauth_pb2.wxAuthStub(channel)
    except Exception as e:
        print("RPC error")
        raise e

  def callAutoEditor(self, file):
    response = self.stub.CallAutoEditor(wxrpcauth_pb2.AuthRequest(name=file))
    print(response.message)
    a,b = os.path.split(response.message)
    tasks = []
    task_status_json = os.path.join(os.path.abspath('.'), "task_status.json")
    if(os.path.exists(task_status_json)):
        with open(task_status_json, encoding='utf-8') as f:
            tasks = json.load(f)
            f.close()
    for t in tasks:
        if(a in t['task'] and b in t['task'] and t['status'] == '已提交'):
            t['status'] = '已完成'
            break

    with open(task_status_json, "w", encoding = 'utf-8') as f:
        f.write(json.dumps(tasks, ensure_ascii = False, indent = 4))
        f.close()

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
            channel = grpc.insecure_channel('{}:{}'.format(host, self.port))
            self.stub = wxrpcauth_pb2.wxAuthStub(channel)
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

        wxBotID = getWxBotID('yiball123.pkl')
        response = self.stub.checkWxBot(wxrpcauth_pb2.AuthRequest(name=wxBotID))
        return response.message

	
if __name__ == '__main__':
    client = AEClient('127.0.0.1')
    client.callAutoEditor("G:/视频剪辑/等级3/PIC_0035_进球/strategy.json")
    # print("first one")
    # sleep(10)
    # client.run("G:/视频剪辑/等级3/PIC_0038_射门/strategy.json")
    # print("second one")
    # client = wxClient('127.0.0.1')
    # # print(client.checkWxUser())
    # print(client.checkVersion("1.01"))