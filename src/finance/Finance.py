class Finance():
    """Players finance info
    """

    def __init__(self, amount, income, expense):
        """initiator

        Args:
            amount (int): amount of starting money
            income (int): starting income
            expense (int): starting expenses
        """
        self.money = amount
        self.inc = income
        self.exp = expense
