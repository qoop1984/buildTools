# coding=GBK
import cx_Oracle,sys,os
print sys.getdefaultencoding()
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'

class oracleUntils:
    def __init__(self,url):
        self.url=url
        self.con=cx_Oracle.connect(url)
    def executeQuery(self,sql):
        cur = self.con.cursor()  # 打开游标
        cur.execute(sql)
        result = cur.fetchall()
        print '数据库记录数'.decode('GBK') + str(cur.rowcount)
        for row in result:
            print row[0].decode('GBK')
            # print row
        cur.close()
        return result
    def insertOrUpdate(self,sql,para):
        cur = self.con.cursor()  # 打开游标
        result=cur.execute(sql,para)
        print result
        self.con.commit()
        cur.close();

    def insertOrUpdateBySql(self, sql):
        cur = self.con.cursor()  # 打开游标
        result = cur.execute(sql)
        print result
        self.con.commit()
        cur.close();

    def executeQueryByBindVar(self,sql,disc):
        cur = self.con.cursor()  # 打开游标
        cur.prepare(sql)
        cur.execute(None,disc)
        result = cur.fetchall()
        print '数据库记录数'.decode('GBK') + str(cur.rowcount)
        for row in result:
            print row[0].decode('GBK')
            # print row
        cur.close()
        return result

    def insertOrUpdateByVar(self, sql, disc):
        cur = self.con.cursor()  # 打开游标
        cur.prepare(sql)
        cur.execute(None, disc)
        self.con.commit()
        cur.close();
    def close(self):
        self.con.close();




if __name__=='__main__':
    oracleUntils=oracleUntils('channel/channel123@//10.7.5.74:1521/AIMCS')
    #result=oracleUntils.execute('SELECT  * FROM TMP_REQ_CODE  c order by c.req_id')
    #oracleUntils.insertOrUpdate('insert into TMP_REQ_CODE values(:1,:2,:3)',['李剑锋测试','9999','code'])
    #oracleUntils.insertOrUpdateBySql('update TMP_REQ_CODE set REQ_NAME=\'李剑锋测试\'where REQ_ID=\'9999\'' )
    oracleUntils.executeQueryByBindVar('SELECT  * FROM TMP_REQ_CODE  c where c.req_id=:id order by c.req_id',{'id':'9999'})