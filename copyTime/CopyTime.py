#! /usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import time

class CopyTime:
    
    def __init__(self):
        # self.timeUnix = self.curentCtime()
        # self.timeData = self.curentDate()
        pass
    
    def curentCtime(self):
        return datetime.datetime.now().timestamp()
    
    def curentTime(self):
        return time.time()
    
    def curentDate(self):
        return datetime.datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
    
    def periodCtime(self,valueTime):
        if valueTime > 0:
            return time.ctime(valueTime)
        return False
    
    def periodDataCopy(self,first,last):
        resultTime = 0; period = 0;
        if first > 0 and last >0 and (last >= first):
            resultTime = last - first 
        period = self.tuNumberFloat(resultTime)
        return self.formatTime(period)
        
        
    def tuNumberFloat(self,number):
        default = 100
        rnumber = 0
        if number > 0:
            rnumber = int(number*default)/default
        return rnumber
    
    def formatTime(self,curtime):
        kof = 60
        resultTimeObj = {}
        curtimeData = curtime
        if curtimeData > kof:
            curtimeData = (curtimeData/kof)
            if curtimeData > kof:
                curtimeData = (curtimeData/kof)
                resultTimeObj = {
                    "value":curtimeData,
                    "type":"часов"
                }
            else:
                resultTimeObj = {
                    "value":curtimeData,
                    "type":"минут"
                }
        else:
            resultTimeObj = {
                    "value":curtimeData,
                    "type":"секунд"
                }      
        return resultTimeObj
    


# import datetime
# import time

# print(dir(datetime.datetime))
# da = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S %s")
# print(da)

# 1601809091

# da = datetime.datetime.now().timestamp()
# print(int(da))

# 1601809091

# da = time.strftime("%Y-%m-%d %H-%M-%S %s")
# print(da)

# 1601809091
# s = 1599350400;
# print(s)
# da = time.ctime(s)
# print(da)

if __name__ == "__main__":
    CT = CopyTime()
    print(CT.curentCtime())
    print(CT.curentDate())
    