# Authors: Konstantinos Papalamprou
# Date: 31/1/2026
# Basic utilities that algorithms need

# Function to validate the accuracy of the sort
def validate_sort(seq):
    val_seq = list(range(1, len(seq) + 1))
    
    if (seq == val_seq): return True
    else: return False

def compare_and_exchange(value_1, value_2, exchanged_values=False):
    if (value_1 > value_2): return value_2, value_1, True
    return value_1, value_2, exchanged_values