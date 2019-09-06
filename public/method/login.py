# -*- coding:utf-8 -*-
'''
author:zhaoyan
time:2018/11/16 13:51
'''
from time import sleep
from public.common import mytest
from  public.pages import zaozuologinPage
from public.common import datainfo


class Login(mytest.MyTest):

    """造作登陆测试"""

    def login(self):
        zaozuopage = zaozuologinPage.ZaozuoLoginPage(self.dr)
        zaozuopage.into_zaozuo_loginpage()
        self.dr.wait(10)
        zaozuopage.choose_login_type()
        self.dr.wait(3)
        zaozuopage.input_name('18611404533')
        zaozuopage.input_password('8655899')
        self.dr.wait(3)
        zaozuopage.click_login_button()
        print('login success')
        sleep(10)


if __name__ == '__main__':
    a=Login()
    a.login()


