# -*- coding:utf-8 -*-
'''
author:zhaoyan
time:2018/11/2 17:44
'''

from public.common import mytest
from  public.pages import zaozuologinPage
from testcase import test_zaozuo_login


class TestZaoZuoLogout(mytest.MyTest):
    """造作用户登出"""
    # def test_logout(self):
    #     zaozuopage = zaozuologinPage.ZaozuoLoginPage(self.dr)
    #     zaozuopage.move_username_info()
    #     self.dr.wait(10)
    #     zaozuopage.logout()
    #     self.dr.wait(10)

    def test_logout_case(self):
        zaozuopage = zaozuologinPage.ZaozuoLoginPage(self.dr)
        test_zaozuo_login.TestZaoZuoLogin.test_login_case(self)
        self.dr.wait(10)
        zaozuopage.move_username_info()
        self.dr.wait(10)
        zaozuopage.logout()






if __name__ == '__main__':
    A = TestZaoZuoLogout
    # A.test_logout_case()