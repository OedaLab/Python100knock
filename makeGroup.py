#!/usr/bin/env python

# 36. グループ分けを行うプログラムを作成せよ．

import sys
import random
import pandas as pd
import numpy as np

# 引数チェック
argvs = sys.argv
argc = len(argvs)

if argc!=3:
	print("Usage: makeGroup クラス人数 1班の人数")
	sys.exit(1)

classNum = int(argvs[1])
groupNum = int(argvs[2])

# ランダムシャッフル	
member = [i+1 for i in range(classNum)]
random.seed(0)
random.shuffle(member)

# 班番号生成
group = []
for i in range(int(classNum/groupNum)):
	group.extend([i+1]*groupNum)

# pandasに投げて，memberでソートする
df = pd.DataFrame([member, group]).T
df.columns = ['member','group']
df = df.sort_values(by='member')
df = df.reset_index(drop=True)