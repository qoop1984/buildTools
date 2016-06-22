#coding=GBK
from DBUtil.oracle import oracleUntils
import decimal
import sys;
reload(sys);
sys.setdefaultencoding('GBK');
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
        self.printConf();

    def printConf(self):
        conf=self.conf
        if conf == None:
            raise ValueError('配置文件信息为空')
        project = conf['projects']
        if len(project) > 0:
            print  len(project)
            for key,value in project.items():
                print '项目信息：'+ key

                for key,value in value.items():
                    print key,value
        else:
            print  '配置文件中没有项目信息'
        num = input('请选择项目'.decode('GBK'))

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