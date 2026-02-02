# Authors: Konstantinos Papalamprou, Koutsoumanis Panagiotis
# Date: 13/1/2026
# General utilities

import random
import utils.timer as timer
from algorithms import bubble_sorts, mergesort, bitonic_mergesort, odd_even_merge_sort, odd_even_transposition_sort, quicksort

t = timer.Timer()

algoList = {
    "Bubble Sort": bubble_sorts.BubbleSort,
    "Parallel Bubble Sort": bubble_sorts.ParallelBubbleSort,
    "Odd-Even Transposition Sort": odd_even_transposition_sort.OddEvenTranspositionSort,
    "Mergesort": mergesort.MergeSort,
    "Quicksort": quicksort.QuickSort,
    "Odd-Even Merge Sort": odd_even_merge_sort.OddEvenMergeSort,
    "Bitonic Mergesort": bitonic_mergesort.BitonicMergeSort
}

seq = [1, 2] # Global list for the sequence
seq_limit = 1000000 # Maximum size of list
thread_limit = 100 # Maximum number of threads

# Generate a random sequence that has numbers that appear only once in it
def generate_sequence(N, min_value=1, max_value=seq_limit):
    return random.sample(range(min_value, max_value+1), N)

# Run the sort using the input of the combobox
def run_sort(seq, algo, thr=1):
    # TODO: Show algorithm complexity (self.complexity variable already on class)

    t.start()
    # print(f"DEBUG: start time: {t.t_start}")
    
    al = algoList[algo](seq,thr).run()
    t.stop()
    
    # print(f"DEBUG: stop time: {t.t_stop}")

    return (al, (t.get_time()/(10**6)))

# DEBUG
if (__name__  == "__main__"):
    print("DEBUG: Utils module test")
    print("DEBUG: Available algorithms:")
    for algo in algoList.items():
        print(f" - {algo[0]}: {algo[1]}")
    seq = generate_sequence(500, max_value=1000)
    print(f"DEBUG: Generated sequence: {seq}")
    result = run_sort(seq, "Quicksort")
    #result = run_sort(seq, "Bubble Sort")
    print(f"DEBUG: Time taken: {t.get_time()/(10**6)} ms") # TODO: Add /(10**6) to get_time() func
    #print(f"DEBUG: {result}")
    #print(f"DEBUG: Parallel Time taken: {t.get_time()/(10**6)} ms")
    print(f"DEBUG: {result}")
