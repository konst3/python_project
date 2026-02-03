# Authors: Konstantinos Papalamprou, Koutsoumanis Panagiotis
# Date: 13/1/2026
# General utilities

import random
import utils.timer as timer
import utils.sort as sort
from algorithms import bubble_sorts, merge_sorts, quicksorts, odd_even_merge_sort, bitonic_merge_sort

VERSION = "0.8"
t = timer.Timer()

algoList = {
    "Bubble Sort": bubble_sorts.BubbleSort,
    "Parallel Bubble Sort/Odd-Even Transposition Sort": bubble_sorts.OddEvenTranspositionSort,
    "Merge Sort": merge_sorts.MergeSort,
    "Parallel Merge Sort": merge_sorts.ParallelMergeSort,
    "Quicksort": quicksorts.QuickSort,
    "Parallel Quicksort": quicksorts.ParallelQuickSort,
    "Odd-Even Merge Sort (Parallel)": odd_even_merge_sort.OddEvenMergeSort,
    "Bitonic Mergesort (Parallel)": bitonic_merge_sort.BitonicMergeSort
}

seq = [1, 2] # Global list for the sequence
seq_limit = 1000000 # Maximum size of list
thread_limit = 100 # Maximum number of threads
seq_display_limit = 100 # limit after which a sequence won't be printed in its entirety on the console
tb_width = 140 # Width of the text box in the UI

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
    seq = generate_sequence(100, max_value=100)

    print(f"DEBUG: Generated sequence: {seq}")
    print(sort.validate_sort(seq))

    # result = run_sort(seq, "Quicksort")
    # result = run_sort(seq, "Bubble Sort")
    result = run_sort(seq, "Parallel Bubble Sort/Odd-Even Transposition Sort", 5)
    
    print(f"DEBUG: Time taken: {t.get_time()/(10**6)} ms") 
    
    print(f"DEBUG: {result}")
    print(sort.validate_sort(result[0]))
