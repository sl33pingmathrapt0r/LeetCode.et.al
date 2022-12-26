from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max=0
        # for i in range(len(height)-1):
        #     for j in range(i+1, len(height)):
        #         value= (j-i)*(min(height[j], height[i]))
        #         if value > max: max= value

        # 2-pointer approach: 
        # Pointer at start and end
        # Area is limited by shorter height; iterate down the side with
        # shorter height to verify if area increases
        start= 0
        end= len(height)-1
        while start<len(height) and height[start]==0: start+=1
        while end>=0 and height[end]==0: end-=1
        w= end-start
        if w<=0: return 0

        max=0
        while start!=end:
            if height[start]<height[end]:
                result= w*height[start]
                start+=1
            else: 
                result= w*height[end]
                end-=1 
            max= result if result>max else max
            w-=1

        return max