# Authors: Konstantinos Papalamprou, 
# Date: 13/1/2026
# Basic utilities that algorithms need

import random

def generate_sequence(N, min_value, max_value):
    return random.sample(range(min_value, max_value+1), N)

