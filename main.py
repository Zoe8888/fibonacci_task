# Fibonacci sequence
# Establish the sequence formula
def recursion_fibonacci(n):
    if n == 1 or n == 0:
        return n
    else:
        return (recursion_fibonacci(n-1)) + recursion_fibonacci(n-2)


# Defining the first 20 numbers in the Fibonacci Sequence
n_terms = 20
print("Fibonacci Sequence: ")
# For each nth term in the sequence
for i in range(n_terms):
    print(recursion_fibonacci(i), end="   ")
# "end" keeps the sequence order next to each other
