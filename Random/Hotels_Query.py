"""
Hotels have ID h. When searching for a hotel
with keywords, the hotel gives the keyword 
some weight. E.g 'grand' has a weight of
100 by The Grand Hotel in Dubai. You are given
the hotel IDs, and the list of keyword-weight
pairs to each hotel. 

Given m queries, return the list of hotels 
relevant to each query. The list should be in
descending order. If there are more than 10
hotels, show the top 10 results only. If
2 hotels have the same score, show the hotel 
with a smaller ID first. 
"""

"""
n m
h k {kw}
l {query}
Input: 
3 2
101 3 grand 100 hotel 10 center 5
201 3 luxury 100 bangkok 10 hotel 1
301 2 goa 50 resort 50
2 grand hotel
1 goa
"""

"""
Output:
101 201
301
"""

n, m= [*map(int, input().split(' '))]
hotels= []
kw= [{} for _ in range(n)]
for i in range(n):
    row= input().split(' ') 
    hid= row[0]
    hotels.append(hid)
    k= int(row[1])
    for j in range(k): 
        kw[i][row[2*j+2]]= int(row[2*j+3])

# print(hotels)
# print(kw)

for _ in range(m):
    row= input().split(' ')
    l= int(row[0])
    score= [0 for _ in range(n)]
    for i in range(n): 
        for j in range(l): 
            score[i]+= kw[i].get(row[j+1], 0) 

    if set(score)== {0}: 
        print(-1)
        continue

    results= [x for x in [*zip(hotels, score)] if x[1]]
    results= sorted(results, key= lambda x: int(x[0]), reverse= False)
    results= sorted(results, key= lambda x: x[1], reverse= True)
    ub= min(10, len(results))
    head= [results[i][0] for i in range(ub)]
    print(' '.join(head))