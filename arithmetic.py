def basemulti(p,q):
    count = 0
    if p-q>0:
        while(p-q>=0):
            p=p-q
            count+=1
    return count,p

def multi(p,q,n):
    count = [0 for i in range(n+1)]
    pp = [0 for i in range(n+1)]
    jinwei = []
    for i in range(n+1):
        jinwei.append(1/(10**i))
    print(jinwei)
    count[0],pp[0]=basemulti(p,q)
    for i in range(n):
        if pp[i]==0:
            break
        if pp[i]!=0:
            count[i+1],pp[i+1]=basemulti(pp[i]*10,q)
    sum=0
    for i in range(n+1):
        sum=sum+count[i]*jinwei[i]
    return sum
print(multi(12.39,9,6))
            
