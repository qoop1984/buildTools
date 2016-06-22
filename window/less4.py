#coding=GBK
import wx
import wx.py.images as images
class ToolbarFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id)
        panel=wx.Panel(self)
        panel.SetBackgroundColour('White')
        statusBar=self.CreateStatusBar()#����״̬��
        toolbar=self.CreateToolBar()#����������
        toolbar.AddSimpleTool(wx.NewId(),images.getPyBitmap(),'New',"Long help for 'New")
        toolbar.Realize()
        menuBar = wx.MenuBar()#�����˵���
        menu1=wx.Menu()
        menuBar.Append(menu1,"&File")
        menu2= wx.Menu()
        #�����˵���Ŀ
        menu2.Append(wx.NewId(),"&Copy","Copy in status bar")
        menu2.Append(wx.NewId(), "&Cut", "")
        menu2.Append(wx.NewId(), "Paste", "")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(), "& Options...", "Display Options")
        menuBar.Append(menu2, "&Edit")
        self.SetMenuBar(menuBar)
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame= ToolbarFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()



