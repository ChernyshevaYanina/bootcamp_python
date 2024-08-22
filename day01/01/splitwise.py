def split_booty(*dicts):
    sum_gold_ingots = 0
    for d in dicts:
        if "gold_ingots" in d:
            sum_gold_ingots += d["gold_ingots"]
    if sum_gold_ingots < 3:
        return "You need more gold ingots"
    base_count = sum_gold_ingots // 3
    remainder = sum_gold_ingots % 3
    
    purse1 = {"gold_ingots": base_count}
    purse2 = {"gold_ingots": base_count}
    purse3 = {"gold_ingots": base_count}
    
    if remainder == 1:
        purse1["gold_ingots"] += 1
    elif remainder == 2:
        purse1["gold_ingots"] += 1
        purse2["gold_ingots"] += 1
    
    return purse1, purse2, purse3
