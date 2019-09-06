# -*- coding:utf-8 -*-
'''
author:zhaoyan
time:2018/11/12 11:07
'''
from public.common import mytest
from public.pages import zaozuoindexPage
from public.pages import zaozuoBuyGoodsPage

class TestZaoZuoBuyGoods(mytest.MyTest):
    """造作购买商品"""

    def test_buy_goods(self):
        """购买单品"""
        zaozuopage = zaozuoindexPage.ZaoZuoIndexPage(self.dr)
        zaozuopage.into_zaozuo_indexpage()
        self.dr.wait(10)
        zaozuotagpage = zaozuoindexPage.zaozuoindex_bed_tag(self.dr)
        zaozuotagpage.second_level_bed()
        self.dr.wait(10)
        zaozuobuypage = zaozuoBuyGoodsPage.ZaoZuoGoodsBuyPage(self.dr)
        zaozuobuypage.click_choose_goods()
        zaozuobuypage.choose_color()
        zaozuobuypage.choose_style()
        zaozuobuypage.change_num()
        zaozuobuypage.addToShoppingCart()
        zaozuobuypage.click_cart()
    def test_buy_suite(self):
        """购买组合"""
        zaozuopage = zaozuoindexPage.ZaoZuoIndexPage(self.dr)
        zaozuopage.into_zaozuo_indexpage()
        self.dr.wait(10)
        zaozuotagpage = zaozuoindexPage.zaozuoindex_bed_tag(self.dr)
        zaozuotagpage.second_level_bed()
        self.dr.wait(10)
        zaozuointobuypage = zaozuoBuyGoodsPage.ZaoZuoBuyGoodsPage(self.dr)
        zaozuointobuypage.click_choose_goods()
        zaozuobuysuitepage = zaozuoBuyGoodsPage.ZaoZUOBuySuitePage(self.dr)
        zaozuobuysuitepage.intoSuite()
        zaozuobuysuitepage.addsuiteTocart()
        zaozuobuysuitepage.addCart()
        zaozuobuysuitepage.close_choose_Popout()



if __name__ == '__main__':
    A = TestZaoZuoBuyGoods(mytest.MyTest)
    A.test_buy_suite()
    A.test_buy_goods()