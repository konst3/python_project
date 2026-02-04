# Authors: Konstantinos Papalamprou, 
# Date: 13/1/2026
#
# Implementation of
#   1. Sequencial Bubble Sort Algorithm
#   2. Parallel Bubble Sort Algorithm
#   3. Odd-Even Transposition Sort Algorithm
#   4. Parallel Odd-Even Transposition Sort Algorithm

from utils.sort import merge_lists

import multiprocessing as mp

# Bubble Sort
class BubbleSort:
    complexity = "O(n^2)"
    parallel = False

    def __init__(self, seq, ps_n=1):
        self.seq = seq

        if (ps_n != 1): print(f"DEBUG: Bubble Sort is not parallel, so it will run on 1 thread instead of {ps_n}")

    def sort(self, a):
        N = len(a)

        for i in range(N-1, 0, -1):
            for j in range(0, i, 1):
                k = j + 1
                if (a[j] > a[k]):
                    tmp = a[j]
                    a[j] = a[k]
                    a[k] = tmp
                
        return a

    def run(self):
        return self.sort(self.seq)

# Parallel Bubble Sort
class ParallelBubbleSort(BubbleSort):
    name = "Parallel Bubble Sort"
    complexity = "O(n)"
    parallel = True
    
    def __init__(self, seq, ps_n):
        self.seq = seq
        self.ps_n = ps_n

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

# Implementation of Odd-Even Transposition Sort
class OddEvenTranspositionSort:
    name = "Odd Even Transposition Sort"
    complexity = "O(n^2)"
    parallel = False
    def __init__(self, seq, ps_n=1):
        self.seq = seq
        self.ps_n = ps_n


        if (ps_n != 1): print(f"DEBUG: Odd-Even Transposition Sort is not parallel, so it will run on 1 thread instead of {ps_n}")

    def __str__(self):
        return f"Algorithm {self.name}, Complexity: {self.complexity}"

    def sort(self, a):
        N = len(a)

        i = 0 # TODO: Remove, only for debug

        while True:
            for i in range(N//2):
                exchanged_values = False

                # Even phase
                for j in range(0, N, 2):
                    k = j + 1

                    if (a[j] > a[k]):
                        tmp = a[j]
                        a[j] = a[k]
                        a[k] = tmp
                        exchanged_values = True

                # Odd phase
                for j in range(1, N-1, 2):
                    k = j + 1

                    if (a[j] > a[k]):
                        tmp = a[j]
                        a[j] = a[k]
                        a[k] = tmp
                        exchanged_values = True

                if (not exchanged_values): break # Finish sort when there was no value exchange made

            return a


    def run(self):
        return self.sort(self.seq)

# Implementation of Parallel Odd Even Transposition Sort
class ParallelOddEvenTranspositionSort:
    complexity = "O(n)"
    parallel = True

    def __init__(self, seq, ps_n):
        self.seq = seq
        self.ps_n = ps_n

    def sort(self, a):
        N = len(a)

        for i in range(N-1, 0, -1):
            for j in range(0, i, 1):
                k = j + 1
                if (a[j] > a[k]):
                    tmp = a[j]
                    a[j] = a[k]
                    a[k] = tmp

        return a
    
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