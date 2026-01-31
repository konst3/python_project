# 1st semester python project at ECE upatras 
## Implementation of various single and parallel sorting algoritms in Python

## How to run
Install dependencies (Run this only the first time):
\
`
pip install -r requirements.txt
`

Run main code via:
\
`
python3 src/main.py
`

(**NOTE:** Run the bash commands on the project directory)



## TO DO
1. Sort algoritmhs implementation:
- <s>Bubble sort/Parallel bubble sort</s> <-- Check Parallel bubble Sort
- <s>odd-even transposition sort</s> <-- Parallel needs improvements
- <s>Mergesort</s>/Parallel mergesort
- quicksort and partitioning schemes                     
- Merging algorithms: odd-even merge/parallel odd-even merge
- bitonic mergesort

2. UI implementation (using matplotlib, pygame, tkinter ?):
- <s>Choose the algorithm you want to use</s>
- Show stats like (1) time, (2) number of processes (would be better if it had core utilization too ?), (3) batch size (WARNING: batch size will be large)

## Links
https://www.dcc.fc.up.pt/~ricroc/aulas/1516/cp/apontamentos/slides_sorting.pdf

Algorithms
https://docs.python.org/3/library/multiprocessing.html
https://docs.python.org/2/library/time.html#time.process_time_ns
https://www.geeksforgeeks.org/dsa/odd-even-transposition-sort-brick-sort-using-pthreads/
https://www.geeksforgeeks.org/python/python-program-for-merge-sort/

UI
ttk.Combobox https://www.geeksforgeeks.org/python/dropdown-menus-tkinter/
tk.Spinbox