def average_list(lst, index=0, total=0):
    if index == len(lst):
        return total / len(lst) if len(lst) > 0 else 0
    total += lst[index]
    return average_list(lst, index + 1, total)
my_list = [10, 20, 30, 40, 50]
avg = average_list(my_list)
print("Average:", avg)