# #タプル型　※リスト型と違い書き換え不可
# t = (1, 2, 3, 4, 1, 2)
# print(t)
# print(type(t))
#
# j = ([1, 2, 3, 4, 1, 2], [2, 3, 4, 5, 2, 3])
# print(j[0][1])
# print(type(j))
#
# #タプル型のアンパッキング
# num_tuple = (10, 20)
# print(num_tuple)
#
# x, y = num_tuple
# print(x, y)
#
# #やっていることは同じ
# x, y = 10, 20
# print(x, y)
# min, max = 0, 100
# print(min, max)
#
# #値の入れ替え
# a = 100
# b = 200
# print(a, b)
# a, b = b, a
# print(a, b)
#
# chose_from_two = ('A', 'B', 'C')
#
# answer = []
# answer.append('A')
# answer.append('C')
#
# print(chose_from_two)
# print(answer)
#
#
# #辞書(ディクショナリ)型　
# d = {'x': 10, 'y': 20}
# print(d)
# print(type(d))
# print(d['x'])
# d['x'] = 100
# print(d)
#
# d['z'] = 200
# print(d)
#
# #キーの表示
# print(d.keys())
# #値の表示
# print(d.values())
#
# d2 = {'x': 1000, 'j': 250}
# d.update(d2)
# print(d)
#
# d.pop('x')
# print(d)
# del d['y']
# print(d)
#
# print('z' in d)

# x = {'a': 1}
# y = x
# y['a'] = 1000
# print(x)
# print(y)

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)

fruits = {
    'apple': 100,
    'orange' : 200,
    'banana': 300
}
print(fruits)
print(fruits['banana'])

#集合型
a = {1, 2, 3, 4, 5, 6, 7}
print(type(a))
b = {2, 3, 4, 8}
print(a - b)
print(b - a)
print(a | b)
print(a ^ b)

s = {1, 2, 3}
print(s)
s.add(6)
print(s)
s.remove(6)
print(s)
s.clear()
print(s)

my_friends = {'A', 'B', 'C'}
A_friends = {'B', 'C', 'D', 'E'}
print(my_friends & A_friends )

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)