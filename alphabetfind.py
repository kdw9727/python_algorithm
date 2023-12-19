S = list(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"


for i in alphabet:
  if i in S:
    print(S.index(i))
  else:
    print(-1)
