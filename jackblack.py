

import random
card_deck = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"] * 4
card_value = []
quit = ['stop', 'quit', 'end', 'i hate myself', 'i quit because i am a sore loser', "my mom doesn't love me", "i diddle sheep like a welshman", "i want to kill myself"]
hold = "hold"
hit = "hit"
acceptable_answers = [hit, hold]
computer_choices = ['hit', 'hold']
user_cards = []
show_cards = True

# create main program function here if name

def get_user_choice(prompt):
    while True:
        user_choice = input(prompt).strip().lower()
        if user_choice in acceptable_answers:
            return user_choice
        else:
            print("You should either hit or hold. ")

# Create function for face vaules here

# create hit/hold function


def win_condition(card_sum):
    if card_sum < 22 and card_sum > 16:
        return "YOU WIN!"
    else:
        return "YOU SUCK!"





random.shuffle(card_deck)
while True:
    if show_cards:
        print(user_cards)
    user_choice = get_user_choice('''Hit or Hold?
    > ''')
    if user_choice == "hit":
        card = card_deck.pop()
        user_cards.append(card)
    elif user_choice == "hold":
        for card in user_cards:
            if card in ("J", "Q", "K"):
                card_value.append(10)
            elif card in ("A",):
                card_value.append(11)
            else:
                card_value.append(card)
        show_cards = False
        print(sum(card_value))
        print(win_condition(sum(card_value)))
