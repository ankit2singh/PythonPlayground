a=int(input("enter a number : "))

for i in range(2,a//2):

    if a%i==0:
         print("this is not a prime number")
         break
else:
    print("this is a prime number")