# Authors: Panagiotis Koutsoumanis
# Date: 3/2/2026
#
# Implementation of Quicksort Algorithm:
#   1. Quicksort
#   2. Parallel Quicksort

class QuickSort:
    complexity = "O(NlogN)"
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

class ParallelQuickSort:
    pass