# -*- coding:utf-8 -*-
'''
author:zhaoyan
time:2018/10/31 16:33
'''
from time import sleep
from public.common import mytest
from  public.pages import zaozuologinPage
from public.common import datainfo


class TestZaoZuoLogin(mytest.MyTest):

    """造作登陆测试"""

    def test_login_case(self):
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

    # def test_login_case2(self):
    #     """循环登录"""
    #     # data_username = datainfo.get_xls_to_list('user.xlsx', 'username')
    #     # print(data_username)
    #     # number = len(data_username)
    #     # count = 0
    #     # while count <= number:
    #     #     self.test_login_case(datainfo.get_login_input_username(),datainfo.get_login_input_password())
    #     #     count += 1
    #     listdata = datainfo.excel_table_byindex('user.xlsx')
    #     if (len(listdata) <= 0):
    #         assert 0,u"Excel数据异常"
    #     for i in range(0,len(listdata)):
    #         zaozuopage = zaozuologinPage.ZaozuoLoginPage(self.dr)
    #         zaozuopage.into_zaozuo_loginpage()
    #         self.dr.wait(10)
    #         zaozuopage.choose_login_type()
    #         self.dr.wait(3)
    #         zaozuopage.input_name(listdata.username)
    #         zaozuopage.input_password(listdata.password)
    #         self.dr.wait(3)
    #         zaozuopage.click_login_button()
    #         sleep(10)




    # def test_login_iput(self):
    #     """使用数据驱动进行测试"""
    #     data_username = datainfo.get_xls_to_list('user.xlsx','username')
    #     data_password = datainfo.get_xls_to_list('user.xlsx', 'password')
    #     L = []
    #     for i in zip(data_username, data_password):
    #         L.append(i)
    #     # print(L)
    #     for i in range(0,len(L)):
    #     #for j in range(0,len(L[i])):
    #         zaozuopage = zaozuologinPage.ZaozuoLoginPage(self.dr)
    #         zaozuopage.into_zaozuo_loginpage()
    #         self.dr.wait(10)
    #         zaozuopage.choose_login_type()
    #         self.dr.wait(3)
    #         zaozuopage.input_name(L[i][0])
    #         zaozuopage.input_password(L[i][1])
    #         self.dr.wait(3)
    #         zaozuopage.click_login_button()
    #         sleep(10)

if __name__ == '__main__':
    A = TestZaoZuoLogin()
    A.test_login_iput()


