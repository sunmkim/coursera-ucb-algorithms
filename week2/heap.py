from typing import List

class MinHeap():
    def __init__(self, arr: List[int]):
        self.A = arr

    def bubble_up(self, j):
        parent = j//2 if j % 2 == 1 else j//2 - 1
        # base case is root elem
        if j == 0:
            return
        else:
            if self.A[j] < self.A[parent]:
                # swap
                self.A[j], self.A[parent] = self.A[parent], self.A[j]
                # recursive run
                self.bubble_up(parent)
        return

    
    def bubble_down(self, j):
        left = 2*j+1 if j > 0 else 1
        right = 2*j+2 if j > 0 else 2
        n = len(self.A)

        # A[j] is leaf with no children (base case)
        if left > n-1 or (self.A[j] <= self.A[left] and self.A[j] <= self.A[right]):
            return

        # A[j] has one child
        if left <= n and right >= n:
            if self.A[j] > self.A[left]:
                # swap
                self.A[j], self.A[left] = self.A[left], self.A[j]
                self.bubble_down(left)
        # A[j] has 2 children
        else:
            # locate the smaller child to swap
            if self.A[left] < self.A[right]:
                smaller = left
            elif self.A[left] > self.A[right]:
                smaller = right
            else:
                smaller = left
            # swap with smaller child
            self.A[j], self.A[smaller] = self.A[smaller], self.A[j]
            self.bubble_down(smaller)


    def insert(self, elem):
        n = len(self.A) # length before appending elem
        self.A.append(elem)
        self.bubble_up(n)

    def delete(self, i):
        if len(self.A) == 1:
            self.A.pop()
            return
        else:
            # swap last elem with elem you want to delete
            self.A[i], self.A[-1] = self.A[-1], self.A[i]

            # remove last elem (elem we want to delete)
            self.A.pop()

            if i == 0:
                parent = None
            elif i % 2 == 1:
                parent = i//2
            elif i % 2 == 0:
                parent = i//2 - 1
            
            left_child = 2*i+1 if i > 0 else 1
            right_child = 2*i+2 if i > 0 else 2
            
            # bubbleup if elem less than its parent AND has no children
            if parent is not None and self.A[i] < self.A[parent]:
                self.bubble_up(i)
            elif left_child < len(self.A) and right_child >= len(self.A):
                return
            elif len(self.A) == 1:
                return
            elif self.A[i] > self.A[left_child] or self.A[i] > self.A[right_child] or parent is None:
                self.bubble_down(i)

    def find_smallest_elem(self):
        return self.A[0]

    def heapify(self):
        n = len(self.A)
        for i in range(n//2, -1, -1):
            self.bubble_down(i)
        return self.A

    def heapsort(self):
        n = len(self.A)
        result = []
        self.heapify()

        for i in range(n):
            result.append(self.A[0])
            self.delete(0)
        return result



a2 = [110, 99, 1, 2, 1]
heap = MinHeap(a2)
sortted = heap.heapsort()
print('final heap: ', sortted)