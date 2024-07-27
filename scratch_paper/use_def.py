import os


def p_list(li,n=20):
    '''将可迭代数据打印出来'''
    for k,v in enumerate(li):
        if k % n == 0:
            print('\n')
        print(f'{k:,}:{v}',end='\t')   
    print() 


def f_b(n1,n2,index_max):
    '''生成一个斐波那契列表'''
    number_m=[n1,n2]
    i=2

    n3=n1+n2
    n1,n2=n2,n3

    while i <= index_max and i > 1:
                       
        i=i+1
        number_m.append(f'{n3:,}')
        n3=n1+n2
        n1,n2=n2,n3
    return number_m  

def w_ytext(li):
    '''判断列表中是否有重复元素'''
    mp={}
    for i in li:
        n=mp.get(i,0)
        if not n:
            mp[i]=n+1
        else:
            return False
    return True    

def binary_search1(date,target,low,high):
    '''二分查找'''
    if low > high:
        return False
    else:
        mid=(low+high) // 2
        if target == date[mid]:
            return True
        elif target > date[mid]:
            return binary_search1(date,target,mid+1,high)
        else:
            return binary_search1(date,target,low,mid-1)
        


def binary_search2(date,target,low,high):
    '''二分查找'''
    while high >= low:
        mid=(low+high) // 2
        if target == date[mid]:
            return True
        elif target > date[mid]:
            low = mid + 1
        else:
            high = mid -1
    else:
        return False

def finddate(name,path):
    '''查找该文件中有无name'''
    
    li1=os.listdir(f'{path}')
    
    for i in li1:
        if i == name:
            return True
    
        elif os.path.isdir(f'{path}\\{i}'):
            if finddate(name, f'{path}\\{i}'):
                return True
    return False                


