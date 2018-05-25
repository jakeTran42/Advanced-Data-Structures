# def fib(seq):
#     if seq == 0:
#         yield 0
#     elif seq == 1:
#         yield 1
    
#     yield from fib(seq - 1) + fib(seq-2)


# for i in range(30):
#     print(fib(i))


# for seq in fib(50):
#     print(seq)

def fib(seq):
    a, b = 0, 1
    for _ in range(seq):
        a, b = b, a + b
    return a

# for seq in fib(122):
#     print(seq)
    
print(fib(121))