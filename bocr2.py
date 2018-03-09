# -*- coding: UTF-8 -*-
import os
from aip import AipOcr
import json

warning_words = "牛"

# 定义常量
APP_ID = '9851066'
API_KEY = 'LUGBatgyRGoerR9FZbV4SQYk'
SECRET_KEY = 'fB2MNz1c2UHLTximFlC4laXPg7CVfyjV'

# 初始化AipFace对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = "./dddd.jpg"
def get_file_content(filePath):
	with open(filePath, 'rb') as fp:
		return fp.read()

# 定义参数变量
options = {
  'detect_direction': 'true',
  'language_type': 'CHN_ENG',
}

# 调用通用文字识别接口
#result = aipOcr.basicGeneral(get_file_content(filePath), options)
#print(json.dumps(result["words_result"][0]["words"]).decode("unicode-escape"))
#print result["words_result"]
try:
	while True:
		os.system("raspistill -o dddd.jpg -t 2 ")
		result = aipOcr.basicGeneral(get_file_content(filePath), options)
		print(json.dumps(result).decode("unicode-escape"))
#		print(json.dumps(result["words_result"][0]["words"]).decode("unicode-escape"))
		
#		result_nu = result["words_result_num"]
#
#		if result_nu != 0:
#			for ii in range(result_nu):
#				print(json.dumps(result["words_result"][ii]["words"]).decode("unicode-escape"))
#				if warning_words in json.dumps(result["words_result"][ii]["words"]).decode("unicode-escape"):
#					print("警告 危险 警告警告警告！！！！！！！")
#				print(json.dumps(result).decode("unicode-escape"))

except KeyboardInterrupt:
	print "log out by keyboard"
