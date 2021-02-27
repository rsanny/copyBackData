#! /usr/bin/python3
# -*- coding: utf-8 -*-

# from scanSectionsFiles.ScanSectionsFiles import ScanSectionsFiles
import shutil

class CopySectionsFiles:
    
    def __init__(self):
        super().__init__()
        
    def copy_file(self,path,pathtu):
        if path !="" and pathtu !="":
            return shutil.copy(path, pathtu)  
        