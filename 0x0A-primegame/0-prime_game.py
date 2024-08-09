#!/usr/bin/python3
"""
0. Prime Game module
"""


def isWinner(x, nums):
    """
    The is winner function
    """
    if x <= 0 or not nums:
        return None

    def Sieve_eratosthenes(max_n):
        """
        Sieve of Eratosthenes
        """
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, max_n + 1):
            if is_prime[i]:
                for j in range(i * 2, max_n + 1, i):
                    is_prime[j] = False
        primes = [i for i in range(max_n + 1) if is_prime[i]]
        return primes

    def simulate_game(n, primes):
        """
        determine the winner
        """
        remaining_numbers = list(range(1, n + 1))
        maria_turn = True

        while True:
            prime_found = False
            for prime in primes:
                if prime in remaining_numbers:
                    prime_found = True
                    break

            if not prime_found:
                return "Ben" if maria_turn else "Maria"

            remaining_numbers = [num for num in remaining_numbers
                                 if num % prime != 0]
            maria_turn = not maria_turn

    maria_wins = 0
    ben_wins = 0

    max_n = max(nums)

    primes = Sieve_eratosthenes(max_n)

    for n in nums:
        winner = simulate_game(n, primes)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
