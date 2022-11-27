from random import randint as r


class Item():
    """a Class for item objects
    """

    def __init__(self, name: str, description: str, effectstr: str, effect: list, price: int,):
        """initiator

        Args:
            name (str): items name
            description (str): items description
            effectstr (str): effect description
            effect (list): list of items effects
            price (int): items price
        """
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
    """a funtion for giving daily items
    Returns:
        list: list of item objects
    """
    length = len(itempool)-1
    itemcompone = itempool[r(0, length)]
    itemcomptwo = itempool[r(0, length)]
    itemcompthree = itempool[r(0, length)]
    itemone = Item(itemcompone[0], itemcompone[1],
                 itemcompone[2], itemcompone[3], itemcompone[4])
    itemtwo = Item(itemcomptwo[0], itemcomptwo[1],
                 itemcomptwo[2], itemcomptwo[3], itemcomptwo[4])
    itemthree = Item(itemcompthree[0], itemcompthree[1],
                 itemcompthree[2], itemcompthree[3], itemcompthree[4])
    return [itemone, itemtwo, itemthree]
