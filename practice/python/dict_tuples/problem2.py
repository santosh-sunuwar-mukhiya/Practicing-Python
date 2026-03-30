#Write a program that asks user for operation. Value of operations could be,
# print: When user enters print it should print following,
# info ==> [600, 630, 620] ==> avg:  616.67
# ril ==> [1430, 1490, 1567] ==> avg:  1495.67
# mtl ==> [234, 180, 160] ==> avg:  191.33
# add: When user enters 'add', it asks for stock ticker and price.
# If stock already exist in your list (like info, ril etc) then it will append the price to the list.Otherwise it will create new entry in your dictionary.
# For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

import statistics

stocks = {
    'info': [600,630,620],
    'ril': [1430,1490,1567],
    'mtl': [234,180,160]
}

def print_all():
    for stock, price in stocks.items():
        avg = statistics.mean(price)
        print(f"{stock} ==> {price} ==> avg: ", round(avg, 2))

def add():
    stock = input("Enter the stock name:")
    price = float(input(f"Enter the price of the stock {stock}:"))
    if stock in stocks:
        stocks[stock].append(price)
    else:
        stocks[stock] = price
    print_all()

def main():
    machine = True
    while machine:
        op=input("Enter operation (print, add or amend):")
        if op.lower() == 'print':
            print_all()
        elif op.lower() == 'add':
            add()
        elif op.lower() == 'stop':
            machine = False
        else:
            print("Unsupported operation:",op)

if __name__ == '__main__':
    main()