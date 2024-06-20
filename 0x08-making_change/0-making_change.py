#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize dp array with value greater than any possible number of coins
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: no coins needed to make total of 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
