from sympy import symbols, Poly, div

def extended_polynomial_euclidean_algorithm(f, g):
    f = Poly(f)
    g = Poly(g)
    if f.degree() < g.degree():
        f, g = g, f
    x0, x1 = Poly(1, f.gen), Poly(0, f.gen)
    y0, y1 = Poly(0, f.gen), Poly(1, f.gen)

    print("Initial Polynomials:")
    print(f"f(x) = {f}")
    print(f"g(x) = {g}")
    print()

    while not g.is_zero:
        q, r = div(f, g)
        f, g = g, r 
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

        print(f"q(x) = {q}")
        print(f"r(x) = {r}")
        print(f"x(x) = {x1}")
        print(f"y(x) = {y1}")
        print()

    gcd = f
    x = x0
    y = y0

    print(f"GCD = {gcd}")
    print(f"x(x) = {x}")
    print(f"y(x) = {y}")
    return gcd, x, y

x = symbols('x')

# Define polynomials
# f = x**3 - 3*x - 2
# g = 3*x**2 - 3
f = x**3 + 3*x + 2
g = 3*x**2 + 3
# f = x**6 - 4*x**4 + 6*x**3 + 4*x**2 - 12*x + 9
# g = 6*x**5 - 16*x**3 + 18*x**2 + 8*x - 12

# Compute the Euclidean Algorithm
gcd, x, y = extended_polynomial_euclidean_algorithm(f, g)
print(f"Result: GCD = {gcd}, x = {x}, y = {y}")