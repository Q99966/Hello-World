s1='aaaaa'
s2='abaa'
try:
    if s1 < s2:
        print('小于')
    else:
        print('大于')
except:
    print('失败')
s2new=sorted(s2)
print(''.join(s2new))
print(list(s2))                
