# Authors: Konstantinos Papalamprou, 
# Date: 13/1/2026
# Basic utilities that algorithms need

import random

# Global list for the sequence
seq = []

def generate_sequence(N, max_value, min_value=1):
    return random.sample(range(min_value, max_value+1), N)

