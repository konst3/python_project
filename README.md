# 1st Semester Python Project ECE upatras - Single and Parallel Sorting Algorithms with GUI

![app](assets/app.png)

A comprehensive Python application demonstrating single-threaded and parallel sorting algorithms with a graphical user interface. This project was developed as a 1st semester assignment for the ECE Department at University of Patras. More specifically, this project implements various sorting algorithms and provides a visual interface to compare their performance characteristics. It includes both sequential and parallel implementations, allowing users to understand the differences between single-threaded and multi-threaded sorting approaches.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Algorithm Complexity](#algorithm-complexity)
- [To-Do List](#to-do-list)
- [Contributors](#contributors)
- [License](#license)
- [Resources](#resources)

## Features

- **Multiple Sorting Algorithms**
  - Bubble Sort
  - Merge Sort (Sequential & Parallel)
  - Quick Sort (Multiple schemes & Parallel)
  - Odd-Even Merge Sort (Parallel) --> Not done
  - Bitonic Merge Sort (Parallel) --> Not done

- **Interactive GUI** (built with tkinter)
  - Generate random sequences of configurable sizes
  - Select sorting algorithms with complexity information
  - Configure number of parallel processes
  - Real-time performance metrics and timing

- **Performance Analysis**
  - Algorithm complexity display
  - Execution timing measurements
  - Support for multi-threaded execution

## Requirements

- Python 3.7+
- tkinter (usually included with Python)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd python_project
```

2. No additional dependencies required (uses Python standard library only)

## Usage

Run the application from the project directory:

```bash
python3 src/main.py
```

### Application Guide (also available in the UI)

1. **Generate Sequence**
   - Enter a sequence size (recommended: 1 to 1.000.000)
   - Click "Generate" to create a random sequence
   - The sequence will contain numbers from 1 to your selected size in random order

**Note:** You must generate a sequence before sorting. The sort button will be disabled until a sequence is available.

2. **Select Algorithm & Threads**
   - Choose a sorting algorithm from the dropdown menu
   - Algorithm complexity is displayed for reference
   - For parallel algorithms, select the number of processes (disabled for single-threaded algorithms)

3. **View Results**
   - Click "Sort" to execute the algorithm
   - Results display:
     - Sorted sequence
     - Execution time in milliseconds
     - Number of processes used


## Project Structure

```
src/
├── main.py                      # Application entry point
├── algorithms/                  # Sorting algorithm implementations
│   ├── bubble_sorts.py         # Bubble sort implementations
│   ├── merge_sorts.py          # Merge sort implementations
│   ├── quicksorts.py           # Quick sort implementations
│   ├── odd_even_merge_sort.py  # Odd-even merge sort
│   └── bitonic_merge_sort.py   # Bitonic merge sort
├── ui/                         # User interface
│   └── ui.py                   # tkinter GUI implementation
└── utils/                      # Utility modules
    ├── sort.py                 # Sorting utilities and helpers
    ├── timer.py                # Performance timing
    └── utils.py                # General utilities
```

## Algorithm Complexity

| Algorithm | Time Complexity | Parallel |
|-----------|-----------------|------------------|
| Bubble Sort | O(n²) | O(n) |
| Merge Sort | O(n log n) | O(n) |
| Quick Sort | O(n log n) avg | O(n) |
| Odd-Even Merge | - | O(log^2 n) |
| Bitonic Merge | - | O(log^2 n) |

## Contributors

- **Konstantinos Papalamprou** (@konst3)
- **Panagiotis Koutsoumanis** (@devnol)

## To-Do List

### 1. Sort Algorithms Implementation
- <s>Bubble sort</s> _@konst3_
- <s>Parallel bubble sort/Odd-Even Transposition Sort</s> <-- Too big overhead _@konst3_
- <s>Mergesort</s> _@konst3_
- <s>Parallel mergesort</s> _@konst3_
- <s>Quicksort</s> _@devnol_
- <s>Lomuto Quicksort Scheme</s> _@konst3_, _co_
- <s>Quicksort Hoare Partition Scheme</s> _@konst3_, _co_
- <s>Parallel Quicksort</s> _@konst3_, _co_
- Merging algorithms: Odd-Even Mergesort (Parallel) _?_
- Bitonic mergesort (Parallel) _?_

### 2. UI Implementation (using tkinter)
- <s>Generate a sequence (WARNING: sequence size will be large)</s> _@konst3_
- <s>Choose the algorithm you want to use</s> _@konst3_, _@devnol_
- <s>Show number of processes</s> (would be better if it had core utilization too ?) _@konst3_, _@devnol_
- <s>Show time taken (ms ?)</s> _@devnol_

### 3. Utils
- <s>UI backend to handle the running of the chosen algorithm</s> _@devnol_
- <s>Unit testing</s> _@devnol_

### 4. Features
- Load a sequence from a file (csv ?)
- <s>Add complexity of an algorithm to UI drop menu</s> _@konst3_

### 5. Presentation
- Make markdown (update images) _@konst3_
- Make paper
- Make pptx
- Make personal description of contributions to the project

## License
This project is released into the public domain under The Unlicense. See the [LICENSE](LICENSE) file for more details.

## Resources

### General Sorting
https://www.dcc.fc.up.pt/~ricroc/aulas/1516/cp/apontamentos/slides_sorting.pdf

### Algorithms & Documentation
- https://docs.python.org/3/library/multiprocessing.html
- https://docs.python.org/2/library/time.html#time.process_time_ns
- https://www.geeksforgeeks.org/dsa/odd-even-transposition-sort-brick-sort-using-pthreads/
- https://www.geeksforgeeks.org/python/python-program-for-merge-sort/
- Γιώργος Μανής - Εισαγωγή στον προγραμματισμό με αρωγό τη γλώσσα python - Kallipos

### UI & GUI
- ttk.Combobox: https://www.geeksforgeeks.org/python/dropdown-menus-tkinter/
- tk.Spinbox.bind() --> bind a function on an event of the widget
- https://stackoverflow.com/questions/74040200/disable-mouse-press-on-tkinter-text-widget --> Scroll text click bug fix