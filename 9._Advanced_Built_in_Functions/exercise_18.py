# Define a PrimeGenerator class
class PrimeGenerator:
    def __init__(self, stop):
        self.stop = stop
        self.start = 2

    def __next__(self):
        # always search from current start (inclusive) to stop (exclusive)
        for n in range(self.start, self.stop):
            for x in range(2, n):
                if n % x == 0:      # not prime
                    break
            else:   # n is prime, because we've gone through the entire loop without having a non-prime situation
                # next time we need to start from n + 1, otherwise we will be trapped on n
                self.start = n + 1
                return n    # return n for this round
        raise StopIteration()  # this is what tells Python we've reached the end of the generator


g = PrimeGenerator(10)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
