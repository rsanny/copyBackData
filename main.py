#! /usr/bin/python3
# -*- coding: utf-8 -*-

from scanSectionsFiles.ScanSectionsFiles import ScanSectionsFiles
import sys

if __name__ == "__main__":
    # print(sys.path)
    OBJCSF = ScanSectionsFiles()
    OBJCSF.scanSectFles()