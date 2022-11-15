import random as r
#import stockhistory as hist
import stocks.stockhistory as hist
def create_stocks():
    #import stocks.stockhistory as hist
    volatility=[]
    stocks=[]
    names=["Kenny's chickens", "Roasted Toast", "GravyGrapes", "MinorMicrodose", "WarTech", "WesternEast", "Musked", "MentalMorgue", "ChinaMade", "Tiimari", "DrugStorez", "Fine9Dine"]
    tempnames=names.copy()
    namel=len(names)
    for i in range(1, 101):
        volatility.append(i)
    for i in range(10):
        startprice=r.choice(volatility)
        variance=r.choice(volatility)/100
        variance=variance*startprice
        temp=r.randint(0, namel-1)
        name=tempnames[temp]
        tempnames.pop(temp)
        namel-=1       
        stock=[name, int(startprice), variance, 0,]
        stocks.append(stock)
    #print(stocks)
    stocks=[stocks]
    return hist.create_history(stocks)
    
