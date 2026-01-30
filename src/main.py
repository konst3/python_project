# Authors: Konstantinos Papalamprou, 
# Date: 13/1/2026

# Libraries
import tkinter as tk

from utils.utils import generate_sequence
from utils.timer import Timer
import algorithms.bubble_sorts as bubble_sorts
import ui.ui as ui

from time import sleep

if (__name__ == "__main__"):
    # NOTE: Make settings change from the UI
    N = 1000 # size of the sequence
    min_value = 1 # minimum value on the list
    max_value = 100001 # maximum value on the list

    # Generate a random sequence for the sorts
    seq = generate_sequence(N, min_value, max_value)
    print(seq)

    t = Timer()

    # Initialize the UI
    root = tk.Tk()
    my_app = ui.UI(root)
    root.mainloop()

    # 1
    # Bubble sort
    # NOTE: Use a copy of the list so that python does not have the same
    #       memory allocation for a the input and the output
    # t.start()
    # sort = bubble_sorts.Bubble_sort(seq.copy())
    # t.stop()

    # print(sort)
    # print(sort.run())
    # print(f"Time: {t.dt():.6f}")

    # # Parallel Bubble sort
    # t.start()
    # parallel_sort = bubble_sorts.Parallel_Bubble_sort(seq.copy(), 100)
    # t.stop()

    # print(parallel_sort)
    # print(parallel_sort.run())
    # print(f"Time: {t.dt():.6f}")

