#-*-coding=utf-8-*-
__author__ = 'rocchen'
from bs4 import BeautifulSoup
import urllib2,sys,StringIO,gzip,time
reload(sys)
sys.setdefaultencoding('utf-8')
class Xitek():
    def __init__(self):
        self.url="http://photo.xitek.com/"
        user_agent="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
        self.headers={"User-Agent":user_agent}
        self.last_page=self.__get_last_page()

    def __getContent(self,url):
        req=urllib2.Request(url,headers=self.headers)
        resp=urllib2.urlopen(req)
        content=resp.read()
        #print content
        data=StringIO.StringIO(content)
        gzipper = gzip.GzipFile(fileobj=data)
        html=gzipper.read()
        return html


    def __get_last_page(self):
        html=self.__getContent(self.url)
        bs=BeautifulSoup(html,"html.parser")
        page=bs.find_all('a',class_="blast")
        last_page=page[0]['href'].split('/')[-1]
        return  int(last_page)

    def __download(self,url):
        html=self.__getContent(url)
        bs=BeautifulSoup(html,"html.parser")
        element_link=bs.find_all('div',class__="element")
        for href in element_link:
            print href.childrenp[0]['href']




    def getPhoto(self):
        start=0
        #use style/0
        photo_url="http://photo.xitek.com/style/0/p/"
        for i in range(start,self.last_page+1):
            url=photo_url+str(i)
            #print url
            time.sleep(1)
            self.__download(url)


def main():
    obj=Xitek()
    obj.getPhoto()


if __name__=="__main__":
    main()




