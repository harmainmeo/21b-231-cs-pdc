"""
Chapter 3 — Multiprocessing and Process Pools
"""
import multiprocessing
import time
from do_something import do_something


def process_task(count):
    return do_something(count)


def run_chapter3():
    print("\n========== CHAPTER 3: MULTIPROCESSING ==========\n")

    NUM_PROCS = 4
    COUNT = 500000
    start_time = time.time()

    with multiprocessing.Pool(processes=NUM_PROCS) as pool:
        results = pool.map(process_task, [COUNT]*NUM_PROCS)

    end_time = time.time()
    total = sum(results)
    elapsed = round(end_time - start_time, 4)

    print("Multiprocessing total:", total)
    print("Multiprocessing time:", elapsed, "seconds\n")
    return elapsed


if __name__ == "__main__":
    run_chapter3()
