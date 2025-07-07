# reverse an array using recursion

#TC -> O(N), SC ->O(N)
 
def re_arr(arr,left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    re_arr(arr, left+1, right-1)
    return arr
print(re_arr([1,2,3,4],0,3))