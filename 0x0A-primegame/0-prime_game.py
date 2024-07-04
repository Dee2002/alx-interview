#!/usr/bin/python3
"""
Prime Game
"""


def sieve(n):
    """Sieve of Eratosthenes to find all primes up to n"""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [num for num, prime in enumerate(is_prime) if prime]


def simulate_game(n, primes):
    """Simulates the game and determines the winner for a given n"""
    nums = list(range(1, n + 1))
    turn = 0  # 0 for Maria, 1 for Ben

    while True:
        found_prime = False
        for prime in primes:
            if prime > n:
                break
            if prime in nums:
                found_prime = True
                nums = [x for x in nums if x % prime != 0]
                break

        if not found_prime:
            return 1 - turn  # The current player loses

        turn = 1 - turn  # Switch turns


def isWinner(x, nums):
    """Determines the overall winner after x rounds"""
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = sieve(max_n)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = simulate_game(n, primes)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
