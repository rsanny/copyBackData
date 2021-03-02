#! /usr/bin/python3
# -*- coding: utf-8 -*-

from softwareСopyData.Platform import Platform
from softwareСopyData.ReadSettingsFile import ReadSettingsFile

class Directories(Platform,ReadSettingsFile):
    
    FIRST = "C:\\data\\python-project\\2021\\filetest\\first\\02\\komi"
    LAST = "C:\\data\\python-project\\2021\\filetest\\result"
    
    FIRST_LINUX = "/mnt/server/home/eratadb/projects/komi-eratadb.ru/www"
    LAST_LINUX = "/home/webrobot/robotsanny/testTest"
    
    def __init__(self):
        super().__init__()
        # self.method_first()
        # self.method_last()
        # self.excFolder = self.excludingFoldersFiles()
        
        # ReadSettingsFile
        self.rUrl(self.windows(),self.linux())
        self.setJson = self.readJson()
        self.path_first = self.setJson["FIRST"]
        self.path_last  = self.setJson["LAST"]
        self.excFolder = self.setJson["EXCFOLDER"]

    def method_first(self):
        if int(self.windows()) == 1:
            self.path_first = Directories.FIRST
        elif int(self.linux()) == 1:
            self.path_first = Directories.FIRST_LINUX
        return self.path_first
    
    def method_last(self):
        if int(self.windows()) == 1:
            self.path_last = Directories.LAST
        elif int(self.linux()) == 1:
            self.path_last = Directories.LAST_LINUX
        return self.path_last
    
    def excludingFoldersFiles(self):
        if int(self.windows()) == 1:
            excFolder = [
                # "C:\\data\\backups\\esplus.ru\\2021\\02\\16\\all\\files\\bitrix",
                # "C:\\data\\backups\\erkc-dzr.ru\\2021\\02\\10\\files\\upload",
                # "C:\\data\\python-project\\2021\\filetest\\first\\komi3"
                ]
        elif int(self.linux()) == 1:
            excFolder = [
                # "/mnt/server/home/projects/ies-garant.dorr-bitt.ru/www/upload/form",
            ]
        return excFolder

    
if __name__ == "__main__":
    OP = Directories()
    tp = OP.method_first();
    print(tp) 
    ReadOb = ReadSettingsFile() 
    ReadOb.jsonFile()
    
    