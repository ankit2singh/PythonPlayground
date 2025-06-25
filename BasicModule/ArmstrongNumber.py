def Armstrong(n):
    num_og = n
    result = 0
    while n > 0:
        digit = n%10
        result = result + digit**3
        n = n//10

    if result == num_og:
        return True
    else:
        return False

print(Armstrong(333)) #153 and 1634 are the armstrong number