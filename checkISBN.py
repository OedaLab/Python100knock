# 現行規格のISBN (ISBN-13) のチェックディジットは、JANコードと同じく、
# 「モジュラス10 ウェイト3・1（モジュラス10 ウェイト3）」という計算法
# にて算出される。

# ここでは例として，ISBNを9784873116556とする．
# 検査数字は，先ずISBNの左から奇数桁の数字の合計と，
# 偶数桁の数字の合計を3倍にしたものを加え，10からその和の下
# 一桁の数字を引いて求める．

# 9784873116556の場合，
# 奇数の和：9+8+8+3+1+5 = 34
# 偶数の和：7+4+7+1+6+5 = 30
# 34 + 30*3 = 124
# 124の一桁目は4
# 10 - 4 = 6
# よって検査数字は6となる．
# これが10になる場合は、検査数字を0にします。

print('input isbn number(13) = ', end='')
isbn = input()
#isbn = '9784873116556'
#isbn = '9784621061220'

even = 0
odd = 0
for (i, num) in enumerate(isbn):
    print(i+1, num)
    if ((i+1)%2==1 and (i+1)!=13):
        odd += int(num)
    elif((i+1)%2==0):
        even += int(num)

print('odd:', odd)
print('even:', even)

first = (odd + even*3)%10
print('the first digit:', first)
ans = 10-first
if ans==10:
    ans = 0

print('ans=', ans)

print('-------')
checkdigit = int(isbn[-1])
if(checkdigit != 'x'):
    if(checkdigit==ans):
        print('OK')
    else:
        print('NG')
