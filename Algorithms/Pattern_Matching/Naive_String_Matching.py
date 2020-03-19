"""'
Basic Description:
    1. Naive String Matching Algorithm is the simplest method for string matching.
    2. Performs checking in all positions of the text whether or not the pattern occurs.
    3. After each appempt the algorithm shifts the pattern by exactly one position to the right.

TIME COMPLEXITY ANALYSIS:-
    n -- length of source string.
    m -- length of pattern string.

Best-Case:
    The best-case occurs when the first character of the pattern does not exist in the source string(T).
    Example:
        T = 'acaabc'
        P = 'daa'
    The number of comparisons in best case is O(n).

Worst-Case:
    The worst-case can occur in the following two situations:
        -> When all characters of the source string(T) and pattern(P) are the same.
            T = 'aaaaaaaaaaa'
            P = 'aaaa'
        -> When only the last character is different.
            T = 'aaaaaaaaaad'
            P = 'aaad'
The number of comparisons in worst case is O(m * (n - m + 1)) or approximately O(m * n).
"""


def naive_string_matching(string, pattern):
    n = len(string)
    m = len(pattern)
    '''
    s <-- Shift Index
    A loop to slide pattern one by one
    '''
    for s in range((n - m) + 1):
        '''
        j is the pointer for the pattern string /
        j pattern match indicator
        '''
        j = 0
        '''
        For current index s find if there is a pattern match by comparing each 
        character in the string starting from current index to each character 
        in the pattern string 
        if a match is not found break loop
        '''
        while j < m:
            if string[s + j] != pattern[j]:
                break
            j += 1
        '''
        j indicates whether the pattern has been compared successfully 
        if the value in  j is equal to the length of the pattern string,
        then there was a successful pattern match else no
        You can break inside this if block if you want to end with one search
        '''
        if j == m:
            print("Pattern Match Found with shift: ", s)


if __name__ == '__main__':
    T = input("Enter the String: ")
    P = input("Enter the Pattern: ")

    naive_string_matching(T, P)
