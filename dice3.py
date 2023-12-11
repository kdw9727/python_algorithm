first, second, third = map(int, input().split())

if (first == second == third):
  print(first * 1000 + 10000)
elif ((first == second) or (first == third)):
  print(first * 100 + 1000)
elif second == third:
  print(1000+second * 100) 
else:
  print(max(first,second,third)*100)
       