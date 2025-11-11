def factorialOf_n(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorialOf_n(n - 1)

print("Factorial of 5 is:", factorialOf_n(5))

num = int(input("Enter a number to find its factorial: "))

# Display the result
print(f"Factorial of {num} is: {factorialOf_n(num)}")