from use_def import p_list
            
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

for i in range(0,10):
    print(f_b(i,i+1,10))

p_list(f_b(100,200,10))      

        
        
  
      


  
    
    
