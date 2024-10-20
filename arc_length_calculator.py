import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Define the derivative of the function f'(x)
def f_prime(x):
    return 3*x**2 - 10*x + 6
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Define the derivative of the function f'(x)
def f_prime(x):
    return 3*x**2 - 10*x + 6

# Define the function under the square root in the arc length formula
def integrand(x):
    return np.sqrt(1 + f_prime(x)**2)

# Set the limits of integration
a, b = 0, 4

# Perform the numerical integration to calculate the arc length
arc_length, error = quad(integrand, a, b)

# Output the result
print(f"Longitud del recorrido: {arc_length:.4f} metros")

# --- Optional: Plot the function f(x) and its profile ---

# Define the original function f(x)
def f(x):
    return x**3 - 5*x**2 + 6*x

# Create an array of x values for plotting
x_vals = np.linspace(0, 4, 400)
y_vals = f(x_vals)

# Plot the curve
plt.plot(x_vals, y_vals, label='f(x) = x^3 - 5x^2 + 6x', color='b')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Perfil de la cronoescalada')
plt.legend()
plt.grid(True)
plt.show()
