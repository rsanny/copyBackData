#! /usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess

class Dump:
    
    USER_NAME = "root"
    USER_PASSWORD = "robotsanny"
    HOST = "localhost"
    NAME_BASE = "db_test2"
    MYSQL_SHEMA = "mysqldump -u {} -p{} -h {} {} > {}"

    def __init__(self):
        self.nameBase = Dump.NAME_BASE
        self.useName = Dump.USER_NAME
        self.userPassword = Dump.USER_PASSWORD
        self.hosts = Dump.HOST
        self.mysqlShema = Dump.MYSQL_SHEMA 

    def fileNameBaseSql(self,path = ""):
        if path !="":
            return "{}/{}.sql".format(path,self.nameBase)
        else:
            return False

    def mysqlDump(self,path):
        self.fileNameBase = self.fileNameBaseSql(path)
        stringZapros = self.mysqlShema.format(self.useName,self.userPassword,self.hosts,self.nameBase,self.fileNameBase)
        subprocess.call(stringZapros, shell=True)
        if self.fileNameBase != False:
            return subprocess.call(stringZapros, shell=True)
        return False

if __name__ == "__main__":
    ObjDump = Dump()
