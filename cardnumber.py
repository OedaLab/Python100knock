import random

num = random.randint(3, 12)
card = [random.randint(0, 9) for i in range(num)]

print('num=', num)
print('card=', card)

# 降順に並び替える
card.sort() # 昇順に並び替え
card.reverse() # そしてlist内容を逆順に並び替える
print(card)

# 一番目に大きな値
no1val = 0
for i in card:
    no1val *= 10
    no1val += i

print('No1 value=', no1val)

# 2番目に大きな値
ct = -1
while True:
    tmp = card[ct]
    card[ct] = card[ct-1]
    card[ct-1]= tmp

    no2val = 0
    for i in card:
        no2val *= 10
        no2val += i

    if no1val != no2val:
        break
    else:
        ct -= 1
        
print('No2 value=', no2val)
