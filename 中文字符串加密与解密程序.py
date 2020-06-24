from urllib.parse import quote
from urllib.parse import unquote
import re
import os

file_name = '中文字符串加密与解密程序历史记录保存.txt'

def read_history_file(file_name):
    try:
        with open(file_name) as f:
            contents = f.read()
            print(contents)
    except:
        print('出现错误...')

def save_encryption(before_encryption,after_encryption):
    try:
        with open(file_name,'a') as f:
            f.write('\n\n加密的字符串:' + before_encryption)
            f.write('\n加密结果:' + after_encryption)
            print('保存成功!!')
    except:
        print('保存失败')
        repeat = input('是否要再次尝试保存：')
        if repeat == '是':
            save_encryption(before_encryption=before_encryption,after_encryption=after_encryption)
        else:
            pass

def save_decrypt(before_decrypt, after_decrypt):
    try:
        with open(file_name, 'a') as f:
            f.write('\n\n解密的编码:' + before_decrypt)
            f.write('\n解密结果:' + after_decrypt)
            print('保存成功!!')
    except:
        print('保存失败')
        repeat = input('是否要再次尝试保存：')
        if repeat == '是':
            save_decrypt(before_decrypt=before_decrypt,after_decrypt=after_decrypt)
        else:
            pass

class Encryption():
    ##加密##
    def __init__(self,word_e):
        self.word_e = word_e

    def encryption(self):
        encryption_result = re.sub('[https://www.baidu.com/s?wd=]', ' ', quote(self.word_e))
        print('加密结果： ' + re.sub('[https://www.baidu.com/s?wd=]', ' ', quote(self.word_e)))
        save_data_e = input('是否要保存本次加密数据：')
        if save_data_e == '是':
            save_encryption(before_encryption=self.word_e,after_encryption=encryption_result)
        else:
            pass

class Decrypt():
    ##解密##
    def __init__(self,word_d):
        self.word_d = word_d

    def decrypt(self):
        decrypt_result = re.sub('[https://www.baidu.com/s?wd=]',' ', unquote(self.word_d))
        print('解密结果： ' + re.sub('[https://www.baidu.com/s?wd=]',' ', unquote(self.word_d)))
        save_data_d = input('是否要保存本次解密数据：')
        if save_data_d == '是':
            save_decrypt(before_decrypt=self.word_d,after_decrypt=decrypt_result)
        else:
            pass

def all_function(answer):
    if answer == 1:
        word_e = input('你需要加密的字符串：')
        e = Encryption(word_e)
        e.encryption()
    elif answer == 2:
        word_d = input('你需要解密的编码：')
        d = Decrypt(word_d)
        d.decrypt()

print('中文字符串加密与解密程序'
          '\n\n使用说明：本程序用于中文字符串的加密与编码解密。'
      '\n\n本程序保存的历史记录在该程序的同级目录下')

while True:
    try:
        answer = int(input('\n需要加密字符串输入1,需要解密字符串输入2：'))
        all_function(answer)
        read_history = input('是否要查看历史保存记录：')
        if read_history == '是':
            read_history_file(file_name=file_name)
        else:
            pass
        run_again = input('\n是否想再次运行?是/否')
        if run_again == '是':
            continue
        else:
            break
    except:
        print('程序报错...'
              '\n请检查你的输入是否符合要求')
        break

print('\n欢迎下次再次运行'
              '\n\n按任意键退出...')
input()



































