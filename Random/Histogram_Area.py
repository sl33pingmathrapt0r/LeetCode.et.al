"""
Have the function HistogramArea(arr) read 
the array of non-negative integers stored 
in arr which will represent the heights of
bars on a histogram (where each bar width 
is 1), and determine the largest area 
underneath the entire bar graph. 

For example: if arr is [2, 1, 3, 4, 1] 
then this looks like the following bar graph

                 ___
             ___|   |
     ___    | X | X |
    |   |___| X | X |___
____|___|___|_X_|_X_|___|_____

You can see in the above bar graph that the 
largest area underneath the graph is covered 
by the x's. The area of that space is equal 
to 6 because the entire width is 2 and the 
maximum height is 3, therefore 2 * 3 = 6. 
Your program should return 6. The array will
always contain at least 1 element.

[6, 3, 1, 4, 12, 4] --> 12
[5, 6, 7, 4, 1] --> 16
"""

# 2-pointer method for most-water-container won't work, 
# since the limit on the height of area is not just the
# left and right bounds, but the min height between the 
# 2 ends. 

def HistogramArea(arr: list):

  # code goes here
  # recursion

  # empty array
  if not arr: return 0
  # one-element
  if len(arr)==1: return arr[0]

  # get effective length
  start=0
  end= len(arr)-1
  while start<len(arr) and arr[start]==0: start+= 1
  while end>=0 and arr[end]==0: end-= 1

  # zero vector
  if end<start: return 0
  # unit vector
  if end==start: return arr[start]
  # leading and trailing zeroes
  if start!=0 or end!= len(arr)-1: return HistogramArea(arr[start: end+1])

  # non-trivial cases
  x= min(arr)
  pivot= arr.index(x)
  area= x * len(arr)
  
  return max(area, HistogramArea(arr[:pivot]), HistogramArea(arr[pivot+1:]))

# keep this function call here 
print(HistogramArea(input()))