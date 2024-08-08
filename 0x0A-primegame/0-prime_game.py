#!/usr/bin/python3
"""
0. Prime Game
"""


def isWinner(x, nums):
    """
    isWinner function
    """
    def sieve_of_eratosthenes(n):
        """
        Sieve of Eratosthenes
        """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        is_prime[0], is_prime[1] = False, False
        return is_prime

    def play_game(n):
        primes = sieve_of_eratosthenes(n)
        available = [i for i in range(1, n + 1)]
        current_player = 0  # 0 for Maria, 1 for Ben

        while True:
            # Find the next prime in the available numbers
            move_made = False
            for num in available:
                if primes[num]:
                    # Remove the number and all its multiples
                    available = [x for x in available if x % num != 0]
                    move_made = True
                    break
            if not move_made:
                return current_player  # The last player to move wins
            current_player = 1 - current_player  # Switch players

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
            # If n is 1, Maria cannot move, Ben wins automatically
        else:
            winner = play_game(n)
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
