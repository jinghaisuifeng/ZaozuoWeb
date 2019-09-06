# -*- coding:utf-8 -*-
'''
author:zhaoyan
time:2018/11/16 11:28
'''

from public.common import mytest
from public.method.login import Login
from public.pages.zaozuoindexPage import ZaoZuoIndexPage
from public.pages.zaozuo_shaidanPage import ZaoZuoShaiDanPage


class TestZaoZuoEvaluation(mytest.MyTest):
    """造作晒单测试"""

    def test_Evaluation_case(self):
        Login.login(self)
        zaozuopage = ZaoZuoIndexPage(self.dr)
        zaozuopage.into_zaozuo_My_order()
        zaozuopage = ZaoZuoShaiDanPage(self.dr)
        zaozuopage.ordershare()
        zaozuopage.ordershare_clickgoods()
        zaozuopage.Editors_note()



if __name__ == '__main__':
    A = TestZaoZuoEvaluation(mytest.MyTest)
    A.test_Evaluation_case()