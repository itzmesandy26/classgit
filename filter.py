numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = lambda x: x % 2 == 0

even_numbers = list(filter(even, numbers))

print("Original list:", numbers)
print("Even numbers:", even_numbers)
