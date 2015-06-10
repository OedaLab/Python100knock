# 値が, 3の倍数，または，3が付く数のとき，1を返す．
def checkNum(num):
    f = 0
    if num%3==0:
        f = 1
    else:
        while(num>0):
            if num%10==3:
                f = 1
                break
            num = int(num/10)
    return f

print('調べる数を入力してください.')
print('num=', end='')
num = int(input())

print('')
for i in range(1,num+1):

    print('%5d'%(i), end='')

    f = checkNum(i)

    if f==1:
        print(' : いまでしょ!')
    else:
        print(' : いつやるか？')
