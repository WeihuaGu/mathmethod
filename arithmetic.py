def notlessthan(p,q):
    if p-q>=0:
        return True
    return False

def basedivision(p,q): #only p notlessthan q,return quotient and remainder
    count = 0
    if notlessthan(p,q):
        while(notlessthan(p,q)):
            p=p-q
            count+=1
    return count,p

def division(p,q,n):
    quotient = [0 for i in range(n+1)]
    remainder = [0 for i in range(n+1)]
    digit = []
    for d in range(n+1):
        digit.append(1.0/(10**d)) # this use divisin only to generate digit list:[1,0.1,0.01,0.001...]

    if p<q:
        quotient[0]=0
        remainder[0]=p
    quotient[0],remainder[0]=basedivision(p,q)
    for i in range(n):
        if remainder[i]==0:
            break
        if remainder[i]!=0:
            quotient[i+1],remainder[i+1]=basedivision(remainder[i]*10,q)

    sum=0
    for i in range(n+1):
        sum=sum+quotient[i]*digit[i]
    return sum
### test methods
print(basedivision(9,2)) #divide 9 by 2
print(division(2.1234,9.566,10)) # divide 2.1234 by 9.566 with keep ten decimal places
            
