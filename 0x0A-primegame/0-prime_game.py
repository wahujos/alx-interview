#!/usr/bin/python3
"""
0. Prime Game
"""


def is_prime(num):
    """
    is_prime
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_primes_up_to(n):
    """
    get prime upto n
    """
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def play_game(n):
    """
    play the game
    """
    primes = get_primes_up_to(n)
    available = list(range(1, n + 1))
    current_player = 0  # 0 for Maria, 1 for Ben

    while True:
        move_made = False
        for prime in primes:
            if prime in available:
                # Remove the prime and all its multiples from available
                available = [x for x in available if x % prime != 0]
                move_made = True
                break
        if not move_made:
            return current_player  # The last player to move wins
        current_player = 1 - current_player  # Switch players


def isWinner(x, nums):
    """
    find out winner
    """
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
