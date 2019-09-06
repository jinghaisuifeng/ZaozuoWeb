# -*- coding:utf-8 -*-
'''
author:zhaoyan
time:2018/10/31 15:18
'''
from public.common import basepage

class ZaozuoLoginPage(basepage.Page):

    def into_zaozuo_loginpage(self):
        """打开造作登陆页面"""
        self.dr.open("https://www.zaozuo.com/login")
    def choose_login_type(self):
        """选择登陆方式"""
        self.dr.click('xpath->//li[contains(text(),"密码登录")]')
    def input_name(self,values):
        """输入用户名"""
        #self.dr.click("xpath->//input[@id='phone_num_passwd']")
        #self.dr.type("xpath->//input[@id='phone_num_passwd']", values)
        self.dr.click('id->phone_num_passwd')
        self.dr.clear_type('id->phone_num_passwd',values)
    def input_password(self,values):
        """输入密码"""
        # self.dr.click('xpath->//*[@id="password"]')
        # self.dr.type('xpath->//*[@id="password"]',values)
        self.dr.click('id->password')
        self.dr.clear_type('id->password',values)
    def click_login_button(self):
        """点击登陆button"""
        self.dr.click('id->login_passwd')
    def move_username_info(self):
        self.dr.move_to_element('class->login')

    def logout(self):
        self.dr.click("xpath->/html/body/div[1]/div[1]/div/div/div/a[8]")






