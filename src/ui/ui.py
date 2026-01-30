# Authors: Konstantinos Papalamprou, 
# Date: 19/1/2026

# TODO: Add results to the UI

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

        self.algorithms = list(utils.algoList.keys()) # Grab the algoList 

        # Generate the sequence
        # TODO: Add a sequence from a file (csv ?)
        self.f1 = tk.Frame(root)
        self.f1.pack()
        self.l1 = tk.Label(self.f1, text=f"Generate the Sequence\nEnter the size of the sequence which should belong to [0, {utils.seq_limit}]")
        self.l1.pack()
        self.f2 = tk.Frame(self.f1)
        self.f2.pack()
        vcmd = (self.f2.register(self.validate_spinbox), "%P", utils.seq_limit) # Register a new command to tkinter (NOTE: %P is the user key input)
        self.s1 = tk.Spinbox(self.f2, from_=0, to=utils.seq_limit, width=7, repeatdelay=500, validate="key", validatecommand=vcmd)
        self.s1.delete(0, tk.END)
        self.s1.insert(0, "100")   # Set the default value to 10
        self.s1.pack(side="left", padx=5, pady=5)
        self.b1 = tk.Button(self.f2, text="Generate", command=self.ui_generate_sequence)
        self.b1.pack()

        # Choose a sorting algorithm
        self.f3 = tk.Frame(root)
        self.f3.pack(side="left")
        self.l3 = tk.Label(self.f3, text="\nSelect a Sorting Algorithm & Number of Threads")
        self.l3.pack()
        self.f4 = tk.Frame(self.f3)
        self.f4.pack()
        self.cb1 = ttk.Combobox(self.f4, values=self.algorithms, state="readonly", width=50) # NOTE: Use state="readonly" to disable typing in the dropbox
        self.cb1.set(self.algorithms[0]) # Set the default algorithm on the drop down menu
        self.cb1.pack(side="left", padx=5, pady=5)
        vcmd = (self.f4.register(self.validate_spinbox), "%P", utils.thread_limit) # Register a new command to tkinter (NOTE: %P is the user key input)
        self.s2 = tk.Spinbox(self.f4, from_=0, to=utils.seq_limit, width=7, repeatdelay=500, validate="key", validatecommand=vcmd)
        self.s2.delete(0, tk.END)
        self.s2.insert(0, "1")   # Set the default value to 10
        self.s2.pack(side="left")
        self.b2 = tk.Button(self.f3, text="Sort", command=self.ui_run_sort)
        self.b2.pack(side="bottom", padx=5, pady=5)

    # A method that constantly checks if the spinbox input is correct
    def validate_spinbox(self, value, limit):
        if (value == ""): return True

        try:
            value = int(value)
            return (0 <= value <= int(limit))
        except:
            return False

    def ui_generate_sequence(self):
        try:
            s1_in = int(self.s1.get())
        except:
            print(f"DEBUG: Wrong UI Sequence Generator input")
            return

        utils.seq = utils.generate_sequence(N=s1_in, min_value=1, max_value=s1_in)
        print(f"DEBUG: Generated Sequence: {utils.seq}")

    def ui_run_sort(self):
        algorithm_choice = self.cb1.get()
        thread_choice = int(self.s2.get())

        print(f"DEBUG: Sorting with {algorithm_choice} with threads: {thread_choice}")
        sorted_seq = utils.run_sort(utils.seq, algorithm_choice, thread_choice)
        #print(f"DEBUG: {sorted_seq}")
        # TODO: Save to a file