# Given N,A,B,C,X,Y and the following functions. Find the hash output of the algo in linear time. 
def gen(N, A, B, C):
    result= [A]
    for i in range(1, N): result+= [(A+ result[i-1]*B) %C]
    return result

def hashV(X, Y, l):
    V= 77
    for x in l: V= (V*X + 7*x) %Y
    return V

algo= lambda N,A,B,C,X,Y: hashV(X,Y, sorted(gen(N,A,B,C)))

# ----------------------
# Start: 

case1= [7,7,77,777,7777,77777]
case2= [23,7,77,777,7777,77777]
case3= [500, 5, 200, 351, 441, 553]
case4= [100, 351, 200, 351, 4411, 553333]
case5= [500, 357, 200, 351, 4441, 55333]
case6= [200, 779, 77, 777, 7777, 77777]   # repeats with no 0
case7= [500000, 5678, 91011, 1213, 141517, 1618192021]

def radix(arr):
    max_val = max(arr)
    num_digits = len(str(max_val))
    for k in range(num_digits):
        sorting_buckets = [[] for _ in range(10)]
        for i in arr:
            digit = (i // (10 ** k)) % 10
            sorting_buckets[digit].append(i)
        arr = []
        for bucket in sorting_buckets:
            arr.extend(bucket)
    return arr

def algo2(N, A, B, C, X, Y):
    V= 77
    if A%C==0: 
        for _ in range(N-1): V= (V*X)%Y
        return (V*X + 7*A)%Y
    
    if A>C: return hashgt(N, A, B, C, X, Y)
    
    p= [A]
    for _ in range(1, N):
        p+= [(A+B*p[-1])%C]
        if p[-1]==p[0]: 
            p.pop()
            break
    if len(p)==N: return hashV(X, Y, radix(p))

    b= radix([p[i] for i in range(N%len(p))])
    p= radix(p)
    V= 77
    for x in p:
        rep= N//len(p)
        if b and x==b[0]:
            rep+=1
            b.pop(0)
        for _ in range(rep): V= (V*X + 7*x) %Y
    return V

def hashgt(N, A, B, C, X, Y):
    p= [A]
    for _ in range(1, N):
        p+= [(A+B*p[-1])%C]
        if _ ==1: continue
        if p[-1]==p[1]: 
            p.pop()
            break
    if len(p) ==N: return hashV(X, Y, radix(p))
    # p does not loop OR p includes A%C
    
    b= radix([p[i] for i in range( 1, N % (len(p)-1) )])
    p= radix(p)
    V=77
    
    for x in p:
        rep= N//(len(p)-1)
        if b and x==b[0]:
            rep+=1
            b.pop(0)
        elif x==A: rep= 1
        for _ in range(rep): V= (V*X + 7*x) %Y
    return V
    
from time import time
print(algo(*case1), algo2(*case1))
print(algo(*case2), algo2(*case2))
print(algo(*case3), algo2(*case3))
print(algo(*case4), algo2(*case4))
print(algo(*case5), algo2(*case5))
print(algo(*case6), algo2(*case6))
print()
start= time()
print(algo(*case7))
print(time()-start)
start= time()
print(algo2(*case7))
print(time()-start)