from random import randint as r


class Item():
    def __init__(self, name: str, description: str, effectstr: str, effect: list, price: int,):
        self.name = name
        self.description = description
        self.effectstr = effectstr
        self.effect = effect
        self.price = price
        self.sold = False


itempool = [
    ["Cash", "You found cash on the floor!", "money +5", [("money", 5)], 0],
    ["Buscard", "You found a buscard on the floor!",
        "expenses-3", [("expenses", -3)], 0],
    ["Mining rig", "Cryptomoney printer", "income +30", [("income", 30)], 250],
    ["Communist manifesto", "life in a commune has its sides",
        "expenses -15, income -5", [("expenses", -15), ("income", -5)], 30],
    ["Coffee", "Makes you fast ... and addicted.",
        "income +10, expenses +3", [("income", 10), ("expenses", 3)], 15],
    ["Loan", "Money is never free", "money +500, expenses+150",
        [("money", 500), ("expenses", 150)], 0],
    ["Lottery ticket", "Luck be a lady tonight.",
        "money +??", [("lottery", 0)], 2],
    ["peasoup diet", "I guess it doesnt kill you.",
        "expenses -5", [("expenses", -5)], 10],
    ["Moneyprinter", "Illegal means looked down upon.",
        "income +400", [("income", 400)], 1000],
    ["Lottery ticket", "Luck be a lady tonight.",
        "money +??", [("lottery", 0)], 2],
    ["Lottery ticket", "Luck be a lady tonight.",
        "money +??", [("lottery", 0)], 2],
    ["Lottery ticket", "Luck be a lady tonight.",
        "money +??", [("lottery", 0)], 2],
    ["Dud", "Filler. Absolutely worthless. Sad even.",
        "none", [("money", 0)], 1]
]


def itemgiver():
    length = len(itempool)-1
    i1 = itempool[r(0, length)]
    i2 = itempool[r(0, length)]
    i3 = itempool[r(0, length)]
    item1 = Item(i1[0], i1[1], i1[2], i1[3], i1[4])
    item2 = Item(i2[0], i2[1], i2[2], i2[3], i2[4])
    item3 = Item(i3[0], i3[1], i3[2], i3[3], i3[4])
    return [item1, item2, item3]
