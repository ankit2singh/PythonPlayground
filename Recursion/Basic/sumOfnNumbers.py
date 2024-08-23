# def sumn(n):   
#     i=0
#     while(i<n):
#         i +=1
#         #print(n,i)
#         res = res+i
#     return res


#recusrsion
def sumn(i,res):
    if i<1:
        print(res)
        return

    sumn(i-1,res+i)  


print(sumn(5,0))        