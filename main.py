#! /usr/bin/python3
# -*- coding: utf-8 -*-

from softwareCopyData.ScanSectionsFiles import ScanSectionsFiles

if __name__ == "__main__":
    # print(sys.path)
    OBJCSF = ScanSectionsFiles()
    OBJCSF.scanSectFles()
    OBJCSF.saveConf()
    OBJCSF.dumpBasa()