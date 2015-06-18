# ファイル40個作成せよ．ファイル名はa8701からa8740とする．
# 内容は'hello world. a8701'とファイル名が記述された内容とする．

#
# basicなファイル書き込みで実現する

for num in range(40):
    if num<9:
        filename =   'tmp/a870' + str(num+1)
    else:
        filename =   'tmp/a87' + str(num+1)

    f = open(filename, 'w')
    f.write('hello world. %s' %(filename))
    f.close()
