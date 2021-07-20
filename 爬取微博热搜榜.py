import requests
import os
import time
from lxml import etree

headers = {
    'Referer': 'https://s.weibo.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
}

def xp_news(html):
    news = html.xpath('//tr/td/a[@target="_blank"]/text()')
    return news

def xp_href(html):
    hf = html.xpath('//tr/td/a[@target="_blank"]/@href')
    return hf

def save_data(news,href):
    DirName = "微博热搜榜爬虫"
    FileName = "微博热搜榜爬虫.txt"
    if not os.path.exists(DirName):
        os.mkdir(DirName)
    n = 0
    with open(DirName + '/' + FileName, 'a') as f:
        f.write("查询时间:"+str(time.ctime())+"\r")
    for i in news:
        try:
            with open(DirName +'/'+ FileName,'a',encoding='gb18030', errors='ignore') as f:
                f.write(str(n+1)+'\r')
                f.write(i+'\r')
                f.write("跳转链接:"+href[n])
                f.write("\r")
        except:
            pass
        n+=1
    return None

def main():
    url = "https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6"
    try:
        resp = requests.get(url=url,headers=headers)
    except:
        print("请求网页错误...")
    html = etree.HTML(resp.text)
    news = xp_news(html)
    href = xp_href(html)
    save_data(news,href)

    return 0

if __name__ == '__main__':
    main()













