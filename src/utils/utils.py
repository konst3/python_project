# Authors: Konstantinos Papalamprou, 
# Date: 13/1/2026
# Basic utilities that algorithms need

import random
import utils.timer as timer
from algorithms import bubble_sorts, mergesort, bitonic_mergesort, odd_even_merge_sort, odd_even_transposition_sort, quicksort

t = timer.Timer()

algoList = {
    "Bubble Sort": bubble_sorts.Bubble_sort,
    "Parallel Bubble Sort": bubble_sorts.Parallel_Bubble_sort,
    "Mergesort": mergesort.MergeSort,
    "Bitonic Mergesort": bitonic_mergesort.BitonicMergeSort,
    "Odd-Even Merge Sort": odd_even_merge_sort.OddEvenMergeSort,
    "Odd-Even Transposition Sort": odd_even_transposition_sort.OddEvenTranspositionSort,
    "Quicksort": quicksort.QuickSort
}
# Global list for the sequence
seq = []
seq_limit = 10000 # Maximum size of list

def generate_sequence(N, min_value=1, max_value=seq_limit):
    return random.sample(range(min_value, max_value+1), N)

def run_sort(list, algo, thr=1):
    t.start()
    #TODO: add code that calls sorting algo
    al = algoList[algo](list,thr).run()
    t.stop()
    return al

if (__name__  == "__main__"):
    print("DEBUG: Utils module test")
    print("DEBUG: Available algorithms:")
    for algo in algoList.items():
        print(f" - {algo[0]}: {algo[1]}")
    seq = generate_sequence(10, 1, 100)
    print(f"DEBUG: Generated sequence: {seq}")
    result = run_sort(seq, "Bubble Sort")
    print(f"DEBUG: Result: {result}")
    print(f"DEBUG: Time taken: {t.get_time()} ns")
