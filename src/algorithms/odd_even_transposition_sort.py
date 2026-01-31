# Authors: Konstantinos Papalamprou
# Date: 31/1/2026
# Implementation of Odd Even Transposition Sort

import multiprocessing as mp

class OddEvenTranspositionSort:
    def __init__(self, seq, ps_n=1):
        self.seq = seq
        self.ps_n = ps_n

        self.name = "Odd Even Transposition Sort"
        self.complexity = "?"
        self.parallel = True

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

# FIXME: Parallel Version is slow
# Parallel Odd Even Transposition Sort
class ParallelOddEvenTranspositionSort(OddEvenTranspositionSort):
    def __init__(self, seq, ps_n=1):
        self.seq = seq
        self.ps_n = ps_n

        # self.exchanged_values=False

        self.name = "Odd Even Transposition Sort"
        self.complexity = "?"
        self.parallel = True

    def __str__(self):
        return f"Algorithm {self.name}, Complexity: {self.complexity}"

    def merge_pairs(self, pairs):
        merged_pairs = []

        for pair in pairs:
            merged_pairs += pair

        return merged_pairs

    def sort(self, a):
        N = len(a)

        # From the link
        # rank = self.process_id()
        # A = self.initial_value()

        # for i in range(N):
        #     if (i % 2 == 0):
        #         if (rank % 2 == 0):
        #             self.recv(B, rank + 1)
        #             self.send(A, rank + 1)
        #             A = min(A, B)

        #         else:
        #             self.send(A, rank - 1)
        #             self.recv(B, rank - 1)
        #             A = max(A, B)

        #     elif ((rank > 0) and (rank < N - 1)):
        #         if (rank % 2 == 0):
        #             self.recv(B, rank - 1)
        #             self.send(A, rank - 1)
        #             A = max(A, B)

        #         else:
        #             self.send(A, rank + 1)
        #             self.recv(B, rank + 1)
        #             A = min(A, B)

        i = 0 # TODO: Remove, only for debug

        # with mp.Pool(self.ps_n) as pool:
            # while True:
            # for i in range(N//2):
                # self.exchanged_values = False

                # Even phase
                # even_pairs = [[a[j], a[j+1]] for j in range(0, N, 2)] # Get the even pairs from the sequence
                # a = self.merge_pairs(pool.map(compare_and_exchange, even_pairs))
                # print(a)
                
                # Odd phase
                # odd_pairs = [[a[j], a[j+1]] for j in range(1, N-1, 2)]
                # a = [a[0]] + self.merge_pairs(pool.map(compare_and_exchange, odd_pairs)) + [a[N-1]]
                # print(a)

                # Odd phase
                # for j in range(1, N-1, 2):
                #     a[j], a[j+1], exchanged_values = compare_and_exchange(a[j], a[j+1], exchanged_values)
                #     print(f"{a[j], a[j+1]}", end=" ")

                # print(f"\t exchanged values: {exchanged_values}")

                # if (not self.exchanged_values): break # Finish sort when there was no value exchange made

        return a
            

    def run(self):
        return self.sort(self.seq)
    