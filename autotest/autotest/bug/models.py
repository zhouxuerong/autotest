from django.db import models
from product.models import Product

class Bug(models.Model):
    Product = models.ForeignKey("product.Product",on_delete=models.CASCADE,null=True)   #关联产品ID
    bugname = models.CharField("bug名称",max_length=64)
    bugdetail = models.CharField("详情",max_length=200)
    BUG_STATUS = (('激活',"激活"),('已解决',"已解决"),('关闭',"关闭"))
    bugstatus = models.CharField(verbose_name="解决状态",choices=BUG_STATUS,default="激活",max_length=32,null=True)
    BUG_LEVEL = (('1',"1"),('2',"2"),('3',"3"))
    bug_level = models.CharField(verbose_name="严重程度",choices=BUG_LEVEL,default="3",max_length=32,null=True)
    bugcreater = models.CharField("创建人",max_length=32)
    bugassign = models.CharField("分配给",max_length=32)
    create_time = models.DateTimeField("创建时间",auto_now=True)
    class Meta:
        verbose_name = "bug管理"
        verbose_name_plural = "bug管理"
    def __str__(self):
        return self.bugname    


