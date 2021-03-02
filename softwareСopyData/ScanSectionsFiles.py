#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os
import os.path
import sys
from softwareСopyData.Directories import Directories
from softwareСopyData.Debug import Debug
from softwareСopyData.WorkingSectionsFiles import WorkingSectionsFiles
# from softwareСopyData.CopyTime import CopyTime
from softwareСopyData.DataСopyTime import DataСopyTime

class ScanSectionsFiles(Directories,Debug,WorkingSectionsFiles,DataСopyTime):
    
    def __init__(self):
        super().__init__()
        self.conf = {}
        self.iterProgres = 0
        self.fileSizeOut = 0
        self.rauri = ""
        self.timeUnix = self.curentCtime()
        self.timeData = self.curentDate()
        self.timeUnixLast = 0
        self.timeDataLast = 0
        self.executionPeriod = 0
        # self.path_first = Directories.FIRST
        # self.path_last = Directories.LAST
        
    
    def razdelitelUrl(self):
        self.rauri = ""
        if int(self.windows()) == 1:
            self.rauri = "{}\\{}"
        elif int(self.linux()) == 1:
            self.rauri = "{}/{}"
        return self.rauri
        
    
    def scanSectFles(self,path = ""):
        self.razdelitelUrl()
        # print("excFolder ",self.excFolder)
        # self.excFolder.count(5)
        
        pathSection = ""
        if path !="":
            arrDataSectionsFiles = self.listDir(path)
        else:
            arrDataSectionsFiles = self.listDir()
        print("arrDataSectionsFiles", arrDataSectionsFiles)
        for section in arrDataSectionsFiles:
            # print(" path_last ", self.path_last)
            if section != "":
                if path !="":
                    pathSection = self.rauri.format(path,section)
                else:
                    pathSection = self.rauri.format(self.path_first,section)
                
                matchFound = self.excFolder.count(pathSection)
                # print(self.excFolder)
                # print("matchFound ",matchFound," pathSection "+pathSection)
                
                if matchFound == 0:
                    self.iterProgres +=1
                    
                    pathSectionLast = pathSection.replace(self.path_first,self.path_last)
                    typeDirStatus = self.isdir(pathSection)
                    typeFileStatus = self.isfile(pathSection)
                    self.DirectoryFileStatus(typeDirStatus, typeFileStatus,pathSectionLast)
                    if typeFileStatus == True:
                        self.copyFile(pathSection,pathSectionLast)
                    
                    # print("first pathSection ",pathSection)
                    # print("pathSectionLast ",pathSectionLast)
                    self.fileSizeOut = self.fileSizeOut+self.getSize(pathSectionLast)
                    resultFileOutRazmer = self.razmerFile(self.fileSizeOut)
                    if len(resultFileOutRazmer) > 0:
                        RNUMBER = self.toNumberFloat(resultFileOutRazmer["value"])
                        self.timeUnixLast = self.curentCtime()
                        self.timeDataLast = self.curentDate()
                        self.executionPeriod = self.periodDataCopy(self.timeUnix,self.timeUnixLast)

                        sys.stdout.write("\n\n количество файлов:{} file в байтах: {} размер файла: {} {} время копирования: {} {} \n".format(self.iterProgres,self.fileSizeOut,RNUMBER,resultFileOutRazmer["type"],self.executionPeriod["value"],self.executionPeriod["type"]))
                        # sys.stdout.write("\n time first: {} time last: {} \n".format(self.timeUnix,self.timeUnixLast))
                        # sys.stdout.write("\n date first: {} date last: {} \n".format(self.timeData,self.timeDataLast))
                        # sys.stdout.write("\n executionPeriod: {} {} \n".format(self.executionPeriod["value"],self.executionPeriod["type"]))
                        sys.stdout.flush()
                        self.conf = self.save({
                          "iterProgres":self.iterProgres,
                          "fileSizeOut":self.fileSizeOut,
                          "rnumber":RNUMBER,
                          "resultFileOutRazmerType":resultFileOutRazmer["type"],
                          "executionPeriodValue":self.executionPeriod["value"],
                          "executionPeriodType":self.executionPeriod["type"]
                        })

                    if typeDirStatus == True:
                        self.scanSectFles(pathSection)
                        
                    # print("pathSection ",pathSection)
                else:
                    print("Пропускаем - найдено соответсвие: {}".format(matchFound))

                    
                    
    def saveConf(self):
        return self.conf       
    
    def listDir(self,path = ""):
        if path !="":
            return os.listdir(path)
        else:
            return os.listdir(self.path_first)
        
if __name__ == "__main__":
    # OBJCSF = ScanSectionsFiles()
    # OBJCSF.scanSectFles()
    print(sys.path)
    