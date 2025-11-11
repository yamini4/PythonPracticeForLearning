from scipy import integrate

# Define the function
def f(x):
    return x**2

# Integrate from 0 to 1
result, error = integrate.quad(f, 0, 1)

# Display result
print(f"Integral of f(x) = x^2 from 0 to 1 is {result}")
