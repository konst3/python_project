# Authors: Konstantinos Papalamprou
# Date: 31/1/2026
#
# Implementation of
#   1. Merge Sort
#   2. Parallel Merge Sort

from utils.sort import merge_lists

import multiprocessing as mp

# Merge Sort implementation
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

# Parallel Merge Sort implementation 
class ParallelMergeSort:
    complexity = "O(n)"
    parallel = True

    def __init__(self, seq, ps_n):
        self.seq = seq
        self.ps_n = ps_n

    def p(self, conn, seq, ps_n):
        sorted_seq = self.sort(seq, ps_n=ps_n)
        conn.send(sorted_seq)
        conn.close()
        
    def sort(self, seq, ps_n):
        if (len(seq) <= 1):
            return seq
        
        # Spawn a child process for the left half
        # Divide process budget: child gets half, parent keeps half
        mid = len(seq) // 2
        left = seq[:mid]
        right = seq[mid:]
        
        child_ps_n = ps_n // 2
        parent_ps_n = ps_n - child_ps_n
        
        parent_conn, child_conn = mp.Pipe()
        process = mp.Process(target=self.p, args=(child_conn, left, child_ps_n))
        process.start()

        # Parent sorts right half with remaining process budget
        right_sorted = self.sort(right, ps_n=parent_ps_n)

        # Get sorted left from child
        left_sorted = parent_conn.recv()
        process.join()

        return merge_lists(left_sorted, right_sorted)

    def run(self):
        return self.sort(self.seq, self.ps_n)