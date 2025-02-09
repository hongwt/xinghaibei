str =' 吃俺老孙一棒!'
str_utf_8 = str.encode('UTF-8')
str_gbk = str.encode('GBK')
print('UTF-8编码：', str_utf_8)
print('GBK编码：', str_gbk)
print('UTF-8解码：', str_utf_8.decode('UTF-8'))
print('GBK解码：', str_gbk.decode('GBK'))