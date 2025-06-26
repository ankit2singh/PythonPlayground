def Armstrong(n):
    num_og = n
    result = 0
    degree = len(str(n))
    while n > 0:
        digit = n%10
        result = result + digit**degree
        n = n//10

    if result == num_og:
        return True
    else:
        return False

print(Armstrong(333)) #153 and 1634 are the armstrong number

print(Armstrong(153)) 

print(Armstrong(1634)) 