#! /usr/bin/python3
# -*- coding: utf-8 -*-

from softwareСopyData.CopyTime import CopyTime

class DataСopyTime(CopyTime):
    
    def __init__(self):
        super().__init__()
        self.conf = {}

    def save(self,dataScan):
        FJC = self.jsonFileCopy()
        print(FJC) 
        for scan in dataScan:
            self.conf[scan] = dataScan[scan]
        return self.conf
    

       
        