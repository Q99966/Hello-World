#堆的节点变化函数

#小根堆
def sift0(li,low,high):
    '''并不能一次成堆
       li:low所对应的堆
       low:根节点
       high:最后的叶子节点'''
    #开局两个指针
    i=low  #父节点
    j=i*2+1  #子节点
    tmp=li[low] 
    while j <= high :
        #比较一下哪个孩子更NB
        if j+1 <= high and li[j+1] > li[j]:
            j += 1    
        #孩子厉害就就让他继承父节点
        if li[j] > tmp:
            li[i]=li[j]
            i=j
            j=i*2+1
        else:
            #发现手里的这个比最NB的孩子都NB
            li[i]=tmp
            break
    else:
        #如果i指针指到最后一个说明没有路可以走了
        #那就直接让tmp待到这里就行了
        li[i]=tmp 



def dui_soft(li):
    '''建立堆'''
    l=len(li) 
    for i in range(l-2>>1,-1,-1):
        sift0(li,i,l-1)
    for i in range(l-1,-1,-1):
        li[0],li[i]=li[i],li[0]
        sift0(li,0,i-1)


#大根堆
def shif1(li,left,right):
    '''
       left root····
       right hight
       '''
    tmp=li[left]
    i=left
    j=i*2+1
    while right >= j :
        if j+1 <= right and li[j+1] < li[j]:
            j += 1
        if li[j] < tmp:
            li[i]=li[j]
            i=j
            j=i*2+1
        else:
            li[i]=tmp
            break
    else:
        li[i] = tmp
              
def topk(li,k):
    '''求堆顶最大的k个数''' 
    #建堆
    heap=li[:k]
    for i in range(k-2>>1,-1,-1):
        shif1(heap,i,k-1)
    #历遍列表    
    for i in range(k,len(li)):
        #无论是哪一种排序算法都逃不过历遍列表
        if li[i] > heap[0]:
            heap[0]=li[i]
            shif1(heap,0,k-1)
    #出数
    for i in range(k-1,0,-1):
        # print(li)
        heap[0],heap[i]=heap[i],heap[0]
        shif1(heap,0,i-1)        

    return heap  

import random
li1=[random.randint(1,100) for _ in range(100)]
print(li1)
dui_soft(li1)
print(li1)              