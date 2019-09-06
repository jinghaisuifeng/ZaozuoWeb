# -*- coding:utf-8 -*-
'''
author:zhaoyan
time:2018/11/15 11:02
'''
from public.common import basepage
from time import sleep
from selenium.webdriver.support.select import Select

class ZaoZuoMyProfilePage(basepage.Page):
    """我的资料页面"""
    def into_zaozuo_myprofile(self):
        """进入我的资料页面"""
        self.dr.open("https://www.zaozuo.com/me")


class ZaoZuoChange_adreesPage(basepage.Page):
    """修改我的收货地址"""
    def add_new_adrees(self):
        """添加新的收获地址"""
        self.dr.click('xpath->//*[@id="new_address_btn"]')
        sleep(10)
    def province(self):
        """选择省"""
        Select(self.dr.get_element('id->s_province')).select_by_value("3")
    def city(self):
        """选择市"""
        Select(self.dr.get_element('id->s_city')).select_by_value("36")
    def county(self):
        """选择县/区"""
        Select(self.dr.get_element('id->s_county')).select_by_value("398")
    def detailedAaddress(self):
        """填写详细地址"""
        self.dr.clear_type('id->address_text','马泉营二区1001号')
    def receipt_name(self):
        """收货人姓名"""
        self.dr.clear_type('id->receipt_name','zhaoyan')
    def receipt_phone(self):
        """收货人联系方式"""
        self.dr.clear_type('id->receipt_phone','18611404533')
    def verify(self):
        """点击确认按钮"""
        self.dr.click('xpath->//*[@id="edit_address_pop"]/div[4]/div[2]')
        sleep(5)
    def set_default_adress(self):
        """设置默认地址"""
        self.dr.move_to_element('xpath->//*[@id="div-address-all"]/div[2]/div[1]')
        sleep(3)
        self.dr.click('class->set-default-address')
        sleep(3)
    def delete_adress(self):
        """删除地址"""
        self.dr.move_to_element('class->f1')
        sleep(3)
        self.dr.click('class->delete-address')
        sleep(3)

