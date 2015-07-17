kana = [['あ', 'い', 'う', 'え', 'お'],
    ['か', 'き', 'く', 'け', 'こ'],
    ['さ', 'し', 'す', 'せ', 'そ'],
    ['た', 'ち', 'つ', 'て', 'と'],
    ['な', 'に', 'ぬ', 'ね', 'の'],
    ['は', 'ひ', 'ふ', 'へ', 'ほ'],
    ['ま', 'み', 'む', 'め', 'も'],
    ['や', 'ゆ', 'よ'],
    ['ら', 'り', 'る', 'れ', 'ろ'],
    ['わ', 'を', 'ん']]


ct = 0
while(1):
    ch = input()
    if ch=='.':
        break
    num = int(ch)
    print(kana[num-1][ct])
    ct += 1
    if(ct==5):
        ct=0

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
