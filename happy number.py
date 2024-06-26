def is_happy(n):
    def get_next(num):
        total_sum = 0
        while num > 0:
            num, digit = divmod(num, 10)
            total_sum += digit ** 2
        return total_sum
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1
print(is_happy(19))  
print(is_happy(2))   
