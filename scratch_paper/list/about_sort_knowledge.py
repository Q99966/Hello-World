from functools import cmp_to_key
#cmp_to_key是一个非常方便的一个函数
#它可以改变内置函数sorted的判断条件
#使用方法如下————————————————————
def stringsort(a1,a2):
    '''string之间的排序'''
    if a1 + a2 > a2 + a1:
        return 1
    else:
        return -1


li=[('a','abcd'),('b','abc'),('c','ac')]
li2=['a','abcd','b','abc','c','ac']

li1=sorted(li2,key=cmp_to_key(stringsort))
print(li1)


# ls=['9','23','3','56','78']
# print(sorted(ls, key=cmp_to_key(lambda x, y: int(x + y) -int(y + x)))) 