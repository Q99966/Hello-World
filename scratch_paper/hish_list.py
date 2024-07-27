# mp={}
# list1=['a','b','c','d','e','f']
# for x,y in enumerate(list1):
#     mp[y] = x
# print(mp)     
# 使用 lambda 在列表中对元组的第二个元素进行排序
# pairs = [(1, 'one'), (4, 'four'), (3, 'three'), (2, 'two')]
# sorted_pairs1 = sorted(pairs, key=lambda x: x[1])
# print(sorted_pairs1)
# sorted_pairs0=sorted(pairs,key=lambda x:x[0])

# print(sorted_pairs0)

# 输出：[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
strs=['the', 'stirng', 'Has', 'many', 'line', 'In', 'THE', 'fIle']
rsorted_strs=sorted(strs,key=str.lower,reverse=True)
sorted_strs=sorted(strs,key=str.lower)
sorted_str=sorted(strs)
print(sorted_strs)
print(rsorted_strs)
print(sorted_str)