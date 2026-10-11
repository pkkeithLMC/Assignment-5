
# ============================================================
# Problem 1: Find Most Frequent Element
# ============================================================
# Given a list of integers, return the value that appears
# most frequently. If tied, return any of the most frequent.
#
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}

    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    most_common = None
    highest_count = 0

    for num, count in counts.items():
        if count > highest_count:
            most_common = num
            highest_count = count

    return most_common


"""
Time and Space Analysis for problem 1:

- Best-case: O(n)
  Every number must be examined, even if all numbers
  are identical.

- Worst-case: O(n) expected/amortized
  We traverse the input and then the dictionary.
  Each dictionary operation is O(1) on average.
  Dictionary resizing occasionally costs O(n),
  but insertion is O(1) amortized.

- Average-case: O(n)
  Counting and finding the maximum are both linear.

- Space complexity: O(n)
  In the worst case, every number is unique, requiring
  n dictionary entries.

- Why this approach?
  A dictionary efficiently counts occurrences without
  repeatedly searching the original list.

- Could it be optimized?
  We could track the maximum while counting to avoid
  the second loop, but complexity remains O(n).

  A shorter solution uses collections.Counter.

NOTE: Pathological hash-table behavior can produce
O(n^2) worst-case time. O(n) is the expected/amortized
analysis appropriate for this course.
"""

# ALTERNATIVE 1: Using max() and list.count()
#
# def most_frequent(numbers):
#     if not numbers:
#         return None
#     return max(numbers, key=numbers.count)
#
# Best: O(n^2) for this implementation
# Worst: O(n^2)
# Average: O(n^2)
# Space: O(1) auxiliary
#
# count() scans the list each time max() evaluates
# a candidate. This is correct but inefficient.


# ALTERNATIVE 2: Using Counter
#
# from collections import Counter
#
# def most_frequent(numbers):
#     if not numbers:
#         return None
#     counts = Counter(numbers)
#     return counts.most_common(1)[0][0]
#
# Expected time: O(n)
# Space: O(n)
# Correct and efficient, but hides the counting logic.


# ============================================================
# Problem 2: Remove Duplicates While Preserving Order
# ============================================================
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result


"""
Time and Space Analysis for problem 2:

- Best-case: O(n)
  Every element must be examined.
  Even if all values are identical, we still check
  every element against the set.

- Worst-case: O(n) expected/amortized
  Set insertion and list append can occasionally
  trigger resizing, costing O(n) for an individual
  operation. Across the sequence, these operations
  are O(1) amortized each.

- Average-case: O(n)
  Set membership is O(1) on average.
  We process n elements.

- Space complexity: O(n)
  Both the set and result list can contain n elements.

- Why this approach?
  The set efficiently identifies duplicates.
  The list maintains the original order.

- Could it be optimized?
  Time complexity is already optimal.
  We could use dict.fromkeys() for a shorter solution.

NOTE: Pathological hash collisions can increase
the strict worst-case runtime to O(n^2).
"""

# ALTERNATIVE 1: List only
#
# def remove_duplicates(nums):
#     result = []
#     for num in nums:
#         if num not in result:
#             result.append(num)
#     return result
#
# Best: O(n) when all elements are identical
# Worst: O(n^2) when all elements are unique
# Average: O(n^2) for typical inputs with many
#          distinct elements
# Space: O(n)
#
# Correct, but list membership is O(n), not O(1).


# ALTERNATIVE 2: Convert to a set
#
# def remove_duplicates(nums):
#     return list(set(nums))
#
# NOT ACCEPTABLE:
# Does not guarantee preservation of input order.


# ALTERNATIVE 3: Dictionary
#
# def remove_duplicates(nums):
#     return list(dict.fromkeys(nums))
#
# Expected time: O(n)
# Space: O(n)
# Correct; dictionaries preserve insertion order.


# ============================================================
# Problem 3: Return All Pairs That Sum to Target
# ============================================================
# Assume the input list has no duplicates.
#
# Input: [1, 2, 3, 4], target = 5
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for num in nums:
        complement = target - num

        if complement in seen:
            pairs.append((complement, num))

        seen.add(num)

    return pairs


"""
Time and Space Analysis for problem 3:

- Best-case: O(n)
  Every element must be examined to find all pairs.
  Even when no pairs exist, the loop runs n times.

- Worst-case: O(n) expected/amortized
  Set membership is O(1) on average.
  Set insertion and list append are O(1) amortized.
  There is one pass through the list.

- Average-case: O(n)
  We perform constant expected work per element.

- Space complexity: O(n)
  The set can hold n values.
  The output can hold up to n/2 pairs.

- Why this approach?
  The set allows us to find complements efficiently.
  Since the input contains no duplicates, each
  valid pair is added only once.

- Could it be optimized?
  O(n) is optimal for an unsorted input.
  If the list were sorted, a two-pointer approach
  would use O(1) auxiliary space, excluding output.

NOTE: Pathological hash collisions can increase
strict worst-case runtime to O(n^2).
"""

# ALTERNATIVE 1: Nested loops
#
# def find_pairs(nums, target):
#     pairs = []
#
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 pairs.append((nums[i], nums[j]))
#
#     return pairs
#
# Best: O(n^2)
# Worst: O(n^2)
# Average: O(n^2)
# Space: O(n) including output; O(1) auxiliary
#
# Correct but less efficient.
# Using j = i + 1 avoids duplicate and self-pairs.


