# coding=GBK
from sqlalchemy import Column,String,create_engine,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class TmpReqCode(Base):
    #表名
    __tablename__='TMP_REQ_CODE'
    #表的结构
    reqName=Column(String(200))
    reqId=Column(Integer)
    code_dir = Column(String(200))
#初始化数据库连接
engine=create_engine('oracle://channel/channel123@//10.7.5.74:1521/AIMCS')
#创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
code = session.query(TmpReqCode).filter(TmpReqCode.reqId=='142').one()
# 打印类型和对象的name属性:
print 'type:', type(code)
print 'name:', TmpReqCode.reqName
# 关闭Session:
session.close()




