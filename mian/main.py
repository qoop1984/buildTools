#coding=GBK
from DBUtil.oracle import oracleUntils
class Untils:
    def __init__(self,path):
        from conf.confuration import loadconf
        #加载配置文件
        loadconf = loadconf()
        conf=loadconf.loadJson(path)
        if conf==None:
            raise ValueError('没有加载到配置文件')
        #查询已存在的数据
        self.conf=conf
        pass
    def saveConf(self):
        pass
    def saveCode(self):
        pass
    def bulidJar(self):
        pass
    def uploadjar(self):
        pass

if __name__ == '__main__':
    untils = Untils('..\\conf.json')
