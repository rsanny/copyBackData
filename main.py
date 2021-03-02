#! /usr/bin/python3
# -*- coding: utf-8 -*-

from softwareСopyData.ScanSectionsFiles import ScanSectionsFiles

if __name__ == "__main__":
    # print(sys.path)
    OBJCSF = ScanSectionsFiles()
    OBJCSF.scanSectFles()
    conf = OBJCSF.saveConf()
    print(conf)