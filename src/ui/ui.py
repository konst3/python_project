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
        self.algorithm = None
        self.algorithms = ["Bubble Sort", "Parallel Bubble Sort"]

        self.f1 = tk.Frame(root)
        self.f1.pack(side="left")
        self.l1 = tk.Label(self.f1, text="Choose your sorting algorithm:")
        self.l1.pack()
        self.cb1 = ttk.Combobox(self.f1, values=self.algorithms)
        self.cb1.pack(side="left", padx=5, pady=5)
        self.b1 = tk.Button(self.f1, text="Sort", command=self.run_sort)
        self.b1.pack()

    def run_sort(self):
        match self.algorithm_choice:
            case 0: pass
            case 1: pass
            case 2: pass
            case 3: pass
            case 4: pass
            case 5: pass