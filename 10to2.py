print("10進数を2進数に変換します．")
print('num=', end='')
num = int(input())

bits = []
while(num>0):
    if (num%2==0):
        bits.append(0)
    else:
        bits.append(1)
    num = int(num/2)

bits.reverse()
for i in bits:
    print(i, end='')
print()
