# Authors: Konstantinos Papalamprou, 
# Date: 13/1/2026
# Implementation of Sequencial Bubble Sort Algorithm

# NOTE: JUST FOR A TEST BASED ON GIVEN PDF --> NOT PRODUCTION READY 

class Bubble_sort:
    def __init__(self, a):
        self.a = a
        self.N = len(a)

        self.name = "Bubble Sort"
        self.complexity = "O(n^2)"

    def __str__(self):
        return f"Algorithm {self.name}, Complexity: {self.complexity}"

    def sort(self):
        for i in range(self.N-1, 0, -1):
            for j in range(0, i, 1):
                k = j + 1

                if (self.a[j] > self.a[k]):
                    tmp = self.a[j]
                    self.a[j] = self.a[k]
                    self.a[k] = tmp

        return self.a
