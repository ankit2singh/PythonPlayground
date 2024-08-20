def insertion_sort(arr):
    # Start from the second element (index 1)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Insert the key element at the correct position
        arr[j + 1] = key
    return arr

# Example usage
print(insertion_sort([7, 8, 1, 2]))
