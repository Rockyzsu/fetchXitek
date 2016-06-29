#-*-coding=utf-8-*-
__author__ = 'rocchen'
from bs4 import BeautifulSoup
import urllib2,sys,StringIO,gzip,time,random,re
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
        print html
        return html

    def __getContentNoZip(self,url):
        req=urllib2.Request(url,headers=self.headers)
        resp=urllib2.urlopen(req)
        time.sleep(2*random.random())
        content=resp.read()

        #print content
        #data=StringIO.StringIO(content)
        #gzipper = gzip.GzipFile(fileobj=data)
        #html=gzipper.read()
        print content
        return content


    def __get_last_page(self):
        html=self.__getContent(self.url)
        bs=BeautifulSoup(html,"html.parser")
        page=bs.find_all('a',class_="blast")
        last_page=page[0]['href'].split('/')[-1]
        return  int(last_page)

    def __download(self,url):
        p=re.compile(r'photoid')
        html=self.__getContent(url)
        #print html
        bs=BeautifulSoup(html,"html.parser")
        print bs.title
        element_link=bs.find_all('div',class_="element")
        print len(element_link)
        k=1
        for href in element_link:

            #print type(href)
            #print href.tag
            '''
            if href.children[0]:
                print href.children[0]
            '''
            t=0

            for i in href.children:
                #if i.a:
                if t==0:
                    #print k
                    link=i['href']
                    print link
                    if p.findall(link):
                        full_path=self.url[0:len(self.url)-1]+link
                        sub_html=self.__getContent(full_path)
                        bs=BeautifulSoup(sub_html,"html.parser")
                        final_link=bs.find('img',class_="mimg")['src']
                        #time.sleep(2*random.random())
                        print final_link
                    #k=k+1
                #print type(i)
                #print i.tag
                #if hasattr(i,"href"):
                    #print i['href']
                #print i.tag
                t=t+1
                #print "*"

            '''
            if href:
                if href.children:
                    print href.children[0]
            '''
            #print "one element link"



    def getPhoto(self):
        '''
        start=0
        #use style/0
        photo_url="http://photo.xitek.com/style/0/p/"
        for i in range(start,self.last_page+1):
            url=photo_url+str(i)
            print url
            #time.sleep(1)
            self.__download(url)
        '''

        url="http://photo.xitek.com/style/0/p/0"
        self.__download(url)
        '''
        url="http://photo.xitek.com/style/0/p/0"
        #html=self.__getContent(url)
        #url="http://photo.xitek.com/"
        html=self.__getContentNoZip(url)
        print html
        '''
def main():
    obj=Xitek()
    obj.getPhoto()


if __name__=="__main__":
    main()




