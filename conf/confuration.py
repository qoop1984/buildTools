# coding=utf-8
import types
class loadconf():

    def loadJson(self, filename):
        import json
        with open(filename) as json_file:
            data = json.load(json_file)
            print type(data)
            return data

    def loadXml(self, filename):
        pass


    def loadpath(self, filename,type):
        fun=loadconf.fileTypes.get(type)
        if(fun==None):
            raise ValueError('没有对应文件的解析方法')
        else:
            fun(filename)

    fileTypes = {'json': loadJson, 'xml': loadXml}
    def __init__(self):
        print '初始化'
    def loadJsonConf(self,filename):
        if type(filename) ==types.StringType:
            loadconf(filename)
        else :
            raise ValueError('请传入正确的路径')


if __name__=='__main__':
    utils=loadconf();
    utils.loadJson('..\\conf.json')