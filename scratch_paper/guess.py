import random
#设置随机数
b=random.randint(9,1000)
i=1
print('请输入数字,退出quit:')

while True:
    print(f'第{i:,}次:',end='')

    c=input('')
    a=eval(c)
    print(f'长度:{len(c)}')
    i+=1
    if c=='quit':
        break
    if a==b:
        print('恭喜你猜对了')
        break
    elif a>b:
        print('大了')
    elif a<b:
        print('小了')
    

            