#Authors: Konstantinos Papalamprou, Panagiotis Koutsoumanis
#Date: 15/1/2026
#Implementation of Quicksort Algorithm
from utils.sort import merge_lists

class QuickSort:
    def __init__(self, seq, ps_n=1):
        self.seq = seq
        self.name = "Bubble Sort"
        self.complexity = "O(NlogN)"
        self.parallel = True

        if (ps_n != 1): print(f"DEBUG: Quicksort is not parallel, so it will run on 1 thread instead of {ps_n}")

    def __str__(self):
        return f"Algorithm {self.name}, Complexity: {self.complexity}"
    
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

