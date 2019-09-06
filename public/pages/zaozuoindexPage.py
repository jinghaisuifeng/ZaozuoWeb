# -*- coding:utf-8 -*-
'''
author:zhaoyan
time:2018/10/31 15:18
'''
from public.common import basepage
from time import sleep

class ZaoZuoIndexPage(basepage.Page):


    def into_zaozuo_indexpage(self):
        """打开造作首页"""
        self.dr.open("https://www.zaozuo.com/")
    def Close_the_card_for_xinjiali(self):
        """关闭新家礼卡片浮层"""
        self.dr.click('class->newindex-autopop-closebtn')
    def into_zaozuo_shopping_cart(self):
        """点击购物车按钮"""
        sleep(3)
        self.dr.click('id->cart_box')
        sleep(5)
    def into_zaozuo_Member_Center(self,values):
        """点击进入会员中心"""
        self.dr.move_to_element('class->login')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/div[1]/div/div/div/a[1]')
    def into_zaozuo_My_evaluation(self):
        """点击进入我的晒单"""
        self.dr.move_to_element('class->login')
        sleep(3)
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/div[1]/div/div/div/a[5]')
        sleep(3)
    def into_zaozuo_My_order(self):
        """点击进入我的订单"""
        self.dr.move_to_element('class->login')
        sleep(3)
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/div[1]/div/div/div/a[2]')
        sleep(3)
    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()


    #首页商品分类
class zaozuoindex_sofa_tag(basepage.Page):
    #1、沙发
    def first_floor_goods_category_sofa(self):
        """沙发"""
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[2]/div/a')
    #沙发二级tag
    def second_level_ThreePeopleSofa(self):
        """三人沙发"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[2]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[2]/ul/li[1]')
    def second_level_DoubleSofa(self):
        """双人沙发"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[2]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[2]/ul/li[2]')
    def second_level_armchair(self):
        """单人沙发"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[2]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[2]/ul/li[3]')
    def second_level_ThreePeopleSofa_big(self):
        """大三人沙发"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[2]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[2]/ul/li[4]')
    def second_level_SofaPire(self):
        """沙发墩"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[2]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[2]/ul/li[5]')

class zaozuoindex_bed_tag(basepage.Page):
    #2、床具
    def first_floor_goods_category_bedclothe(self):
        """床具"""
        self.dr.click('xpath->/html/body/div[1]/ul/li[3]/div')
    # 床具二级tag
    def second_level_bed(self):
        """床"""
        self.dr.move_to_element('xpath->/html/body/div[1]/ul/li[3]/div')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[3]/ul/li[1]/a')
    def second_level_mattress(self):
        """床垫"""
        self.dr.move_to_element('xpath->/html/body/div[1]/ul/li[3]/div')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[3]/ul/li[2]/a')
    def second_level_SheetSuite(self):
        """床单四件套"""
        self.dr.move_to_element('xpath->/html/body/div[1]/ul/li[3]/div')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[3]/ul/li[3]/a')
    def second_level_Quilt(self):
        """被芯"""
        self.dr.move_to_element('xpath->/html/body/div[1]/ul/li[3]/div')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[3]/ul/li[4]/a')
    def second_level_Pillow(self):
        """枕芯"""
        self.dr.move_to_element('xpath->/html/body/div[1]/ul/li[3]/div')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[3]/ul/li[5]/a')
    def second_level_NightTable(self):
        """床头柜"""
        self.dr.move_to_element('xpath->/html/body/div[1]/ul/li[3]/div')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[3]/ul/li[6]/a')
    def second_level_BedStorageBox(self):
        """床下储物盒"""
        self.dr.move_to_element('xpath->/html/body/div[1]/ul/li[3]/div')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[3]/ul/li[7]/a')
    def second_level_BedChair(self):
        """床尾凳"""
        self.dr.move_to_element('xpath->/html/body/div[1]/ul/li[3]/div')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[3]/ul/li[8]/a')

class zaozuoindex_tankBracket_tag(basepage.Page):
    # 3、柜架
    def first_floor_goods_category_tank_bracket(self):
        """柜架"""
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[4]/div/a')
    #柜架二级tag
    def second_level_locker(self):
        """置物柜"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[4]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[4]/ul/li[1]/a')
    def second_level_bookcase(self):
        """书柜"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[4]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[4]/ul/li[2]/a')
    def second_level_TVBench(self):
        """电视柜"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[4]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[4]/ul/li[3]/a')
    def second_level_StorageRack(self):
        """置物架"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[4]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[4]/ul/li[4]/a')
    def second_level_Wardrobe(self):
        """衣柜"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[4]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[4]/ul/li[5]/a')
    def second_level_Cell(self):
        """单元格"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[4]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[4]/ul/li[6]/a')
    def second_level_hallstand(self):
        """衣帽架"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[4]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[4]/ul/li[8]/a')
    def second_level_Sideboard(self):
        """玄关柜"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[4]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[4]/ul/li[9]/a')
    def second_level_cosmo(self):
        """cosmo"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[4]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[4]/ul/li[10]/a')

