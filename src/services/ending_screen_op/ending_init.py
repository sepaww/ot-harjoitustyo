def need_new_name(days, data_base):
    """A function determining whether a
    name needed or not based
    on did the player make it to highscore table

    Args:
        days (int): the amount of survived days
        data_base (data_base object): the data_basease class

    Returns:
        bool: A bool to give back info if name is needed.
    """
    if data_base.score_list[-1][1] > days:
        return False
    length = len(data_base.score_list)
    for i in range(length):
        if data_base.score_list[i][1] < days:
            break
    copyl = data_base.score_list[:i]
    copyl.append(["____", days])
    for index in range(i, len(data_base.score_list)-1):
        copyl.append(data_base.score_list[index])
    data_base.score_list = copyl.copy()

    data_base.ind = i
    return True
