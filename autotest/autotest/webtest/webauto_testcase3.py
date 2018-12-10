import os
import time 
import unittest
from selenium import webdriver
import pymysql,requests,time,sys,re
import urllib,zlib
import json
sys.path.append("..")
from autotest.common import mySqlOperation
import HTMLTestRunner
PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

global driver

HOSTNAME = "127.0.0.1"
class Search(unittest.TestCase):
    def setUp(self):
        self.driver =webdriver.Firefox()
        self.driver.get("htpp://baidu.com")
        time.sleep(1)

    def test_readSQLcase1(self):
        sql = "select id,webfindmethod,webevelement,weboptmethod,webtestdata,webassertdata \
            webtestresult from webtest_webcasestep where webtest_appcasestep.Webcase_id=1 \
            order by ASC"
        mysqloperate = mySqlOperation()    
        info = mysqloperate.fetchmany(sql)    
        for i in info:
            case_list = []
            case_list.append(i)
            webtestcase(case_list,self)
        mysqloperate.closeCon()

    def test_readSQLcase2(self):
        sql = "select id,webfindmethod,webevelement,weboptmethod,webtestdata,webassertdata \
            webtestresult from webtest_webcasestep where webtest_appcasestep.Webcase_id=1 \
            order by ASC"
        mysqloperate = mySqlOperation()    
        info = mysqloperate.fetchmany(sql)    
        for i in info:
            case_list = []
            case_list.append(i)
            webtestcase(case_list,self)
        mysqloperate.closeCon()

    def tearDown(self):
        self.driver.quit()

def webtestcase(case_list,self):  
    for case in case_list:
        try:
            case_id = case[0]      
            findmethod = case[1]      
            evelement = case[2]      
            optmethod = case[3] 
            testdata = case[4]
        except Exception as e:
            return "测试用例格式不正确%s"%e
        print(case)
        time.sleep(5)
        if optmethod == "sendkeys" and findmethod == "find_element_by_id":
            self.driver.find_element_by_id(evelement).send_keys(testdata)
        elif optmethod == "click" and findmethod == "find_element_by_name":
            print(evelement)
            self.driver.find_element_by_name(evelement).click()
        elif optmethod == "click" and findmethod == "find_element_by_id":
            self.driver.find_element_by_id(evelement).click()

# 向appcasestep里写入结果
# def writeResult(case_id,result):
#     result = result.encode("utf-8")
#     now = time.strftime("%Y-%m-%d %H:%M:%S")
#     sql = "update apptest_appcasestep set apptestresult=%s,create_time=%s \
#            where id=%s"
#     param =(result,now,case_id)
#     print("app autotest result is " + result.decode("utf-8"))
#     operate = mySqlOperation()
#     operate.sqlexecute(sql,param)
#     operate.closeCon()

# 向case表里写入结果
# def casewriteResult(case_id,result):
#     result = result.encode("utf-8")
#     now = time.strftime("%Y-%m-%d %H:%M:%S")
#     sql = "update apptest_appcase set apptestresult=%s,create_time=%s \
#            where id=%s"
#     param =(result,now,case_id)
#     print("app autotest result is " + result.decode("utf-8"))
#     operate = mySqlOperation()
#     operate.sqlexecute(sql,param)
#     operate.closeCon()

if __name__ == '__main__':
    time.sleep(1)
    now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))
    testunit = unittest.TestSuite()
    testunit.addTest(Search("test_readSQLcase1"))
    testunit.addTest(Search("test_readSQLcase2"))
    filename = os.path.split(os.path.realpath(__file__))[0] + "/webtest_report.html"
    fp = open(filename,"wb")
    runner  = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"自动化测试报告",description=u"搜索测试测试")
    runner.run(testunit)

    
                


        

        