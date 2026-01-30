# Authors: Konstantinos Papalamprou
# Date: 31/1/2026
# Implementation of Odd Even Transposition Sort

# XXX: Make in multi threaded

class OddEvenTranspositionSort:
    def __init__(self, seq, thr=1):
        self.seq = seq

        self.name = "Odd Even Transposition Sort"
        self.complexity = "?"

    def __str__(self):
        return f"Algorithm {self.name}, Complexity: {self.complexity}"

    def sort(self, a):
        N = len(a)
        is_sorted = False

        while not (is_sorted):
            is_sorted = True

            print(a)

            # Odd Phase
            for i in range(1, N-1, 2):
                if (a[i] > a[i+1]):
                    tmp = a[i]
                    a[i] = a[i+1]
                    a[i+1] = tmp

                    is_sorted = False

            print(a)

            # Even Phase
            for i in range(0, N-1, 2):
                if (a[i] > a[i+1]):
                    tmp = a[i]
                    a[i] = a[i+1]
                    a[i+1] = tmp

                    is_sorted = False

        return a
            

    def run(self):
        return f"Result: {self.sort(self.seq)}"