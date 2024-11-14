N =int(input())
a = N // 100
b = (N - a*100) // 10
c = N%10
print(b*100+c*10+a)
print(c*100+a*10+b)