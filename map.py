def square(num):
    return num * num

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))

print("Original numbers :", numbers)
print("Squared numbers :", squared_numbers)
