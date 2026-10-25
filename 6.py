import random

def generate_random(n=1):
    if n == 1:
        return random.random()
    return [random.random() for _ in range(n)] if n > 1 else []

def f(x):
    return x**2 + 2*x

print("Single uniform random number:", round(generate_random(), 4))

N = 10
samples = generate_random(N)
total = 0

print("\nEvaluation of f(x) = x^2 + 2x")
print("Sample (x)\tFunction Value")

for x in samples:
    fx = f(x)
    print(round(x, 4), "\t\t", round(fx, 4))
    total += fx

print("\nMonte Carlo Integration")
print("Sum of function values:", round(total, 4))
print("Number of samples:", N)
print("Estimated integral:", round(total / N, 4))

print("Exact integral value:", round(4/3, 4))

a, b = 10, 20
print("\nRandom number between", a, "and", b, ":",
      round(a + (b-a) * generate_random(), 4))