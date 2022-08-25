def insert(arr: list, j: int) -> list:
    for i in range(j-1, -1, -1):
        if arr[i] > arr[i+1]:
            # swap
            temp_i = arr[i]
            arr[i] =  arr[i+1] 
            arr[i+1] = temp_i
        else:
            break
    return arr

def insertion_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        new_arr = insert(arr, i)
    return new_arr

inserted_arr = insertion_sort([7,2,0,11,9,8,-1])
print(inserted_arr)