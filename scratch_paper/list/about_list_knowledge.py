import random
def title(n):
    '''生成一个标题来区分输出内容'''

    print(f'\n\n{n:-^100}')


#关于浅拷贝与深拷贝的理解
li = [random.randint(1,100) for i in range(100)]
title('初始列表')
print(li)
#浅拷贝
li1=li
#深拷贝
li2=li[:]
li.sort()
title('已排序的初始列表')
print(li)
title('对初始列表的浅拷贝')
print(li1)
title('对初始列表的深拷贝')
print(li2)
