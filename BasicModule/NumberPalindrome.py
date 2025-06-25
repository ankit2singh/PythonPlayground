def checkPalindrome(n:list):
    
    num_og = n
    result = 0

    while n > 0:
        digit = n%10
        result = result*10 + digit  # 678
        n = n//10

    if result == num_og:
        return True
    else:
        return False
    # return result

print(checkPalindrome(444))
print(checkPalindrome(4434))