# -*- coding:utf-8 -*-
'''
author:zhaoyan
time:2018/10/31 15:18
'''
from public.common import basepage
from time import sleep

#选择商品
class ZaoZuoBuyGoodsPage(basepage.Page):
    def click_choose_goods(self):
        """点击选中的商品"""
        self.dr.click("xpath->//div[@id='screening_wrapper']/div[3]/div/div/div[3]/a/div/div")
        self.dr.into_new_window()

#购买单品
class ZaoZUOBuySkuPage(basepage.Page):
    def choose_color(self):
        """选择颜色"""
        self.dr.click('xpath->//*[@id="item-buy-box"]/div[2]/div/div[4]/dl[1]/dd/div[2]')
        sleep(2)
    def choose_style(self):
        """选择款型"""
        self.dr.click('xpath->//*[@id="item-buy-box"]/div[2]/div/div[4]/dl[2]/dd/div[2]')
        sleep(2)
    def change_num(self):
        """修改数量"""
        self.dr.click('xpath->//*[@id="item-buy-box"]/div[2]/dl/dt/input')
        self.dr.type_and_enter('xpath->//*[@id="item-buy-box"]/div[2]/dl/dt/input','3',secs=0.5)
    def buy_now(self):
        """立即购买"""
        self.dr.click('xpath->//*[@id="item-buy-box"]/div[2]/dl/dd/div[1]')
    def addCart(self):
        """点击加入购物车"""
        self.dr.click('xpath->//*[@id="item-buy-box"]/div[2]/dl/dd/div[2]')

#购买组合商品
class ZaoZUOBuySuitePage(basepage.Page):
    def intoSuite(self):
        """购买组合商品入口"""
        self.dr.click('id->goto_combination')
        sleep(3)
    def addsuiteTocart(self):
        """组合商品点击加入购物车按钮"""
        self.dr.click('xpath->//*[@id="recommend_part"]/div/div/div[2]/div/div[1]/div[2]/div/div/div')
        sleep(3)
    def choose_color(self):
        """组合商品选择颜色"""
        self.dr.click('xpath->//*[@id="suite-pop-2416"]/div[1]/dl[1]/dd/div/div/dl[1]/dd/div[1]')
        sleep(2)
    def choose_style(self):
        """选择款型"""
        self.dr.click('xpath->//*[@id="suite-pop-2416"]/div[1]/dl[1]/dd/div/div/dl[2]/dd/div[1]')
        sleep(2)
    def change_num(self):
        """修改数量"""
        self.dr.click('xpath->//*[@id="suite-pop-footer-2416"]/dl[1]/dt/input')
        self.dr.type_and_enter('xpath->//*[@id="suite-pop-footer-2416"]/dl[1]/dt/input','3',secs=0.5)
    def close_choose_Popout(self):
        """关闭选择浮层"""
        self.dr.click('xpath->//*[@id="suite-buy-box"]/div[1]')
    def buy_now(self):
        """组合商品立即购买"""
        self.dr.click('xpath->//*[@id="suite-pop-footer-2416"]/dl[1]/dd/div[1]')
    def addCart(self):
        """组合商品点击加入购物车"""
        self.dr.click('xpath->//*[@id="suite-pop-footer-2416"]/dl[1]/dd/div[2]')
        sleep(10)
