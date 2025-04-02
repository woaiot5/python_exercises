from os import system, name
import random
import deck


game_on = True
score_board = {"you": 0, "dealer": 0}
streak = 0
wallet_start = 1000
wallet = wallet_start
bet = 0

def set_a_bet(my_wallet):
    print(f"You have ${my_wallet}")
    my_bet = 0
    while not(0 < my_bet <= my_wallet):
        try:
            if my_bet > my_wallet:
                print("Insufficient amount.")
            my_bet = int(input("Your bet: $"))
        except ValueError:
            print("Please use numbers to set a bet.")
    system('cls' if name == 'nt' else 'clear')
    return my_bet

while game_on:
    system('cls' if name == 'nt' else 'clear')
    bet = set_a_bet(wallet)

    if game_on:
        game_deck = {"cards" : {}}
        my_hand = {"cards": [], "ranks": {}, "score": [0,0], "final score": 0}
        dealer_hand = {"cards": [], "ranks": {}, "score": [0,0], "final score": 0}
        game_deck = deck.new_deck(game_deck)
        deck.deal_cards(game_deck,my_hand,2)
        deck.deal_cards(game_deck,dealer_hand,2)

        print(f"Your bet: ${bet}\nYour hand:")
        deck.show_hand(my_hand)
        deal_new = (my_hand["final score"] != 21)

        while deal_new:
            print(f"Dealer's first card: {dealer_hand["cards"][0]}")
            if input("Do you want to deal a card? y/n: ").lower() == "y":
                deck.deal_cards(game_deck, my_hand, 1)
                system('cls' if name == 'nt' else 'clear')
                print(f"Your bet: ${bet}\nYour hand:")
                deck.show_hand(my_hand)
                if my_hand["score"][0] > 21 or my_hand["final score"]==21:
                    deal_new = False
            else:
                deal_new = False
        deck.final_score(my_hand)
        system('cls' if name == 'nt' else 'clear')

        deal_new = not(my_hand["final score"] >= 21 or dealer_hand["final score"] > my_hand["final score"])
        while deal_new:
            take_card = random.randrange(0, 100)
            if ((dealer_hand["final score"] == my_hand["final score"] and take_card > 50)
                    or dealer_hand["final score"] < my_hand["final score"]):
                deck.deal_cards(game_deck, dealer_hand, 1)
            deal_new = not(my_hand["final score"] >= 21 or dealer_hand["final score"] > my_hand["final score"])
        deck.final_score(dealer_hand)

        print("Your hand:")
        deck.show_hand(my_hand)
        print("\nDealer hand:")
        deck.show_hand(dealer_hand)

        if (my_hand["final score"] == 21
                or (my_hand["final score"] < 21 < dealer_hand["final score"])
                or (21 > my_hand["final score"] > dealer_hand["final score"])):
            print(f"\nYou win ${bet}!")
            score_board["you"] += 1
            streak += 1
            wallet += bet
        elif my_hand["final score"] == dealer_hand["final score"] < 21:
            print("\nIt's a tie!")
        else:
            print(f"\nYou lose ${bet}!")
            score_board["dealer"] += 1
            streak = 0
            wallet -= bet

        print(f"\nYou: {score_board["you"]} vs Dealer: {score_board["dealer"]}\nWinning streak: {streak}")
        if wallet == 0:
            game_on = False
        elif input(f"\nYou now have {wallet}$\nDo you want to play again? y/n: ").lower() != "y":
            game_on = False
        bet = 0

if wallet != 0: system('cls' if name == 'nt' else 'clear')

result = ""
if wallet >= wallet_start:
    result= f"You won ${wallet-wallet_start}"
elif wallet < wallet_start:
    result = f"You lost ${wallet_start-wallet}"

print(f"\nYour wallet balance is: ${wallet}\n{result}")
if wallet == 0: print("Get out!")