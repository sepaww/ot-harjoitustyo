
import random as r


def apply_effect(effects: list, finance_info: object):
    """Applies the items effect to player finance object

    Args:
        effects (list): a list with effect tuples
        finance_info (Finance object): players finance info
    """
    for effect in effects:
        if effect[0] == "money":
            finance_info.money += effect[1]
        elif effect[0] == "income":
            finance_info.inc += effect[1]
        elif effect[0] == "expenses":
            finance_info.exp += effect[1]
        elif effect[0] == "lottery":
            chance = r.randint(0, 100)
            if chance == 1:
                apply_effect([("money", 1000)], finance_info)
            elif chance <= 10:
                apply_effect([("money", 100,)], finance_info)
            elif chance <= 30:
                apply_effect([("money", 10)], finance_info)
            elif chance <= 50:
                apply_effect([("money", 4)], finance_info)
