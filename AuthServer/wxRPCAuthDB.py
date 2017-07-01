#! /usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

class AuthDb(object):
    """docstring for AuthDb"""
    def __init__(self, db):
        super(AuthDb, self).__init__()
        self.db = db

    def createAuthDB(self):
        conn = sqlite3.connect(self.db)
        conn.execute('''CREATE TABLE COMPANY
               (ID INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,
               NICKNAME       TEXT  NOT NULL,
               WXID           TEXT  NOT NULL,
               ROLE           INT       NOT NULL,
               STATUS         INT       NOT NULL,
               POWER          INT);''')
        conn.close()
        print("Create database successfully")

    def newRecord(self, nickname, wxid, role=3):
        conn = sqlite3.connect(self.db)
        sql = "INSERT INTO COMPANY (NICKNAME,WXID,ROLE,STATUS) VALUES ('%s', '%s', %s, 1)" \
              % (nickname, wxid, role)
        conn.execute(sql)
        conn.commit()
        conn.close()
        print("New Record successfully")

    def updateRecord(self):
        conn = sqlite3.connect(self.db)
        conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
        conn.close()
        print("Update Record successfully")

    def viewAuthDB(self):
        conn = sqlite3.connect(self.db)
        cursor = conn.execute("SELECT * from COMPANY")
        for row in cursor:
           print(row)
        conn.close()
        print("View database successfully")

    def searchWxID(self, wxid):
        conn = sqlite3.connect(self.db)
        sql = "SELECT * from COMPANY WHERE WXID='%s'" % (wxid)
        cursor = conn.execute(sql)
        rows = cursor.fetchall()
        if len(rows) == 0:
            print ('WXID NOK')
            return False
        print ('WXID OK')
        return True
 

def main():
    authDB = AuthDb('wxRPCAuth.dll')
    authDB.createAuthDB()
    authDB.newRecord("leo", "288c6a60")
    authDB.viewAuthDB()
    authDB.searchWxID("288c6a61")

if __name__ == '__main__':
    main()
