# -*- coding:utf-8 -*-
'''
author:zhaoyan
time:2018/11/16 11:49
'''
from public.common import basepage
from time import sleep


class ZaoZuoShaiDanPage(basepage.Page):

    def ordershare(self):
        """点击添加晒单"""
        self.dr.click('xpath->/html/body/div[2]/div')
        sleep(3)
    def ordershare_clickgoods(self):
        """选中待晒单商品"""
        self.dr.double_click('xpath->/html/body/section/div[1]/div/div[2]')
    def Editors_note(self):
        """编辑备注"""
        self.dr.type('class->textarea-box','我是晒单第一条')

