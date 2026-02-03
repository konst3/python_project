# Authors: Konstantinos Papalamprou, 
# Date: 13/1/2026
# Implementation of Sequencial Bubble Sort Algorithm

from utils.sort import merge_lists

import multiprocessing as mp

# Bubble Sort
class BubbleSort:
    name = "Bubble Sort"
    complexity = "O(n^2)"
    parallel = False
    def __init__(self, seq, ps_n=1):
        self.seq = seq


        if (ps_n != 1): print(f"DEBUG: Bubble Sort is not parallel, so it will run on 1 thread instead of {ps_n}")


    def __str__(self):
        return f"Algorithm {BubbleSort.name}, Complexity: {BubbleSort.complexity}"

    def sort(self, a):
        N = len(a)

        for i in range(N-1, 0, -1):
            for j in range(0, i, 1):
                k = j + 1
                if (a[j] > a[k]):
                    tmp = a[j]
                    a[j] = a[k]
                    a[k] = tmp

                # a[j], a[j+1], _ = compare_and_exchange(a[j], a[j+1])
                
        return a

    def run(self):
        return self.sort(self.seq)

# XXX: ONLY DEMO, NOT FINISHED
# Parallel Bubble Sort
class ParallelBubbleSort(BubbleSort):
    name = "Parallel Bubble Sort"
    complexity = "O(n)"
    parallel = True
    
    def __init__(self, seq, ps_n):
        self.seq = seq
        self.ps_n = ps_n
    
    def __str__(self):
        return f"Algorithm {ParallelBubbleSort.name}, Complexity: {ParallelBubbleSort.complexity}"



    def parallel_sort(self, a, p_ps):
        # Devide the sequence into chunks
        self.chunks = []

        # print("Generating chunks... ")

        stp = max(1, round(len(a)/p_ps)) # step for seperating chunks

        for i in range(0, len(a), stp):
            self.chunks.append(a[i:i+stp])
        # print(f"Generated: {len(self.chunks)}")

        # Make a pool of processes to sort each chunk
        with mp.Pool(processes=p_ps) as pool:
            self.sorted = pool.map(self.sort, self.chunks)

        # Merge the chunks
        while (len(self.sorted)-1 > 0):
            self.sorted[0] = merge_lists(self.sorted[0], self.sorted[1])
            self.sorted.pop(1)

        return self.sorted[0]

    def run(self):
        return self.parallel_sort(self.seq, self.ps_n)
