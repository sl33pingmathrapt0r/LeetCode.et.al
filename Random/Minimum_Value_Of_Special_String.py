# A special string is a string made from translating a digit to text. 
# E.g. 'one' is a special string. 
# Given a string shuffled with any number of special string characters, 
# find the minimum numerical value of the string. 

# SOLUTION: 
"""
Uniquely identify each word by a signature character. 
When finding a signature, all remaining words must 
have no conflict. i.e. no remaining words can have the
character used as the signature of the current word. 

Conversely, special strings that have already been 
acdigitCount for may contain the character used as 
signature for the current word. No conflict arises since
previous words are no longer in consideration. 
"""

# zero --> z
# two --> w
# four --> u
# six --> x
# eight --> g

# one --> o
# three --> h
# five --> f
# seven --> s

# nine --> i

# number to word dict
n2w= {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}

def countDigits(letterCount):
    """
    Given the number of occurences of 
    each character in the original string, 
    determine the number of all digits. 
    """
    # count= {str(i):0 for i in range(10)}
    count= {}
    signature= ['z', 'w', 'u', 'x', 'g', 'o', 'h', 'f', 's', 'i']
    sign_digit= [0,2,4,6,8,1,3,5,7,9]
    for i in range(len(signature)):
        if letterCount.get(signature[i]):
            rep= letterCount.get(signature[i])
            # update the number of times the digit was used
            count[str(sign_digit[i])]= rep
            # update the count of letters still unaccounted for
            for x in n2w[str(sign_digit[i])]: letterCount[x]-= rep
    
    return count


def minVal(digitCount):
    """
    Given the number of occurences 
    of each digit, form the smallest
    integer value using all digits 
    with no leading zeroes. 
    """
    s= ''
    for i in range(1,10):
        # find smallest non-zero leading digit
        if digitCount.get(str(i),0):
            digitCount[str(i)]-= 1
            s+= str(i)
            break
    for i in range(10):
        s+= str(i) * digitCount.get(str(i), 0)
    
    return int(s)


# TESTING
cases= [438700971, 601247318, 2102, 82719834202218766397000001938459038459813459817598242897573427395035880354083450187508417357093184289020985408394050810384950134801938410398401983509384501394850139845103984019384519830475089347107984890734718089374701354018491083941039840614385673607034703603457089341094103418090170139075081345923901990190370259999991188271983420221876639700000193845903845981345981759824289757342739503588035408345018750841735709318428902098540839405081038495013480193841039840198350938450139485013984510398401938451983047508934710798489073471808937470135401849108394103984061438567360703470360345708934109410341809017013907508134592390199019037025999999118827198342022187663970000019384590384598134598175982428975734273950358803540834501875084173570931842890209854083940508103849501348019384103984019835093845013948501398451039840193845198304750893471079848907347180893747013540184910839410398406143856736070347036034570893410941034180901701390750813459239019901903702599999911882719834202218766397000001938459038459813459817598242897573427395035880354083450187508417357093184289020985408394050810384950134801938410398401983509384501394850139845103984019384519830475089347107984890734718089374701354018491083941039840614385673607034703603457089341094103418090170139075081345923901990190370259999991188271983420221876639700000193845903845981345981759824289757342739503588035408345018750841735709318428902098540839405081038495013480193841039840198350938450139485013984510398401938451983047508934710798489073471808937470135401849108394103984061438567360703470360345708934109410341809017013907508134592390199019037025999999118827198342022187663970000019384590384598134598175982428975734273950358803540834501875084173570931842890209854083940508103849501348019384103984019835093845013948501398451039840193845198304750893471079848907347180893747013540184910839410398406143856736070347036034570893410941034180901701390750813459239019901903702599999911882719834202218766397000001938459038459813459817598242897573427395035880354083450187508417357093184289020985408394050810384950134801938410398401983509384501394850139845103984019384519830475089347107984890734718089374701354018491083941039840614385673607034703603457089341094103418090170139075081345923901990190370259999991188271983420221876639700000193845903845981345981759824289757342739503588035408345018750841735709318428902098540839405081038495013480193841039840198350938450139485013984510398401938451983047508934710798489073471808937470135401849108394103984061438567360703470360345708934109410341809017013907508134592390199019037025999999118827198342022187663970000019384590384598134598175982428975734273950358803540834501875084173570931842890209854083940508103849501348019384103984019835093845013948501398451039840193845198304750893471079848907347180893747013540184910839410398406143856736070347036034570893410941034180901701390750813459239019901903702599999911882719834202218766397000001938459038459813459817598242897573427395035880354083450187508417357093184289020985408394050810384950134801938410398401983509384501394850139845103984019384519830475089347107984890734718089374701354018491083941039840614385673607034703603457089341094103418090170139075081345923901990190370259999991188271983420221876639700000193845903845981345981759824289757342739503588035408345018750841735709318428902098540839405081038495013480193841039840198350938450139485013984510398401938451983047508934710798489073471808937470135401849108394103984061438567360703470360345708934109410341809017013907508134592390199019037025999999118]

# Convert integer numbers to strings, by converting each DIGIT to TEXT. 
d2t= lambda n: ''.join([n2w[c] for c in str(n)])

test= [d2t(case) for case in cases]
for string in test:
    store={}
    # count the number of occurences of each character
    for c in string: store[c]= store.get(c,0)+1
    print(minVal(countDigits(store)))
    
# print('lol', len(str(cases[-1])))