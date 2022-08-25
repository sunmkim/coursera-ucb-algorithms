from typing import List


def BSH_helper(elem: int, lst: int, left: int, right: int):
    """
    0 <= left <= right < size(lst)
    invariant property: if elt in lst, it must be between lst[left] and lst[right]
    """
    # if pointers crossover, elem not in list
    if left > right:
        print('Element not found in list')
        return None
    else:
        # compute mid-point
        mid = (left + right) // 2
        # then compare mid-point to search elem
        if lst[mid] == elem:
            print(f'Element found in index {mid}')
            return mid
        elif lst[mid] < elem:
            return BSH_helper(elem, lst, mid+1, right)
        elif lst[mid] > elem:
            return BSH_helper(elem, lst, left, mid-1)


def binary_search(elem: int, lst: List[int]):
    # call helper on whole list
    # will use recursion down the list
    BSH_helper(elem, lst, 0, len(lst))

binary_search(11, [-1,0,2,7,8,9,11])