#coding=GBK
from DBUtil.oracle import oracleUntils
import decimal
import sys;
reload(sys);
sys.setdefaultencoding('GBK');
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
        self.printConf();

    def printConf(self):
        conf=self.conf
        if conf == None:
            raise ValueError('�����ļ���ϢΪ��')
        project = conf['projects']
        if len(project) > 0:
            print  len(project)
            for key,value in project.items():
                print '��Ŀ��Ϣ��'+ key

                for key,value in value.items():
                    print key,value
        else:
            print  '�����ļ���û����Ŀ��Ϣ'
        num = input('��ѡ����Ŀ'.decode('GBK'))

    def bulidJar(self):
        from buildJar.warBuilder import Builder
        builder=Builder()
        print self.conf
        sql = builder.getBuildSql('chnl_beij', '123')
        builder.build('D:\AeWorkspace\chnl_beij\web', sql)
    def uploadjar(self):
        pass

if __name__ == '__main__':
    untils = Untils('.\\conf.json')
    untils.bulidJar();