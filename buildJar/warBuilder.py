#coding=GBK
from DBUtil import oracle
class Builder:
    def __init__(self):
        pass
    def getBuildSql(self,projectName,version):
        sql=  'select \'jar -cvf '+projectName+'@\'||t.req_name|| to_char(sysdate,\'yyyymmdd\')||\'_'+version+'.war \'|| replace(wmsys.wm_concat(t.code_dir),\',\',\' \') jar_command'
        sql+= ' from TMP_REQ_CODE t where t.req_id=\'472\'group by t.req_name '
        print sql
        return sql
    def build(self,workPath,sql):
        from DBUtil.oracle import oracleUntils
        oracleUntils=oracleUntils('channel/channel123@//10.7.5.74:1521/AIMCS')
        result = oracleUntils.executeQueryOneColb(sql)
        print result.decode('GBK')
        self.buildWar(result.decode('GBK'),workPath)

    def buildWar(self,cmd,workpath):
        import os
        #换目录
        os.chdir(workpath);
        #当前目录
        print os.getcwd()
        result=os.popen(cmd).readlines()
        print result[0].decode('GBK')




if __name__=='__main__':
    builder=Builder()
    sql = builder.getBuildSql('chnl_beij','123')
    builder.build('D:\AeWorkspace\chnl_beij\web',sql)
    print

