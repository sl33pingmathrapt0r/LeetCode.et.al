from random import randint

S1= "((?)][?]?)"
# ((?), ][?]?)
# ((?)][, ?]?)
# ...= 3 WAYS
S2= "(][?(]?[[("
S3= "??[?(]?(()"
S4= "[(?][??["
S5= "[[?()]()]?"

def fillMissingBrackets(s):
    if len(s)%2: return 0
    split_count= 0
    front_log= {'(':0, '[':0, '?':0}
    back_log= {'(':s.count('(')-s.count(')'), '[':s.count('[')-s.count(']'), '?':s.count('?')}
    # print('initial', back_log)
    
    for i in range(2, len(s)-1, 2):
        # update
        # print('cycle:', i//2)
        changes= update(s[i-1])
        front_log[changes[0]]+=changes[1]; back_log[changes[0]]-=changes[1]
        changes= update(s[i-2])
        front_log[changes[0]]+=changes[1]; back_log[changes[0]]-=changes[1]
        # validity
        if valid(front_log) and valid(back_log): 
            split_count+=1
            # print(s[:i], s[i+1:])
    
    return split_count
    
def update(c):
    if c=='(': return (c, 1)
    elif c== ')': return ('(', -1)
    elif c== '[': return (c, 1)
    elif c== ']': return ('[', -1)
    elif c== '?': return (c, 1)


def valid(log):
    # print(log)
    require= abs(log['(']) + abs(log['['])
    return log['?']>= require and not (log['?']-require)%2


gen= lambda n: ''.join([['(',')','[',']','?'][randint(0,4)] for _ in range(n)])
        
# print(*map(fillMissingBrackets, [S1, S2, S3, S4, S5]))
# print(fillMissingBrackets(''.join([S1, S2, S3, S4, S5])))