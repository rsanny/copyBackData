#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import os.path
from softwareCopyData.CopySectionsFiles import CopySectionsFiles

class WorkingSectionsFiles(CopySectionsFiles):
    
    def __init__(self):
        pass
    
    def create_dir(self,path):
        if path !="":
            return os.mkdir(path)
            # try:
            #     return os.mkdir(path)
            # except FileNotFoundError:
            #     return False
        else:
            return False
        
    def isfile(self,path):
        if path !="":
            return os.path.isfile(path)
        else:
            return False
        
    def isdir(self,path):
        if path !="":
            return os.path.isdir(path)
        else:
            return False
        
    def exists(self,path):
        if path !="":
            return os.path.exists(path)
        else:
            return False
        
    def getSize(self,file):
        if file !="":
            return os.path.getsize(file)
        else:
            return False

    def dirFile(self,dirstatus,filestatus):
        if dirstatus == True:
            return "dir"
        elif dirstatus == False and filestatus == True:
            return "file"
        return False
        
    def DirectoryFileStatus(self,dirstatus,filestatus,path):
        if dirstatus !="" and filestatus !="" and path !="":
            pathExit = self.exists(path)
            sdirfile = self.dirFile(dirstatus,filestatus)
            if sdirfile == "dir" and pathExit == False:
                return self.create_dir(path)
        return False
    
    def fileSizeCheck(self,fileActual,fileCopied):
        sizeFileActual = self.getSize(fileActual)
        sizeFileCopied = self.getSize(fileCopied)
        if sizeFileActual == sizeFileCopied:
            return True
        elif sizeFileActual != sizeFileCopied:
            return False
        
    def copyFile(self,path,pathtu):
        
        # print(" path Actual ",path)
        # print(" pathtu Copied ",pathtu)
            
        path_status = self.isfile(path)
        pathtu_status = self.exists(pathtu)
        
        # basename = os.path.basename(path)
        # basename_pathtu = "{}\\{}".format(pathtu,basename)
        # basename_pathtu_status = self.exists(basename_pathtu)
        
        # print(" basename ",basename)
        # print(" basename_pathtu ",basename_pathtu)
        
        # self.fileSizeCheck(path,basename_pathtu)       
        if path_status == True and pathtu_status == False:
            return self.copy_file(path,pathtu)
        elif path_status == True and pathtu_status == True:
            statusFileSize = self.fileSizeCheck(path,pathtu)  
            # print(" statusFileSize ",statusFileSize)
            if statusFileSize == False:
                return self.copy_file(path,pathtu)
            
    def razmerFile(self,number):
        kof = 1024
        resultObj = {}
        numberRazmer = number
        if numberRazmer > kof:
            numberRazmer = (numberRazmer/kof)
            if numberRazmer > kof:
                numberRazmer = (numberRazmer/kof)
                if numberRazmer > kof:
                    numberRazmer = (numberRazmer/kof)
                    resultObj = {
                        "value":numberRazmer,
                        "type":"GB"
                    }
                else:
                    resultObj = {
                        "value":numberRazmer,
                        "type":"MB"
                    }
            else:
                resultObj = {
                        "value":numberRazmer,
                        "type":"KB"
                    }      
        return resultObj
    
    def toNumberFloat(self,number):
        default = 100
        rnumber = 0
        if number > 0:
            rnumber = int(number*default)/default
        return rnumber
    
    def writeFile(self,file,data):
        try:
            fileJson = open(file, 'w')
            fileJson.write(data)
            fileJson.close()
            return True;
        except:
            return False;
        
            
            
        