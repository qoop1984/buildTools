#coding=GBK
import wx
class Frame(wx.Frame):
    def __init__(self, image, parent=None, id=-1,pos=wx.DefaultPosition,title='Hello, wxPython!'):
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)

class App(wx.App):  # 5 wx.App子类
    def OnInit(self):
        image = wx.Image('C:\\Users\\李剑锋\\Desktop\\a03c89113c966b90abe711619af0d962.jpeg', wx.BITMAP_TYPE_JPEG)
        self.frame = Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

def main():  # 7
    app = App()
    app.MainLoop()
if __name__ == '__main__':
    main()