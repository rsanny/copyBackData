#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import platform

class Platform(object):
    
    NAME_WINDOWS = "Windows"
    NAME_MAC = "Darwin"
    NAME_LINUX = "Linux"
    
    def __init__(self):
        self.linux_type = Platform.NAME_LINUX
        self.windows_type = Platform.NAME_WINDOWS
        self.mac_type = Platform.NAME_MAC
    
    def type_platform(self):
        return platform.system()
    
    def windows(self):
        typePlatform = self.type_platform()
        if typePlatform == self.windows_type: 
            return 1
        return 0
    
    def linux(self):
        typePlatform = self.type_platform()
        if typePlatform == self.linux_type: 
            return 1
        return 0
    
    def mac(self):
        typePlatform = self.type_platform()
        if typePlatform == self.mac_type: 
            return 1
        return 0
        
if __name__ == "__main__":
    OPP = Platform()
    tp = OPP.windows();
    print(tp)  