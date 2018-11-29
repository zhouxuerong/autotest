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
    strinfo1 = re.compile('{AssetId}')
    strinfo2 = re.compile('{PointId}')
    assetinfo = re.compile('{assetno}')
    tasknoinfo = re.compile('{tasknoinfo}')
    schemainfo = re.compile('{schema}')
    for case in case_list:
        try:
            case_id = case[0]
            interface_name = case[1]
            url = case[2]
            method = case[3]
            param = case[4]
            res_check = case[5]
        except Exception as e:
            return "测试用例格式不正确%s"%e  

        if param == "":
            new_url = "http://"+"api.test.com.cn"+url
        elif param == "null":
            new_url = "http://"+url
        else:
            # 正则表达式匹配
            url = strinfo.sub(TaskId,url)  
            param= strinfo.sub(TaskId,param)
            param = tasknoinfo.sub(taskno,param)
            new_url = "http://"+"127.0.0.1"+url
            request_urls.append(new_url)
        if method.upper() == "GET":
            headers = {"Authorization":"","Content-Type":"application/json"}       
            if "=" in urlParam(param):   








