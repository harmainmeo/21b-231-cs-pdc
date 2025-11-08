# main.py
# Combined project demonstrating:
# Classes, loops, file handling, threading, multiprocessing, and process pools

import time
import threading
import multiprocessing
from do_something import do_something
import os


# -----------------------------
# 1️⃣ CLASSES & INHERITANCE
# -----------------------------
class MyClass:
    common = 10

    def __init__(self):
        self.myvariable = 3

    def myfunction(self, arg1, arg2):
        return self.myvariable + arg1 + arg2


class AnotherClass(MyClass):
    def __init__(self, arg1):
        super().__init__()
        print(f"Message from AnotherClass: {arg1}")


# Demonstration
obj = MyClass()
print("MyClass.myfunction(1,2):", obj.myfunction(1, 2))

obj2 = AnotherClass("Hello from inherited class!")
print("AnotherClass.myfunction(5,5):", obj2.myfunction(5, 5))


# -----------------------------
# 2️⃣ CONTROL STRUCTURES
# -----------------------------
num = 5
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

numbers = [6, 6, 3, 8, -3, 2, 5, 44, 12]
sum_nums = 0
for val in numbers:
    sum_nums += val
print("Sum of numbers:", sum_nums)

n = 5
sum_natural = 0
i = 1
while i <= n:
    sum_natural += i
    i += 1
print("Sum of first 5 natural numbers:", sum_natural)


# -----------------------------
# 3️⃣ FILE HANDLING
# -----------------------------
with open("sample.txt", "w") as f:
    f.write("This is a test file.\n")
    f.write("We are writing and reading from it.\n")

with open("sample.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)


# -----------------------------
# 4️⃣ THREADING EXAMPLE
# -----------------------------
def threaded_task(name, count, results, lock):
    lock.acquire()
    print(f"{name} started by thread {threading.current_thread().name}")
    lock.release()
    result = do_something(count)
    results.append(result)
    print(f"{name} finished.")


def run_threads():
    NUM_THREADS = 4
    COUNT = 1000000
    results = []
    threads = []
    lock = threading.Lock()

    start_time = time.time()

    for i in range(NUM_THREADS):
        t = threading.Thread(target=threaded_task,
                             args=(f"Task-{i+1}", COUNT, results, lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()
    total = sum(results)
    print("Threading total:", total)
    print("Threading time:", round(end_time - start_time, 4), "seconds")
    return round(end_time - start_time, 4)


# -----------------------------
# 5️⃣ MULTIPROCESSING EXAMPLE
# -----------------------------
def process_task(count):
    return do_something(count)


def run_processes():
    NUM_PROCS = 4
    COUNT = 1000000
    start_time = time.time()

    with multiprocessing.Pool(processes=NUM_PROCS) as pool:
        results = pool.map(process_task, [COUNT]*NUM_PROCS)

    end_time = time.time()
    total = sum(results)
    print("Multiprocessing total:", total)
    print("Multiprocessing time:", round(end_time - start_time, 4), "seconds")
    return round(end_time - start_time, 4)


# -----------------------------
# 6️⃣ SERIAL EXECUTION
# -----------------------------
def run_serial():
    NUM_TASKS = 4
    COUNT = 1000000
    start_time = time.time()
    results = []
    for _ in range(NUM_TASKS):
        results.append(do_something(COUNT))
    end_time = time.time()
    total = sum(results)
    print("Serial total:", total)
    print("Serial time:", round(end_time - start_time, 4), "seconds")
    return round(end_time - start_time, 4)


# -----------------------------
# 7️⃣ COMPARISON + OUTPUT FILE
# -----------------------------
if __name__ == "__main__":
    print("\n========== RUNNING COMPARISONS ==========\n")
    serial_time = run_serial()
    thread_time = run_threads()
    process_time = run_processes()

    comparison = (
        f"--- Execution Time Comparison ---\n"
        f"Serial Execution      : {serial_time} seconds\n"
        f"Threading Execution   : {thread_time} seconds\n"
        f"Multiprocessing Exec. : {process_time} seconds\n"
    )

    print("\n" + comparison)

    # Save comparison results
    with open("output_comparison.txt", "w") as f:
        f.write(comparison)

    print("Comparison written to output_comparison.txt")
