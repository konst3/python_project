# Authors: Konstantinos Papalamprou
# Date: 31/1/2026
#
# Implementation of
#   1. Merge Sort
#   2. Parallel Merge Sort

from utils.sort import merge_lists

class MergeSort:
    complexity = "O(nlogn)"
    parallel = False

    def __init__(self, seq, ps_n=1):
        self.seq = seq

        if (ps_n != 1): print(f"DEBUG: Merge Sort is not parallel, so it will run on 1 thread instead of {ps_n}")

    def sort(self, a):
        N = len(a)
        mid = N//2
        
        if (N == 1): return a # Stop recursion when there is only one item left

        a_left = a[:mid]
        a_right = a[mid:]

        a_left = self.sort(a_left)
        a_right = self.sort(a_right)
        
        a = merge_lists(a_left, a_right)
        return a

    def run(self):
        return self.sort(self.seq)
    
class ParallelMergeSort:
    name = "Parallel Merge Sort"
    complexity = "-"
    parallel = True

    def __init__(self, seq, ps_n):
        self.seq = seq
        self.ps_n = ps_n

    def parallel_sort(self, seq, ps_n):
        N = len(seq)

        return seq

    def run(self):
        return self.parallel_sort(self.seq, self.ps_n)
    
# Unit testing
if (__name__ == "__main__"):
    from utils.utils import generate_sequence

    seq = generate_sequence(N=8, max_value=8)
    print(f"DEBUG: seq = {seq}")

    sort = ParallelMergeSort(seq, 7)
    print(f"DEBUG: solved seq = {sort.run()}")