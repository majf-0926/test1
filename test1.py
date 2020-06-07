#!/usr/bin/python3
import re

words = input("请输入一个英文单词(可包含空格)：")
output = ""
pattern = re.compile(r'[^A-Za-z ]')
result = pattern.findall(words)
if result:
   print (result)
   print("输入错误！输入只能为英文单词字符和空格！")
else:
   print ("No match!!")
   words = words.upper()
   lw = len(words)
   for i in range(lw):
       if words[i] in "ABC":
           output += "2"
       elif words[i] in "DEF":
           output += "3"
       elif words[i] in "GHI":
           output += "4"        
       elif words[i] in "JKL":
           output += "5"        
       elif words[i] in "MNO":
           output += "6"
       elif words[i] in "PQRS":
           output += "7"
       elif words[i] in "TUV":
           output += "8"
       elif words[i] in "DEF":
           output += "9"
       else:
           output += "0"
   print("输出是：",output)
