# -*- coding:utf-8 -*-
'''
author:zhaoyan
time:2018/11/15 11:12
'''
from public.common import mytest
#from public.pages import zaozuologinPage
from public.pages import zaozuoMyProfilePage
from testcase.test_zaozuo_login import TestZaoZuoLogin


class ZaoZuoMyProfilePage(mytest.MyTest):
    """我的资料页面"""
    def test_zaozuo_add_adress(self):
        """添加新的收获地址"""
        TestZaoZuoLogin.test_login_case(self)
        zaozuoadresspage = zaozuoMyProfilePage.ZaoZuoMyProfilePage(self.dr)
        zaozuoadresspage.into_zaozuo_myprofile()
        zaozuoaddadresspage = zaozuoMyProfilePage.ZaoZuoChange_adreesPage(self.dr)
        zaozuoaddadresspage.add_new_adrees()
        zaozuoaddadresspage.province()
        zaozuoaddadresspage.city()
        zaozuoaddadresspage.county()
        zaozuoaddadresspage.detailedAaddress()
        zaozuoaddadresspage.receipt_name()
        zaozuoaddadresspage.receipt_phone()
        zaozuoaddadresspage.verify()
        zaozuoaddadresspage.set_default_adress()
        zaozuoaddadresspage.delete_adress()
if __name__ == '__main__':
    a=ZaoZuoMyProfilePage(mytest.MyTest)
    a.test_zaozuo_add_adress()

