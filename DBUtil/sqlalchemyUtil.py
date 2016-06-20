# coding=GBK
from sqlalchemy import Column,String,create_engine,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class TmpReqCode(Base):
    #����
    __tablename__='TMP_REQ_CODE'
    #��Ľṹ
    reqName=Column(String(200))
    reqId=Column(Integer)
    code_dir = Column(String(200))
#��ʼ�����ݿ�����
engine=create_engine('oracle://channel/channel123@//10.7.5.74:1521/AIMCS')
#����DBSession����:
DBSession = sessionmaker(bind=engine)

# ����Session:
session = DBSession()
# ����Query��ѯ��filter��where������������one()����Ψһ�У��������all()�򷵻�������:
code = session.query(TmpReqCode).filter(TmpReqCode.reqId=='142').one()
# ��ӡ���ͺͶ����name����:
print 'type:', type(code)
print 'name:', TmpReqCode.reqName
# �ر�Session:
session.close()




