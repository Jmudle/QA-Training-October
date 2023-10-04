def getIncomeTax(salary):
    Tax = 0
    if salary > 150000:
        Tax += ((salary - 150000) * 45) / 100
        Tax += (115500 * 40) / 100
        Tax += (22650 * 20) / 100
        return Tax
    elif salary > 34500:
        Tax += ((salary - 34500) * 40) / 100
        Tax += (22650 * 20) / 100
        return Tax
    elif salary > 11850:
        Tax += ((salary - 11850) * 40) / 100
        return Tax
    else:
        pass

print(getIncomeTax())
        