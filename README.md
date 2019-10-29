# List Puzzles
There are 7 List puzzles in this lab.  There are a series of print
statements in the main method of which you need to create some simple
tests.

## Same End
Given 2 arrays (lists) of ints, a and b, return True if they have the
same first element or they have the same last element.
Both arrays will be length 1 or more.

```python
same_end([1, 2, 3], [7, 3]) → True
same_end([1, 2, 3], [7, 3, 2]) → False
same_end([1, 2, 3], [1, 3]) → True

def same_end(list_a, list_b):
    # ++ Your code here ++

    return "a boolean"
```

## List Sum
Given an array (list) of ints, return the sum of all the elements.
You must use a loop and may not use the sum() function

```python
list_sum([1, 2, 3]) → 6
list_sum([5, 11, 2]) → 18
list_sum([7, 0, 0]) → 7

def list_sum(num_list):
    # ++ Your code here ++

    return "the sum"
```

## Backwards
Given an array (list), return an array with the elements in backwards order
You must use a loop and may not use the reverse() function

```python
backwards([1, 2, 3]) → [3, 2, 1]
backwards([5, 11, 9, 8]) → [8, 9, 11, 5]
backwards([7, 0, "zero"]) → ["zero", 0, 7]
backwards(["pig", "horse", "cat"]) → ["cat", "horse", "pig"]

def backwards(list):
    # ++ Your code here ++

    return "the array backwards"
```

## Average
Given an array (list) of numbers, return the average of the array

```python
average([1, 2, 3]) → 2
average([5, 11, 2]) → 6
average([7, 0, 1]) → 2.6666666667

def average(num_list):
    # ++ Your code here ++

    return "the average"
```

## Count Evens
Return the number of even ints in the given array (should return an int).
Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

```python
count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
"""
def count_evens(list):
    # +++ Your code here +++

    return "number of evens"
```

## Biggest Difference
Given an array length 1 or more of ints, return the difference between
the largest and smallest values in the array (should return an int).
Note: the built-in min(v1, v2) and max(v1, v2) functions return the
smaller or larger of two values.

```python
big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([-20, -10, -7, -2]) → 18

def big_diff(list):
    # +++ Your code here +++

    return "biggest difference"
```

## Centered Average
Return the "centered" average of an array of ints, which we'll say is
the mean average of the values, except ignoring the largest and smallest
values in the array.
If there are multiple copies of the smallest value,
ignore just one copy, and likewise for the largest value. You may assume
that the array is length 3 or more. (should return a float)


```python
centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 10, 8, 7]) → 5.25
centered_average([-10, -4, -2, -4, -2, 1]) → -3

def centered_average():
    # +++ your code here +++

    return "centered average"
```