import time
#海象运算符测试时间

list1=[i for i in range(1,11) if i!=5]

#测试一

print(f'{"测试一":-^50}')
p1=time.time()
mp={'a':(a := len(list1)),
    'b':(b := sum(list1)),
    'c':b / a}
p2=time.time()
print(mp,(p2-p1)*10000,sep='\n')
print()


#测试二

print(f"{'测试二':-^50}")
q1=time.time()
a=len(list1)
b=sum(list1)
mp={'a':a,
    'b':b,
    'c':b/a}
q2=time.time()
print(mp,(q2-q1)*10000,sep='\n')
print()

#测试三

print(f'{"测试三":-^50}')
p1=time.time()
mp={'a':len(list1),
    'b':sum(list1),
    'c':sum(list1)/len(list1)}
p2=time.time()
print(mp,(p2-p1)*10000,sep='\n')
print()




