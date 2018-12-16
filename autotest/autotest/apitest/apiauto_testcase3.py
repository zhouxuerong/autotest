import requests,time,sys,re,os
import urllib,zlib
import pymysql
from trace import CoverageResults
import json
from idlelib.rpc import response_queue
from time import sleep
sys.path.append("..")
from autotest.common import mySqlOperation
import unittest
import HTMLTestRunner

HOSTNAME = "127.0.0.1"

class ApiFlow(unittest.TestCase):
    def setUp(self):
        time.sleep(1)

    def test_readSQLcase(self):                     # 读取数据库中相应的接口用例数据
        sql = "select id,apiname,apiurl,api_method,apiparamvalue,apiresult,apistatus from apitest_apistep where apitest_apistep.Apitest_id = 2"
        operation = mySqlOperation()
        info = operation.fetchmany(sql)
        print(info)
        for li in info:
            case_list = []
            case_list.append(li)
            CredentialId()
            interfaceTest(case_list)
        operation.closeCon()     

    def tearDown(self):
        time.sleep(1)    

# def readSQLcase(self):                     # 读取数据库中相应的接口用例数据
#     sql = "select id,apiname,apiurl,api_method,apiparamvalue,apiresult,apistatus from apitest_apistep where apitest_apistep.Apitest_id = 2"
#     operation = mySqlOperation()
#     info = operation.fetchmany(sql)
#     print(info)
#     for li in info:
#         case_list = []
#         case_list.append(li)
#         CredentialId()
#         interfaceTest(case_list)
#     operation.closeCon()   


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
            new_url = "http://" + "api.test.com.cn" + url
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
                data = None
                print(str(case_id)+'request is get' + new_url.encode("utf-8")+"?"+urlParam(param).encode("utf-8"))
                results = requests.get(new_url+"?"+urlParam(param),data,headers=headers).text
                print("response is get"+results.encode("utf-8"))
                responses.append(results)
                res = readRes(results,"")
            else:
                print("request is get" + new_url + "body is" + urlParam(param))
                data = None
                req = urllib.request.Request(url=new_url,data=data,headers=headers,method="get")
                results = urllib.request.urlopen(req).read()
                print("response is get")
                print(results)
                res = readRes(results,res_check)
            if "pass" == res:
                writeResult("case_id",'1')
                res_flags.append("pass")
            else:
                res_flags.append("fail")
                writeResult("case_id","0")  
                writeBug(case_id,interface_name,new_url,results,res_check)
                try:
                    preOrderSN(results)
                except:
                    print("ok")

        if method.upper() == "PUT":
            headers = {"Host":HOSTNAME,"Connection":"keep-alive","CredentialId":id,"Content-Type":"application/json"}      
            body_data = param     
            results = requests.put(url=url,data=body_data,headers=headers).text
            responses.append(results)
            res = readRes(results,res_check)  
            if "pass" == res:
                writeResult("case_id",'1')
                res_flags.append("pass")
            else:
                res_flags.append("fail")
                writeResult("case_id","0")  
                writeBug(case_id,interface_name,new_url,results,res_check)
                try:
                    preOrderSN(results)
                except:
                    print("ok")    

        if method.upper() == "PATCH":
            headers = {"Host":HOSTNAME,"Connection":"keep-alive","CredentialId":id,"Content-Type":"application/json"}      
            body_data = param     
            results = requests.patch(url=url,data=body_data,headers=headers).text
            responses.append(results)
            res = readRes(results,res_check)  
            # 1代表true,0代表false
            if "pass" == res:
                writeResult("case_id",'1')
                res_flags.append("pass")
            else:
                res_flags.append("fail")
                writeResult("case_id","0")  
                writeBug(case_id,interface_name,new_url,results,res_check)
                try:
                    preOrderSN(results)
                except:
                    print("ok")    

        if method.upper() == "POST":
            headers = {"Authorization":"Credential"+id,"Content-Type":"application/json"}       
            if "=" in urlParam(param):   
                data = None
                results = requests.post(new_url +"?" + urlParam(param),data,headers=headers).text
                print("response is post" + results.encode("utf-8"))
                responses.append(results)
                res = readRes(results,"")
            else:
                print(str(case_id)+"request is " + new_url.encode("utf-8")+"body is "+urlParam(param).encode("utf-8"))
                results = requests.post(new_url,data=urlParam(param).encode("utf-8"),headers=headers).text    
                print("response is post" + results.encode("utf-8"))
                responses.append(results)
                res = readRes(results,res_check)
            if "pass" == res:
                writeResult("case_id",'1')
                res_flags.append("pass")
            else:
                res_flags.append("fail")
                writeResult("case_id","0")  
                writeBug(case_id,interface_name,new_url,results,res_check)
                try:
                    preOrderSN(results)
                except:
                    print("ok")        



