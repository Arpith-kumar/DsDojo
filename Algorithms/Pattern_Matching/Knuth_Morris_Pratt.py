"""'
Basic Description:
    1. The Knuth Morris Pratt(KMP) uses degenerating property of the pattern and improves the worst case complexity to O(n).
    2. Degenerating property means pattern having same sub-patterns appearning more than once in the pattren are considered.
    3. KMP involves in constructing a LPS/IPS table or pi table which indicates longest proper prefix which is also a suffix.
    4. This LPS/IPS table is of same size as the pattern string.
    5. After the LPS/IPS table is constructed we use it to find the pattern in the given string without backtracking as in Naive String Matching Algorithm.

TIME COMPLEXITY ANALYSIS:-
    n -- length of source string.
    m -- length of pattern string.
    
    We go through the string only once without backtracking hence -- n times.
    To prepare the LPS/IPS table or pi table we parse through the pattern  -- m times

    Therefore time complexity is O(m + n) or approximately O(n). 
"""


'''
Generate LPS table with time complexity O(size_of_pattern)
'''
def generate_ips_table(pattern):
    # Initilize LPS table
    lps = [None] * len(pattern)
    # Two pointer are required for the pattern string i.e j and i
    j = 0
    i = 1

    # First value for the LPS table is always 0
    lps[0] = 0

    # Generate ILP
    while(i < len(pattern)):
        '''
        If char at ith and jth position are equal then the ilp table 
        value for the ith position is j + 1, the increment both i and j
        '''
        if(pattern[i] == pattern[j]):
            lps[i] = j + 1
            j += 1
            i += 1
        else:
            '''
            Else if j is not 0 then the jth pointer movers to the ilp
            table value present at position j-1, if j is 0 the we simply 
            assign the LPS table value for that ith positon to be 0-
            '''
            if(j != 0):
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    # Return the generated LPS Table
    return lps

'''
KMP pattern matching algorithm. 
'''
def kmp_algorithm(source, pattern):
    # Get ILP
    lps = generate_ips_table(pattern)
    '''
    We need two pointers one pointer for source string(i) and one for
    pattern string(j)
    '''
    i = 0
    j = 0

    while(i < len(source) and j < len(pattern)):
        ''' 
        Continue incrementing i and j if char at i and j are equal
        else if j is not at 0 the move j to the index value specified
        at the j - 1 position in the LPS table.
        If j is at 0 then simply increment i.
        '''
        if(source[i] == pattern[j]):
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    if j == len(pattern):
        pattern_position = (i - j)
        return (True, pattern_position)
        
    return (False, None)

if __name__ == "__main__":
    source_string = input("Enter the source string: ")
    pattern_string = input("Enter the pattern string: ")

    result, position = kmp_algorithm(source_string, pattern_string)
    print("Pattern present: ", result)
    print("Pattern Match Found at position: ", position)
