# def bubblesoryt(a: list):
#     for i in len(a)-1:
#         i=0
#         j=i+1
#         if a[j]<a[i]:
#             a[j] , a[i] = a[i],a[j]
#     return a            

# print(bubblesoryt([7,8,1,2]))     

def bubblesoryt(a: list):
    n = len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

print(bubblesoryt([7, 8, 1, 2]))
