# 各変数の使い方

#　リスト型
l = [1, 20, 4, 50,2, 1, 2]
print(l[3])
print(l[2:5])
print(l[2:])
print(l[::2])
print(l[::-1])

s = ['a', 'b', 'c', 'd', 'e', 'f']
print(s[0])
s[0] = 'X'
print(s[0])
print(s[2:5])
s[2:5] = ['B', 'C', 'D']
print(s[2:5])

s = []
print(s)

n = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print(n)
# リスト最後に値追加
n.append(100)
print(n)
# リスト指定位置に値追加
n.insert(0, 200)
print(n)

# リスト値の取り出し
n.pop()
print(n)
n.pop(0)
print(n)

# リスト値の削除
# n.remove(2)
# print(n)

del n[0]
print(n)

# リストの結合
a = ['1', '2', '3']
b = ['4', '5', '6']
# s = a + b
# print(s)
# a += b
a.extend(b)
print(a)