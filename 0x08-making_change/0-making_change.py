#!/usr/bin/python3
'''
making change solution
'''


def makeChange(coins, total):
    '''
    making change solution function
    '''
    # dynamic programming -> tabulation
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for a in range(1, total + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a-c])
    return dp[total] if dp[total] != total + 1 else -1
