#! /usr/bin/python
# -*- coding: utf-8 -*-

from wxpy import *
from wxRPCAuthDB import *
import os

def isValidMember(wxBotID):
    authDB = AuthDb('wxRPCAuth.dll')
    return authDB.searchWxID(wxBotID)

def getWxBotKey(file):
    with open(file,'rb') as f:
       text = f.read()
    return text

def getWxBotID(file):
    robot = Bot()
    robot.enable_puid(file)
    return (robot.self.puid, robot.self.nick_name)
 

def wxBotReg(file):
    wxBotID, nickName = getWxBotID(file)
    authDB = AuthDb('wxRPCAuth.dll')
    if not authDB.searchWxID(wxBotID):
        authDB.newRecord(nickName, wxBotID)
    authDB.viewAuthDB()


def main():
    wxBotReg('yiball.pkl')

if __name__ == '__main__':
    main()
