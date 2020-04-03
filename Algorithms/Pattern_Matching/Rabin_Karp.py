"""
Basic Description:
    1. In Rabin Krap Algorithm we compare the hash value of the pattern and the sub-string.
    2. If the hash matches with any sub-string then we start comparing each character of pattern with that of the substring.
    3. If the hash does not match then we simplly move to the next sub-string by increment of one.
    4. Also we use a method called rolling hash to compute the hash values efficiently.

TIME COMPLEXITY ANALYSIS:-
    n -- length of source string.
    m -- length of pattern string.

Best-Case:
    The average and the best case time complexity of this algorithm is O(m + n).

Worst-Case:
    Worst case time complexity of this algorithm is O(mn).

    Worst case in this algorithm occurs when all the sub-string if the source string matches with hash value of the pattern string.

    Example:
        T = "AAAAAAAAA"
        P = "AAA"

Rabin-Karp is really helpful when we have to match multile patterns with a given source string.
"""
prime = 101

def check_equality(string_one, string_two):

    if len(string_one) != len(string_two):
        return False

    for char_1, char_2 in zip(string_one, string_two):
        if char_1 != char_2:
            return False
    return True

def generate_hash(pattern, length):
    hash = 0
    for i in range(length + 1):
        hash += ord(pattern[i]) * pow(prime, i)
    
    return hash

def rolling_hash(source, old_index, new_index, old_hash, pattern_len):
    new_hash = old_hash - ord(source[old_index])
    new_hash /= prime
    new_hash += ord(source[new_index]) * pow(prime, pattern_len - 1)
    return new_hash

def rabin_karp(source, pattern):
    n =len(source)
    m = len(pattern)

    pattern_hash = generate_hash(pattern, m - 1)
    source_hash = generate_hash(source, m - 1)

    for i in range(1, n - m + 2):
        if pattern_hash ==  source_hash:
            if check_equality(source[i - 1: i + m - 1], pattern):
                return i - 1
        if i < n - m + 1:
            source_hash = rolling_hash(source, i - 1, i + m - 1, source_hash, m)

    return -1

if __name__ == "__main__":
    
    inputs = [
        ("ArpithKumar", "Kumar"),
        ("ArpithKumar", "pith"),
        ("ArpithKumar","mar"),
        ("ArpithKumar","Arp"),
        ("ArpithKumar","tha"),
    ]
        
    for source_string, pattern_string in inputs:
        result = rabin_karp(source_string, pattern_string)
        if result >= 0:
            print(f"=> ({source_string},{pattern_string}) -- Match found at position: {result}")
        else:
            print(f"=> ({source_string},{pattern_string}) -- Match Not found")
