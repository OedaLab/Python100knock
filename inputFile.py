f = open('data.dat', 'r')

for line in f:
    print(line, end='')
f.close()
