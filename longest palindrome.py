def longest_palindrome(s):
    from collections import Counter
    count = Counter(s)
    length = 0
    odd_present = False
    for val in count.values():
        if val % 2 == 0:
            length += val
        else:
            length += val - 1
            odd_present = True
    
    return length + 1 if odd_present else length
print(longest_palindrome("abccccdd"))  
print(longest_palindrome("a"))         