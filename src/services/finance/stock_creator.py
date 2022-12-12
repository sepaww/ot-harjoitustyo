import random as r
#import stockhistory as hist
import services.finance.stock_history as hist


def create_stocks():
    """a function for creating stocks with random names, prices, volatilities.

    Returns:
        matrix: a matrix with 10 days worth of stock history
    """
    volatility = []
    stocks = []
    names = ["Kenny's chickens", "Roasted Toast", "GravyGrapes", "MinorMicrodose", "WarTech",
             "WesternEast", "Musked", "MentalMorgue", "ChinaMade",
             "Tiimari", "DrugStorez", "Fine9Dine"]
    temp_names = names.copy()
    namel = len(names)
    for i in range(1, 101):
        volatility.append(i)
    for i in range(10):
        start_price = r.choice(volatility)
        variance = r.choice(volatility)/100
        variance = variance*start_price
        temp = r.randint(0, namel-1)
        name = temp_names[temp]
        temp_names.pop(temp)
        namel -= 1
        stock = [name, int(start_price), variance, 0,]
        stocks.append(stock)

    stocks = [stocks]
    return hist.create_history(stocks)


def create_history_view(stocks, index):
    """counts the percentual differences in each days stockprice-minprice compared to maxvalue-minvalue of selected stock.
    then returns the calculated percentual values.

    Args:
        stocks (matrix): matrix of all stocks
        index (int): selected stocks index

    Returns:
        _type_: _description_
    """
    max_price = 0
    min_price = 1000000
    height_list = []
    # Find max and min values in stocks history
    for days_list in stocks:
        price = days_list[index][1]
        if price > max_price:
            max_price = price
        if price < min_price:
            min_price = price
    difference = max_price-min_price
    for days_list in stocks:
        price = days_list[index][1]
        days_price_diff = price-min_price
        percentual_height = (days_price_diff/difference)
        height_list.append(percentual_height)
    ret_list = [height_list.copy(), max_price, min_price]
    return ret_list
