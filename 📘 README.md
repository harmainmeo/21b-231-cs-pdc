# Combined Python Project (Chapter 1–3)

## 🧭 Overview
This project organizes all lessons into **separate chapters** for clarity:
- **Chapter 1:** Python Basics, OOP, Loops, File Handling  
- **Chapter 2:** Threading & Synchronization  
- **Chapter 3:** Multiprocessing & Process Pools  

Each chapter can run independently or together via `main.py`.

---

## 🗂️ Folder Structure
Combined_Project/
├── Chapter1_Basics/
│ └── chapter1.py
├── Chapter2_Threading/
│ └── chapter2.py
├── Chapter3_Multiprocessing/
│ └── chapter3.py
├── do_something.py
├── main.py
├── README.md
└── output_comparison.txt


---

## ⚙️ How to Run

### Option 1: Run Everything
```bash
python main.py

========== CHAPTER 1: Basics ==========
Positive number
Sum using for loop: 83
Sum of first 5 natural numbers: 15

========== CHAPTER 2: THREADING ==========
Threading time: 1.84 seconds

========== CHAPTER 3: MULTIPROCESSING ==========
Multiprocessing time: 1.12 seconds

--- Execution Time Comparison ---
Serial Execution      : 3.21 seconds
Threading Execution   : 1.84 seconds
Multiprocessing Exec. : 1.12 seconds

| Chapter | Key Topics                                 |
| ------- | ------------------------------------------ |
| **1**   | Classes, Inheritance, Loops, File I/O      |
| **2**   | Threading, Lock, Synchronization           |
| **3**   | Multiprocessing, Process Pool, Parallelism |


