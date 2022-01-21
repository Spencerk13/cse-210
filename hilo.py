import random

score = 300
def main():
    card = card_number()
    print(f"The card is {card} ")
    guess = str(input("Higher or Lower? (h,l): "))
    new_card = card_number()
    bigger = higher_or_lower(card,new_card)
    points(bigger,guess,score)
def higher_or_lower(card,new_card):
    if card > new_card:
        return 1
    elif card < new_card:
        return 2
    else:
        return 0
def points(bigger,guess,points):
    if bigger.lower() == guess.lower():
        points += 100
    else:
        points -=75

def card_number():
    return random.random(1,13)

def game_over(score):
    if score>0:
        input = str(("Play again? (y/n): "))
        if input.lower() == "y":
            return False
        else:
            return True
    else:
        return True
if __name__ == "__main__":
    main()
