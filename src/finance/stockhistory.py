
import random as r


def stock_operator(stock):
    """function that updates stocks price based on vi

    Args:
        stock (list): a stock

    Returns:
        list: updated stock (next days stock)
    """
    change = r.randint(0, 50)
    posmin = r.randint(0, 1)
    if posmin == 1:
        temp1 = stock[1]+stock[2]*(stock[2]/100)
    else:
        temp1 = stock[1]-stock[2]*(stock[2]/100)

    posmin = r.randint(0, 1)
    if posmin == 1:
        temp2 = stock[2]+stock[2]*(change/100)
    else:
        temp2 = stock[2]-stock[2]*(change/100)

    if temp2 >= 50:
        temp2 = 48

    temp2 += 2
    if temp1 <= 5:
        temp1 = r.randint(3, 5)

    growth = ((int(temp1)-stock[1])/stock[1])*100

    newstock = [stock[0], int(temp1), round(temp2, 2), round(growth)]
    return newstock


def create_history(s):
    """gives the stock created in stockcreator.py a 10 day history with price changes and growth indcators

    Args:
        s (matrix): list that has the stocks of each in sublists and each stock in sublist is a 4 item long list itself

    Returns:
        matrix: updated stocklist (9 days worth of history added)
    """
    i = 0
    for i in range(9):
        s.append([])
        cur = s[i]
        j = 0
        for stock in cur:
            newstock = stock_operator(stock)
            j += 1

            s[i+1].append(newstock)
    return s


def stock_update(s):
    """same type of function as create_history but instead pops the zero inxed stock to keep stocklist at a length of 10.
    add a new days stocks to stocklist

    Args:
        s (matrix): list that has the stocks of each in sublists and each stock in sublist is a 4 item long list itself

    Returns:
        matrix: updated stocklist (earliest day removed and new days stocks added)
    """
    s.pop(0)
    s.append([])
    i = len(s)-2
    cur = s[i]
    j = 0
    for stock in cur:
        newstock = stock_operator(stock)
        j += 1

        s[i+1].append(newstock)
    return s
