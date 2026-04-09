#Pisano set from k-Pisano-Legendre primes
#See https://doi.org/10.62072/acm.2026.09011
from sympy import legendre_symbol, primerange

def check(p,in1,in2,k):
    L, a, b, in1, in2 = [], in1, in2, in1%p, in2%p
    while True:
        L.append(legendre_symbol(a, p))
        a, b = b, (a + b)%p
        if (a, b) == (in1, in2): break
    return L.count(1) - L.count(-1) - L.count(0) == k 

def pisanoset(in1,in2,k1,k2,maxp):
    prime = list(primerange(3,maxp))
    kint = range(k1,k2+1,1)
    pisanoset = []
    for k in kint:
        if any(check(p, in1, in2, k) for p in prime):
            pisanoset.append(k)
    return pisanoset
        
    
print(pisanoset(0,1,-100,100,1000))
