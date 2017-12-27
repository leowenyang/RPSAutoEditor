#! /usr/bin/python
# -*- coding: utf-8 -*-

from wxpy import *

def getWxBotID(file):
    robot = Bot()
    robot.enable_puid(file)
    return robot.self.puid

def getWxBotMsg(file):
    robot = Bot()
    robot.enable_puid(file)
    return robot.self.puid, robot.self.nick_name

def main():
    pass
    # getWxBotID('yiball.pkl')

if __name__ == '__main__':
    main()
