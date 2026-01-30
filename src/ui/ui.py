# Authors: Konstantinos Papalamprou, 
# Date: 19/1/2026

import utils.utils as utils

from tkinter import ttk
import tkinter as tk

class UI:
    def __init__(self, root):
        self.root = root

        root.title("1st Semester Python Project - Sort Algorithms")
        # root.geometry("600x300")
        root.resizable(False, False)

        # Algorithms
        # 0: Bubble Sort
        # 1: Parallel Bubble Sort

        self.algorithm_choice = 0
        self.algorithms = ["Bubble Sort/Parallel Bubble Sort", "Odd-Even Transposition Sort", "Mergesort/Parallel Mergesort",
                           "Quicksort and Partitioning schemes", "Merging Algorithms: Odd-Even Merge/Parallel Odd-Even merge",
                           "Bitonic Mergesort"]

        # Generate the sequence
        # TODO: Add a sequence from a file (csv ?)
        self.f1 = tk.Frame(root)
        self.f1.pack()
        self.l1 = tk.Label(self.f1, text="Generate the Sequence")
        self.l1.pack()
        vcmd = (self.f1.register(self.validate_spinbox), "%P") # Command for the verification function
        self.s1 = tk.Spinbox(self.f1, from_=0, to=10000, width=7, repeatdelay=500, validate="key", validatecommand=vcmd) # TODO: to=utils.seq_limit
        self.s1.delete(0, tk.END)
        self.s1.insert(0, "10")   # Set the default value to 10
        self.s1.pack(side="left", padx=5, pady=5)
        self.b1 = tk.Button(self.f1, text="Generate", command=self.ui_generate_sequence)
        self.b1.pack()

        # Choose a sorting algorithm
        self.f2 = tk.Frame(root)
        self.f2.pack(side="left")
        self.l2 = tk.Label(self.f2, text="Select a Sorting Algorithm")
        self.l2.pack()
        self.cb1 = ttk.Combobox(self.f2, values=self.algorithms, state="readonly", width=50) # NOTE: Use state="readonly" to disable typing in the dropbox
        self.cb1.set("Bubble Sort/Parallel Bubble Sort") # Set the default algorithm on the drop down menu
        self.cb1.pack(side="left", padx=5, pady=5)
        self.b2 = tk.Button(self.f2, text="Sort", command=self.run_sort)
        self.b2.pack()

    # A method that constantly checks if the spinbox input is correct
    def validate_spinbox(self, value):
        if (value == ""): return True

        try:
            value = int(value)
            return (0 <= value <= 10000)
        except:
            return False

    def ui_generate_sequence(self):
        s1_in = int(self.s1.get())

        utils.seq = utils.generate_sequence(N=s1_in, min_value=1, max_value=s1_in)
        print(f"DEBUG: Generated Sequence: {utils.seq}")

    def run_sort(self):
        self.algorithm_choice = self.cb1.get()
        print(f"DEBUG: Sorting with {self.algorithm_choice}")

        match self.algorithm_choice:
            case "Bubble Sort/Parallel Bubble Sort": pass
            case "Odd-Even Transposition Sort": pass
            case "Mergesort/Parallel Mergesort": pass
            case "Quicksort and Partitioning schemes": pass
            case "Merging Algorithms: Odd-Even Merge/Parallel Odd-Even merge": pass
            case "Bitonic Mergesort": pass