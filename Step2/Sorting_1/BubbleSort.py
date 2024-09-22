def bubblesoryt(a: list):
    n = len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

print(bubblesoryt([7, 8, 1, 2]))