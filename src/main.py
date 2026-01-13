# Authors: Konstantinos Papalamprou, 
# Date: 13/1/2026

# Libraries
import matplotlib.pyplot as plt
import numpy as np

from algorithms.utils import generate_sequence
import algorithms.bubble_sort as bubble_sort

# NOTE: Make settings change from the UI
N = 8 # size of the sequence
min_value = 1 # minimum value on the list
max_value = 10 # maximum value on the list

# Bubble Sort test
a = generate_sequence(N, min_value, max_value)
print(a)

s = bubble_sort.Bubble_sort(a)
print(s)
print(s.sort())

# UI test
# x = 0.5 + np.arange(N)
# y = a

## plt.style.use('_mpl-gallery')

# fig, ax = plt.subplots()
# fig.patch.set_facecolor("black")
# ax.bar(x, y, width=1, color="white", edgecolor="white", linewidth=0.7)
# ax.set(xlim=(0, N), xticks=np.arange(1, N+1),
#        ylim=(0, max_value+1), yticks=np.arange(0, max_value+1))
# ax.set_facecolor('black')          # Axes background
# ax.set_title(s, color="white", fontsize=14)

# ax.grid(True, color='gray', linestyle='-', linewidth=0.5, alpha=0.5)

# # Change axis colors to make them visible
# ax.spines['bottom'].set_color('white')
# ax.spines['top'].set_color('white')
# ax.spines['left'].set_color('white')
# ax.spines['right'].set_color('white')
# ax.tick_params(colors='white')      # Tick marks
# ax.xaxis.label.set_color('white')   # X-axis label
# ax.yaxis.label.set_color('white')   # Y-axis label

# plt.show()