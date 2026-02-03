# Authors: Konstantinos Papalamprou, 
# Date: 19/1/2026

import utils.utils as utils
import utils.sort as sort_utils

from tkinter import ttk, scrolledtext
import tkinter as tk

class UI:
    def __init__(self, root):
        self.root = root

        root.title(f"1st Semester Python Project - Sort Algorithms (v{utils.VERSION})")
        # root.geometry("600x300")
        root.resizable(False, False)

        self.algorithms = list(utils.algoList.keys()) # Grab the algorithm names from the algoList keys
        # Generate the sequence
        # TODO: Add a sequence from a file (csv ?)
        self.f1 = tk.Frame(self.root)
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
        self.f3 = tk.Frame(self.root)
        self.f3.pack(side="top")
        self.l3 = tk.Label(self.f3, text="\nSelect a Sorting Algorithm & Number of Threads")
        self.l3.pack()
        self.f4 = tk.Frame(self.f3)
        self.f4.pack()
        self.cb1 = ttk.Combobox(self.f4, values=self.algorithms, state="readonly", width=50) # NOTE: Use state="readonly" to disable typing in the dropbox
        self.cb1.set(self.algorithms[0]) # Set the default algorithm on the drop down menu
        self.cb1.bind("<<ComboboxSelected>>", self.toggle_box) # NOTE: <<ComboboxSelected>> to check every time an algorithm is selected if it could have thread selection
        self.cb1.pack(side="left", padx=5, pady=5)
        vcmd2 = (self.f4.register(self.validate_spinbox), "%P", utils.thread_limit) # Register a new command to tkinter (NOTE: %P is the user key input)
        self.s2 = tk.Spinbox(self.f4, from_=1, to=utils.thread_limit, width=7, repeatdelay=500, validate="key", validatecommand=vcmd2) # NOTE: command=self.toggleBox, will run only on event to the spinbox. We want to run it on event to the Combobox
        self.s2.delete(0, tk.END) # Clear the default of the Spinbox
        self.s2.insert(0, "1") # Set the new default value of the Spin box to 1
        self.s2.config(state="disabled") # Run on the first time so that the thread option is disabled for the default algorithm (BubbleSort is single threaded)
        self.s2.pack(side="left")
        self.b2 = tk.Button(self.f3, text="Sort", command=self.ui_run_sort, state="disabled") # Button gets enabled after first sequence generation
        self.b2.pack(side="bottom", padx=5, pady=5)

        # Programmers names
        # NOTE: With side="bottom" you pack widgets from the bottom --> up so the names will appear on the bottom
        self.l4 = tk.Label(self.root, text="Made by Koutsoumanis Panagiotis and Papalamprou Konstantinos, 2026") # ,\nsee LICENSE file for licensing information
        self.l4.pack(side="bottom", padx=10, pady=10)

        # Results
        self.tb = scrolledtext.ScrolledText(self.root, wrap = tk.WORD, height=20, state="normal", font=("Courier", 10)) # NOTE: use monospace for support on any os (alternatively use JetBrains Mono)
        self.tb.pack(side="bottom", padx=10, pady=10)
        #self.tb.insert(tk.INSERT,"hello")
        self.tb.configure(state="disabled")

        # Load instructions to the UI
        self.printUI(f"{" Manual ":=^80}")
        self.printUI("1. On the \"Generate Sequence\" Section you must first select the size of the sequence you want & click generate for your sequence to be generated")
        self.printUI("  NOTE: The sequence will be a list of numbers from 1 to the number you selected in a random order")
        self.printUI("  WARNING: You must generate a sequence before sorting otherwise the sort button will be disabled")
        self.printUI("2. Then on the \"Select a Sorting Algorithm & Number of Threads\" you can choose from a variety of single and parallel processing sorting algorithms to sort your list and if the algorithm is parallel you could select a different number of processes from the box next")
        self.printUI("  WARNING: The thread option will be deactivated for single threaded algorithms")
        self.printUI("3. When you press the \"Sort\" button the sorting results will appear under here")
        self.printUI(f"{"":=^80}")

        self.printUI(" ")
        self.printUI(f"{" Results ":=^80}")


    # Helper function for printing to the UI "console"
    def printUI(self, text):
       self.tb.config(state="normal") # Make the console edible for an automated insert of data
       self.tb.insert(tk.INSERT, text+"\n")
       self.tb.config(state="disabled") # Make the console unedible for the user
       self.tb.see(tk.END) # Always scroll to the bottom line

    # A method that on an event checks if the spinbox input is correct
    def toggle_box(self, event):
        if not utils.algoList[self.cb1.get()].parallel:
            # self.s2.delete(0, tk.END)
            # self.s2.insert(0,"1")
            self.s2.config(state="disabled")
            # print("DEBUG: Disabled Spinbox for non-parallel algorithm")

        else:
            self.s2.config(state="normal")
    
    # Runs every time there is an event on the SpinBox to validate that its input is correct
    def validate_spinbox(self, value, limit):
        try:
            if (value == ""): return True
            value = int(value)
            return (1 <= value <= int(limit))
        except:
            return False

    # Button handler for the sequence generation
    def ui_generate_sequence(self):
        try:
            s1_in = int(self.s1.get())
        except:
            self.printUI(f"Wrong UI Sequence Generator input")
            return

        utils.seq = utils.generate_sequence(N=s1_in, min_value=1, max_value=s1_in)
        print(f"DEBUG: Generated Sequence: {utils.seq}, size: {len(utils.seq)}")

        # Show a part of the sequence if it is too big to render
        if len(utils.seq) <= utils.seq_display_limit:
            self.printUI(f"\nGenerated new Sequence: {utils.seq}, size: {len(utils.seq)}\n")
        else:
            self.printUI(f"\nGenerated new large Sequence: {utils.seq[0:20]}...{utils.seq[len(utils.seq)-20:len(utils.seq)+1]}, size {len(utils.seq)}\n")

        self.b2.config(state="normal")

    # Button handler to run the choosen algorithm
    def ui_run_sort(self):
        # try:
        algorithm_choice = self.cb1.get()
        thread_choice = int(self.s2.get())
        threads_used = (thread_choice if utils.algoList[algorithm_choice].parallel else 1) # Actual number of used threads
        # except:
        #     print(f"Wrong UI Sort Algorithm input")
        #     return

        print(f"DEBUG: Starting with: {utils.seq}")
        print(f"DEBUG: User chose {algorithm_choice} with {thread_choice} threads")
        #if (len(sorted_seq)<= utils.seq_display_limit): # truncate seq for giant sizes
        #    self.printUI(f"Result: {sorted_seq}")

        sorted_seq, time_taken = utils.run_sort(utils.seq.copy(), algorithm_choice, thread_choice) # NOTE: Use a copy of the list so that the main list does not get overwritten
        outln = f"{algorithm_choice:<30}| Threads: {threads_used:>5} | Time Taken: {time_taken:>15.3f}ms" # NOTE: ":" right aligned, "<" left aligned, "^" center aligned
        self.printUI(outln)
        #debug prints
        print(f"DEBUG: Time taken: {time_taken} ms")
        print(f"DEBUG: {"Sort was correct" if sort_utils.validate_sort(sorted_seq.copy()) else "Sort was wrong"}")
        print(f"DEBUG: Result: {sorted_seq}")
        # TODO: Save to a file