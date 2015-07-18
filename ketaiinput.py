kana = [['あ', 'い', 'う', 'え', 'お'], #1
    ['か', 'き', 'く', 'け', 'こ'], #2
    ['さ', 'し', 'す', 'せ', 'そ'], #3
    ['た', 'ち', 'つ', 'て', 'と'], #4
    ['な', 'に', 'ぬ', 'ね', 'の'], #5
    ['は', 'ひ', 'ふ', 'へ', 'ほ'], #6
    ['ま', 'み', 'む', 'め', 'も'], #7
    ['や', 'ゆ', 'よ'], #8
    ['ら', 'り', 'る', 'れ', 'ろ'],#9
    ['わ', 'を', 'ん']] #0

message = []
pre = ''
ct = 0
while(1):
    while(1):
        ch = input()
        if ord('0') <= int(ch) and int(ct) <= ord('9'):
            break
    if ch=='.':
        break
    if int(ch)==0:
        num = 10
    else:
        num = int(ch)

    if(ct==len(kana[num-1])):
        ct = 0
    print(kana[num-1][ct])
    message.append(kana[num-1][ct])
    ct += 1

print('your input = ', message)

'''
message = []
ct = 0

num = ''
tmp = ''
flag = 1
while(num!='.'):
    if ct==5:
        ct = 0
    num = input()
    if tmp==num:
        print(kana[num-1][ct])
        ct += 1
    else:
        message.append(kana[int(num)-1][ct])
        ct = 0
'''
