#to make a tic tac toe game using lists

L1=[0,0,0]
L2=[0,0,0]
L3=[0,0,0]
print(L1,L2,L3,sep='\n')
x=1
while x<11:
    if x%2==0:
        y='Player 2'
    else:
        y='Player 1'

    print('%s: Choose the cell number 1-9 where u want to place 1-' %y)
    n=int(input())
    if n==1:
        L1[0]=1
        print(L1,L2,L3,sep='\n')
        x+=1
    elif n==2:
        L1[1]=1
        print(L1,L2,L3,sep='\n')
        x+=1
    elif n==3:
        L1[2]=1
        print(L1,L2,L3,sep='\n')
        x+=1
    elif n==4:
        L2[0]=1
        print(L1,L2,L3,sep='\n')
        x+=1
    elif n==5:
        L2[1]=1
        print(L1,L2,L3,sep='\n')
        x+=1
    elif n==6:
        L2[2]=1
        print(L1,L2,L3,sep='\n')
        x+=1
    elif n==7:
        L3[0]=1
        print(L1,L2,L3,sep='\n')
        x+=1
    elif n==8:
        L3[1]=1
        print(L1,L2,L3,sep='\n')
        x+=1
    elif n==9:
        L3[2]=1
        print(L1,L2,L3,sep='\n')
        x+=1
    else:
        print('Invalid number, select again')
        x+=0
        continue
    
    if L1[0]==L1[1]==L1[2]==1 or L2[0]==L2[1]==L3[2]==1 or L3[0]==L3[1]==L3[2]==1 or L1[0]==L2[0]==L3[0]==1 or L1[1]==L2[1]==L3[1]==1 or L1[2]==L2[2]==L3[2]==1 or L1[0]==L2[1]==L3[2]==1 or L1[2]==L2[1]==L3[0]==1:
        print('{0} is the winner'.format(y))
        break








        
        
    
