import sys
sys.path.append("/Users/zhouxuerong/projects/autotest/autotest/autotest")
from django.test import TestCase
from apitest.views import Login
from django.http import HttpRequest

class titlePageTest(TestCase):
    def test_loginPage(self):
        request = HttpRequest()
        Response = Login(request)
        print(Response.content)

