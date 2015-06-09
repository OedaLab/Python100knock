def pound2kg(m):
    return m*0.45359237

print('ポンド（重さ）を入力してください．')
print('pound=', end='')
pound = int(input())

kg = pound2kg(pound)

print('%fポンドは%fkgです．' %(pound, kg))
