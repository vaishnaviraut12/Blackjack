import random

# Define card ranks and suits
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Define card values
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
          'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Card class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'

# Deck class to handle shuffling and dealing
class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

# Hand class to handle player's and dealer's hands
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def calculate_score(self):
        score = sum(values[card.rank] for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == 'A')
        
        # Adjust for aces if the score is over 21
        while score > 21 and aces:
            score -= 10
            aces -= 1
        
        return score

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

# Function to display the player's and dealer's hands
def display_hands(player_hand, dealer_hand, show_dealer_card=False):
    print("\nPlayer's hand:", player_hand)
    print("Player's score:", player_hand.calculate_score())
    
    print("\nDealer's hand:", end=" ")
    if show_dealer_card:
        print(dealer_hand)
        print("Dealer's score:", dealer_hand.calculate_score())
    else:
        print(dealer_hand.cards[0], "and a hidden card")

# Function to simulate the dealer's actions
def dealer_turn(dealer_hand, deck):
    while dealer_hand.calculate_score() < 17:
        print("\nDealer hits.")
        dealer_hand.add_card(deck.deal_card())
        print("Dealer's hand:", dealer_hand)

# Main function to run the game
def play_blackjack():
    print("Welcome to Blackjack!\n")

    # Initialize deck, hands, and deal initial cards
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    # Deal two cards to player and dealer
    for _ in range(2):
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

    # Player's turn
    while True:
        display_hands(player_hand, dealer_hand)
        if player_hand.calculate_score() > 21:
            print("\nYou busted! Dealer wins.")
            return

        action = input("\nDo you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            player_hand.add_card(deck.deal_card())
        elif action == 'stand':
            break
        else:
            print("Invalid choice. Please type 'hit' or 'stand'.")

    # Dealer's turn
    dealer_turn(dealer_hand, deck)
    
    # Final scores
    player_score = player_hand.calculate_score()
    dealer_score = dealer_hand.calculate_score()
    
    # Display hands and scores
    display_hands(player_hand, dealer_hand, show_dealer_card=True)
    
    if dealer_score > 21:
        print("\nDealer busted! You win!")
    elif player_score > dealer_score:
        print("\nYou win!")
    elif player_score < dealer_score:
        print("\nDealer wins.")
    else:
        print("\nIt's a tie!")

# Run the game
if __name__ == "__main__":
    play_blackjack()
