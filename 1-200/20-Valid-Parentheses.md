# 20. Valid Parentheses

## Problem Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

---

## Algorithm Analysis

### Approach: Stack

The problem requires checking whether elements match in a Last-In-First-Out (LIFO) manner, which makes a **Stack** the perfect data structure. 

**Steps:**
1. Initialize a hash map (dictionary) to map closing brackets to their corresponding opening brackets.
2. Initialize an empty list to serve as the stack.
3. Iterate through each character in the given string `s`:
   - If the character is a closing bracket (i.e., it exists as a key in the hash map):
     - Check the top of the stack. If the stack is empty or the popped element does not match the required opening bracket, the string is invalid (`return False`).
   - If the character is an opening bracket:
     - Push it onto the stack.
4. After traversing the string, if the stack is completely empty, it means all opening brackets were properly closed (`return True`). If it is not empty, it means there are unmatched opening brackets (`return False`).

### Complexity

- **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. The string is traversed exactly once, and stack operations (push/pop) take $O(1)$ time.
- **Space Complexity:** $O(n)$ in the worst-case scenario (e.g., all opening brackets `'((((('`), where the stack will store all $n$ characters.
