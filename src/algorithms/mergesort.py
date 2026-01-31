# Authors: Konstantinos Papalamprou
# Date: 31/1/2026
# Implementation of Merge Sort

from utils.sort import compare_and_exchange

class MergeSort:
    def __init__(self, seq, ps_n=1):
        self.seq = seq

        self.name = "Merge Sort"
        self.complexity = "O(n^2)"
        self.parallel = False

        if (ps_n != 1): print(f"DEBUG: Merge Sort is not parallel, so it will run on 1 thread instead of {ps_n}")

    def __str__(self):
        return f"Algorithm {self.name}, Complexity: {self.complexity}"

    def sort(self, a):
        N = len(a)
        mid = N//2
        
        if (N == 1): return a # Stop recursion when there is only one item left

        a_left = a[:mid]
        a_right = a[mid:]

        print(a_left, a_right)

        self.sort(a_left)
        
        a_left, a_right, _ = compare_and_exchange(a_left, a_right)

        return a

    def run(self):
        return self.sort(self.seq)