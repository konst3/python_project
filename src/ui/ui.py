# Authors: Konstantinos Papalamprou, 
# Date: 19/1/2026

import utils.utils as utils
import utils.sort as sort_utils

from tkinter import ttk, scrolledtext
import tkinter as tk

class UI:
    def __init__(self, root):
        self.root = root

        root.title("1st Semester Python Project - Sort Algorithms")
        # root.geometry("600x300")
        root.resizable(False, False)

        self.algorithms = list(utils.algoList.keys()) # Grab the algorithm names from the algoList keys
        # Generate the sequence
        # TODO: Add a sequence from a file (csv ?)
        self.f1 = tk.Frame(root)
        self.f1.pack()
        self.l1 = tk.Label(self.f1, text=f"Generate the Sequence\nEnter the size of the sequence which should belong to [0, {utils.seq_limit}]")
        self.l1.pack()
        self.f2 = tk.Frame(self.f1)
        self.f2.pack()
        vcmd1 = (self.f2.register(self.validate_spinbox), "%P", utils.seq_limit) # Register a new command to tkinter (NOTE: %P is the user key input)
        self.s1 = tk.Spinbox(self.f2, from_=1, to=utils.seq_limit, width=7, repeatdelay=500, validate="key", validatecommand=vcmd1)
        self.s1.delete(0, tk.END) # Clear the default of the Spinbox
        self.s1.insert(0, "100") # Set the new default value of the Spin box to 1
        self.s1.pack(side="left", padx=5, pady=5)
        self.b1 = tk.Button(self.f2, text="Generate", command=self.ui_generate_sequence)
        self.b1.pack()

        # Choose a sorting algorithm
        self.f3 = tk.Frame(root)
        self.f3.pack(side="top")
        self.l3 = tk.Label(self.f3, text="\nSelect a Sorting Algorithm & Number of Threads")
        self.l3.pack()
        self.f4 = tk.Frame(self.f3)
        self.f4.pack()
        self.cb1 = ttk.Combobox(self.f4, values=self.algorithms, state="readonly", width=50) # NOTE: Use state="readonly" to disable typing in the dropbox
        self.cb1.set(self.algorithms[0]) # Set the default algorithm on the drop down menu
        self.cb1.pack(side="left", padx=5, pady=5)
        # TODO: Make thread number unusable for single threaded sorts (ex. Bubble Sort)

        vcmd2 = (self.f4.register(self.validate_spinbox), "%P", utils.thread_limit) # Register a new command to tkinter (NOTE: %P is the user key input)
        self.s2 = tk.Spinbox(self.f4, from_=1, to=utils.thread_limit, width=7, repeatdelay=500, validate="key", validatecommand=vcmd2, command=self.toggleBox)
        self.s2.delete(0, tk.END) # Clear the default of the Spinbox
        self.s2.insert(0, "1") # Set the new default value of the Spin box to 1
        self.s2.pack(side="left")
        self.b2 = tk.Button(self.f3, text="Sort", command=self.ui_run_sort, state="disabled") #button gets enabled after first list gen
        self.b2.pack(side="bottom", padx=5, pady=5)

        # Results
        self.tb = scrolledtext.ScrolledText(root, wrap = tk.WORD, height=15, state="normal", font=("JetBrains Mono", 10))
        self.tb.pack(side="bottom", padx=10, pady=10)
        #self.tb.insert(tk.INSERT,"hello")
        self.tb.configure(state="disabled")

        # TODO: StringVar for time_taken variable in ui_run_sort and tk.Label ?

    #Helper function for printing to the UI "console"
    def printUI(self, text):
       self.tb.config(state="normal")
       self.tb.insert(tk.INSERT, text+"\n")
       self.tb.config(state="disabled") 

    # A method that constantly checks if the spinbox input is correct
    def toggleBox(self):
        try:
            if not utils.algoList[self.cb1.get()].parallel:
                print("ass")
                self.s2.config(state="readonly")
                self.s2.delete(0, tk.END)
                self.s2.insert(0,"1")
                print("DEBUG: algo is not parallel")
                #return False
            else: self.s2.config(state="normal")
        except:
            pass
        
    
    def validate_spinbox(self, value, limit):
        try:
            if (value == ""): return True
            value = int(value)
            return (1 <= value <= int(limit))
        except:
            return False

    def ui_generate_sequence(self):
        try:
            s1_in = int(self.s1.get())
        except:
            self.printUI(f"Wrong UI Sequence Generator input")
            return

        utils.seq = utils.generate_sequence(N=s1_in, min_value=1, max_value=s1_in)
        print(f"DEBUG: Generated Sequence: {utils.seq}, size: {len(utils.seq)}")

        if len(utils.seq) <= utils.seq_display_limit:
            self.printUI(f"Generated Sequence: {utils.seq}, size: {len(utils.seq)}")
        else: self.printUI(f"""======
Generated new array of size {len(utils.seq)}
======""")
        self.b2.config(state="active")

    def ui_run_sort(self):
        try:
            algorithm_choice = self.cb1.get()
            thread_choice = int(self.s2.get())
            threads_used = (thread_choice if utils.algoList[algorithm_choice].parallel else 1) #actual number of used threads
        except:
            print(f"Wrong UI Sort Algorithm input")
            return

        sorted_seq, time_taken = utils.run_sort(utils.seq.copy(), algorithm_choice, thread_choice) # NOTE: Use a copy of the list so that the main list does not get overwritten
        outln = f"{algorithm_choice:<30} | Threads: {threads_used:>3} | Time Taken: {time_taken:>.3f}ms"
        self.printUI(outln)
        #debug prints
        #self.printUI(f"Starting with: {utils.seq}")
        #self.printUI(f"User chose {algorithm_choice} with {thread_choice} threads")
        #if (len(sorted_seq)<= utils.seq_display_limit): # truncate seq for giant sizes
        #    self.printUI(f"Result: {sorted_seq}")
        #self.printUI(f"Time taken: {time_taken} ms")
        #self.printUI(f"{"Sort was correct 👍" if sort_utils.validate_sort(sorted_seq.copy()) else "Whoops, the sorted list isn't sorted 🤦"}")
        print(f"DEBUG: Result: {sorted_seq}")
        # TODO: Save to a file