# 次の学籍番号を生成するプログラムを作成せよ． a8701, a8702, ... , a8740

# 解1
f = open('hoge.csv', 'w')

base = 'a87'
for i in range(1, 41):
    if i<10:
        j = '0' + str(i)
        f.write(base+str(j)+'\n')
        print(base+str(j))
    else:
        f.write(base+str(i)+'\n')
        print(base+str(i))
f.close()
print()

# 解2
for i in range(8701, 8741):
    print('a'+str(i))
