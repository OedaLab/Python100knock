# あみだくじを判定
# あみだくじデータは次のようになっている．
'''
1,0,0
0,1,0
0,0,1
0,0,1
'''
# 1, 2, 3, 4のくじを選ぶと
# 3, 1, 2, 4に到達する．


# 作戦
# うーん，次のようにするのが簡単かな．
'''
0 1 2 3 4 5 6
0,1,0,0,0,0,0
0,0,0,1,0,0,0
0,0,0,0,0,1,0
0,0,0,0,0,1,0
'''
# のような感じ

data = [
    [1,0,0],
    [0,1,0],
    [0,0,1],
    [0,0,1],
    ]

data2 = [
    [1,0,1,0],
    [0,1,0,1],
    [1,0,0,1],
    [1,0,1,0],
    [0,1,0,1],
    [0,0,1,0],
    [0,1,0,1],
    [1,0,0,0]
]
data = data2
# あみだくじの本数
linenum = len(data[0])

# まず，データを増やす
added = []
for j in range(len(data)):
    line = []
    for i in range(linenum):
        line.append(0)
        line.append(data[j][i])
    line.append(0)
    added.append(line)

# position -> 0,2,4,6 つまり．ラインの最大値はlinenum*2
for p in range(len(data[0])+1):
    position = p*2
    stage = 0
    while(stage<len(added)):
        flag = 0
        if (position<len(added[stage])-1):
            if added[stage][position+1]==1:
                position += 2
                flag = 1
        if (flag == 0 and position>0):
            if added[stage][position-1]==1:
                position -= 2

        stage+=1

    print(position//2+1)
