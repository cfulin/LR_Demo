# coding:utf-8
import pymssql
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class MSSQL:
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    # mssql_host, mssql_user, mssql_pw, mssql_db
    def mssql(self):
        if not self.db:
            raise (NameError, "There is no set up the database information")
        if(self.pwd == self.user == ""):
            self.conn = pymssql.connect(host=self.host, database=self.db, charset='utf8')
        else:
            self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset='utf8')
        # getcursorpos
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "database connection failed")
        else:
            return cur

    def test(self):
        cur = self.mssql()
        cur.execute("select count(*) from EngLogins")
        idNum = cur.fetchone()[0]
        cur.executemany("insert into EngLogins(EngId, EngName) values (%d, %s)",
            [(idNum + 1, 'John Smith'),
             (idNum + 2, 'Jane Doe'),
             (idNum + 3, 'Mike T.')])
        #  [(1, 'John Smith'), (2, 'Jane Doe'), (3, 'Mike T')]
        self.conn.commit()

        # cur.execute(u"SELECT * FROM dbo.t_Task".encode('gb2312'))  #如果你的表名是中文
        cur.execute('select top 1 * from [dbo].[Englogins]')

        row = cur.fetchone()
        print (row)
        while row:
            print("ID = %d, Name = %s" % (row[0], row[1]))
            row = cur.fetchone()
        # 如果update/delete/insert记得要conn.commit()
        # 否则数据库事务无法提交
        # data = cur.fetchall()
        # print (data)

        cur.close()
        self.conn.close()


def main():
    conn_mssql = MSSQL('.', '', '', 'EngManager')
    # conn_mssql.mssql()
    conn_mssql.test()


if __name__ == '__main__':
    main()
