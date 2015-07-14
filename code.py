print("平文を入力してください.")
plain = input()

print("暗号化する鍵を入力してください.")
key = int(input())
key %= 26

code = []
for i in plain:
    ch = ord(i)+key
    if ch>ord('z'):
        ch = ch - ord('z') + ord('a')-1
    code.append(chr(ch))

code = "".join(code)
print(code)
