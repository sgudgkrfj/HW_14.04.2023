
import random

list1 = [random.randint(1, 10) for i in range(5)]
list2 = [random.randint(1, 10) for i in range(7)]

all_elements = list1 + list2

unique_elements = list(set(all_elements))

common_elements = list(set(list1) & set(list2))

unique_list1 = list(set(list1) - set(list2))
unique_list2 = list(set(list2) - set(list1))
unique_elements_in_lists = unique_list1 + unique_list2

min_max_elements = [min(list1), max(list1), min(list2), max(list2)]

print("Елементи обох списків:", all_elements)
print("Елементи обох списків без повторень:", unique_elements)
print("елементи, спільні для двох списків:", common_elements)
print("Тільки унікальні елементи кожного зі списків:", unique_elements_in_lists)
print("тільки мінімальне та максимальне значення кожного зі списків:", min_max_elements)
