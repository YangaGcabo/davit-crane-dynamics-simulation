import numpy as np

g = 9.81  # gravity
load_mass = 1700  # kg
arm_length = 2.5  # meters

force = load_mass * g
moment = force * arm_length

print(f"Lifting force: {force:.2f} N")
print(f"Bending moment at base: {moment:.2f} Nm")
