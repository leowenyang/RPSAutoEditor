#! /usr/bin/python
# -*- coding: utf-8 -*-

from client.ae_client import AEClient, wxClient

	
# client = AEClient('127.0.0.1')
# client.callAutoEditor("//Yiball-server/延十八比赛/等级3/[2上半场0.01.34][等级3][进球]/strategy.json")
# client.run("G:/视频剪辑/等级3/PIC_0032_进球/strategy.json")
# print("first one")
# # sleep(10)
# client.run("G:/视频剪辑/等级3/PIC_0038_射门/strategy.json")
# print("second one")

client = wxClient('127.0.0.1')
# client = wxClient('192.168.0.140')
print(client.checkWxUser())
print(client.checkVersion("1.0.2"))
client = AEClient('127.0.0.1')
client.callAutoEditor("//Yiball-server/延十八比赛/等级3/[2上半场0.01.34][等级3][进球]/strategy.json")