def f(n):
  if n < 2:
     return n
  else:
     return f(n-1) + f(n-2)
      
i = input("n:")
i = int(i)
while i < 20:   
  print(f(i), end=" ")
  i = i + 1

print()