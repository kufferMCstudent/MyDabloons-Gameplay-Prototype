"""
Katherine Uffer
April 9, 2023

GAME TITLE: My Dabloons!
VERSION a1.1.0

Main Class

FEATURES:
    - Deck of cards
    - Main gameplay loop
    - "Haunt" Mechanic: After the "Haunt" counter reaches 10 the game will end in 10 turns

CHANGELOG:
    - Added Haunt value to main()
    - Changed gameplay while loop to call gameplayLoop() function instade of Phase1() and Phase3()
    - Changed while loop condition to go until haunt = 10
    - Added endgame while loop in main() where game will end in 10 turns
    - Added haunt variable parameter to Phase1()
    - Added positive Haunt value to 3 cards
    - Added end-game spash screen to show final stats
    - Added description of main() function

"""
import random
import Card #cardName, cardType, fightStat, armorStat, flavorText
import Player #name, fightStat, armorStat, balance, hand, effect, challengeEffect, haunt

DECK = [ Card.Card("Plus 1 Coin", 0, 3, 0, "Challenge: Plus 1 extra coin", 1, 2, 1), Card.Card("Minus 1 Coin", 0, 3, 0, "Challenge: Loose no coins", -1, 0, 0), 
         Card.Card("Plus 1 Coin", 0, 4, 0, "Challenge: Plus 1 extra coin", 1, 2, 0), Card.Card("Minus 1 Coin", 0, 4, 0, "Challenge: Loose no coins", -1, 0, 1),
         Card.Card("Plus 1 Coin", 0, 5, 0, "Challenge: Plus 1 extra coin", 1, 2, 0), Card.Card("Minus 1 Coin", 0, 5, 0, "Challenge: Loose no coins", -1, 0, 1),
         Card.Card("Armor", 2, 0, 1, "Plus 1 Armor Stat", 0, 0, 0), Card.Card("Sword", 2, 1, 0, "Plus 1 Fight Stat", 0, 0, 0)  ]

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
PARAMETERS: Player object, int haunt
RETURN: int haunt
PURPOSE: Run player through Phase 1 of the core gameplay loop. This includes: 
            - Drawing a card from the deck
            - (Based on card type) Prompting the user to enter Phase 2
            - If Phase 2 is entered, take in choice and update stats according to win or loose
            - If Phase 2 is NOT entered, update stats or add Item card to player's hand
            - If card with a haunt value is pulled, increment haunt
        Returns haunt value abck to where it was called from
"""
def phaseOne(a, b):
    pick = DECK[random.randrange(0, 7, 1)]
    print(pick.getCardName())
    print(pick.getFlavorText())
    if pick.getCardType() == 0: #if coin card, check haunt and offer challenge(Phase 2) and update stats

        if pick.getHaunt() > 0: #if there is a Haunt value to the card
            b += pick.getHaunt()

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

    return b
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

"""
FUNCTION: gameplayLoop()
PARAMETERS: Player object, int haunt
RETURN: int haunt
PURPOSE: Run player through Phase 1, 2, and 3, and print Player stats. Keep track of haunt value.
         Returns the haunt value to where it was called from
"""
def gameplayLoop(player, haunt):
    haunt = phaseOne(player, haunt)
    phaseThree(player)
    print()
    print("Balance: " + str(player.getBalance()) + "\tFight Stat: " + str(player.getFightStat()) + "\tArmor Stat: " + str(player.getArmorStat()))
    print()
    return haunt

"""
FUNCTION: main()
PARAMETERS: none
RETURN: none
PURPOSE: Print start game splashscreen, call makePlayer() and save object to a variable. Print beginning stats.
         Run main game while loop and endgame while loop. Print endgame stats.
"""
def main():
    print('                   _ |\_')
    print("                   \` ..\ ")
    print('              __,.-" =__Y=')
    print('            ."        )             My Dabloons!')
    print('      _    /   ,    \/\_   The Prorotype for the card game.')
    print('     ((____|    )_-\ \_-`         Version a1.1.0')
    print("     `-----'`-----` `--`")

    player = makePlayer()
    counter = 0
    haunt = 0
    print(player.getName())
    print("Balance: " + str(player.getBalance()) + "\tFight Stat: " + str(player.getFightStat()) + "\tArmor Stat: " + str(player.getArmorStat()))

    while haunt != 10:
        counter += 1
        print("--------------------------- Turn", counter)
        haunt = gameplayLoop(player, haunt)

    for i in range(10, 0, -1):
        print("---------------------------", i, "Turns Left!")
        gameplayLoop(player, haunt)

    print("Thanks for Playing!!!")
    print(player.getName(), "'s Final Stats:")
    print("Balance: " + str(player.getBalance()) + "\tFight Stat: " + str(player.getFightStat()) + "\tArmor Stat: " + str(player.getArmorStat()))
        

if __name__ == "__main__":
    main()
