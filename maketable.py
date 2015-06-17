import random
import pandas as pd

num = [i for i in range(1, 41)]
random.shuffle(num)

# もう面倒なので，pandasで処理．
# pandasを使うと素朴なpythonを使えなくなるな．．．

df = pd.read_csv('number.csv', names=['student'])
df['num'] = pd.Series(num, index=df.index)

df.to_csv('hoge.csv')
