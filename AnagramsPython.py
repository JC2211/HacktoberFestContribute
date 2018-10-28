a=list(input())
b=list(input())
f=0
for i in (a):
  if i in b:
    b.remove(i)
  else:
    f=1
    break
if len(b)==0:
  if f==0:
    print("Yes")
  else:
    print("No")
else:
  print("No")
