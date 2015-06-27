import sys

argvs = sys.argv  # コマンドライン引数を格納したリストの取得
argc = len(argvs) # 引数の個数

print(argvs)
print(argc)
print()
if (argc != 2):   # 引数が足りない場合は、その旨を表示
    print('your input=[%s]' % argvs[0])
    sys.exit()         # プログラムの終了

print('your input=[%s]' % argvs[1])

total = 0
isbn = argvs[1]
for i in isbn:
    print(i)
    total += int(i)

print()
print(total)
