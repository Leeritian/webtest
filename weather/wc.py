#crwal weather
import requests
import urllib
import datetime
from bs4 import BeautifulSoup

class WeatherCrawl():
    placeurl = 'http://toy1.weather.com.cn/search?cityname=%s'
    wurl_1 = 'http://www.weather.com.cn/weather1d/%s.shtml'
    wurl_2 = 'http://www.weather.com.cn/weather/%s.shtml'
    wurl_3 = 'http://www.weather.com.cn/weather15d/%s.shtml'
    wurl_4 = 'http://www.weather.com.cn/weather40d/%s.shtml'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    
    def __init__(self):
        pass

    def getPlaceCode(self,place):
        p=urllib.parse.quote(place)
        link = self.placeurl % p
        r=requests.get(link,headers=self.headers)
        print('code requests ok: ')
        text = r.text[r.text.find('{'):-2]
        dic=eval(text)
        code=dic[0]['ref'][0:9]
        print(code)
        return code

    def getWeather(self,code):
        text=self.crawl(code)
        tw=self.parse(text)
        self.fout(tw)
        return tw

    def fout(self,tw):
        with open('fd.txt','a',encoding='utf-8') as f:
            for i in tw:
                f.write(str(i)+'\n')
        
    def crawl(self,code):
        r=requests.get(self.wurl_1 % code,headers=self.headers)
        if r.status_code  != 200:
            return 'error'
        print('weather requests ok! ')
        r.encoding='utf-8'
        return r.text

    def parse(self,text):
        bs=BeautifulSoup(text,'html.parser')
        try:
            data=bs.find_all('script')[2].get_text()
        except IndexError:
            return 'error:不存在的'
        today_day=datetime.datetime.now().strftime('%d')+'日'
        tomorrow_day=datetime.datetime.now().strftime('%d')+'d'
        data = data[data.find('["'):data.find(',%s' % tomorrow_day)]
        data = [i.strip('"') for i in data.strip("[]").split('",')]
        tw=[]
        for i in range(0,len(data)):
            data[i]=data[i].strip().split(',')
            del data[i][6],data[i][1]
            if today_day in data[i][0]:
                tw.append(data[i])
        return tw
 
if __name__ =='__main__':
    w=WeatherCrawl()
    s = w.getPlaceCode('侯马')
    print(s)
    k=w.getWeather(s)
    print(k)

