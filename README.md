# 1st semester python project at ECE upatras 
## Implementation of various single and parallel sorting algoritms in Python

## TO DO
1. Sort algoritmhs implementation:
- Bubble sort/Parallel bubble sort
- odd-even transposition sort
- Mergesort/Parallel mergesort
- quicksort and partitioning schemes                     
- Merging algorithms: odd-even merge/parallel odd-even merge
- bitonic mergesort

2. UI implementation (using matplotlib, pygame, tkinter ?):
- Choose the algorithm you want to use
- Show stats like (1) time, (2) number of processes (would be better if it had core utilization too ?), (3) batch size (WARNING: batch size will be large)

## How to run
1. Install dependencies (Run this only the first time):
\
`
pip install -r requirements.txt
`

2. Run main code via:
\
`
python3 src/main.py
`

(**NOTE:** Run the bash commands on the project directory)

## Links
https://www.dcc.fc.up.pt/~ricroc/aulas/1516/cp/apontamentos/slides_sorting.pdf

Algorithms
https://docs.python.org/2/library/time.html#time.process_time_ns

UI
ttk.Combobox https://www.geeksforgeeks.org/python/dropdown-menus-tkinter/
tk.Spinbox