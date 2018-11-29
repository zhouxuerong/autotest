import pymysql

class mySqlOperation:
    def __init__(self,user="root",passwd="password123",db="autotest",port=3306,host="127.0.0.1"):
        self.coon = pymysql.connect(user=user,passwd=passwd,db=db,port=port,host=host)
        self.cursor = self.coon.cursor()
        print("success")

    def fetchmany(self,sql):       
        aa = self.cursor.execute(sql)
        info = self.cursor.fetchmany(aa)
        return info

    def sqlexecute(self,sql,param):
        self.cursor.execute(sql,param)
        self.coon.commit()
        self.cursor.close()
        self.coon.close()


    def closeCon(self):
        self.coon.commit()
        self.cursor.close()
        self.coon.close()
            