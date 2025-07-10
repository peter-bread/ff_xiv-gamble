import random
import time

total_players = 2


def switch(player: int):
    return (player % total_players) + 1


def play(output: bool = True, sleep: bool = False):
    target = 1

    player = 1

    num = 100000

    while not num == target:
        if sleep:
            time.sleep(0.5)

        num = random.randrange(1, num + 1)

        if output:
            print(f"Player {player}: {num}")
        player = switch(player)

    if output:
        print(f"\nPlayer {player} wins!!!")

    if player == 1:
        return 1, 0

    return 0, 1


player1_count = 0
player2_count = 0

runs = 10_000

for _ in range(runs):
    a, b = play(output=False)
    player1_count = player1_count + a
    player2_count = player2_count + b

print(f"Player 1 wins: {player1_count}")
print(f"Player 2 wins: {player2_count}")
