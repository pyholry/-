import requests
import os
import time
from lxml import etree
from selenium import webdriver

class Spider():
    def __init__(self,**kwargs):
        '''private'''
        self.__Headers = {
            'Referer': 'http://btfox0.co/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
        }
        self.__key = kwargs['key']
        self.__num = kwargs['num']
        self.__startPage = 1
        self.__page = (self.__num//12)+1
        self.__magnetData = []
        self.__nameData = []
        self.__typeData = []
        self.__storageData = []
        self.__dateData = []
        '''public'''
        self.DirName = "磁力链爬虫"
        self.MainPage = "http://btfox0.co/s?wd="

    def getBranchData(self,page):
        self.Url = self.MainPage + self.__key + "&sort=time&page=" + str(page)
        resp = requests.get(url=self.Url,headers=self.__Headers)
        html = etree.HTML(resp.text)
        '''branch url'''
        self.branchUrl = html.xpath("//div[@class='thread_check']/div/a/@href")
        count = 0
        while count<=(len(self.branchUrl)-1):
            self.branchUrl[count] = "http://btfox0.co" + self.branchUrl[count]
            count+=1
        '''magnet uri'''
        temporaryListForMagnet = []
        for i in self.branchUrl:
            r = requests.get(url=i,headers=self.__Headers)
            innerHtml = etree.HTML(r.text)
            self.magnetURI = innerHtml.xpath("//textarea[@id='thread_share_text']/text()")
            for j in self.magnetURI:
                temporaryListForMagnet.append(j.strip())
        self.magnet = temporaryListForMagnet
        '''other data'''
        self.branchName = html.xpath("//div[@class='thread_check']/div/a/@title")
        '''以下待更新'''
        #self.branchMoreInformation = html.xpath("//div[@class='threadlist_note']/text()")#type;bit;date
        return

    def distribute(self):
        for i in range(1,self.__page+1):
            self.getBranchData(page=i)
            if not os.path.exists(self.DirName):
                os.mkdir(self.DirName)
            FileName = "%s磁力链%s.txt"%(self.__key,time.strftime("%Y_%m_%d_%H_%M_%S"))
            for j in range(0,len(self.magnet)):
                with open(self.DirName+"/"+FileName,'a') as f:
                    f.write("%s.\n"%(j+1))
                    f.write("标题:%s\n"%self.branchName[j])
                    f.write("磁力链接:%s\n\n"%self.magnet[j])

    def test(self):
        return

def main()->int:
    global spider
    key = input("输入关键词:")
    require = int(input("输入爬取条数m:(输出条数n=12*((m//12)+1))"))
    spider = Spider(key=key,num=require)
    spider.distribute()

    return 0

if __name__ == '__main__':
    print("磁力链爬虫1.0")
    print("-----------------欢迎-----------------")
    print("输入关键字与期盼获取磁力链条数，进行爬取，爬取所得数据保存在本脚本的同级目录名为“磁力链爬虫”的文件夹中")
    print("注意:若磁力链数据条数少于期盼条数，则会爬取期盼条数以内所有的磁力链")
    if main()==0:
        print("爬取完成！")
        input("按任意键退出...")






















