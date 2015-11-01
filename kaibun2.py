num = 11
while True:
        if (str(num) == str(num)[::-1]) and \
           (bin(num)[2::] == bin(num)[2::][::-1]) and \
           (oct(num)[2::] == oct(num)[2::][::-1]):
                print(num)
                break
        num += 2


