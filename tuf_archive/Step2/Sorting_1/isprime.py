a = int(input())
# print(a)
# 7 -> 2,3,4,5,6,  7//2 =3
for i in range(2,a//2 +1):
    if a%i ==0:
        print("This no. is not prime")
        break
else:
    print("this is prime")    

