import random

def create_shoe(decks=6):
    """Create a shoe of cards for multiple decks using standard deck representation."""
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    shoe = []
    for suit in suits:
        for rank in ranks:
            shoe.append(rank if isinstance(rank, int) else 10 if rank in ['J', 'Q', 'K'] else 11)
    return shoe * decks

def shuffle_shoe(shoe):
    """Shuffle the shoe of cards."""
    random.shuffle(shoe)

def get_card_input(message="Enter card value (2-11), 'J', 'Q', 'K', or 'A' (press Enter to finish, type 'reset' to restart): "):
    """Get card input from the user with improved validation."""
    while True:
        card_val = input(message).upper()
        if card_val == 'RESET':
            return 'reset'
        elif not card_val:  # Check for empty input (Enter key pressed)
            return None
        elif card_val in ['J', 'Q', 'K']:
            return 10
        elif card_val == 'A':
            return 11
        try:
            card_val = int(card_val)
            if 2 <= card_val <= 11:
                return card_val
            else:
                print("Invalid card value (out of range). Please enter a number between 2 and 11.")
        except ValueError:
            print("Invalid card. Please enter a valid card value (number or 'J', 'Q', 'K', or 'A').")

def update_counts(card, running_count, decks_left, cards_dealt):
    """Update running and true counts based on Hi-Lo system."""
    if card in [7, 8, 9]:
        pass  # Neutral value for 7, 8, 9
    elif card in [2, 3, 4, 5, 6]:
        running_count += 1
    elif card in [10, 11]:  # including 10, Jack, Queen, King, and Ace
        running_count -= 1
    true_count = running_count / (decks_left - (cards_dealt // 52))
    return running_count, true_count

def estimate_decks_left(cards_dealt, total_cards):
    """Estimate the number of decks left in the shoe, considering cards dealt."""
    return (total_cards - cards_dealt) // 52 + 1

def suggest_bet(true_count):
    """Suggest betting strategy based on the true count (more levels)."""
    if true_count > 2:
        return "Consider significantly higher bets, the count is strongly in your favor."
    elif true_count > 1:
        return "Consider higher bets, the count is in your favor."
    elif true_count < -1:
        return "Consider lower bets, the count is against you."
    else:
        return "Normal betting advised."

def main():
    while True:
        print("Card Counter Program (Hi-Lo System)")
        print("Enter dealt cards one by one (2-11, J/Q/K/A), press Enter to finish.")
        print("Type 'reset' at any time to start a new session.")
        print("Cards will be displayed, and the count will be updated after each card.")

        shoe = create_shoe()
        shuffle_shoe(shoe)
        total_cards = len(shoe)
        cards_dealt = 0
        running_count = 0
        dealt_cards = []

        while cards_dealt < total_cards:
            card = get_card_input()
            if card is None:
                break
            elif card == 'reset':
                print("Resetting session...\n")
                break
            cards_dealt += 1
            dealt_cards.append(str(card))
            running_count, true_count = update_counts(card, running_count, estimate_decks_left(cards_dealt, total_cards), cards_dealt)

            print(f"\nDealt Cards: {', '.join(dealt_cards)}")
            print(f"Card: {card}, Running Count: {running_count}, True Count: {true_count:.1f}")
            print(suggest_bet(true_count))

        if card == 'reset':
            continue
        else:
            print(f"Card counting session ended. Final Running Count: {running_count}, True Count: {true_count:.1f}")
            break

if __name__ == "__main__":
    main()

 
