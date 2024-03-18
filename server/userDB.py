import sqlite3

# 创建数据库连接，如果数据库不存在，将会在当前目录下创建一个名为userDB的数据库文件
conn = sqlite3.connect('userDB.db')

# 创建一个游标对象
c = conn.cursor()

# 使用游标对象的execute方法执行SQL语句
c.execute('''
    CREATE TABLE Users (
        code TEXT,
        name TEXT,
        password TEXT
    )
''')

# 提交事务
conn.commit()

# 关闭连接
conn.close()