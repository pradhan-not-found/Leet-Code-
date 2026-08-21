# 739. Daily Temperatures

## Problem Description

Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`-th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

---

## Algorithm Analysis

### Approach: Monotonic Decreasing Stack

The problem requires finding the "next greater element" for each item in the array, which is a classic use case for a Monotonic Stack.

**Steps:**
1. Initialize an `ans` array of the same length as `temperatures`, filled with `0`s. This handles the default case where no warmer day is found.
2. Initialize an empty `stack` which will store the **indices** of the temperatures (not the actual temperature values).
3. Iterate through the array using the index `i` and temperature `t`:
   - While the `stack` is not empty and the current temperature `t` is strictly greater than the temperature at the index currently at the top of the stack (`temperatures[stack[-1]]`):
     - It means we have found a warmer day for the temperature at the top of the stack.
     - Pop the index from the stack (let's call it `p`).
     - Calculate the waiting days as the difference between the current index and the popped index (`i - p`).
     - Assign this difference to `ans[p]`.
   - Push the current index `i` onto the stack to find its next warmer day in the future.
4. Return the `ans` array.

### Complexity

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the length of the `temperatures` array. Each index is pushed onto the stack exactly once and popped from the stack at most once. Thus, the inner `while` loop runs at most $n$ times globally across the entire `for` loop.
- **Space Complexity:** $\mathcal{O}(n)$, for storing the `ans` array and the `stack`. In the worst-case scenario (e.g., temperatures are strictly decreasing), the stack will store all $n$ indices.
