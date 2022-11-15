
import random as r

def create_history(s):
    i=0
    growth=0
    
    for i in range(10):
        s.append([])
        cur=s[i]
        j=0
        for stock in cur:
            change=r.randint(0,50)
            posmin=r.randint(0,1)
            if posmin==1:
                temp1=stock[1]+stock[2]*(stock[2]/100)
            else:
                temp1=stock[1]-stock[2]*(stock[2]/100)
            posmin=r.randint(0,1)
            if posmin==1:
                temp2=stock[2]+stock[2]*(change/100)
            else:
                temp2=stock[2]-stock[2]*(change/100)
            if temp2>=50:
                temp2=48
            temp2+=2
            if temp1<=5:
                temp1=r.randint(3,5)
            if i!=0:
                growth=((int(temp1)-s[i-1][j][1])/s[i-1][j][1])*100
            j+=1
            
            s[i+1].append([stock[0], int(temp1), round(temp2, 2), round(growth)])
            
    #for i in range(10):
        #print(s[i][0])
    return s
        
def stock_update(s):
    s.pop(0)
    s.append([])
    i=len(s)-2
    cur=s[i]
    j=0
    for stock in cur:
        change=r.randint(0,50)
        posmin=r.randint(0,1)
        if posmin==1:
            temp1=stock[1]+stock[2]*(stock[2]/100)
        else:
            temp1=stock[1]-stock[2]*(stock[2]/100)
        posmin=r.randint(0,1)
        if posmin==1:
            temp2=stock[2]+stock[2]*(change/100)
        else:
            temp2=stock[2]-stock[2]*(change/100)
        if temp2>=50:
            temp2=48
        temp2+=2
        if temp1<=5:
            temp1=r.randint(3,5)
        if i!=0:
            growth=((int(temp1)-s[i][j][1])/s[i][j][1])*100
        j+=1
        
        s[i+1].append([stock[0], int(temp1), round(temp2, 2), round(growth)])
    return s