# Authors: Konstantinos Papalamprou, 
# Date: 27/1/2026
# A timer class to measure the performance of the algorithms

from time import time

class Timer:
    def start(self):
        self.t_start = time()

    def stop(self):
        self.t_stop = time()

    # def reset(self):
    #     self.t_start = 0
    #     self.t_stop = 0

    def dt(self):
        return self.t_stop - self.t_start