"""
Problem

Alan just had his first cryptography class in school today. He 
 decided to apply what he learned and come up with his own cipher. 
 He will map each English letter from A to Z to a decimal digit 0
 through 9. He will then try to encode each word to a string 
 consisting of decimal digits by replacing each letter in the word 
 with its mapped digit.

In his excitement, Alan failed to notice that there are 26
 letters in the English alphabet and only 10 decimal digits. As 
 a result, there might be collisions, that is, pairs of different 
 words whose encoding is the same.

Given a list of N
 words that Alan wants to encode and the mapping that he uses, 
 can you find out if there would be any collisions between words 
 on the list?

Input
 The first line of the input gives the number of test cases, T. 
 T test cases follow. The first line of each test case contains
 26 decimal digits (integers between 0 and 9, inclusve) DA,DB,…,DZ
 , representing the mapping that Alan uses. A letter α is mapped 
 to digit Dα.
 The second line of each test case contains N, the number of words 
 Alan will encode. The i-th of the last N lines contains a string 
 Si, representing the i-th word Alan will encode. 
 
Output
 For each test case, output one line containing Case #x: y, where 
 x is the test case number (starting from 1) and y is either YES, 
 if there is at least one pair of different words from the list 
 whose encoding coincides, and NO otherwise.

Limits
 Time limit: 20 seconds.
 Memory limit: 2 GB.
 1≤T≤100. 
 0≤Dα≤9, for all α.
 1≤ the length of Si ≤10, for all i.

 Each character of Si is an uppercase English letter A through Z, 
 for all i.
 Si≠Sj, for all i≠j.

Test Set 1 (Visible Verdict)
 1≤N≤100.
Test Set 2 (Visible Verdict)
 1≤N≤6×104.
"""

T= int(input())
A_ord= ord('A')
Z_ord= ord('Z')

for case in range(T):
    crypt= {key:value for key, value in zip(
        [chr(i) for i in range(A_ord, Z_ord+1)], 
        input().split()
        )}
    N= int(input())
    used_words= set()
    used_nums= set()
    flag= False
    for _ in range(N):
        word= input()
        if flag: continue
        if word in used_words: continue
        else: used_words.add(word)
        num= ''
        for x in word: num+= crypt[x]
        if num in used_nums: flag=True
        else: used_nums.add(num)
    
    flag= "YES" if flag else "NO"
    
    print("Case #{case}: {flag}".format(case=case+1, flag=flag))