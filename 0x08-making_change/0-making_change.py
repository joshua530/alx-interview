#!/usr/bin/python3
'''
making change solution
'''


from typing import Dict, List


def makeChange(coins: List[int], amount: int) -> int:
    '''
    making change solution function
    '''
    # dynamic programming -> tabulation
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a-c])
    return dp[amount] if dp[amount] != amount + 1 else -1

    # dumb!
    # num_coins = 0
    # left_over_amount = total
    # coins.sort(reverse=True)

    # for i in range(len(coins)):
    #     denom = coins[i]
    #     if left_over_amount == 0:
    #         break
    #     if left_over_amount > denom:
    #         num_denoms = left_over_amount // denom
    #         num_coins += num_denoms
    #         left_over_amount -= (denom * num_denoms)

    # if left_over_amount != 0:
    #     return -1

    # return num_coins
