
import random as r


def stock_operator(stock):
    """function that updates stocks price based on vi

    Args:
        stock (list): a stock

    Returns:
        list: updated stock (next days stock)
    """
    change = r.randint(0, 50)
    pos_min = r.randint(0, 1)
    if pos_min == 1:
        temp_1 = stock[1]+stock[2]*(stock[2]/100)
    else:
        temp_1 = stock[1]-stock[2]*(stock[2]/100)

    pos_min = r.randint(0, 1)
    if pos_min == 1:
        temp_2 = stock[2]+stock[2]*(change/100)
    else:
        temp_2 = stock[2]-stock[2]*(change/100)

    if temp_2 >= 50:
        temp_2 = 48

    temp_2 += 2
    if temp_1 <= 5:
        temp_1 = r.randint(3, 5)

    growth = ((int(temp_1)-stock[1])/stock[1])*100

    new_stock = [stock[0], int(temp_1), round(temp_2, 2), round(growth)]
    return new_stock


def create_history(stocks):
    """gives the stock created in stockcreator.py a 10
    day history with price changes and growth indcators

    Args:
        s (matrix): list that has the stocks of each in sublists
        and each stock in sublist is a 4 item long list itself

    Returns:
        matrix: updated stocklist (9 days worth of history added)
    """
    i = 0
    for i in range(9):
        stocks.append([])
        cur = stocks[i]
        j = 0
        for stock in cur:
            new_stock = stock_operator(stock)
            j += 1

            stocks[i+1].append(new_stock)
    return stocks


def stock_update(stocks):
    """same type of function as create_history but instead pops
    the zero inxed stock to keep stocklist at a length of 10.
    add a new days stocks to stocklist

    Args:
        s (matrix): list that has the stocks of each in sublists
        and each stock in sublist is a 4 item long list itself

    Returns:
        matrix: updated stocklist (earliest day removed
                and new days stocks added)
    """
    stocks.pop(0)
    stocks.append([])
    i = len(stocks)-2
    cur = stocks[i]
    j = 0
    for stock in cur:
        new_stock = stock_operator(stock)
        j += 1

        stocks[i+1].append(new_stock)
    return stocks
