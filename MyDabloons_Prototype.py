"""
Katherine Uffer
March 26, 2023

GAME TITLE: My Dabloons!
VERSION a1.0.1

Main Class

FEATURES:
    - Deck of cards
    - Main gameplay loop
    - Option to end game every 10 turns

CHANGELOG:
    - Added DECK constant list
    - Added +1 and -1 coins cards with fight stats 3-5
    - Added +1 armor and fight cards
    - Added Phase 1, 2, and 3 of main gameplay loop (only 1 and 3 are their own functions)

"""
import random
import Card #cardName, cardType, fightStat, armorStat, flavorText
import Player #name, fightStat, armorStat, balance, hand, effect, challengeEffect

DECK = [ Card.Card("Plus 1 Coin", 0, 3, 0, "Challenge: Plus 1 extra coin", 1, 2), Card.Card("Minus 1 Coin", 0, 3, 0, "Challenge: Loose no coins", -1, 0), 
         Card.Card("Plus 1 Coin", 0, 4, 0, "Challenge: Plus 1 extra coin", 1, 2), Card.Card("Minus 1 Coin", 0, 4, 0, "Challenge: Loose no coins", -1, 0),
         Card.Card("Plus 1 Coin", 0, 5, 0, "Challenge: Plus 1 extra coin", 1, 2), Card.Card("Minus 1 Coin", 0, 5, 0, "Challenge: Loose no coins", -1, 0),
         Card.Card("Armor", 2, 0, 1, "Plus 1 Armor Stat", 0, 0), Card.Card("Sword", 2, 1, 0, "Plus 1 Fight Stat", 0, 0)  ]

"""
FUNCTION: makePlayer()
PARAMETERS: none
RETURN: Player object
PURPOSE: Propmt user for string to name their character and return
         Player object with given name and set stats
"""
def makePlayer():
    name = input("Type your character's name here: ")
    return Player.Player(name, 3, 0, 5, [])

"""
FUNCTION: phaseOne()
PARAMETERS: Player object
RETURN: none
PURPOSE: Run player through Phase 1 of the core gameplay loop. This includes: 
            - Drawing a card from the deck
            - (Based on card type) Prompting the user to enter Phase 2
            - If Phase 2 is entered, take in choice and update stats according to win or loose
            - If Phase 2 is NOT entered, update stats or add Item card to player's hand
"""
def phaseOne(a):
    pick = DECK[random.randrange(0, 7, 1)]
    print(pick.getCardName())
    print(pick.getFlavorText())
    if pick.getCardType() == 0: #if coin card, offer challenge(Phase 2) and update stats

        choice = input("Would you like to challenge this card (y/n): ")

        if choice == 'y':
            if(a.getFightStat()+a.getArmorStat() > pick.getFightStat()+pick.getArmorStat()): #if Player is stronger
                print("You win the challenge! Bonus activated.")
                a.setBalance(a.getBalance() + pick.getChallengeEffect())

            else:
                print("You did not win the challenge. :(")
                a.setBalance(a.getBalance() + pick.getEffect())

        else: #if no challenge made
            a.setBalance(a.getBalance() + pick.getEffect())

    elif pick.getCardType() == 1: #if enemy card (Phase 2)
        pass

    elif pick.getCardType() == 2: #if item card, add to hand
        a.addCard(pick)
"""
FUNCTION: phaseThree()
PARAMETERS: Player object
RETURN: none
PURPOSE: Run player through Phase 3 of the core gameplay loop. This includes: 
            - Prompting user to use item cards or not
            - If used, update stats and remove card from player's hand
"""
def phaseThree(a):
    currentHand = a.getHand()
    if len(currentHand) != 0:
        counter = 1
        for card in currentHand:
            text = str(card.printItemCard()[0])
            print(str(counter) + ".\t" + text)
        choice = input("---- Would you like to use any of these cards? (y/n): ")
        if choice == 'y':
            while choice.isalpha(): #dummy-proof myself lmao
                choice = input("Which card would you like to use (1 - " + str(counter) + "): ").strip()
            a.setFightStat((a.getFightStat() + currentHand[int(choice)-1].getFightStat()))
            a.setArmorStat((a.getArmorStat() + currentHand[int(choice)-1].getArmorStat()))
            currentHand.remove(currentHand[int(choice)-1])
            a.setHand(currentHand)
        

def main():
    print('                   _ |\_')
    print("                   \` ..\ ")
    print('              __,.-" =__Y=')
    print('            ."        )             My Dabloons!')
    print('      _    /   ,    \/\_   The Prorotype for the card game.')
    print('     ((____|    )_-\ \_-`         Version a1.0.1')
    print("     `-----'`-----` `--`")

    player = makePlayer()
    counter = 0
    print(player.getName())
    print("Balance: " + str(player.getBalance()) + "\tFight Stat: " + str(player.getFightStat()) + "\tArmor Stat: " + str(player.getArmorStat()))

    while True:
        counter += 1
        print("--------------------------- Turn", counter)
        phaseOne(player)
        phaseThree(player)
        print()
        print("Balance: " + str(player.getBalance()) + "\tFight Stat: " + str(player.getFightStat()) + "\tArmor Stat: " + str(player.getArmorStat()))
        print()

        if counter%10 == 0: #arbitrary condition to ask user to end gameplay
            cont = input("Would you like to continue playing (y/n): ").strip()
            if cont == 'n':
                break
        

if __name__ == "__main__":
    main()
