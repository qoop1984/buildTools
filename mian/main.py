#coding=GBK
from DBUtil.oracle import oracleUntils
class Untils:
    def __init__(self,path):
        from conf.confuration import loadconf
        #���������ļ�
        loadconf = loadconf()
        conf=loadconf.loadJson(path)
        if conf==None:
            raise ValueError('û�м��ص������ļ�')
        #��ѯ�Ѵ��ڵ�����
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
