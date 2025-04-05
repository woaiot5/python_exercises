import random

RANKS = {
        '2':[2],
        '3':[3],
        '4':[4],
        '5':[5],
        '6':[6],
        '7':[7],
        '8':[8],
        '9':[9],
        '10':[10],
        'J':[10],
        'Q':[10],
        'K':[10],
        'A':[1,11]
         }

SUITS = ['♤', '♡', '♧', '♢']

def new_deck(deck_dict):
    for rank in RANKS:
        for suit in SUITS:
            deck_dict["cards"][f"{rank}{suit}"] = rank
    return deck_dict

def deal_cards(deck, hand, number):
    cards_in_deck = deck["cards"]
    for i in range(0,number):
        card = random.choice(list(cards_in_deck.keys()))
        hand["cards"].append(card)
        if cards_in_deck[card] in hand["ranks"]:
            hand["ranks"][cards_in_deck[card]] +=1
        else:
            hand["ranks"][cards_in_deck[card]] = 1
        deck["cards"].pop(card)
    count_score(hand)
    final_score(hand)

def count_score(hand):
    hand["score"][0] = 0
    hand["score"][1] = 0
    for rank in hand["ranks"]:
        if rank == 'A' and hand["ranks"]['A'] == 1:
            hand["score"][0] += 1
            hand["score"][1] += 11
        if rank == 'A' and hand["ranks"]['A'] == 2:
            hand["score"][0] += 2
            hand["score"][1] += 12
        if rank == 'A' and hand["ranks"]['A'] == 3:
            hand["score"][0] += 3
            hand["score"][1] += 13
        if rank == 'A' and hand["ranks"]['A'] == 4:
            hand["score"][0] += 4
            hand["score"][1] += 15
        if rank != 'A':
            hand["score"][0] += (RANKS[rank][0]*hand["ranks"][rank])
            hand["score"][1] += (RANKS[rank][0]*hand["ranks"][rank])

def final_score(hand):
    if (hand["score"][0] != hand["score"][1]
            and (hand["score"][0] > 21 or hand["score"][1] > 21 or hand["score"][0] == hand["score"][1])):
        hand["final score"] = int(hand["score"][0])
    else:
        hand["final score"] = int(hand["score"][1])

def show_hand(hand):
    print(f"{", ".join(hand["cards"])}")
    if 'A' in list(hand["ranks"].keys()) and hand["score"][1] < 21:
        print(f"Score: {hand["score"][0]} or {hand["score"][1]}")
    else:
        print(f"Score: {hand["final score"]}")


