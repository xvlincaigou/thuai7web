import sqlite3

# 连接到数据库
conn = sqlite3.connect('userDB.db')
c = conn.cursor()

# 执行查询
c.execute('SELECT * FROM Users')

# 打印查询结果
for row in c.fetchall():
    print(row)

# 关闭连接
conn.close()