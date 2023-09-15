"""
Description given in each function
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'pointsBelong' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER y1
#  3. INTEGER x2
#  4. INTEGER y2
#  5. INTEGER x3
#  6. INTEGER y3
#  7. INTEGER xp
#  8. INTEGER yp
#  9. INTEGER xq
#  10. INTEGER yq
#

def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    # Write your code here
    """
    If a point P lies in triangle ABC, then
    the sum of the areas of triangles PAB,
    PAC, PBC must cover ABC, i.e. = area ABC.
    """
    abc= [(x1,y1), (x2,y2), (x3,y3)]
    p= (xp,yp)
    q= (xq,yq)

    area_abc=   triangle_area(*abc[0], *abc[1], *abc[2])
    # degenerate triangle when area == 0
    if not area_abc:
        return 0

    p_inside= False
    q_inside= False

    if  (xp<x1 and xp<x2 and xp<x3) or \
        (xp>x1 and xp>x2 and xp>x3) or \
        (yp<y1 and yp<y2 and yp<y3) or \
        (yp>y1 and yp>y2 and yp>y3):
        pass
    else:
        areas_p =   triangle_area(*abc[0], *abc[1], *p) + \
                    triangle_area(*abc[0], *p, *abc[2]) + \
                    triangle_area(*p, *abc[1], *abc[2])
        p_inside=   area_abc == areas_p

    if  (xq<x1 and xq<x2 and xq<x3) or \
        (xq>x1 and xq>x2 and xq>x3) or \
        (yq<y1 and yq<y2 and yq<y3) or \
        (yq>y1 and yq>y2 and yq>y3):
        pass
    else:
        areas_q =   triangle_area(*abc[0], *abc[1], *q) + \
                    triangle_area(*abc[0], *q, *abc[2]) + \
                    triangle_area(*q, *abc[1], *abc[2])
        q_inside=   area_abc == areas_q

    if p_inside and q_inside:
        return 3
    if p_inside:
        return 1
    if q_inside:
        return 2
    return 4
    
def triangle_area(x1, y1, x2, y2, x3, y3):
    """
    Use shoelace method to find area of
    triangle in coordinate geometry
    """
    # (x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3) /2
    return (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1 = int(input().strip())

    y1 = int(input().strip())

    x2 = int(input().strip())

    y2 = int(input().strip())

    x3 = int(input().strip())

    y3 = int(input().strip())

    xp = int(input().strip())

    yp = int(input().strip())

    xq = int(input().strip())

    yq = int(input().strip())

    result = pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq)

    fptr.write(str(result) + '\n')

    fptr.close()
