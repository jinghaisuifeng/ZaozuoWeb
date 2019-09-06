#coding=utf-8

import codecs
import os
import xlrd
from config import globalparam
from selenium.common.exceptions import NoSuchElementException

data_path = globalparam.data_path
def get_xls_to_dict(xlsname, sheetname):
	"""
	读取excel表结果为dict
	第一行为字典的key，下面的为值
	return [{'title':'1','user':'root'},{'title':'2','user':'xiaoshitou'}]
	"""
	# dataresult = []
	# result = []
	datapath = os.path.join(data_path,xlsname)
	xls1 = xlrd.open_workbook(datapath)
	table = xls1.sheet_by_name(sheetname)
	# for i in range(0,table.nrows):
	# 	dataresult.append(table.row_values(i))
	dataresult = [table.row_values(i) for i in range(0, table.nrows)]
	#将list转化成dict
	# for i in range(1,len(dataresult)):
	# 	temp = dict(zip(dataresult[0],dataresult[i]))
	# 	result.append(temp)
	result = [ dict(zip(dataresult[0], dataresult[i])) for i in range(1, len(dataresult))]
	print(result)
	return result

def get_url_data(title):
	"""
	读取txt文件，转化成dict;读取url和导航栏的对应关系
	将txt转化成一个字典:下单=>/admin/order/index
	{'title1':'url1','下单':'/admin/order/index'}
	"""
	name = 'urlsource.txt'
	txtpath = os.path.join(data_path,name)
	with codecs.open(txtpath,'r',encoding='utf-8') as f:
		txtcontent = f.readlines()
	txtdict = dict([txt.strip().replace('\ufeff','').split('=>') for txt in txtcontent])
	return txtdict[title]

def get_xls_to_list(excelname, sheetname):
	"""
	读取excel表，返回一个list,只是返回第一列的值
	return [1,2,3,4,5]
	"""
	datapath = os.path.join(data_path, excelname)
	print(datapath)
	excel = xlrd.open_workbook(datapath)#打开xls文件，并赋值给excel
	table = excel.sheet_by_name(sheetname)#选取一个工作表进行读取
	result = [int(table.row_values(i)[0])for i in range(1, table.nrows)]
	#result = [table.row_values(i)[0].Strip() for i in range(1, table.nrows)]
	#list内值进行转换
	#  for result in result():
	# if isinstance(result,float):
	# 	if result == int(result):
	# 		result = int(result)
	# 		#result = str(result)
	return result

def get_login_input_username():
	data_username = get_xls_to_list('user.xlsx', 'username')
	for username in range(len(data_username)):
		return data_username[username]


def get_login_input_password():
	data_password = get_xls_to_list('user.xlsx', 'password')
	for password in range(len(data_password)):
		return data_password[password]

def open_excel(excelname):
	try:
		datapath = os.path.join(data_path, excelname)
		excel = xlrd.open_workbook(datapath)  # 打开xls文件，并赋值给excel
		return excel
	except Exception as e:
		print(str(e))
def excel_table_byindex(excelname,colnameindex=0,by_index=0):
	data = open_excel(excelname)
	table = data.sheets()[by_index]
	nrows = table.nrows
	colnames = table.row_values(colnameindex)
	list = []
	for rownum in range(1,nrows):
		row = table.row_values(rownum)
		if row:
			app = {}
			for i in range(len(colnames)):
				app[colnames[i]] = row[i]
			list.append(app)
	print(list)
	return list

if __name__=='__main__':
	res = get_xls_to_list('user.xlsx','username')
	print(res)




