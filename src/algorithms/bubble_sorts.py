# Authors: Konstantinos Papalamprou, 
# Date: 13/1/2026
# Implementation of Sequencial Bubble Sort Algorithm

# ONLY DEMO, NOT FINISHED

import multiprocessing as mp

class Bubble_sort:
    def __init__(self, seq,thr=1):
        self.seq = seq

        self.name = "Bubble Sort"
        self.complexity = "O(n^2)"

    def __str__(self):
        return f"Algorithm {self.name}, Complexity: {self.complexity}"

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
        return f"Result: {self.sort(self.seq)}"

class Parallel_Bubble_sort(Bubble_sort):
    def __init__(self, seq, ps_n):
        self.seq = seq
        self.ps_n = ps_n

        if (ps_n == 0):
            print("ERROR: You must select the single thread sort")
            exit(-1)

        self.name = "Parallel Bubble Sort"
        self.complexity = "O(n^2/p + n), p: number of threads"

    def merge_lists(self, l1, l2):
        merged = []
        i = 0
        j = 0

        while ((i < len(l1)) and (j < len(l2))):
            if (l1[i] < l2[j]):
                merged.append(l1[i])
                i += 1
            else:
                merged.append(l2[j])
                j += 1

        if (i < len(l1)): merged += l1[i:]
        elif (j < len(l2)): merged += l2[j:]

        return merged

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
            self.sorted[0] = self.merge_lists(self.sorted[0], self.sorted[1])
            self.sorted.pop(1)

        return self.sorted[0]
    
    def run(self):
        return f"Result: {self.parallel_sort(self.seq, self.ps_n)}"
