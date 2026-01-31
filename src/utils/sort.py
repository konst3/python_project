# Authors: Konstantinos Papalamprou
# Date: 31/1/2026
# Basic utilities that algorithms need

# Function to validate the accuracy of the sort
def validate_sort(seq):
    val_seq = list(range(1, len(seq) + 1))
    
    if (seq == val_seq): return True
    else: return False

# Merge 2 sorted lists into one sorted list
def merge_lists(l1, l2):
    merged = []
    i = 0
    j = 0

    while ((i < len(l1)) and (j < len(l2))):
        if (l1[i] < l2[j]):
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1

    if (i < len(l1)): merged += l1[i:]
    elif (j < len(l2)): merged += l2[j:]

    return merged

# NOTE: Too slow
# Compare and exchange 2 values
# def compare_and_exchange(value_1, value_2, exchanged_values=False):
#     if (value_1 > value_2): return value_2, value_1, True
#     return value_1, value_2, exchanged_values