def  readRes(res,res_check):
    # Python decode() 方法以 encoding 指定的编码格式解码字符串。默认编码为字符串编码
    res = res.decode().replace('":"',"=").replace('":',"=")   
    res_check = res_check.split(';')
    for s in res_check:
        if s in res:
            pass
        else:
            return "错误，返回参数和预期结果不一致"+s 
        return "pass"            

    # url引号转换
def urlParam(param):
    # 转换引号
    param1 = param.replace('&quot;','"')
    return param1

def CredentialId():
    global id
    url = 'http://'+'api.test.com.cn'+'/api/Security/Authentication/Signin/web'
    body_data = json.dumps({"Identity":"test","Password":"test"})
    headers = {"Connection":"keep-alive","Content-Type":"application/json" }
    response = requests.post(url=url,data=body_data,headers=headers)
    data = response.text
    regx ='.*"CredentialId":"(.*)","Scene"'
    pm = re.search(regx,data)
    id = pm.group(1)

def preOrderSN(results):
    global preOrderSN   
    regx = '.*"preOrderSN":"(.*)","toHome"'
    pm = re.search(regx,results)
    if pm:
        preOrderSN = pm.group(1).encode("utf-8")
        return preOrderSN
    return False   

def TaskId(results):
    global TaskId
    regx = '.*"TaskId":(.*),"PlanId"'
    pm = re.search(regx,results)
    if pm:
        TaskId = pm.group(1).encode("utf-8")
        return TaskId
    return False  

def taskno(param):
    global taskno
    a = int(time.time())  
    taskno = "task_" + str(a)
    return taskno

def writeResult(case_id,result):
    result = result.encode("utf-8")
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    sql = "update apitest_apistep set apitest_apistep.apistatus=%s where apitest_apistep.Apitest_id=%s"
    param = (result,case_id)
    print("api autotest result is" + result.decode())
    mySqlOperation().sqlexecute(sql,param)

def writeBug(bug_id,interface_name,request,response,res_check):
    interface_name = interface_name.encode("utf-8")
    res_check = res_check.encode("utf-8")
    request = request.encode("utf-8")
    now = time.strftime("%Y-%m-%d %H:%M:%S")  
    bugname = str(bug_id) + "_" + interface_name.decode() + "_出错了"
    bugdetail ='[请求数据]<br/>' + request.decode() + "<br/>" + "[预期结果]<br/>" + res_check.decode() + "<br/>" + "<br/>" +"[响应数据]<br/>"+"<br/>"+response.decode()
    print("bugdetail:",bugdetail)
    sql = "insert into 'bug_bug' ('bugname','bugdetail','bugstatus','buglevel','bugcreater','bugassign','created_time','Product_id') \
            VALUES('%s','%s','1','1','周雪荣','周雪荣','%s','2');"
    param = (bugname,pymysql.escape_string(bugdetail),now)
    mySqlOperation().sqlexecute(sql,param)
        
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    testunit = unittest.TestSuite()
    testunit.addTest(ApiFlow("test_readSQLcase"))
    filename =os.path.split(os.path.realpath(__file__))[0] + "/templates/apitest_report.html"
    fp = open(filename,"wb")


        











