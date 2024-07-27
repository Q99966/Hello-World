#位运算
import time

#判断该数是否为偶数
def odd(n):
    '''判断是否为偶数'''
    return not n & 1
# print(odd(10000))

#2**n
def nPower(n):
    '''2**n'''
    return 1 << n

a=time.time()
print(nPower(10000))
b=time.time()
print(2**10000)
c=time.time()
print((b-a)*1000)
print((c-b)*1000)
# print((c+a-2*b)*10**7)

