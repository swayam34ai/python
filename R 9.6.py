def sanitize_list(lst, index=0):
    if index == len(lst):
        return lst
    if lst[index] < 0:
        lst[index] = 0
    return sanitize_list(lst, index + 1)
my_list = [10, -5, 3, -1, 4, -9, 7]
print("Original List:", my_list)
sanitized_list = sanitize_list(my_list)
print("Sanitized List:", sanitized_list)
