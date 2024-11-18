import timeit 
import sys

# Task 1

def generate_squares(n):
    return [i**2 for i in range(1, n + 1)]

# Example usage:
n = 10
squares_list = generate_squares(n)
print(squares_list)


# Measure execution time
n = 1000
time_taken = timeit.timeit('generate_squares(n)', globals=globals(), number=1000)
print(f"Time taken: {time_taken:.5f} seconds")

# Measure memory usage
squares_list = generate_squares(n)
memory_usage = sys.getsizeof(squares_list)
print(f"Memory usage: {memory_usage} bytes")



#Analysis

# Time Complexity:
# The list comprehension iterates over each number from 1 to 𝑛, performing a constant-time operation (squaring the number) for each element.
# The time complexity is 𝑂(𝑛).

# Space Complexity:
# The space complexity is determined by the space required to store the list.
# Since the list contains 𝑛 elements, and each element is an integer, the space complexity is 𝑂(𝑛).



# Task 2

def reverse_sublist(lst, i, j):
    if i < 0 or j >= len(lst) or i > j:
        raise ValueError("Invalid indices")
    
    # Slice the sublist, reverse it, and assign it back
    lst[i:j+1] = lst[i:j+1][::-1]
    return lst

# Example usage:
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i, j = 2, 5
reversed_lst = reverse_sublist(lst, i, j)
print(reversed_lst)


# Measure execution time
lst = list(range(1000))
i, j = 200, 800
time_taken = timeit.timeit('reverse_sublist(lst, i, j)', globals=globals(), number=1000)
print(f"Time taken: {time_taken:.5f} seconds")

# Measure memory usage
reversed_lst = reverse_sublist(lst, i, j)
memory_usage = sys.getsizeof(reversed_lst)
print(f"Memory usage: {memory_usage} bytes")



# Analysis

# Time Complexity:
# Slicing the sublist from index 𝑖 to 𝑗 takes 𝑂(𝑗−𝑖+1) time.
# Reversing the sublist also takes 𝑂(𝑗−𝑖+1) time.
# Assigning the reversed sublist back to the original list takes 𝑂(𝑗−𝑖+1) time.
# Therefore, the overall time complexity is 𝑂(𝑗−𝑖+1).


# Space Complexity:
# The space complexity is determined by the space required to store the sliced sublist.
# Since the sublist contains 𝑗−𝑖+1 elements, the space complexity is 𝑂(𝑗−𝑖+1).
# The operation is in-place, as the original list's memory is reused.



# Task 3

def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    
    # Merge the lists
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # Append remaining elements
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    return merged_list

# Example usage:
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
merged_list = merge_sorted_lists(list1, list2)
print(merged_list)

# Measure execution time
list1 = list(range(0, 1000, 2))
list2 = list(range(1, 1000, 2))
time_taken = timeit.timeit('merge_sorted_lists(list1, list2)', globals=globals(), number=1000)
print(f"Time taken: {time_taken:.5f} seconds")

# Measure memory usage
merged_list = merge_sorted_lists(list1, list2)
memory_usage = sys.getsizeof(merged_list)
print(f"Memory usage: {memory_usage} bytes")



# Analysis
# Time Complexity:
# The function iterates through each element of both lists exactly once.
# If the lengths of the two lists are 𝑛 and 𝑚, the time complexity is 𝑂(𝑛+𝑚).

# Space Complexity:
# The space complexity is determined by the space required to store the merged list.
# Since the merged list contains all elements of both input lists, the space complexity is 𝑂(𝑛+𝑚).