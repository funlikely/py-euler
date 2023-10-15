"""
    Poker Hands

    Problem 54

    In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

    The cards are valued in the order:
    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

    If two players have the same ranked hands then the rank made up of the highest value wins; for example,
    a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players
    have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards
    tie then the next highest cards are compared, and so on.
"""

debug = True


def is_flush(hand):
    return len(set([card[-1:][0] for card in hand])) == 1


def is_straight(hand):
    values = get_values_string(hand)
    return values in ('23456', '34567', '45678', '56789', '6789T', '789TJ', '89TJQ', '9TJKQ', 'TAJKQ')


def get_values_string(hand):
    return ''.join(sorted([card[:-1] for card in hand]))


def get_high_card(hand):
    values = get_values_string(hand)
    if 'A' in values:
        return 'A'
    elif 'K' in values:
        return 'K'
    elif 'Q' in values:
        return 'Q'
    elif 'J' in values:
        return 'J'
    elif 'T' in values:
        return 'T'
    else:
        return max([int(val) for val in values])


def get_hand_kindness(hand):
    kindness = 'unknown'
    values = get_values_string(hand)
    four_test = [values[i] == values[i + 3] for i in range(len(values) - 3)]
    if True in four_test:
        return 'four_of_a_kind'
    three_test = [values[i] == values[i + 2] for i in range(len(values) - 3)]
    if True in three_test:
        full_house_test = sorted([values[i] == values[i + 1] for i in range(len(values) - 3)])
        if full_house_test[-3:][0]:
            return 'full_house'
        else:
            return 'three_of_a_kind'
    two_pair_test = sorted([values[i] == values[i + 1] for i in range(len(values) - 3)])
    if two_pair_test[-2:][0]:
        return 'two_pairs'
    if two_pair_test[-1:][0]:
        return 'one_pair'

    return kindness


def get_hand_rank(hand):
    hand_kindness = get_hand_kindness(hand)
    if hand_kindness in ['four_of_a_kind', 'full_house', 'three_of_a_kind', 'two_pairs', 'one_pair']:
        return hand_kindness
    if is_flush(hand):
        if is_straight(hand):
            if get_high_card(hand) == 'A':
                return 'royal_flush'
            else:
                return 'straight_flush'

    return 'high_card'


def get_winner(p1_hand, p2_hand):
    p1_rank = get_hand_rank(p1_hand)
    p2_rank = get_hand_rank(p2_hand)

    ranks = {'royal_flush': 10, 'straight_flush': 9, 'four_of_a_kind': 8, 'full_house': 7, 'flush': 6,
             'straight': 5, 'three_of_a_kind': 4, 'two_pairs': 3, 'one_pair': 2, 'high_card': 1}

    if ranks[p1_rank] > ranks[p2_rank]:
        return 'player1'
    else:
        return 'player2'


def get_player1_win_count(hands):
    count = 0

    for hand in hands:
        if get_winner(hand[0], hand[1]) == 'player1':
            count += 1

    return count


def get_hands_from_file():
    file = open('data/project_euler_054.txt')
    lines = file.readlines()
    cards = [line.strip('\n').split(' ') for line in lines]
    hands = [[row[:5], row[5:]] for row in cards]
    return hands


def run_some_tests(hands):
    for hand in hands[:20]:
        p1_hand = hand[0]
        print_hand_state(p1_hand)
    for hand in hands[:20]:
        p2_hand = hand[1]
        p2_hand[0] = 'T'
        print_hand_state(p2_hand)
    print_hand_state(['3S', '3D', '3C', 'JH', 'JS'])
    print_hand_state(['3S', '4S', '6S', '5S', '7S'])
    print_hand_state(['KS', 'QS', 'JS', 'AS', 'TS'])


def print_hand_state(hand):
    print(
        f'hand [{hand}], rank = {get_hand_rank(hand)}, high card = {get_high_card(hand)}, values string = {get_values_string(hand)}')


def main():
    hands = get_hands_from_file()

    if debug:
        print(f'first ten player 1 hands: {[hand[0] for hand in hands[:10]]}')
        print(f'first ten player 2 hands: {[hand[1] for hand in hands[:10]]}')
        run_some_tests(hands)

    answer = get_player1_win_count(hands)
    print(f"The Answer to Project Euler 054 is {answer}")

    # The Answer to Project Euler 054 


if __name__ == "__main__":
    main()
