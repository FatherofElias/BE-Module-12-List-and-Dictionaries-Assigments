# Task 1

def generate_squares(n):
    return [i**2 for i in range(1, n + 1)]

# Example usage:
n = 10
squares_list = generate_squares(n)
print(squares_list)
#Analysis

# Time Complexity:
# The list comprehension iterates over each number from 1 to 𝑛, performing a constant-time operation (squaring the number) for each element.
# The time complexity is 𝑂(𝑛).

# Space Complexity:
# The space complexity is determined by the space required to store the list.
# Since the list contains 𝑛 elements, and each element is an integer, the space complexity is 𝑂(𝑛).