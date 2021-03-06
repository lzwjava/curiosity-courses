def f(n):
  if n < 2:
     return n
  else:
     return f(n-1) + f(n-2)
      
i = 0
while i < 20:   
  print(f(i), end=" ")
  i = i + 1