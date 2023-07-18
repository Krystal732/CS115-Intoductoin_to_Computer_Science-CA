def change(amount, coins):
    if amount == 0:
        return 0
    if coins == []:
        return float("inf")
    if coins[0] > amount:
        return change(amount, coins[1:])
    else:
        use = 1 + change(amount - coins[0], coins)
        lose = change(amount, coins[1:])
        return min(use,lose)

def mychange(amount, coins):
    if amount == 0:
        return 0
    if coins == [] or amount < 0:
        return float("inf")
    loseit = mychange(amount,coins[1:])
    useit = 1 + mychange(amount-coins[0], coins)
    return min(loseit, useit)
