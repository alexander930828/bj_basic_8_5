#1

a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    print(int(a/(c-b)+1))


# 2

n = int(input())

c = 1

while n > 1:
    n -= (6 * c)
    c += 1

print(c)


#3

X = int(input())

line = 1

while X > line:
    X -= line
    line += 1

if line % 2 == 0: # 짝수 줄
    a = X
    b = line - X + 1

else:
    a = line - X + 1
    b = X

print(a, '/', b, sep='')