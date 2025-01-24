def paren_match(str_array):
    stack = list() #O(1) time and O(n) space
    for i in str_array: #O(n) time and O(1) space
        if i == '(':
            stack.append(i) #O(1) time
        else:
            if len(stack) != 0 :
                stack.pop(i) #O(1) time
            else:
                return False
    return True

#O(n) work and O(log n) span
def helper(str_array): #returns a six elem tuple
    if len(str_array) == 0:
        return (0,0,0,0,0,0)
    elif len(str_array) == 1 and str_array[0] == '(':
        return (1,0,1,0,0,1)
    elif len(str_array) == 1 and str_array[0] == ')':
        return (0,1,0,1,0,1)
    else:
        mid = len(str_array)//2
        Left,Right = str_array[:mid], str_array[mid:]
        (lU,rU,lD,rD,mD,tD), (lU1,rU1,lD1,rD1,mD1,tD1) = helper(Left), helper(Right)
        new_tD = tD + tD1
        matched = min(lU, rU1)
        new_lU = lU+lU1-matched
        new_rU = rU+rU1-matched
        if lU > rU1:
            new_lD = lD + tD1
        else:
            new_lD = lD1
        if lU < rU1:
            new_rD = rD1 + tD
        else:
            new_rD = rD
        if lU == rU1:
            new_mD = lD+rD1
        else:
            new_mD = 0 # Validity of parenthesis in between
        return (new_lU, new_rU, new_lD, new_rD, new_mD, new_tD)

        

        

def max_paren_dist_div_conq(str_array):
    (a,b,c,d,e,f) = helper(str_array)
    if a == 0 and b == 0 and f >= 2:
        return f - 2
    else:
        return None


