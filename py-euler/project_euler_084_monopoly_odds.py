"""
    Monopoly Odds

    Problem 84

    In the game, Monopoly, the standard board is set up in the following way:
    0084_monopoly_board.png

    A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they
    advance in a clockwise direction. Without any further rules we would expect to visit each square with equal
    probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this
    distribution.

    In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player
    rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to
    jail.

    At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

        Community Chest (2/16 cards):
            Advance to GO
            Go to JAIL
        Chance (10/16 cards):
            Advance to GO
            Go to JAIL
            Go to C1
            Go to E3
            Go to H2
            Go to R1
            Go to next R (railway company)
            Go to next R
            Go to next U (utility company)
            Go back 3 squares.

    The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of
    finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which
    the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a
    movement to another square, and it is the final square that the player finishes at on each roll that we are
    interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore
    the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.

    By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to
    produce strings that correspond with sets of squares.

    Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10,
    E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the
    six-digit modal string: 102400.

    If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
"""
import random
from typing import List
import time

"""
    Notes:
    
    Two four-sided dice.
    Rolls and their probabilities:
    { 2: 1/16, 3: 1/8, 4: 3/16, 5: 1/4: 6: 3/16, 7: 1/8, 8: 1/16}
    
    Possible strategy:
        1. Encode the rules with G2J, CH, and CC.
        2. Simulate a few thousand games of a hundred moves
        
    Notes on encoding the rules:
        1. Before each game, shuffle the CC and CH cards. Order is preserved, and the decks are cycled without
           shuffling.
        2. Start each game at GO, and run some number of moves, N.  A value for N may make a difference. It may be
           something worth adjusting to see if it changes the answer.  E.g., if N is low enough, then the chance
           of getting to the fourth board row may be low or zero.  If N is low then the chance of landing in the first
           board row is higher because that's where the first moves are.
"""

debug = True


def get_shuffled_cc_deck() -> List[int]:
    cc = ['X' for i in range(14)] + ['00', '10']
    random.shuffle(cc)
    return cc


def get_shuffled_ch_deck() -> List[int]:
    ch = ['X' for i in range(6)] + ['00', '10', '11', '24', '39', '05', 'R', 'R', 'U', '-3']
    random.shuffle(ch)
    return ch


def get_roll():
    chance = random.randint(0, 15)
    rolls = {0: 2, 1: 3, 2: 3, 3: 4, 4: 4, 5: 4, 6: 5, 7: 5, 8: 5, 9: 5, 10: 6, 11: 6, 12: 6, 13: 7, 14: 7, 15: 8}
    return rolls[chance]


def generate_next_position(position, cc, ch) -> (int, List[int], List[int]):
    if random.randint(1, 64) == 1:
        # 1/64 chance of rolling 'doubles' three times in a row
        # let's just simulate that with a flat probability
        position = 10
        return position, cc, ch
    roll = get_roll()
    position = (position + roll) % 40
    if position in [7, 22, 36]:
        # chance
        ch_card = ch[0]
        ch = ch[1:] + [ch[0]]
        if ch_card in ['00', '10', '11', '24', '39', '05']:
            position = int(ch_card)
        elif ch_card == 'R':
            position = (position % 10) + 5
        elif ch_card == 'U':
            position = 28 if position == 22 else 12
        elif ch_card == '-3':
            position -= 3
    if position in [2, 17, 33]:
        # community chest
        cc_card = cc[0]
        cc = cc[1:] + [cc[0]]
        if cc_card in ['00', '10']:
            position = int(cc_card)

    return position, cc, ch


def best_chance_string_for_monopoly():
    max_turns = 30000
    position = 0
    cc = get_shuffled_cc_deck()
    ch = get_shuffled_ch_deck()

    turn_count = 0
    position_count = [0 for i in range(40)]

    for g in range(1, 301):
        for i in range(max_turns):
            position, cc, ch = generate_next_position(position, cc, ch)
            position_count[position] += 1
            turn_count += 1
        if g % 10 == 0:
            # print(f'Game {g}, position count: {position_count}')
            position_count_dict = {i: round(e / turn_count, 5) for i, e in enumerate(position_count) if e / turn_count > 0.03}
            print(f'Position count dict: {position_count_dict}')

    position_count_dict = {i: e/turn_count for i, e in enumerate(position_count) if e/turn_count > 0.03}
    print(f'Position count dict: {position_count_dict}')
    return 1


def main():
    start = time.time()
    answer = best_chance_string_for_monopoly()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Project Euler 084 is {answer}")

    # The Answer to Project Euler 084 is


if __name__ == "__main__":
    main()
