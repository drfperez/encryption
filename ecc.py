import matplotlib.pyplot as plt

# Allow the user to input the parameters of the elliptic curve
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Define the range of x-values to plot
x = range(-5, 6)

# Calculate the corresponding y-values for the elliptic curve
y = [((i**3 + a*i + b) % 11) for i in x]

# Plot the curve
plt.plot(x, y, 'b', label='y^2 = x^3 + {}x + {}'.format(a, b))

# Allow the user to input two points on the curve
x1 = int(input("Enter the x-coordinate of the first point: "))
y1 = int(input("Enter the y-coordinate of the first point: "))
x2 = int(input("Enter the x-coordinate of the second point: "))
y2 = int(input("Enter the y-coordinate of the second point: "))

# Plot the selected points on the curve
plt.plot(x1, y1, 'go', label='P ({}, {})'.format(x1, y1))
plt.plot(x2, y2, 'yo', label='Q ({}, {})'.format(x2, y2))

# Perform point addition
if x1 == x2 and y1 == y2:
    m = (3 * x1**2 + a) / (2 * y1)
else:
    if x1 != x2:
        m = (y2 - y1) / (x2 - x1)
    else:
        print("Error: x-coordinates of the two points are equal.")
        exit()

    x3 = m**2 - x1 - x2
    y3 = m * (x1 - x3) - y1

# Plot the result of the point addition
plt.plot(x3, y3, 'ro', label='R ({}, {})'.format(x3, y3))

# Display the formula used for point addition
if x1 == x2 and y1 == y2:
    formula = 'm = (3x1^2 + a) / (2y1)'
else:
    if x1 != x2:
        formula = 'm = (y2 - y1) / (x2 - x1)'
    else:
        formula = 'Error: x-coordinates of the two points are equal.'

plt.text(-4, 9, formula, size=10, bbox=dict(facecolor='white', alpha=0.5))

# Add annotations to the graph
plt.annotate('P', xy=(x1, y1), xytext=(-4, 3), arrowprops=dict(facecolor='green', shrink=0.05))
plt.annotate('Q', xy=(x2, y2), xytext=(-3, -7), arrowprops=dict(facecolor='yellow', shrink=0.05))

# Add a title and axis labels to the graph
plt.title('Elliptic Curve Cryptography')
plt.xlabel('x')
plt.ylabel('y')

# Show the legend
plt.legend()

# Show the graph
plt.show()
