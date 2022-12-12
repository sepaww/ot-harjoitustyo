from random import randint as r


class Item():
    """a Class for item objects
    """

    def __init__(self, name: str, description: str, effect_str: str, effect: list, price: int,):
        """initiator

        Args:
            name (str): items name
            description (str): items description
            effect_str (str): effect description
            effect (list): list of items effects
            price (int): items price
        """
        self.name = name
        self.description = description
        self.effect_str = effect_str
        self.effect = effect
        self.price = price
        self.sold = False


item_pool = [
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


def item_giver():
    """a funtion for giving daily items
    Returns:
        list: list of item objects
    """
    length = len(item_pool)-1
    item_comp_one = item_pool[r(0, length)]
    item_comp_two = item_pool[r(0, length)]
    item_comp_three = item_pool[r(0, length)]
    item_one = Item(item_comp_one[0], item_comp_one[1],
                   item_comp_one[2], item_comp_one[3], item_comp_one[4])
    item_two = Item(item_comp_two[0], item_comp_two[1],
                   item_comp_two[2], item_comp_two[3], item_comp_two[4])
    item_three = Item(item_comp_three[0], item_comp_three[1],
                     item_comp_three[2], item_comp_three[3], item_comp_three[4])
    return [item_one, item_two, item_three]
