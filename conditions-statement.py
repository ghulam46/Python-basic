def evaluate_temp(temp):
    message = "Normal temperature"
    if temp > 38:
        message = "Fever!"
    return message

print(evaluate_temp(37))

# use else
def evaluate_temp_with_else(temp):
    if temp > 38:
        message = "Fever!"
    else:
        message = "Normal temperature"
    return message

print(evaluate_temp_with_else(40))

# use elif / else if
def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature"
    else:
        message = "Low temperature"
    return message

print(evaluate_temp_with_elif(32))

# In this next example, say you live in a country with only two tax brackets. Everyone earning less than 12,000 pays 25% in taxes, and anyone earning 12,000 or more pays 30%. The function below calculates how much tax is owed.
def get_tax(earnings):
    if earnings < 12000:
        tax_owned = earnings * .25
    else:
        tax_owned = earnings * .30
    return tax_owned

print(get_tax(9000))

def get_dose(weight):
    if weight < 5.2:
        dose = 1.25
    elif weight < 7.9:
        dose = 2.5
    elif weight < 10.4:
        dose = 3.75
    elif weight < 15.9:
        dose = 5
    elif weight < 21.2:
        dose = 7.5
    else:
        dose = 10
    return dose

print(get_dose(15.9))