# ALTERNATIVE 2: Two pointers with sorting
#
# def find_pairs(nums, target):
#     nums = sorted(nums)
#     left = 0
#     right = len(nums) - 1
#     pairs = []
#
#     while left < right:
#         total = nums[left] + nums[right]
#
#         if total == target:
#             pairs.append((nums[left], nums[right]))
#             left += 1
#             right -= 1
#         elif total < target:
#             left += 1
#         else:
#             right -= 1
#
#     return pairs
#
# Worst: O(n log n) due to sorting
# Space: O(n) including output and sorted copy
#
# Correct, but sorting makes this slower than
# the expected O(n) set-based approach.


# ============================================================
# Problem 4: Simulate List Resizing (Amortized Cost)
# ============================================================
# Add n elements to a list with fixed initial capacity.
# When capacity is reached, double the capacity and
# explicitly copy the existing elements.
#
# Example: add_n_items(6)
# Resizing from 2 to 4
# Resizing from 4 to 8

def add_n_items(n):
    capacity = 2
    size = 0
    data = [None] * capacity

    for value in range(n):

        if size == capacity:
            new_capacity = capacity * 2

            print(f"Resizing from {capacity} "
                  f"to {new_capacity}")

            new_data = [None] * new_capacity

            for i in range(size):
                new_data[i] = data[i]

            data = new_data
            capacity = new_capacity

        data[size] = value
        size += 1

    return data[:size]


"""
Time and Space Analysis for problem 4:

- When do resizes happen?
  With initial capacity 2, resizing occurs before
  adding the 3rd, 5th, 9th, 17th, etc. elements.

  Capacity progression: 2, 4, 8, 16, 32...

- What is the worst-case for a single append?
  O(n)
  When capacity is reached, all existing elements
  must be copied to the larger array.

- What is the amortized time per append overall?
  O(1)
  Most appends require only one assignment.
  Occasional expensive resizes are distributed
  across many inexpensive operations.

- Space complexity: O(n)
  The allocated array grows proportionally to n.
  During resizing, both arrays temporarily exist,
  but total space remains O(n).

- Why does doubling reduce the cost overall?
  Each resize provides capacity for many new items.

  Total copying across n appends is bounded by:

      2 + 4 + 8 + ... < 2n

  Thus, total work for n appends is O(n).

  Amortized cost per append:
      O(n) / n = O(1)

ADDITIONAL:
- Best-case single append: O(1)
- Worst-case single append: O(n)
- Amortized append: O(1)
- Total n appends: O(n)

The final slice data[:size] also takes O(n) time
and O(n) space, without changing these bounds.
"""

# ALTERNATIVE 1: Track capacity without copying
#
# def add_n_items(n):
#     capacity = 2
#     size = 0
#
#     for i in range(n):
#         if size == capacity:
#             print("Resizing:", capacity, "to", capacity * 2)
#             capacity *= 2
#         size += 1
#
# This identifies WHEN resizing occurs.
# However, it does not simulate copying.
# It does not demonstrate the expensive operation
# that motivates amortized analysis.


# ALTERNATIVE 2: Python append()
#
# def add_n_items(n):
#     data = []
#     for i in range(n):
#         data.append(i)
#     return data
#
# Total time: O(n) amortized
# Space: O(n)
#
# NOT SUFFICIENT for this assignment.
# Python manages resizing internally, so the
# student has not simulated capacity or copying.


# ============================================================
# Problem 5: Compute Running Totals
# ============================================================
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]

def running_total(nums):
    result = []
    total = 0

    for num in nums:
        total += num
        result.append(total)

    return result


"""
Time and Space Analysis for problem 5:

- Best-case: O(n)
  Every input element must be processed to produce
  the complete result.

- Worst-case: O(n)
  There is one pass through the input.
  Although an individual append may require O(n)
  time during resizing, appends are O(1) amortized.
  Across n appends, total work remains O(n).

- Average-case: O(n)
  Each element requires one addition and one append.

- Space complexity: O(n)
  A new list is created containing n running totals.

- Why this approach?
  Keeping a running sum avoids recalculating
  sums for values already processed.

- Could it be optimized?
  Time complexity is already optimal.
  Space could be O(1) auxiliary if we modified
  the original list, but the problem asks for
  a new list.
"""

# ALTERNATIVE 1: Repeated sum() with slicing
#
# def running_total(nums):
#     result = []
#     for i in range(len(nums)):
#         result.append(sum(nums[:i + 1]))
#     return result
#
# Best: O(n^2)
# Worst: O(n^2)
# Average: O(n^2)
# Space: O(n) for output and temporary slices
#
# Correct, but repeatedly recalculates sums.
# Total work: 1 + 2 + 3 + ... + n = O(n^2).


# ALTERNATIVE 2: Modify input in place
#
# def running_total(nums):
#     for i in range(1, len(nums)):
#         nums[i] += nums[i - 1]
#     return nums
#
# Time: O(n)
# Auxiliary space: O(1)
#
# Correct mathematical result, but changes the
# input rather than creating a new list.


# ALTERNATIVE 3: itertools.accumulate
#
# from itertools import accumulate
#
# def running_total(nums):
#     return list(accumulate(nums))
#
# Time: O(n)
# Space: O(n)
# Correct and efficient, but hides the logic.


# ============================================================
# TEST CASES
# ============================================================

print("Problem 1:",
      most_frequent([1, 3, 2, 3, 4, 1, 3]))
# 3

print("Problem 2:",
      remove_duplicates([4, 5, 4, 6, 5, 7]))
# [4, 5, 6, 7]

print("Problem 3:",
      find_pairs([1, 2, 3, 4], 5))
# [(2, 3), (1, 4)] or equivalent

print("Problem 4:")
print(add_n_items(6))
# Resizing from 2 to 4
# Resizing from 4 to 8
# [0, 1, 2, 3, 4, 5]

print("Problem 5:",
      running_total([1, 2, 3, 4]))
# [1, 3, 6, 10]
