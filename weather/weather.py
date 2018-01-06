import tkinter
import wc
import threading

class App(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.pList=[]
        self.p=tkinter.StringVar()
        self.createWidgets()

    def createWidgets(self):  #//界面优化
        self.places=tkinter.Entry(self,textvariable=self.p)
        self.places.pack(side='top')

        self.commit=tkinter.Button(self)
        self.commit["text"]='提交'
        self.commit["command"]=self.getWeather
        self.commit.pack(side='top')
        img = tkinter.PhotoImage(file = "img\loading.gif")
        
        self.weather = tkinter.Label(text='请输入天气',bg='red')
        self.weather.pack(side='top')

        self.loadingImg = tkinter.PhotoImage(file = "img\loading.gif")

    def getWeather(self):  #//todo 取得天气
     #  if len(self.pList) > 3
         #   self.pList.pop()
      #  self.pList.append(self.p.get()) //todo  关注列表
        if self.p:
            #self.weather["image"]=self.loadingImg
            thr = threading.Thread(target=self.wcWeather(),args=())
            thr.start()
        else:
            self.weather["text"]='您还没有输入地点'

    def wcWeather(self):
        w=wc.WeatherCrawl()
        code=w.getPlaceCode(self.p.get())
        if code is None:
            self.weather["text"]='你有病我有病'
        data=w.getWeather(code)
        word=''
        for i in data:
            for k in i:
                word += k
            word+='\n'
        self.weather["text"]=word

def setScreenSize(root):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    width=240
    height=400
    size = '%dx%d+%d+%d' % (width, height,
                            (screenwidth - width)/5*4,
                            (screenheight - height)/2)
    root.geometry(size)
    

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title('天气')
    setScreenSize(root)
    app=App()
    app.mainloop()
