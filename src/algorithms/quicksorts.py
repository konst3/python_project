# Authors: Panagiotis Koutsoumanis, Konstantinos Papalamprou
# Date: 3/2/2026
#
# Implementation of Quicksort Algorithm:
#   1. Quicksort
#   2. Lomuto Quicksort
#   3. Hoare Quicksort
#   4. Parallel Quicksort

import multiprocessing as mp

# Normal Quicksort implementation
class QuickSort:
    complexity = "O(nlogn)"
    parallel = False
    
    def __init__(self, seq, ps_n=1):
        self.seq = seq

        if (ps_n != 1): print(f"DEBUG: Quicksort is not parallel, so it will run on 1 thread instead of {ps_n}")

    def sort(self, a):
        #N = len(a)
        lt = []
        ht = []
        if len(a) > 1:
            piv =  a[0]
            for i in a:
                if i < piv: lt.append(i)
                elif i > piv: ht.append(i) 
                #doesn't incl. elements equal to piv but we don't have dupes in this so w/e
            return self.sort(lt) + [piv] + self.sort(ht)
        else: 
            return a
    
    def run(self):
        return self.sort(self.seq)

###

# Lomuto Quicksort implementation
class LomutoQuickSort(QuickSort):
    def partition_lomuto(self, a, low, high):
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[high] = a[high], a[i + 1]
        return i + 1

    def sort_helper(self, a, low, high):
        if low < high:
            pi = self.partition_lomuto(a, low, high)
            self.sort_helper(a, low, pi - 1)
            self.sort_helper(a, pi + 1, high)

    def sort(self, a):
        if len(a) <= 1:
            return a
        a_copy = a.copy()
        self.sort_helper(a_copy, 0, len(a_copy) - 1)
        return a_copy

# Hoare Quicksort implementation
class HoareQuickSort(QuickSort):
    def partition_hoare(self, a, low, high):
        pivot = a[low]
        i = low - 1
        j = high + 1
        while True:
            # Move i to the right until we find element > pivot
            i += 1
            while i <= high and a[i] < pivot:
                i += 1
            # Move j to the left until we find element < pivot
            j -= 1
            while j >= low and a[j] > pivot:
                j -= 1
            # If pointers crossed, partition is done
            if i >= j:
                return j
            # Swap elements and continue
            a[i], a[j] = a[j], a[i]

    def sort_helper(self, a, low, high):
        if low < high:
            pi = self.partition_hoare(a, low, high)
            self.sort_helper(a, low, pi)
            self.sort_helper(a, pi + 1, high)

    def sort(self, a):
        if len(a) <= 1:
            return a
        a_copy = a.copy()
        self.sort_helper(a_copy, 0, len(a_copy) - 1)
        return a_copy

class ParallelQuickSort:
    complexity = "O(n)"
    parallel = True
    
    def __init__(self, seq, ps_n):
        self.seq = seq
        self.ps_n = ps_n

    def sort(self, a, ps_n=None):
        if ps_n is None:
            ps_n = self.ps_n
        
        if len(a) <= 1:
            return a
        
        # Partition: classic quicksort style
        piv = a[0]
        lt = [x for x in a[1:] if x < piv]
        ht = [x for x in a[1:] if x >= piv]
        
        # If ps_n <= 1, run sequentially
        if ps_n <= 1:
            return self.sort(lt, ps_n=1) + [piv] + self.sort(ht, ps_n=1)
        
        # Otherwise, spawn child process for left partition
        child_ps_n = ps_n // 2
        parent_ps_n = ps_n - child_ps_n
        
        parent_conn, child_conn = mp.Pipe()
        process = mp.Process(target=self.p, args=(child_conn, lt, child_ps_n))
        process.start()
        
        # Parent sorts right partition
        ht_sorted = self.sort(ht, ps_n=parent_ps_n)
        
        # Get sorted left from child
        lt_sorted = parent_conn.recv()
        process.join()
        
        return lt_sorted + [piv] + ht_sorted
    
    def p(self, conn, seq, ps_n):
        sorter = ParallelQuickSort(seq, ps_n)
        sorted_seq = sorter.sort(seq, ps_n=ps_n)
        conn.send(sorted_seq)
        conn.close()
    
    def run(self):
        return self.sort(self.seq, self.ps_n)