from django.db import models

# Create your models here.
class Product(models.Model):
    productname = models.CharField("产品名称",max_length=64)  #产品名称
    productdesc = models.CharField("产品描述",max_length=200)  #产品描述
    producter = models.CharField("产品负责人",max_length=200)    #产品负责人
    create_time = models.DateTimeField("创建时间",auto_now=True)   #创建时间，自动获取当前时间

    class Meta:
        verbose_name = '产品管理'
        verbose_name_plural = '产品管理'  #人类可读的单复数名称（verbose_name和verbose_name_plural）
    def __str__(self):
        return self.productname  

class Apitest(models.Model):
    Product = models.ForeignKey('product.Product',on_delete=models.CASCADE,null=True)
    apitestname = models.CharField('流程接口名称',max_length=64) #流程接口测试场景      
    apitestdesc = models.CharField('描述',max_length=64,null=True) #流程接口描述      
    apitester = models.CharField('测试负责人',max_length=16) #执行人      
    apitestresult = models.BooleanField('测试结果') #流程接口测试结果  
    create_time = models.DateField("创建时间",auto_now=True) #创建时间
    
    class Meta:
        verbose_name = '流程场景接口'
        verbose_name_plural = '流程场景接口'   
    def __str__(self):
        return self.apitestname

class Apistep(models.Model):
    Apitest =models.ForeignKey("product.Apitest",on_delete=models.CASCADE,null=True)
    apiname = models.CharField('接口名称',max_length=100) # 接口标题
    apiurl = models.CharField('url地址',max_length=200) #地址
    apistep = models.CharField('测试步骤',max_length=100,null=True) # 测试步骤
    apiparamvalue = models.CharField('请求参数和值',max_length=800) #参数和值
    REQUEST_METHOD = (('get','get'),('post','post'),('put','put'),('delete','getdelete'),('patch','patch'))

