import os
import time 
import unittest
from appium import webdriver
import pymysql,requests,time,sys,re
import urllib,zlib
import json
sys.path.append("..")
from autotest.common import mySqlOperation
import HTMLTestRunner
PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

global driver

HOSTNAME = "127.0.0.1"
class Calculator(unittest.TestCase):
    def setUp(self):
        time.sleep(1)

    def test_readSQLcase(self):
        sql = "select id,appcasename,appfindmethod,appevelement,appoptmethod,appassertdata \
            apptestresult from apptest_appcasestep where apptest_appcasestep.Appcase_id=1 \
            order by ASC"
        mysqloperate = mySqlOperation()    
        info = mysqloperate.fetchmany(sql)    
        for i in info:
            case_list = []
            case_list.append(i)
            apptestcase(case_list)
        mysqloperate.closeCon()

    def tearDown(self):
        driver.quit()

def apptestcase(case_list):  
    for case in case_list:
        try:
            case_id = case[0]      
            findmethod = case[2]      
            evelement = case[3]      
            optmethod = case[4] 
        except Exception as e:
            return "测试用例格式不正确%s"%e
        print(evelement)
        time.sleep(10)
        if optmethod == "click" and findmethod == "find_element_by_id":
            driver.find_element_by_id(evelement).send_keys("wayto")
        elif optmethod == "click" and findmethod == "find_element_by_name":
            driver.find_element_by_name(evelement).click()
        elif optmethod == "sendkey":
            driver.find_element_by_name(evelement).send_keys()

# 向appcasestep里写入结果
def writeResult(case_id,result):
    result = result.encode("utf-8")
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    sql = "update apptest_appcasestep set apptestresult=%s,create_time=%s \
           where id=%s"
    param =(result,now,case_id)
    print("app autotest result is " + result.decode("utf-8"))
    operate = mySqlOperation()
    operate.sqlexecute(sql,param)
    operate.closeCon()

# 向case表里写入结果
def casewriteResult(case_id,result):
    result = result.encode("utf-8")
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    sql = "update apptest_appcase set apptestresult=%s,create_time=%s \
           where id=%s"
    param =(result,now,case_id)
    print("app autotest result is " + result.decode("utf-8"))
    operate = mySqlOperation()
    operate.sqlexecute(sql,param)
    operate.closeCon()

if __name__ == '__main__':
    desired_caps = {}
    desired_caps['platformName'] = "Android"
    desired_caps['appPackage'] = "com.android.test"
    desired_caps['appActivity'] = ".Test"
    desired_caps['platformVersion'] = "4.4"
    desired_caps['deviceName'] = "emulator-5554"
    desired_caps['app'] =PATH("C:\\release\\csdn.apk") 
    time.sleep(1)
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
    now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))
    testunit = unittest.TestSuite()
    testunit.addTest(Calculator("test_readSQLcase"))
    filename = os.path.split(os.path.realpath(__file__))[0] + "/apptest_report.html"
    fp = open(filename,"wb")
    runner  = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"自动化测试汇总报告",description=u"app自动化测试")
    runner.run(testunit)
    driver.quit()
    
                


        

        