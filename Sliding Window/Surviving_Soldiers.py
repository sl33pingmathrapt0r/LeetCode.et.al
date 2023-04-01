"""
A tower consists of N floors. 
Each floor has one boss of power b_i. After
defeating the boss, its spirit becomes your
foot soldier of power s_i. While you have the
strength to defeat all bosses, foot soldiers 
with less power than the bosses will be 
eliminated. 

After conquering the last boss, how many
soldiers will you bring back?

Input: 
1st Line: an integer N
2nd Line: N space separated integers b_i
3rd Line: N space separated integers s_i

Return an integer
"""

"""
Solution: 
- Find index of max
- All units before max will die 
- Find new max on higher floors
- Repeat till tower conquered
"""

n= input()
b= [*map(int, input().split(" "))]
s= [*map(int, input().split(" "))]

soldier= 0
flag=0  # first floor completed
while b:
    strong= max(b)
    for i in range(b.index(strong)+flag): 
        if s[i]>=strong: soldier+=1
    b,s= b[b.index(strong)+1:], s[b.index(strong)+flag:]
    flag=1

print(soldier+1)