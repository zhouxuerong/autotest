import requests,time,sys,re,os
import urllib,zlib
import pymysql
from trace import CoverageResults
import json
from idlelib.rpc import response_queue
from time import sleep
sys.path.append("..")
from autotest.common import mySqlOperation


import pymysql



HOSTNAME = "127.0.0.1"

def readSQLcase():                     # 读取数据库中相应的接口用例数据
    sql = "select id,apiname,apiurl,api_method,apiparamvalue,apiresult,apistatus from apitest_apistep where apitest_apistep.Apitest_id = 2"
    operation = mySqlOperation()
    info = operation.fetchmany(sql)
    print(info)
    for li in info:
        case_list = []
        case_list.append(li)
    operation.closeCon() 

def interfaceTest(case_list):
    res_flags = []
    request_urls = []
    responses = []
    strinfo = re.compile('{TaskId}')







