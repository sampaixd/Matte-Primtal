import sys

s= 61

if (len(sys.argv)>1):
  s=int(sys.argv[1])

u=4
n=pow(2,s)-1
print (f"n=2^{s}-1={n}\n")

for k in range(1,s-1):
  u=((u*u)-2) %n
  print (u,end=' ')

if (u==0):
  print ("\n\nIt is prime")
else:
  print ("\n\nIt is not prime")