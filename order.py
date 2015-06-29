# データ処理を行う．order.tsvはあるシステムで書籍注文したデータである．注文した書籍の総額を計算せよ．

import pandas as pd

df = pd.read_table('order.tsv', header=None)

# 金額のカラムはindex=5である．
value = list(df[5])

for (i, val) in enumerate(value):
    val = val.replace(',', '')
    value[i] = int(val)

print(sum(value))
