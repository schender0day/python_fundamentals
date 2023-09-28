# Table of Contents

- [Summary](#summary)
  - [Arithmetic Operators](#arithmetic-operators)
- [Operation Nuances](#operation-nuances)
- [Precedence and Associativity](#precedence-and-associativity)
- [Additional Knowledge](#additional-knowledge)

---

## Summary

### Arithmetic Operators

Python supports various arithmetic operators: `+`, `-`, `*`, `/`, `%`, `//` and `**`.
These operators perform operations such as addition, subtraction, multiplication, division, modulus, floor division, and exponentiation.

**Real-world Example:**  
Imagine you're building a calculator app. The user inputs two numbers and selects an operation (like addition, subtraction, etc.). Behind the scenes, your Python code will use these arithmetic operators to compute and display the result.

**QA Flashcards:**  
**Q (EN/中文)**: What is the role of the `//` operator in Python?/Python 中的 `//` 运算符的作用是什么？  
**A (EN/中文)**: The `//` operator in Python performs floor division, which divides and returns the largest integer less than or equal to the quotient./Python 中的 `//` 运算符执行地板除法，除法后返回小于或等于商的最大整数。

---

## Operation Nuances

Floor division (`//`) returns the quotient's largest integer after discarding the fractional part.  
The modulus operation (`%`) returns the remainder of the division.  
True division (`/`) returns a float result.

**Real-world Example:**  
In a baking application, suppose you have 10 cookies and want to distribute them equally among 3 friends. Using floor division (`//`), you'd determine that each friend gets 3 cookies. Using the modulus (`%`), you'd know that 1 cookie remains undistributed.

**QA Flashcards:**  
**Q (EN/中文)**: How is the modulus operation different from floor division?/模运算与地板除法有何不同？  
**A (EN/中文)**: The modulus operation (`%`) returns the remainder of a division, while floor division (`//`) returns the quotient's largest integer after discarding the fractional part./模运算 (`%`) 返回除法的余数，而地板除法 (`//`) 返回舍去小数部分后的商的最大整数。

---

## Precedence and Associativity

Arithmetic expressions in Python are evaluated based on the precedence (priority) of the operators.  
If operators have the same precedence, their associativity determines the order of operations.

**Real-world Example:**  
Consider the process of solving a math problem on paper. You typically follow the order of operations (PEMDAS/BODMAS). In Python, when you evaluate an expression like `3 + 4 * 2`, the multiplication is performed before the addition, resulting in 11.

**QA Flashcards:**  
**Q (EN/中文)**: In the expression `3 + 4 * 2`, which operation is performed first according to Python's order of operations?/在表达式 `3 + 4 * 2` 中，根据 Python 的运算顺序，首先执行哪个运算？  
**A (EN/中文)**: In the expression `3 + 4 * 2`, the multiplication (`*`) is performed first according to Python's order of operations./在表达式 `3 + 4 * 2` 中，根据 Python 的运算顺序，首先执行乘法 (`*`)。

---

## Additional Knowledge (not covered in the content but useful)

- Be cautious when dealing with floating-point arithmetic due to potential precision issues.
- Python's `math` module provides a set of mathematical functions and constants to complement arithmetic operations.

**QA Flashcards:**  
**Q (EN/中文)**: Why might you need to be cautious when dealing with floating-point arithmetic in Python?/为什么在 Python 中处理浮点算术时可能需要小心？  
**A (EN/中文)**: Floating-point arithmetic in Python (and most programming languages) can have precision issues, leading to unexpected results due to the way floating-point numbers are represented internally./由于内部表示浮点数的方式，Python（和大多数编程语言）中的浮点算术可能存在精度问题，导致意外的结果。
