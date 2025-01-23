
# This function returns the maximum contiguous subsequence sum in an int array

#1st approach
#O(n) time complexity and O(1) space complexity
# By time complexity, I mean work and span in this case
def mcss(s):
    maxSum, currSum = 0 #O(1) time complexity, O(1) space complexity
    for i in s: #O(n) time complexity
        currSum += i
        maxSum = max(maxSum, currSum) #O(1)
        if currSum < 0:
            currSum = 0
    return maxSum

#Divide and Conquer Approach
#Useful if there are multiple processors 

# takes an integer array and returns a 4-elem tuple (a,b,c,d)
# a -> max contiguous subsequence sum
# b -> max contiguous prefix sum
# c -> max contiguous suffix sum
# d-> total sum of array

import math
def mcss_div_conq_helper(s):
    if len(s) == 0: #O(1) time (work and span) and space
        return (0,0,0,0)
    elif len(s) == 1: #O(1) time (work and span) and space
        # m = max(0,s[0])
        m = s[0]
        return (m,m,m,s[0])
    else:
        total_len = len(s) #O(1) time (work and span) and space
        mid = len(s) // 2
        Left, Right = s[:mid], s[mid:]
        #O(1) time (work and span) and space
        (a,b,c,d), (e,f,g,h)  = mcss_div_conq_helper(Left), mcss_div_conq_helper(Right)
        #O(n) work, O(log n) span and O(1) space
        return (max(a, e, c+f), max(b, d+f), max(g, h+c), d+h)
        #O(1) time (work and span) and space
    
def mcss_div_conq(s): return mcss_div_conq_helper(s) [0]  #O(n) work, O(log n) span and O(1) space
        

