import sys

change = (5000, 1000, 500, 100, 50, 10, 5, 1)

print('おつりを計算するので，おつりの金額を入力してください:')
money = int(input())
if money>=10000:
    print('おつりは10000円未満を入力してください.')
    sys.exit()
    
pay = [0 for i in range(len(change))]

ct = 0;
while(money>0):
    print(ct)
    if money >= change[ct]:
        pay[ct] = money//change[ct]
    if pay[ct]>0:
        money -= change[ct] * pay[ct]
    ct += 1

for (i, val) in enumerate(pay):
    print('%5d:%2d' %(change[i], val))
