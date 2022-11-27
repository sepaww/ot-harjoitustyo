def need_new_name(days, datab):
    """A function determining whether a
    name needed or not based
    on did the player make it to highscore table

    Args:
        days (int): the amount of survived days
        datab (database object): the database class

    Returns:
        bool: A bool to give back info if name is needed.
    """
    if datab.scorelist[-1][1] > days:
        return False
    length=len(datab.scorelist)
    for i in range(length):
        if datab.scorelist[i][1] < days:
            break
    copyl = datab.scorelist[:i]
    copyl.append(["____", days])
    for index in range(i, len(datab.scorelist)-1):
        copyl.append(datab.scorelist[index])
    datab.scorelist = copyl.copy()

    datab.ind = i
    return True
