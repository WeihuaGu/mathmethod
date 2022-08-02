def notlessthan(p,q):
    if p-q>=0:
        return True
    return False

def basedivision(p,q):
    count = 0
    if notlessthan(p,q):
        while(notlessthan(p,q)):
            p=p-q
            count+=1
    else: 
        return 0,p
    return count,p

def division(p,q,n):
    quotient = [0 for i in range(n+2)] # [0,0,0,...0]
    remainder = [0 for i in range(n+2)] # [0,0,0,...0]
    digit = [1.0/(10**i) for i in range(n+2)] # this use divisin only to generate digit list:[1,0.1,0.01,0.001...]

    quotient[0],remainder[0]=basedivision(p,q)
    for i in range(n+1):
        if remainder[i]==0:
            break
        if remainder[i]!=0:
            quotient[i+1],remainder[i+1]=basedivision(remainder[i]*10,q)

    sum=0
    for i in range(n+1):
        sum=sum+quotient[i]*digit[i]
        if i!=0 and quotient[i]==0:
            return sum
    if quotient[n]>=5: # rounding-off
        sum=sum+digit[n]
    return sum
### test methods
print(basedivision(9,2)) #divide 9 by 2
print(division(2.1234,9.566,10)) # divide 2.1234 by 9.566 with keep ten decimal places
print(division(9,2.4,5))
print(division(3,9,10))
            
