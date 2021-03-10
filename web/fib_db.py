import sqlite3

v = []
for x in range(1000000):
   v.append(-1)

def fplus(n):
   if n > 800:         
      fplus(n-800)
      return f(n)
   else:
      return f(n)

def f(n):
   if v[n] != -1:
      return v[n]
   else:
      a = 0
      if n < 2:
         a = n
      else:
         a = f(n-1) + f(n-2)
      v[n] = a
      return v[n]

def create_table(cur: sqlite3.Connection):
    cur.execute('CREATE TABLE IF NOT EXISTS vs(v text)')

def read():
    con = sqlite3.connect('fib.db')
    cur = con.cursor()    
    create_table(cur)
    i = 0
    for row in cur.execute('SELECT * FROM vs'):
        v[i] = int(row[0])
        i += 1
    con.close()

def save():
    con = sqlite3.connect('fib.db')
    cur = con.cursor()
    create_table(cur)
    for vv in v:
        if vv != -1:
            cur.execute("INSERT INTO vs VALUES('" +str(vv) + "')")
        else:
            break
    con.commit()
    con.close()

read()
# for i in range(10):
#     print(v[i])
fplus(100)
save()
            
