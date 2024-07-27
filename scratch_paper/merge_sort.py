import random
#消耗空间大,但稳定性高
#python的内置排序函数即为该函数
def merge_sort(li,low,high):
    '''归并排序'''
    #分
    if high > low:
        mid=(high+low) >> 1
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
    #和
        left,right=low,mid+1
        li1=[]
        while left <= mid and right <= high:
            if li[left] < li[right]:
                li1.append(li[left])
                left += 1
            else:
                li1.append(li[right])
                right += 1
        li[low:high+1] = li1 + (li[left:mid+1] if left <= mid else li[right:high+1])
        print(li[low:high+1])        


li=[random.randint(1,100) for _ in range(100)]
merge_sort(li,0,len(li)-1)
print(li)