print("10進数を2進数に変換します．")
print('num=', end='')
num = int(input())

bits = []
while(num>0):
    if (num%2==0):
        bits.append(0)
    else:
        bits.append(1)
    num = num//2 # 整数除算演算子 演算結果の小数点以下は切り捨て

bits.reverse()
for i in bits:
    print(i, end='')
print()
