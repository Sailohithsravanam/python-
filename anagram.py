def isAnagram(s, t):
    return sorted(s) == sorted(t)
print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
