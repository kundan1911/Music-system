import sqlite3 as sq
con=sq.connect('data.db')
c=con.cursor()
# c.execute(""" INSERT INTO data VALUES('kundan',19,'fgsv')

# """)
# many=[('a',18,'b'),
# ('c',18,'D'),
# ('e',18,'f')
# ]
# c.executemany("INSERT INTO data VALUES(?,?,?)",many)
# c.execute("delete from data where rowid=2")
# con.commit()
print(c.execute("select * from data order by rowid desc "))
items=c.fetchall()
for item in items:
    print(item)
con.commit()
con.close()