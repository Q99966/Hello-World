a=input('请输入字符串:')
b=input('请输入子串:')

#设置n,i变量
def index_position(a,b):
    '''找到b在a中的位置'''
    n=[]
    i=0
    m=a.split()
    for k in m:
        i+=1
        if k==b:
            n.append(i)
    return n
n=index_position(a,b)
print(n)