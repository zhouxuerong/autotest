import configparser
import os

# 返回配置文件指定配置的值
def getConfig(section,key):
    config = configparser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0]+"/setting.conf"
    config.read(path)
    return config.get(section,key)

# a = getConfig("user","username")    
# print(a)