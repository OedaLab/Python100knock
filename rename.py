import pandas as pd
import os
import shutil

df = pd.read_csv('rename/henkan.csv', index_col=0) # index_colで一列目を読み込まない

ls = os.listdir('rename')

num = 0
for i in range(40):
    if df.student[i]==ls[num]:
        shutil.copyfile('rename/' + str(df.student[i]), 'rename/' + str(df.num[i]))
        num+=1
