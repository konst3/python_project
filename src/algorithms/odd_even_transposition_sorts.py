# Authors: Konstantinos Papalamprou
# Date: 31/1/2026
# Implementation of Odd Even Transposition Sort

import multiprocessing as mp

class OddEvenTranspositionSort:
    name = "Odd Even Transposition Sort"
    complexity = "-"
    parallel = True

    def __init__(self, seq, ps_n=1):
        self.seq = seq
        self.ps_n = ps_n

        if (ps_n != 1): print(f"DEBUG: Odd-Even Transposition Sort is not parallel, so it will run on 1 thread instead of {ps_n}")

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