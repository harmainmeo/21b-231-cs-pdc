"""
Chapter 1 — Basic Python Concepts:
Classes, Loops, File Handling, and Conditions
"""

# ------------------- CLASSES -------------------
class MyClass:
    common = 10
    def __init__(self):
        self.myvariable = 3

    def myfunction(self, arg1, arg2):
        return self.myvariable + arg1 + arg2


class AnotherClass(MyClass):
    def __init__(self, message):
        super().__init__()
        print(f"Message from AnotherClass: {message}")


def run_chapter1():
    print("\n========== CHAPTER 1: Basics ==========\n")
    obj = MyClass()
    print("MyClass.myfunction(1, 2):", obj.myfunction(1, 2))

    obj2 = AnotherClass("Hello from inheritance!")
    print("AnotherClass.myfunction(5, 5):", obj2.myfunction(5, 5))

    # ------------------- CONDITIONS -------------------
    num = 3
    if num > 0:
        print("Positive number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative number")

    # ------------------- LOOPS -------------------
    numbers = [6, 6, 3, 8, -3, 2, 5, 44, 12]
    print("Sum using for loop:", sum(numbers))

    n = 5
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    print("Sum of first 5 natural numbers:", total)

    # ------------------- FILE HANDLING -------------------
    with open("sample.txt", "w") as f:
        f.write("This is a test file.\nSecond line written!\n")

    with open("sample.txt", "r") as f:
        print("\nFile Content:\n" + f.read())


if __name__ == "__main__":
    run_chapter1()
