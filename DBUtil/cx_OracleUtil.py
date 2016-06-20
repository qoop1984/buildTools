# coding=utf-8
import cx_OracleUtil

con=cx_OracleUtil.connect('channel/channel123@//10.7.5.74:1521/AIMCS')
cur=con.cursor()
cur.execute('select * from departments order by department_id') #execute() 方法分析并执行语句。
