def cost (price):
    if price < 5:
        pay = price
    elif price >= 5 and price < 30:
        sub = (price/3)
        pay = price - sub
    elif price >= 30:
        pay = price - 10
        print(pay)
        return pay
cost(50)
