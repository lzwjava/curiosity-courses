def f(n):
  if n < 2:
     return n
  else:
     return f(n-1) + f(n-2)
      
  
print(f(10))