# Design an algorithm to encode a list of strings to a string. 
# The encoded string is then sent over the network and is decoded 
# back to the original list of strings.

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        final= ""
        for word in strs: 
            length= len(word)
            str= ""
            str+= format(length, '02x')
            for x in word: str+= format(ord(x), '02x')
            final+= str
            
        return final

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        final=[]
        while str!='':
            length= int(str[:2], 16)
            str= str[2:]
            wordhex= str[:length*2]
            str= str[length*2:]
            word= ""
            for i in range(length): word+= chr(int(wordhex[2*i:2*i+2], 16))
            final.append(word)
            
        return final
