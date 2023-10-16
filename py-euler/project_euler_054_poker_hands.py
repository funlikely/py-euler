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

ranks = {'royal_flush': 10, 'straight_flush': 9, 'four_of_a_kind': 8, 'full_house': 7, 'flush': 6,
         'straight': 5, 'three_of_a_kind': 4, 'two_pairs': 3, 'one_pair': 2, 'high_card': 1}
card_ranks = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3,
              '2': 2}


def card_rank_sorted(cards):
    return sorted(cards, key=lambda x: -1 * card_ranks[x])


debug = True


def does_hand_have_flush(hand):
    return len(set([card[-1:][0] for card in hand])) == 1


def does_hand_have_straight(hand):
    values = get_values_string(hand)
    return values in ('23456', '34567', '45678', '56789', '6789T', '789JT', '89JQT', '9JKQT', 'AJKQT')


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
        return str(max([int(val) for val in values]))


def is_hand_four_of_a_kind(hand):
    values = get_values_string(hand)
    return True in [values[i] == values[i + 3] for i in range(len(values) - 3)]


def is_hand_full_house(hand):
    values = get_values_string(hand)
    return not is_hand_four_of_a_kind(hand) and \
        True in [values[i] == values[i + 2] for i in range(len(values) - 2)] and \
        sorted([values[i] == values[i + 1] for i in range(len(values) - 1)])[-3:][0]


def is_hand_three_of_a_kind(hand):
    values = get_values_string(hand)
    return not is_hand_full_house(hand) and True in [values[i] == values[i + 2] for i in range(len(values) - 2)]


def is_hand_two_pairs(hand):
    values = get_values_string(hand)
    two_pair_test = sorted([values[i] == values[i + 1] for i in range(len(values) - 1)])
    return not is_hand_three_of_a_kind(hand) and two_pair_test[-2:][0]


def is_hand_one_pair(hand):
    values = get_values_string(hand)
    one_pair_test = sorted([values[i] == values[i + 1] for i in range(len(values) - 1)])
    return not is_hand_two_pairs(hand) and one_pair_test[-1:][0]


def is_hand_royal_flush(hand):
    values = get_values_string(hand)
    return does_hand_have_flush(hand) and does_hand_have_straight(hand) and 'A' in values


def is_hand_straight_flush(hand):
    return not is_hand_royal_flush(hand) and does_hand_have_flush(hand) and does_hand_have_straight(hand)


def is_hand_flush(hand):
    return does_hand_have_flush(hand) and not does_hand_have_straight(hand)


def is_hand_straight(hand):
    return not does_hand_have_flush(hand) and does_hand_have_straight(hand)


def get_hand_rank(hand):
    values = get_values_string(hand)

    if is_hand_four_of_a_kind(hand):
        hand_rank = ['four_of_a_kind', values[2]]
    elif is_hand_full_house(hand):
        hand_rank = ['full_house', values[2], values[1] if values[3] == values[2] else values[3]]
    elif is_hand_three_of_a_kind(hand):
        hand_rank = ['three_of_a_kind', values[2]]
    elif is_hand_two_pairs(hand):
        sorted_pairs = card_rank_sorted([values[i] for i in range(len(values)) if values[i] in values[i + 1:]])
        hand_rank = ['two_pairs'] + [card for card in sorted_pairs] + [card for card in values if
                                                                       card not in sorted_pairs]
    elif is_hand_one_pair(hand):
        pair_card = [values[i] for i in range(len(values)) if values[i] in values[i + 1:]][0]
        hand_rank = ['one_pair'] + [pair_card] + card_rank_sorted(values.replace(pair_card, ''))
    elif is_hand_royal_flush(hand):
        hand_rank = ['royal_flush']
    elif is_hand_straight_flush(hand):
        hand_rank = ['straight_flush'] + [card_rank_sorted(values)[0]]
    elif is_hand_flush(hand):
        hand_rank = ['flush'] + card_rank_sorted(values)
    elif is_hand_straight(hand):
        hand_rank = ['straight'] + [card_rank_sorted(values)[0]]
    else:
        hand_rank = ['high_card'] + card_rank_sorted(values)

    return hand_rank


def identify_pair_card(hand):
    values = get_values_string(hand)
    pair_card = [values[i] for i in range(len(values) - 1) if values[i + 1] == values[i]]
    return pair_card


def get_winner_by_high_card_only(p1_hand, p2_hand):
    if card_ranks[get_high_card(p1_hand)] > card_ranks[get_high_card(p2_hand)]:
        return 'player1'
    else:
        return 'player2'


def get_winner(p1_hand, p2_hand):
    p1_rank = get_hand_rank(p1_hand)
    p2_rank = get_hand_rank(p2_hand)

    if ranks[p1_rank[0]] > ranks[p2_rank[0]]:
        return 'player1'
    elif ranks[p1_rank[0]] < ranks[p2_rank[0]]:
        return 'player2'
    else:
        for i in range(1, len(p1_rank)):
            if card_ranks[p1_rank[i]] > card_ranks[p2_rank[i]]:
                return 'player1'
            elif card_ranks[p1_rank[i]] < card_ranks[p2_rank[i]]:
                return 'player2'
    return 'player2'


def get_player1_win_count(hands):
    count = 0

    for hand in hands:
        if debug:
            print_hand_state(hand[0])
            print_hand_state(hand[1])
            if get_winner(hand[0], hand[1]) == 'player1':
                print('First hand wins')
            else:
                print('Second hand wins')
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
        print_hand_state(p2_hand)
    print_hand_state(['TS', '9D', 'JC', '7H', '8S'])
    print_hand_state(['TS', 'TD', 'JC', '8H', '8S'])
    print_hand_state(['TS', '8D', 'JC', '8H', '8S'])
    print_hand_state(['2D', '3D', '7D', 'JD', 'AD'])
    print_hand_state(['3S', '3D', '3C', 'JH', 'JS'])
    print_hand_state(['5S', 'JS', 'JH', '5D', 'JC'])
    print_hand_state(['TD', '9D', 'TC', 'TH', 'TS'])
    print_hand_state(['3S', '4S', '6S', '5S', '7S'])
    print_hand_state(['KS', 'QS', 'JS', 'AS', 'TS'])
    print('')


def get_suits(hand):
    return ''.join(sorted([card[1] for card in hand]))


def print_hand_state(hand):
    print(
        f'hand {hand}, rank = {get_hand_rank(hand)}, high card = {get_high_card(hand)}, values string = {get_values_string(hand)}, suits = {get_suits(hand)}')


def main():
    hands = get_hands_from_file()

    if debug:
        print(f'first ten player 1 hands: {[hand[0] for hand in hands[:10]]}')
        print(f'first ten player 2 hands: {[hand[1] for hand in hands[:10]]}')
        run_some_tests(hands)

    answer = get_player1_win_count(hands)
    print(f"The Answer to Project Euler 054 is {answer}")

    # The Answer to Project Euler 054 is 376


if __name__ == "__main__":
    main()
