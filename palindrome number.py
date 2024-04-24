def is_palindrome(x):
    if x < 0:
        return False
    elif x == int(str(x)[::-1]):
        return True
    else:
        return False
print(is_palindrome(121))  
print(is_palindrome(-121))
print(is_palindrome(10)) 
