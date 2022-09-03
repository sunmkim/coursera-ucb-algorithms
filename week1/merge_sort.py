def merge(left_arr, right_arr):
    i,j = 0,0
    tmp = []
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            tmp.append(left_arr[i])
            i += 1
        elif left_arr[i] >= right_arr[j]:
            tmp.append(right_arr[j])
            j += 1

    if i < len(left_arr):
        tmp.extend(left_arr[i:])
    elif j < len(right_arr):
        tmp.extend(right_arr[j:])
    return tmp



def mergesort(arr):
    # base case of arr n=1
    if len(arr) == 1:
        return arr
    # base case of arr n=2
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr.reverse()
        return arr 
    else:
        mid = len(arr) // 2
        left_half = arr[:mid+1]
        right_half = arr[mid+1:]
        left_half = mergesort(left_half)
        right_half = mergesort(right_half)
    
        # merge 
        return merge(left_half, right_half)

# BEGIN TEST CASES
arr1 = [-1, 1, 4, 0]
j1 = mergesort(arr1)
print(f'Arr after mergesort: {j1}')
assert j1 == [-1, 0, 1, 4], "Test Case # 1 failed"


arr2 = [0, 5, 4.1, -9, -10, 50, 47, 0]
j2 = mergesort(arr2)
print(f'Arr after mergesort: {j2}\n')
assert j2 == [-10, -9, 0, 0, 4.1, 5, 47, 50], "Test Case # 2 failed"

arr3 = [10,9,8,-7,7,6,5,4,3,2,1]
j3 = mergesort(arr3)
print(f'Arr after mergesort: {j3}\n')
assert j3 == [-7,1,2,3,4,5,6,7,8,9,10], "Test Case # 3 failed"

print('Congratulations: all test cases passed')
#END TEST CASES