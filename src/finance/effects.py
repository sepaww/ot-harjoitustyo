
import random as r


def apply_effect(effects: list, financeinfo: object):
    """Applies the items effect to player finance object

    Args:
        effects (list): a list with effect tuples
        financeinfo (Finance object): players finance info
    """
    for effect in effects:
        if effect[0] == "money":
            financeinfo.money += effect[1]
        elif effect[0] == "income":
            financeinfo.inc += effect[1]
        elif effect[0] == "expenses":
            financeinfo.exp += effect[1]
        elif effect[0] == "lottery":
            chance = r.randint(0, 100)
            if chance == 1:
                apply_effect([("money", 1000)], financeinfo)
            elif chance <= 10:
                apply_effect([("money", 100,)], financeinfo)
            elif chance <= 30:
                apply_effect([("money", 10)], financeinfo)
            elif chance <= 50:
                apply_effect([("money", 4)], financeinfo)
