v = []
for x in range(1000):
   v.append(-1)

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

n = input("n:")
n = int(n)
i = 0
while i < n:   
  print(f(i), end=" ")
  i = i + 1

print()