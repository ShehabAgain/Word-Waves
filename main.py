
import random
k=random.randint(10,17)
p="i"*k
a="H"+p


while True:
  if ((n:=len(a))>1):
    print(a)
    a=a[:-1]
  elif ((n:=len(a))>=1 and (n:=len(a))<=7):
      for i in range(k):
        a+="i"
        print(a)
    