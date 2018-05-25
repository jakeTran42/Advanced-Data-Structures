#!python

class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
	        self.memo[args] = self.fn(*args)
        return self.memo[args]

def fibonacci(n):
    """fibonacci(n) returns the n-th number in the Fibonacci sequence,
    which is defined with the recurrence relation:
    fibonacci(0) = 0
    fibonacci(1) = 1
    fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2), for n > 1"""
    # Check if n is negative or not an integer (invalid input)
    if not isinstance(n, int) or n < 0:
        raise ValueError('fibonacci is undefined for n = {!r}'.format(n))
    # Implement fibonacci_recursive, _memoized, and _dynamic below, then
    # change this to call your implementation to verify it passes all tests
    return fibonacci_recursive(n)
    # return fibonacci_memoized(n, memo={})
    # return fibonacci_dynamic(n)

@Memoize
def fibonacci_recursive(n):
    # Check if n is one of the base cases
    if n == 0 or n == 1:
        return n
    # Check if n is larger than the base cases
    elif n > 1:
        # Call function recursively and add the results together
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memoized(n, memo):
    # TODO: Memoize the fibonacci function's recursive implementation here
    # Once implemented, change fibonacci (above) to call fibonacci_memoized
    # to verify that your memoized implementation passes all test cases
    
    # Check if value is in cache, return it
    
    # if its not in cache then computers, assign it into cache and returns
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
        return memo[n]


def fibonacci_dynamic(n, table=[]):
    # TODO: Implement the fibonacci function with dynamic programming here
    # Once implemented, change fibonacci (above) to call fibonacci_dynamic
    # to verify that your dynamic implementation passes all test cases
    while len(table) < n+1: table.append(0)

    if n <= 1:
       return n
    else:
       if table[n-1] ==  0:
           table[n-1] = fibonacci_dynamic(n-1)

       if table[n-2] ==  0:
           table[n-2] = fibonacci_dynamic(n-2)

       table[n] = table[n-2] + table[n-1]

    return table[n]

    


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = fibonacci(num)
        print('fibonacci({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
