"""
Chapter 2 — Threading, Locks, and Synchronization
"""
import threading
import time
from do_something import do_something


def threaded_task(name, count, results, lock):
    with lock:
        print(f"{name} started by {threading.current_thread().name}")
    result = do_something(count)
    results.append(result)
    print(f"{name} finished.")


def run_chapter2():
    print("\n========== CHAPTER 2: THREADING ==========\n")

    NUM_THREADS = 4
    COUNT = 500000
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
    elapsed = round(end_time - start_time, 4)

    print("Threading total:", total)
    print("Threading time:", elapsed, "seconds\n")
    return elapsed


if __name__ == "__main__":
    run_chapter2()
