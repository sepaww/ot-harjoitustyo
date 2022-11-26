def need_new_name(days, datab):
    if datab.scorelist[-1][1] > days:
        return False
    for i in range(len(datab.scorelist)):
        if datab.scorelist[i][1] < days:
            break
    copyl = datab.scorelist[:i]
    copyl.append(["____", days])
    for l in range(i, len(datab.scorelist)-1):
        copyl.append(datab.scorelist[l])
    datab.scorelist = copyl.copy()
    print(datab.scorelist, "paiv")
    datab.ind = i
    return True
