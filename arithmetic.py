def notlessthan(p,q):
    if p-q>=0:
        return True
    return False
def popnumdot(q,dotindex):
    qlist=list(str(q))
    qlist.pop(dotindex)
    qstr=''.join(qlist)
    return int(qstr)
def adddottonum(q,index):
    qlist=list(str(q))
    qlist.insert(index,'.')
    qstr=''.join(qlist)
    return float(qstr)


def getdigits(num):
    numstr = str(num)
    numlen = len(numstr)
    decimalpointindex = numstr.find('.')
    if decimalpointindex > -1 :
        return decimalpointindex,numlen-1-decimalpointindex
    return numlen,0

def basedivision(p,q):
    count = 0
    if notlessthan(p,q):
        while(notlessthan(p,q)):
            p=p-q
            count+=1
    else: 
        return 0,p
    return count,p

def division(p,q,n=7):
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
def basemultiplication(p,q):
    sum =0
    for i in range(q):
        sum = p+sum
    return sum
def basepower(n,m):
    product = 1
    for i in range(m):
        product=basemultiplication(product,n)
    return product
def multiplication(p,q):
    interindex,decimal=getdigits(q)
    if decimal == 0:
        return basemultiplication(p,q)
    numwithnodot=popnumdot(q,interindex)
    multinum = basemultiplication(p,numwithnodot)
    multinuminter,multinumdecimal=getdigits(multinum)
    if multinumdecimal==0:
        return adddottonum(multinum,len(str(multinum))-decimal)
    else:
        return adddottonum(popnumdot(multinum,multinuminter),multinuminter-decimal)

def sprt(p,n=2):  # not start write
    return 1

def power(n,p:int,q:int=1):
    if q==1:
        return basepower(n,p)
    else:
        return multiplication(basepower(n,p),sprt(n,q))



