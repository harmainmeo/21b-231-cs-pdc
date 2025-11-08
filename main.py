"""
main.py
-----------------------------------------
Runs all three chapters sequentially
and compares performance results.
-----------------------------------------
"""
from Chapter1_Basics.chapter1 import run_chapter1
from Chapter2_Threading.chapter2 import run_chapter2
from Chapter3_Multiprocessing.chapter3 import run_chapter3
from do_something import do_something
import time


def run_serial():
    NUM_TASKS = 4
    COUNT = 500000
    start_time = time.time()
    results = []
    for _ in range(NUM_TASKS):
        results.append(do_something(COUNT))
    end_time = time.time()
    total = sum(results)
    elapsed = round(end_time - start_time, 4)
    print("Serial total:", total)
    print("Serial time:", elapsed, "seconds\n")
    return elapsed


if __name__ == "__main__":
    print("\n========== COMBINED PROJECT ==========\n")

    # Run Chapter 1 (Basics)
    run_chapter1()

    # Run Chapter 2 (Threading)
    thread_time = run_chapter2()

    # Run Chapter 3 (Multiprocessing)
    process_time = run_chapter3()

    # Serial execution for comparison
    serial_time = run_serial()

    comparison = (
        f"--- Execution Time Comparison ---\n"
        f"Serial Execution      : {serial_time} seconds\n"
        f"Threading Execution   : {thread_time} seconds\n"
        f"Multiprocessing Exec. : {process_time} seconds\n"
    )

    print(comparison)
    with open("output_comparison.txt", "w") as f:
        f.write(comparison)

    print("Comparison written to output_comparison.txt ✅")
