class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        dict={}
        for i in arr:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
    
        arr1=[0]*N
        
        for i in range(1,N+1):
            if i not in dict:
                arr[i-1]=0
            else:
                arr[i-1]=dict[i]
        return arr1     

ob = Solution()
print(ob.frequencyCount([2, 3, 2, 3, 5]))
