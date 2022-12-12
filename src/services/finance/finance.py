class Finance():
    """Players finance info
    """

    def __init__(self, chr_info):
        """initiator

        Args:
            amount (int): amount of starting money
            income (int): starting income
            expense (int): starting expenses
        """
        self.money = chr_info[3]
        self.inc = chr_info[4]
        self.exp = chr_info[5]
        self.reroll_price = chr_info[6]
        self.explist = chr_info[7]
        self.standard_exp_increase = chr_info[8]

    def change_amount(self, price):
        self.money -= price

    def change_amount_up(self, price):
        self.money += price

    def reroll_doubler(self):
        self.reroll_price *= 2


# character attributes:
character_list = [
    ("Jami", "your average 'Jantteri'", "average",
     300, 50, 50, 25, [20, 20, 30, 30, 40, 40], 50),
    ("Sanna", "High life", "harsh", 1000, 500, 100,
     100, [100, 100, 100, 200, 200, 200], 300),
    ("Sampo", "professional risk taker", "average",
     100, 50, 50, 1, [30, 35, 40, 45], 50),
    ("Niilo", "Unemployed with little expenses", "low", 50, 0,
     5, 10, [1, 1, 1, 2, 2, 5, 5, 10, 10, 20, 20, 30, 30], 40),
]
