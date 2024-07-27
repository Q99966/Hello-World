#通透！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
import sys
sys.setrecursionlimit(3000)
import random
import time
import pandas as pd
def potion(li,left,right):
    '''将某元素在列表中归位'''
    md=li[left]
    while left < right:
        #left < right不能缺，否则
        # md=li[right]时，right会超出index
        # 如li[left]为第一个元素且最小时
        # right=left时会变为-1

        #如果其大于md,则跳过它即right -= 1
        while left < right and md <= li[right]:
            right -= 1
        #将right的值放到left空位上    
        li[left]=li[right]
        #与上面同理
        while left < right and md >= li[left]:
            left += 1
        li[right] = li[left]
     
    li[left]=md
    return left
def quick_sort(li,left,right):
    '''快速排序'''
    if left >= right:
        return
    mid=potion(li,left,right)
    # print(list1)
    quick_sort(li,mid+1,right)
    quick_sort(li,left,mid-1)

#用来测试时间    
li=[]    
for i in range(1,7):    
    

    list1=[ random.randint(1,10000) for _ in range(10**i)]
    # if i == 6:
    #     print(list1)
    p1=time.time()
    quick_sort(list1,0,len(list1)-1)
    p2=time.time()
    li.append(p2-p1)
s=pd.Series(li,[10**i for i in range(1,7)]) 
print(s)   


# print(list1)

# print(list1[:5000]) 

# #有重复值也没问题
# list2=[2,5,6,9,3,5,5]
# quick_sort(list2,0,len(list2)-1)
# print(list2)