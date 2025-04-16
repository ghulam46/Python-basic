def get_pay(num_hours):
    pay_pretax = num_hours * 15
    pay_aftertax = pay_pretax * (1 - .12)
    return pay_aftertax

pay_fulltime = get_pay(40)
pay_parttime = get_pay(32)
print(pay_parttime)