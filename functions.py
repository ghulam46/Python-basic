# Function with 1 argument
def get_pay(num_hours):
    pay_pretax = num_hours * 15
    pay_aftertax = pay_pretax * (1 - .12)
    return pay_aftertax

pay_fulltime = get_pay(40)
pay_parttime = get_pay(32)
print(pay_parttime)


# Function with multiple arguments
def get_pay(num_hours, hourly_rate, tax_rate):
    pay_pretax = num_hours * hourly_rate
    pay_aftertax = pay_pretax * (1 - tax_rate)
    return pay_aftertax

pay_fulltime = get_pay(40, 15, .12)
pay_parttime = get_pay(32, 15, .12)
print(pay_fulltime)

# Function with no arguments
def print_hello():
    print("hello")
    print("Good morning")

print_hello()