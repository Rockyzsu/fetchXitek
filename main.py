#-*-coding=utf-8-*-
__author__ = 'rocchen'
from bs4 import BeautifulSoup
import urllib2,sys,StringIO,gzip
reload(sys)
sys.setdefaultencoding('utf-8')
class Xitek():
    def __init__(self):
        self.url="http://photo.xitek.com/"
        user_agent="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
        self.headers={"User-Agent":user_agent}


    def get_last_page(self):
        req=urllib2.Request(self.url,headers=self.headers)
        resp=urllib2.urlopen(req)
        content=resp.read()
        #print content

        data=StringIO.StringIO(content)
        gzipper = gzip.GzipFile(fileobj=data)
        html=gzipper.read()
        #print html


        bs=BeautifulSoup(html,"html.parser")
        title=bs.title.string
        #print title
        page=bs.find_all('a',class_="blast")
        #print type(page)
        '''
        for i in page:
            print i['href']
        '''

        last_page=page[0]['href'].split('/')[-1]
        print last_page

def main():
    obj=Xitek()
    obj.get_last_page()

if __name__=="__main__":
    main()




