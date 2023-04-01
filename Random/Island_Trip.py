y, n= [*map(int, input().split(' '))]
islands= [*map(int, input().split(' '))]

def getPrimes(n): 
    primes= []
    base= 3
    while n>1:
        if not n%base: primes.append(base)
        while not n%base: n/=base
        base+=1

    return primes

def sum_sets(nums):
    output= []
    for x in nums: output.append(x)
    for i in range(len(nums)):
        output+= [*map(lambda x: x+ nums[i], sum_sets(nums[:i] + nums[i+1:]))]

    return set(output)


primes= getPrimes(y)        
sums= sum_sets(primes)

choice= [i+1 for i in range(len(islands)) if islands[i] in sums]
print(len(choice))
print(' '.join([*map(str, choice)]))
