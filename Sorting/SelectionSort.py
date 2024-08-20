def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the current position is the minimum
        min_index = i
        # Check the rest of the array for a smaller element
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage
print(selection_sort([7, 8, 1, 2]))
