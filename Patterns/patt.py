# * * * * * * 
# * *     * * 
# *         * 
# *         * 
# * *     * * 
# * * * * * *

def pat(n):
    for i in range(n,-1,-1):
      for j in range(i):
         print("*")
      j -= 1   
    i-=1
pat(5)   