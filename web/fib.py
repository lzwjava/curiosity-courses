v = []
for x in range(1000000):
   v.append(-1)

def read():
   file = open('fib_v', 'r')
   s = file.read()
   if len(s) > 0:
      lines = s.split('\n')
      if (len(lines) > 0):
        for i in range(len(lines)):
           v[i] = int(lines[i])   

def save():
   file = open('fib_v', 'w')
   s = ''
   start = True
   for vv in v:
      if vv == -1:
         break      
      if start == False:
         s += '\n'
      start = False   
      s += str(vv)
   file.write(s)
   file.close()

def fcache(n):
   x = fplus(n)
   save()
   return x

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

read()
fcache(10)
save()
