# -*- coding: utf-8 -*-
import os
import json
import sys
import shutil
import time
import subprocess
import zipfile
import traceback
import requests
import urllib.request

UPGRADE_PROGRAM_NAME = "ae_server.exe"
YUN_ADMIN_SERVER_URL = "http://180.76.189.114:4545"
URL_DOWNLOAD_UPGRADE = "//Yiball-server/忆球工具/自动化剪辑工具/剪辑服务器/升级包"
SERVER_NAME = "ae_server"

class YiballRemoteTool:
    def __init__(self):
        self.name = SERVER_NAME
        self.version = '2.00.00'
        self.timeout = 5
        self.percent = 0

    def get_current_version(self):
        result = None
        cmd = '%s --version' % (os.path.join(os.path.abspath('.'),UPGRADE_PROGRAM_NAME))
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        p.wait()
        result = p.stdout.read().splitlines()
        self.version = result[0].decode('utf-8')

    def check_version(self):
        r = {}
        r['success'] = False
        r['new_version'] = None
        try:
            self.get_current_version()

            url = YUN_ADMIN_SERVER_URL+'/yunadmin/toolsversion/checkversion'
            quest_filter = {"name": self.name, "version": self.version}
            f = requests.post(url, data=quest_filter, timeout=self.timeout)
            result = json.loads(f.text)
            if('success' in result.keys() and result['success'] != None):
                if(result['success'] == True):
                    r['success'] = True
                else:
                    r['success'] = False
                    if('message' in result.keys() and result['message'] != None):
                        m = result['message']
                        r['new_version'] = m[m.rfind(' ')+1:]
        except:
            print("check_version throw exception.")
            print(traceback.format_exc())
        return r

    def report(self, count, blockSize, totalSize):
        try:
            percent = int(count*blockSize*100/totalSize)
            if(percent - self.percent >= 10 or percent >= 100):
                print('已下载 %d%%...' % percent)
                self.percent = percent
        except:
            print(traceback.format_exc())

    def download_upgrade_package(self, version):
        try:
            upgrade_package = os.path.join(URL_DOWNLOAD_UPGRADE, ('%s.zip' % version))
            local_package = os.path.join('.', 'upgrade.zip')
            print("当前版本号：" + self.version)
            print("最新版本号：" + version)
            print(upgrade_package)
            if(not os.path.exists(upgrade_package)):
                print('请联系开发人员上传最新版本软件')
                return False
            print("发现新版本，正在下载...")
            shutil.copy(upgrade_package, local_package)
        except Exception as err:
            print('下载升级包失败，请手动下载完整客户端！')
            return False
        return True

    def extract_package(self, version):
        try:
            local_package = os.path.join('.', 'upgrade.zip')
            extract_path = os.path.abspath('.')
            if(zipfile.is_zipfile(local_package)):
                fz = zipfile.ZipFile(local_package,'r')
                for file in fz.namelist():
                    fz.extract(file,extract_path)
            return True
        except Exception as err:
            print(err)
            return False
        return True



if __name__=="__main__":
    y = YiballRemoteTool()
    result = y.check_version()
    if(result['success']):
        os.system(UPGRADE_PROGRAM_NAME)
    else:
        if(result['new_version'] == None):
            input('无法获取服务器版本信息，按回车键退出...')
        else:
            print('发现新版本，开始下载...')
            if(y.download_upgrade_package(result['new_version'])):
                if(y.extract_package(result['new_version'])):
                    print("更新完毕，将会启动新版本！")
                    os.system(UPGRADE_PROGRAM_NAME)
                else:
                    input('解压新版本失败，请重试...')
            else:
                input('新版本下载失败，请重试...')
    sys.exit()
