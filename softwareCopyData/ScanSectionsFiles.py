#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os
import os.path
import sys
from softwareCopyData.Directories import Directories
from softwareCopyData.Debug import Debug
from softwareCopyData.WorkingSectionsFiles import WorkingSectionsFiles
# from softwareCopyData.CopyTime import CopyTime
from softwareCopyData.DataСopyTime import DataСopyTime
from softwareCopyData.Dump import Dump

class ScanSectionsFiles(Directories,Debug,WorkingSectionsFiles,DataСopyTime,Dump):
    
    def __init__(self):
        super().__init__()
        Dump.__init__(self)
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
        # print("arrDataSectionsFiles", arrDataSectionsFiles)
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
                        PERIOD = self.toNumberFloat(self.executionPeriod["value"])
                        WRITE_STRING = "\n\n количество файлов:{} file в байтах: {} размер файла: {} {} время копирования: {} {} \n"
                        sys.stdout.write(WRITE_STRING.format(self.iterProgres,self.fileSizeOut,RNUMBER,resultFileOutRazmer["type"],PERIOD,self.executionPeriod["type"]))
                        sys.stdout.flush()
                        self.conf = self.save({
                          "iterProgres":self.iterProgres,
                          "fileSizeOut":self.fileSizeOut,
                          "rnumber":RNUMBER,
                          "resultFileOutRazmerType":resultFileOutRazmer["type"],
                          "executionPeriodValue":PERIOD,
                          "executionPeriodType":self.executionPeriod["type"]
                        })

                    if typeDirStatus == True:
                        self.scanSectFles(pathSection)
                        
                else:
                    print("Пропускаем - найдено соответсвие: {}".format(matchFound))

                  
    def saveConf(self):
        return self.saveDataFileJson()  

    def dumpBasa(self):
        return self.mysqlDump(self.basaDumpPuth)
    
    def listDir(self,path = ""):
        if path !="":
            return os.listdir(path)
        else:
            return os.listdir(self.path_first)
        
if __name__ == "__main__":
    # OBJCSF = ScanSectionsFiles()
    # OBJCSF.scanSectFles()
    print(sys.path)
    