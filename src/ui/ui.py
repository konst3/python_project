# Authors: Konstantinos Papalamprou, 
# Date: 19/1/2026

from tkinter import ttk
import tkinter as tk

class UI:
    def __init__(self, root):
        self.root = root
        root.title("1st Semester Python Project - Sort Algorithms")
        # root.geometry("600x300")
        # root.resizable(False, False)

        # Algorithms
        # 0: Bubble Sort
        # 1: Parallel Bubble Sort

        self.algorithm_choice = 0
        self.algorithms = ["Bubble Sort/Parallel Bubble Sort", "Odd-Even Transposition Sort", "Mergesort/Parallel Mergesort",
                           "Quicksort and Partitioning schemes", "Merging Algorithms: Odd-Even Merge/Parallel Odd-Even merge",
                           "Bitonic Mergesort"]

        # Generate the sequence
        self.f1 = tk.Frame(root)
        self.f1.pack()
        self.l2 = tk.Label(self.f1, text="Generate the sequence")
        self.l2.pack()
        self.cb2 = ttk.Combobox(self.f1, values=self.algorithms, state="readonly", width=50) # NOTE: Use state="readonly" to disable typing in the dropbox
        self.cb2.set("Bubble Sort/Parallel Bubble Sort") # Set the default algorithm on the drop down menu
        self.cb2.pack(side="left", padx=5, pady=5)
        self.b2 = tk.Button(self.f1, text="Sort", command=self.run_sort)
        self.b2.pack()

        # Choose a sorting algorithm
        self.f2 = tk.Frame(root)
        self.f2.pack(side="left")
        self.l1 = tk.Label(self.f2, text="Select a sorting algorithm:")
        self.l1.pack()
        self.cb1 = ttk.Combobox(self.f2, values=self.algorithms, state="readonly", width=50) # NOTE: Use state="readonly" to disable typing in the dropbox
        self.cb1.set("Bubble Sort/Parallel Bubble Sort") # Set the default algorithm on the drop down menu
        self.cb1.pack(side="left", padx=5, pady=5)
        self.b1 = tk.Button(self.f2, text="Sort", command=self.run_sort)
        self.b1.pack()

    def run_sort(self):
        self.algorithm_choice = self.cb1.get()
        print(self.algorithm_choice)

        match self.algorithm_choice:
            case "Bubble Sort/Parallel Bubble Sort": pass
            case "Odd-Even Transposition Sort": pass
            case "Mergesort/Parallel Mergesort": pass
            case "Quicksort and Partitioning schemes": pass
            case "Merging Algorithms: Odd-Even Merge/Parallel Odd-Even merge": pass
            case "Bitonic Mergesort": pass