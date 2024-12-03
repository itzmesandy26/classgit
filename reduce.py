from functools import reduce

list_ = [1, 2, 3, 4, 5]

multiply = lambda x, y: x * y

product = reduce(multiply, list_)

print("Original list:", list_)
print("Product of all elements:", product)
