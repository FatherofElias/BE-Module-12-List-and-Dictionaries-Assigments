import timeit
import sys


# Task 1 

def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  # Create a copy of dict1 to avoid modifying the original
    merged_dict.update(dict2)   # Update with dict2, preserving dict2's values for common keys
    return merged_dict

# Example usage:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'd': 4}
merged_dict = merge_dictionaries(dict1, dict2)
print(merged_dict)



dict1 = {f'key{i}': i for i in range(1000)}
dict2 = {f'key{i}': i * 10 for i in range(500, 1500)}

# Measure execution time
time_taken = timeit.timeit('merge_dictionaries(dict1, dict2)', globals=globals(), number=1000)
print(f"Time taken: {time_taken:.5f} seconds")

# Measure memory usage
merged_dict = merge_dictionaries(dict1, dict2)
memory_usage = sys.getsizeof(merged_dict)
print(f"Memory usage: {memory_usage} bytes")

# Analysis
# Time Complexity: 𝑂(𝑛+𝑚), where 𝑛 is the number of keys in dict1 and 𝑚 is the number of keys in dict2. The update operation iterates over each key-value pair in dict2.
# Space Complexity: 𝑂(𝑛+𝑚), as a new dictionary is created containing all key-value pairs from both dict1 and dict2.


# Task 2

def intersect_dictionaries(dict1, dict2):
    intersection = {k: dict1[k] for k in dict1 if k in dict2}
    return intersection

# Example usage:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 30, 'd': 40}
intersection = intersect_dictionaries(dict1, dict2)
print(intersection)


dict1 = {f'key{i}': i for i in range(1000)}
dict2 = {f'key{i}': i * 10 for i in range(500, 1500)}

# Measure execution time
time_taken = timeit.timeit('intersect_dictionaries(dict1, dict2)', globals=globals(), number=1000)
print(f"Time taken: {time_taken:.5f} seconds")

# Measure memory usage
intersection = intersect_dictionaries(dict1, dict2)
memory_usage = sys.getsizeof(intersection)
print(f"Memory usage: {memory_usage} bytes")


# Analysis
# Time Complexity: 𝑂(𝑛+𝑚), where 𝑛 is the number of keys in dict1 and 𝑚 is the number of keys in dict2. The check 𝑘∈𝑑𝑖𝑐𝑡2 for each key 𝑘 in dict1 takes average 𝑂(1) time due to the hash table implementation of dictionaries, but we iterate over all keys in dict1.
# Space Complexity: 𝑂(𝑘), where 𝑘 is the number of common keys between dict1 and dict2.

# Task 3

def word_frequencies(words):
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return freq_dict

# Example usage:
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
frequencies = word_frequencies(words)
print(frequencies)

words = ['apple'] * 500 + ['banana'] * 300 + ['orange'] * 200

# Measure execution time
time_taken = timeit.timeit('word_frequencies(words)', globals=globals(), number=1000)
print(f"Time taken: {time_taken:.5f} seconds")

# Measure memory usage
frequencies = word_frequencies(words)
memory_usage = sys.getsizeof(frequencies)
print(f"Memory usage: {memory_usage} bytes")


# Analysis
# Time Complexity: 𝑂(𝑛), where 𝑛 is the number of words in the list. Each word lookup and insertion in the dictionary takes average 𝑂(1) time due to the hash table implementation of dictionaries.
# Space Complexity: 𝑂(𝑘), where 𝑘 is the number of unique words in the list.
