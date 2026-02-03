# Authors: Konstantinos Papalamprou, Panagiotis Koutsoumanis
# Date: 27/1/2026
#
# A timer class to measure the performance of the algorithms

from time import time_ns as pt

class Timer:
    def start(self):
        self.t_start = pt()

    def stop(self):
        self.t_stop = pt()

    # def reset(self):
    #     self.t_start = 0
    #     self.t_stop = 0

    def get_time(self):
        return self.t_stop - self.t_start