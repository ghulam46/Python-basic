# Define a float
y = 1.
print(y)
print(type(y))

# Convert float to integer with the int function
z = int(y)
print(z)
print(type(z))

print(int(1.2321))
print(int(1.747))
print(int(-3.94535))
print(int(-2.19774))

print(3 * True)
print(-3.1 * True)
print(type("abc" * False))
print(len("abc" * False))

def get_expected_cost(beds, baths, has_basement):
    value = 80000 + 30000 * beds + 10000 * baths + 40000 * has_basement
    return value

print(get_expected_cost(3, 2, True))

print("F + T = ", False + False)
print("T + F = ", True + False)
print("F + T = ", False + True)
print("T + T = ", True + True)
print("F + T + T + T = ", False + True + True + True)

def cost_of_project(engraving, solid_gold):
    cost = solid_gold * (100 + 10 * len(engraving)) + (not solid_gold) * (50 + 7 * len(engraving))
    return cost

project_one = cost_of_project("Charlie+Denver", True)
print(project_one)

project_two = cost_of_project("08/10/2000", False)
print(project_two)