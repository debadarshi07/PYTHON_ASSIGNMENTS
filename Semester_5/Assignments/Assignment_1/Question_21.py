from math import sqrt
d = float(input("Enter the height in meters: "))

vf = sqrt(2 * 9.8 *d)
print(f"Final velocity is: {vf:.2f} m/s")