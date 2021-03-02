#! /usr/bin/python3
# -*- coding: utf-8 -*-

import json
import os
import sys

class ReadSettingsFile:
    
    fileSettings = "settings.json"
    fileCopyTime = "dataСopyTime.json"
    attrWin = "windows"
    attrLin = "linux"
    
    def __init__(self):
        self.redpath = ""
        self.fileSettings = ReadSettingsFile.fileSettings
        self.fileCopyTime = ReadSettingsFile.fileCopyTime
        self.win = ""
        self.lin = ""
        self.fileJsonData = {};
    
    def readJson(self):
        file = self.jsonFile()
        with open(file) as dFile:
            data = json.load(dFile)
        self.readJsonList(data)
        return self.fileJsonData;
    
    def readJsonList(self,data):
        if int(self.win) == 1:
            self.fileJsonData =  data[ReadSettingsFile.attrWin]
        elif int(self.lin) == 1:
            self.fileJsonData = data[ReadSettingsFile.attrLin]
        return self.fileJsonData
        
    
    def rUrl(self,win,lin):
        self.win = win
        self.lin = lin
        self.redpath = ""
        if int(win) == 1:
            self.redpath = "{}\\{}"
        elif int(lin) == 1:
            self.redpath = "{}/{}"
        return self.redpath
    
    def jsonFile(self):
        pathname = os.path.dirname(sys.argv[0])
        path = self.redpath.format(pathname,self.fileSettings)
        return path
    
    def jsonFileCopy(self):
        pathname = os.path.dirname(sys.argv[0])
        path = self.redpath.format(pathname,self.fileCopyTime)
        return path
    
    
if __name__ == "__main__":
   ReadOb = ReadSettingsFile() 
   print(os.getcwd())
        