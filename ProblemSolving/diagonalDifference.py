# diagonal Difference

'''
input

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

#print(len(arr))
'''
'''
To access the elements of the array arr in the given diagonalDifference function, you can use the indices of the array. Here's how it works:

- arr[i][i] accesses the elements of the left diagonal (from top-left to bottom-right).
- arr[i][n-i-1] accesses the elements of the right diagonal (from top-right to bottom-left).

Here's the code with a bit of explanation:

python
def diagonalDifference(arr):
    n = len(arr)  # Get the size of the array (number of rows or columns, since it's a square matrix)
    left = 0      # Initialize sum for the left diagonal
    right = 0     # Initialize sum for the right diagonal

    for i in range(n):
        left += arr[i][i]        # Sum up the left diagonal elements
        right += arr[i][n-i-1]   # Sum up the right diagonal elements

    return abs(left - right)     # Return the absolute difference between the two sums


Let's break down the example array:

python
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]


- For the left diagonal:
  - arr[0][0] = 1
  - arr[1][1] = 5
  - arr[2][2] = 9
  - Sum: 1 + 5 + 9 = 15

- For the right diagonal:
  - arr[0][2] = 3
  - arr[1][1] = 5
  - arr[2][0] = 9
  - Sum: 3 + 5 + 9 = 17

The absolute difference between the sums is |15 - 17| = 2.

You can test the function with the given array like this:

python
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

print(diagonalDifference(arr))  # Output: 2
'''


def diagonalDifference(arr):
    n = len(arr)
    left = 0
    right = 0

    for i in range(n):
        left += arr[i][i]
        right += arr[i][n-i-1]

    return abs(left - right)