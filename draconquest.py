import random
key = random.randint(0,99)

hp = 1000
while(hp>0):
    print('HP=%d' %(hp))
    usrInput = int(input())
    if usrInput>key:
        print('small')
    elif usrInput<key:
        print('big')
    else:
        break
    hp -= random.randint(0,50)

if hp>0:
    print('Clear')
else:
    print('Game Over')
