class Prime:

    primes = range(2, 10000)

    def __init__(self):
        self.preparePrimes()

    def preparePrimes(self):
        for i in self.primes:
            n = i
            while n < max(self.primes):
                n += i
                if (n in self.primes):
                    self.primes.remove(n)

    def test(self, arg):
        curr = 1
        count = 0
        while curr < max(self.primes):
            if curr in self.primes:
                count += 1
            if count == arg:
                return curr
            curr += 1
    

p = Prime()
print p.test(100)
print p.test(16)
print p.test(9)
