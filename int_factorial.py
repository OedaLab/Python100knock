n = 0
ans = 1

if n == 0:
    ans = 1
else:
    for i in range(0,n-1):
        ans = ans*(n-i)

print(ans)
