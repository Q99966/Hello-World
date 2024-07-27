class alien:
    '''外星人的简单模拟'''
    
    def __init__(self,a) -> None:
        self.a=a

    def alien_maker(self):
        '''制作一个包含外星人信息的
        嵌套字典'''
        
        message_aliens_list={}                                 #嵌套，从里到外开始套
        #打包一个外星人信息
        n,k,w={},{},{}                                     

        k['head']='green'
        k['body']='yellow'
        k['foot']='red'                                     

        w['direction']='north'
        w['size']=5                                          

        n['alien_v']=w
        n['alien_color']=k
        n['alien_speed']='slow'                             

        #生成外星人所需要的个数

        for i in range(self.a):                                           
            message_aliens_list[f'message_aliens_{i+1}']=n         
        self.mal= message_aliens_list
    
    def P_alienlist(self):
        '''打印外星人所有信息'''
        print(self.mal)

    def P_alienname(self):
        '''打印外星人名字'''
        print('\n\n外星人名单:')
        for r in self.mal.keys():                        #外星人名单
            print(r,end=' \t') 




    def P_alienmessage(self):
        '''列打印外星人信息'''
        
        print('\n\n外星人信息:')
        for m,val in self.mal.items():                   #输出所有外星人信息
            print(f'\n\n{m}:')                                 

            for q,v1 in val.items():                                    
                                                     
                print(f'\t{q}:')                                  
                                                                    
                try:                        
                    for b in v1:                            
                        val_2=v1[b]
                        print(f'\t\t{b}:',end='')
                        print(f'{val_2}')
                except(TypeError):
                    print(f'\t\t{v1}')
                # for b in v1:                            
                #         val_2=v1[b]
                #         print(f'\t\t{b}:',end='')
                #         print(f'{val_2}')    

    def C_mal(self,*c,head='green',body='yellow',foot='red',direction='north'
              ,size=5,alien_speed='slow'):
        '''更改个别外星人信息'''
        #新建一个外星人
        n,k,w={},{},{}                                     

        k['head']=head
        k['body']=body
        k['foot']=foot                                     

        w['direction']=direction
        w['size']=size                                          

        n['alien_v']=w
        n['alien_color']=k
        n['alien_speed']=alien_speed
        
        for i in c:
            self.mal[f'message_aliens_{i}']=n                
        


#创建10个外星人信息
                    
alien1=alien(9)
alien1.alien_maker()
# alien1.P_alienlist()


# alien1.P_alienname()
alien1.P_alienmessage()
alien1.C_mal(6,8,head='blue')
alien1.P_alienmessage()                     

       
            



