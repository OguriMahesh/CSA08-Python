
integer_array = [11, 21, 3, 4, 5]

print("Array of integers:", integer_array)
array_length = int(input("Enter the length of the array: "))

user_integer_array = [int(input(f"Enter integer {i + 1}: ")) for i in range(array_length)]

print("User-defined array of integers:", user_integer_array)
