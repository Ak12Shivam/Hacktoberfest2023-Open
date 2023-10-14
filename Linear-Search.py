def linear_search(arr, target):
    """
    Linear search function to find the target element in the given array.

    Args:
    arr (list): The list to search.
    target: The element to search for.

    Returns:
    int: The index of the target element if found, or -1 if not found.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Target found, return its index
    return -1  # Target not found

# Example usage:
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target_element = 9
result = linear_search(my_list, target_element)

if result != -1:
    print(f"{target_element} found at index {result}")
else:
    print(f"{target_element} not found in the list")
