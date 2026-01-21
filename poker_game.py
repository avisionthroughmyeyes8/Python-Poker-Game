import random
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['hearts', 'diamonds', 'clubs', 'spades']

deck = []
for suit in suits:
    for rank in ranks:
        deck.append((rank, suit))

print(deck)


def deal_hand(deck, num_cards=5):
    hand = []
    for _ in range(num_cards):
        card = deck.pop()
        hand.append(card)
    return hand


random.shuffle(deck)

player_hand = deal_hand(deck)
computer_hand = deal_hand(deck)

print("Your hand:", player_hand)
print("Computer's hand:", computer_hand)

raank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def sort_hand(hand):
    return sorted(hand, key=lambda card: raank_values[card[0]])


def display_hand(hand):
    sorted_hand = sort_hand(hand)
    hand_str = []
    for rank, suit in sorted_hand:
        hand_str.append(f"{rank} of {suit}")
    return ", ".join(hand_str)


print("Your hand:", display_hand(player_hand))
print("Computer's hand:", display_hand(computer_hand))


def is_flush(hand):
    suits = [card[1] for card in hand]
    return len(set(suits)) == 1


def is_straight(hand):
    sorted_ranks = [raank_values[0]]
    for card in sort_hand(hand):
        sorted_ranks.append(raank_values[card[0]])
    return (max(sorted_ranks) - min(sorted_ranks) == 4) and (len(set(sorted_ranks)) == 5)


def count_ranks(hand):
    rank_count = {}
    for card in hand:
        rank = card[0]
        if rank in rank_count:
            rank_count[rank] += 1
        else:
            rank_count[rank] = 1
    return rank_count


def evaluate_hand(hand):
    rank_count = count_ranks(hand)
    is_flush_hand = is_flush(hand)
    is_straight_hand = is_straight(hand)

    if is_flush_hand and is_straight_hand:
        return "Straight Flush"
    elif 4 in rank_count.values():
        return "Four of a Kind"
    elif 3 in rank_count.values() and 2 in rank_count.values():
        return "Full House"
    elif is_flush_hand:
        return "Flush"
    elif is_straight_hand:
        return "Straight"
    elif 3 in rank_count.values():
        return "Three of a Kind"
    elif list(rank_count.values()).count(2) == 2:
        return "Two Pair"
    elif 2 in rank_count.values():
        return "One Pair"
    else:
        return "High Card"


player_hand_rank = evaluate_hand(player_hand)
computer_hand_rank = evaluate_hand(computer_hand)
print("Your hand rank:", player_hand_rank)
print("Computer's hand rank:", computer_hand_rank)
hand_ranks = ["High Card", "One Pair", "Two Pair", "Three of a Kind",
              "Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush"]
if hand_ranks.index(player_hand_rank) > hand_ranks.index(computer_hand_rank):
    print("You win!")
elif hand_ranks.index(player_hand_rank) < hand_ranks.index(computer_hand_rank):
    print("Computer wins!")
else:
    print("It's a tie!")

player_eval = evaluate_hand(player_hand)
computer_eval = evaluate_hand(computer_hand)
print("Your hand type:", player_eval)
print("Computer's hand type:", computer_eval)


while True:
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    player_hand = deal_hand(deck)
    computer_hand = deal_hand(deck)
    print("\nNew Round!")
    print("Your hand:", display_hand(player_hand))
    print("Computer's hand:", display_hand(computer_hand))
    player_hand_rank = evaluate_hand(player_hand)
    computer_hand_rank = evaluate_hand(computer_hand)
    print("Your hand rank:", player_hand_rank)
    print("Computer's hand rank:", computer_hand_rank)
    if hand_ranks.index(player_hand_rank) > hand_ranks.index(computer_hand_rank):
        print("You win!")
    elif hand_ranks.index(player_hand_rank) < hand_ranks.index(computer_hand_rank):
        print("Computer wins!")
    else:
        print("It's a tie!")
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        break
