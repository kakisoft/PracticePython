fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')

print(fruits.count('apple'))

fruits.count('tangerine')

print(fruits.index('banana'))

fruits.index('banana', 4)  # インデックス4から数えて次の banana の位置

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

fruits.pop()
print(fruits)