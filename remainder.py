list = []
for i in range(10):
  num = int(input())
  remainder = num % 42
  list.append(remainder)

print(len(set(list)))
