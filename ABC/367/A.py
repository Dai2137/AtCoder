A,B,C=map(int,input().split())

if B<C:
  if C<A or A<B:
    print("Yes")
  else:
    print("No")
  exit()
else:
  if C<A<B:
    print("Yes")
  else:
    print("No")
