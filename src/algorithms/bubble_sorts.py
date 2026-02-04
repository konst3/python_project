# Authors: Konstantinos Papalamprou, 
# Date: 13/1/2026
#
# Implementation of
#   1. Sequencial Bubble Sort Algorithm
#   2. Parallel Bubble Sort Algorithm/Odd-Even Transposition Sort Algorithm

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

                # a[j], a[j+1], _ = compare_and_exchange(a[j], a[j+1])
                
        return a

    def run(self):
        return self.sort(self.seq)

# Implementation of Odd Even Transposition Sort
class OddEvenTranspositionSort:
    # complexity = "O(n)"
    # parallel = True

    # def __init__(self, seq, ps_n=1):
    #     self.seq = seq
    #     self.ps_n = ps_n

    # def sort(self, a):
    #     self.N = len(a)
        
    #     # Use multiprocessing with a manager for shared list
    #     with mp.Manager() as manager:
    #         shared_list = manager.list(a)
    #         sorted_flag = manager.Value("b", False)
    #         phase = 0

    #         # print(f"DEBUG: Phase {phase} - Active children BEFORE pool: {len(mp.active_children())}")

    #         with mp.Pool(processes=self.ps_n) as pool: # NOTE: Add the pool outside of the loop to avoid overhead
    #             while not sorted_flag.value:
    #                 # print(f"DEBUG: Phase {phase} - INSIDE even pool: {len(mp.active_children())} processes")
    #                 sorted_flag.value = True

    #                 # Even phase
    #                 if (phase % 2 == 0):  
    #                     args = [(shared_list, i, i + 1, sorted_flag) for i in range(0, self.N - 1, 2)]
    #                     pool.starmap(self.compare_and_exchange, args) # Map the args (NOTE: starmap takes the arguments) to the processes
    #                     # print(phase, list(args[0][0]))
        
    #                 # Odd phase
    #                 else:
    #                     args = [(shared_list, i, i + 1, sorted_flag) for i in range(1, self.N - 1, 2)]
    #                     pool.starmap(self.compare_and_exchange, args) # Execute comparisons in parallel, limited by pool size
    #                     # print(phase, list(args[0][0]))

    #                 phase += 1

    #         # print(f"DEBUG: Phase {phase} - Active children AFTER pool: {len(mp.active_children())}")
            
    #         return list(shared_list)

    # def compare_and_exchange(self, shared_list, i, j, sorted_flag):
    #     if shared_list[i] > shared_list[j]:
    #         tmp = shared_list[i]
    #         shared_list[i] = shared_list[j]
    #         shared_list[j] = tmp
    #         sorted_flag.value = False

    # def run(self):
    #     return self.sort(self.seq)
    
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

                # a[j], a[j+1], _ = compare_and_exchange(a[j], a[j+1])
                
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