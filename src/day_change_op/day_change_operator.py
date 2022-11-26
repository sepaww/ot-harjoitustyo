

def summary(stocks, finance, owned):
    curstock = stocks[-1]

    sumofmoney = 0
    for i in range(len(curstock)):
        if owned.owned[i] > 0:
            sumofmoney += curstock[i][1]*owned.owned[i]
    sumofmoney += finance.money
    print(sumofmoney)
    return sumofmoney


def finance_update(finance, timer):
    explist = [10, 10, 20, 20, 30, 30, 40, 40]
    finance.money -= finance.exp
    finance.money += finance.inc
    if timer.day > len(explist)-1:
        finance.exp += 50
    else:
        finance.exp += explist[timer.day]
