
import random

def do_something(count):
    """Generate a list of random numbers and return their sum."""
    total = 0
    for _ in range(count):
        total += random.random()
    return total
