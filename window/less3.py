#coding=GBK
import wx
class InsertFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Frame With Button',size=(300,100))
        panel=wx.Panel(self)#��������
        button=wx.Button(panel,label='Close',pos=(125,10),size=(50,50))#������ť��ӵ�����
        self.Bind(wx.EVT_BUTTON,self.OnCloseMe,button)#�󶨰�ť�ĵ����¼�
        self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)#����󶨴��ڵĹر��¼�
    def OnCloseMe(self,event):
        self.Close(True)
    def OnCloseWindow(self,event):
        self.Destroy()
if __name__=='__main__':
    app=wx.PySimpleApp()#����app
    frame=InsertFrame(parent=None,id=-1)#����frame
    frame.Show()
    app.MainLoop()






