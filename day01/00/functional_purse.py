def add_ingot(purse):
    new_purse = purse.copy()
    if "gold_ingots" in new_purse and \
        new_purse ["gold_ingots"] > 0:
        new_purse["gold_ingots"] += 1
    else:
        new_purse = empty(new_purse)
        new_purse["gold_ingots"] = 1
    return new_purse
def get_ingot(purse):
    new_purse = purse.copy()
    if "gold_ingots" in new_purse and \
        new_purse["gold_ingots"] > 0:
        new_purse["gold_ingots"] -= 1
    else:
        return empty(new_purse)
    return new_purse

def empty(purse): return dict()