class zaozuoindex_chairs_tag(basepage.Page):
    #4、椅凳
    def first_floor_goods_category_chairs(self):
        """椅凳"""
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[5]/div/a')
    #椅凳二级tag
    def second_level_seat(self):
        """座椅"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[5]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[5]/ul/li[1]/a')
    def second_level_sitPier(self):
        """坐墩"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[5]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[5]/ul/li[2]/a')
    def second_level_leisureChair(self):
        """休闲椅"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[5]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[5]/ul/li[3]/a')
    def second_level_stool(self):
        """凳子"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[5]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[5]/ul/li[4]/a')

class zaozuoindex_stool_tag(basepage.Page):
    #5、桌几
    def first_floor_goods_category_stool(self):
        """桌几"""
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[6]/div/a')
    #桌几二级tag
    def second_level_desk_dining_table(self):
        """书桌*餐桌"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[6]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[6]/ul/li[1]/a')
    def second_level_end_table(self):
        """茶几"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[6]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[6]/ul/li[2]/a')
    def second_level_side_table(self):
        """边几"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[6]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[6]/ul/li[3]/a')

class zaozuoindex_LampAndLanterns_tag(basepage.Page):
    # 6、灯具
    def first_floor_goods_category_lamp(self):
        """灯具"""
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[7]/div/a')
    def second_level_deskLamp(self):
        """台灯"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[7]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[7]/ul/li[1]/a')
    def second_level_floorlamp(self):
        """地灯"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[7]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[7]/ul/li[2]/a')
    def second_level_ceilinglamp(self):
        """吊灯"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[7]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[7]/ul/li[3]/a')
    def second_level_nightlamp(self):
        """夜灯"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[7]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[7]/ul/li[4]/a')

class zaozuoindex_mendale_tag(basepage.Page):
    #7、家纺
    def first_floor_goods_category_mendale(self):
        """家纺"""
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[8]/div/a')
    def second_level_FourPieceBeddingSet(self):
        """床品四件套"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[8]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[8]/ul/li[1]/a')
    def second_level_quilt(self):
        """被芯"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[8]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[8]/ul/li[2]/a')
    def second_level_pillowInner(self):
        """枕芯"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[8]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[8]/ul/li[3]/a')
    def second_level_bedding(self):
        """床褥"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[8]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[8]/ul/li[4]/a')
    def second_level_blanket(self):
        """盖毯"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[8]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[8]/ul/li[5]/a')
    def second_level_carpet(self):
        """地毯"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[8]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[8]/ul/li[6]/a')
    def second_level_NeckPpillow(self):
        """抱枕·颈枕"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[8]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[8]/ul/li[7]/a')
    def second_level_TowelBathTowel(self):
        """毛巾·浴巾"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[8]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[8]/ul/li[8]/a')
    def second_level_accept(self):
        """收纳"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[8]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[8]/ul/li[9]/a')

class zaozuoindex_tableware_tag(basepage.Page):
    #8、餐具
    def first_floor_goods_category_tableware(self):
        """餐具"""
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[9]/div/a')
    def second_level_tablewareSet(self):
        """套装"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[9]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[9]/ul/li[1]/a')
    def second_level_dish(self):
        """盘碗"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[9]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[9]/ul/li[2]/a')
    def second_level_cup(self):
        """杯子"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[9]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[9]/ul/li[3]/a')
    def second_level_TablewareStorage(self):
        """储物"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[9]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[9]/ul/li[4]/a')
    def second_level_trays(self):
        """托盘"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[9]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[9]/ul/li[5]/a')

class zaozuoindex_adorn_tag(basepage.Page):
    #9、装饰
    def first_floor_goods_category_adorn(self):
        """装饰"""
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[10]/div/a')
    def second_level_TableVase(self):
        """摆件·花瓶"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[10]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[10]/ul/li[1]/a')
    def second_level_accept(self):
        """收纳"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[10]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[10]/ul/li[2]/a')
    def second_level_decorativePicture (self):
        """装饰画"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[10]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[10]/ul/li[3]/a')

class zaozuoindex_cosmo_tag(basepage.Page):
    # 10、cosmo
    def first_floor_goods_category_COSMO(self):
        """COSMO"""
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[11]/div/a')

    def second_level_locker(self):
        """置物柜"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[11]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[11]/ul/li[1]/a')
    def second_level_bookcase(self):
        """书柜"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[11]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[11]/ul/li[2]/a')
    def second_level_TVBench(self):
        """电视柜"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[11]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[11]/ul/li[3]/a')
    def second_level_Wardrobe(self):
        """衣柜·斗柜"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[11]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[11]/ul/li[4]/a')
    def second_level_Sideboard(self):
        """玄关柜"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[11]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[11]/ul/li[5]/a')
    def second_level_3Dcustomization(self):
        """3D定制"""
        self.dr.move_to_element('xpath->//*[@id="index_body"]/div[1]/ul/li[11]/div/a')
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[11]/ul/li[6]/a')

class zaozuoindex_familycard_tag(basepage.Page):
    # 11、新家卡
    def first_floor_goods_category_familycard(self):
        """新家卡"""
        self.dr.click('xpath->//*[@id="index_body"]/div[1]/ul/li[12]/div/a')