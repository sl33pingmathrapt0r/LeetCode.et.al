"""
Have the function StringReduction(str) take 
the str parameter being passed and return 
the smallest number you can get through the 
following reduction method. The method is: 
Only the letters a, b, and c will be given 
in str and you must take two different 
adjacent characters and replace it with the
third. For example "ac" can be replaced with
"b" but "aa" cannot be replaced with 
anything. This method is done repeatedly 
until the string cannot be further reduced, 
and the length of the resulting string is to
be outputted.

For example: 
if str is "cab", then "ca" can be reduced to 
"b" and you get "bb" (you can also reduce it 
to "cc"). The reduction is done so the output 
should be 2. If str is "bcab", "bc" reduces 
to "a", so you have "aab", then "ab" reduces 
to "c", and the final string "ac" is reduced 
to "b" so the output should be 1.

abcabc --> 2
cccc --> 4
"""

def StringReduction(strParam):

  # code goes here
  if len(strParam)==0: return 0
  if len(strParam)==1: return 1
  if len(strParam)==2: 
    if strParam[0]==strParam[1]: return 2
    else: return 1
  
  stack= [strParam[0]]
  for i in range(1,len(strParam)):
    stack.append(strParam[i])
    while len(stack)>1 and stack[-1] != stack[-2]: 
      stack.append(changes( (stack.pop(), stack.pop()) ))
  
  return len(stack)
  

def changes(x: tuple):
  """
  Takes in a tuple of 2 characters 
  as input. Returns the character 
  not in the tuple. 
  """
  if 'a' not in x: return 'a'
  if 'b' not in x: return 'b'
  return 'c'

# keep this function call here 
print(StringReduction(input()))