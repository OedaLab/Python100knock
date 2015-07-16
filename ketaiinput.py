kana = [['あ', 'い', 'う', 'え', 'お'],
    ['か', 'き', 'く', 'け', 'こ'],
    ['さ', 'し', 'す', 'せ', 'そ']]

message = []
ct = 0

num = ''
tmp = ''
flag = 1
while(num=='.'):
    if ct==5:
        ct = 0
    num = input()
    if tmp==num
        print(kana[num-1][ct])
        ct += 1
    else:
        message.append(kana[num-1][ct])
        ct = 0
