"""
Katherine Uffer
April 10, 2023

GAME TITLE: My Dabloons!
VERSION a1.2.0

Main Class

FEATURES:
    - Deck of cards
    - Main gameplay loop
    - "Haunt" Mechanic: After the "Haunt" counter reaches 10 the game will end in 10 turns
    - Shop to buy items

CHANGELOG:
    - Updated Armor and Sword cards in DECK with buy and sell values
    - Created SHOPDECK constant list to include exclusive shop cards
    - Added enterShop() and description
    - Added buy() and description

"""
import random
import Card #cardName, cardType, fightStat, armorStat, flavorText
import Player #name, fightStat, armorStat, balance, hand, effect/buyPrice, challengeEffect/ sellPrice, haunt

DECK = [ Card.Card("Plus 1 Coin", 0, 3, 0, "Challenge: Plus 1 extra coin", 1, 2, 1), Card.Card("Minus 1 Coin", 0, 3, 0, "Challenge: Loose no coins", -1, 0, 0), 
         Card.Card("Plus 1 Coin", 0, 4, 0, "Challenge: Plus 1 extra coin", 1, 2, 0), Card.Card("Minus 1 Coin", 0, 4, 0, "Challenge: Loose no coins", -1, 0, 1),
         Card.Card("Plus 1 Coin", 0, 5, 0, "Challenge: Plus 1 extra coin", 1, 2, 0), Card.Card("Minus 1 Coin", 0, 5, 0, "Challenge: Loose no coins", -1, 0, 1),
         Card.Card("Armor", 2, 0, 1, "Plus 1 Armor Stat", 7, 5, 0), Card.Card("Sword", 2, 1, 0, "Plus 1 Fight Stat", 7, 5, 0)  ]

SHOPDECK = [ Card.Card("Armor", 2, 0, 1, "Plus 1 Armor Stat", 7, 5, 0), Card.Card("Sword", 2, 1, 0, "Plus 1 Fight Stat", 7, 5, 0),
             Card.Card("Armor", 2, 0, 2, "Plus 2 Armor Stat", 14, 9, 0), Card.Card("Sword", 2, 2, 0, "Plus 2 Fight Stat", 14, 9, 0),
             Card.Card("Armor", 2, 0, 3, "Plus 3 Armor Stat", 18, 11, 0), Card.Card("Sword", 2, 3, 0, "Plus 3 Fight Stat", 18, 11, 0)  ]

"""
FUNCTION: makePlayer()
PARAMETERS: none
RETURN: Player object
PURPOSE: Propmt user for string to name their character and return
         Player object with given name and set stats
"""
def makePlayer():
    name = input("Type your character's name here: ")
    return Player.Player(name, 3, 0, 100, [])

"""
FUNCTION: buy()
PARAMETERS: Player Object, int Number of Cards, string Input, list Shop Deck
RETURN: Player object, Number of Cards
PURPOSE:
        - Propmt Player with 3 items from SHOPDECK the Player can buy using balance. 
        - If balance insufficent, tell Player purchase not made. 
        - If balance sufficient, update balance and add card to Player Hand. 
        - If no more cards to buy, state shop empty
"""
def buy(player, numbCards, buySell, inShop):
    if numbCards > 0: #If there is still things to buy

        while buySell != 'n' and numbCards != 0:
            printNumb = ""
            for i in range(0, numbCards): #Print cards
                print(f"{i+1}: {inShop[i].printBuyCard()}")
                printNumb = printNumb + str(i+1) + ","

            buySell = input(f"--- What would you like to buy (n for none)? ({printNumb} n): ").strip() #Get input
                    
            if buySell.isnumeric(): #if number
                buySell = int(buySell) #turn into int from string
                if buySell <= numbCards and buySell > 0: #if selected number in in range
                    if inShop[buySell-1].getEffect() < player.getBalance(): #if the player can afford the item
                        player.addCard(inShop[buySell-1]) #add card to hand
                        player.setBalance(player.getBalance() - inShop[buySell-1].getEffect()) #Update player balance
                        inShop.remove(inShop[buySell-1]) #remove card from shop
                        numbCards -= 1 #subtract number of cards
                        print("---Thanks for purchasing", inShop[buySell-1].getCardName())
                    else:
                        print("--- Sorry! Looks like you cannot afford that item.")
                else:
                     print("--- Incorrect Input.")
    else:
        print("--- You've bought out the whole shop!")
    return player, numbCards, inShop
        
"""
FUNCTION: enterShop()
PARAMETERS: Player Object
RETURN: Player object
PURPOSE: Propmt Player to Buy Items, Sell items, or leave. First, generate the cards that the shop has
         to sell that is passed to the buy() function if it is called
           
         If sell:
                - Prompt player with all cards in Hand and number them
                - Player will select card to sell by number
                - Update balance and remove card from Hand
         Player may leave the shop by typing 'L'
"""
def enterShop(player):
    print("\n--- Welcome to the Shop!---\n")

    buySell = 'a' #Initial value

    numbCards = 3 #initial number of cards in shop
    inShop = []
    toAdd = []
    for i in range(0, 4): #pick out 3 cards
        temp = random.randrange(0, len(SHOPDECK)) #generate random number
        while temp in toAdd: #generate new numbers if first number already included
            temp = random.randrange(0, len(SHOPDECK))
        toAdd.append(temp) #add number to list
        inShop.append(SHOPDECK[temp]) #add card to shop

    while buySell != 'L': #Exit loop when Player want to leave shops
        buySell = input("--- Would you like to Buy (b), Sell (s), or Leave (L)?: ").strip() #Prompt input
        
        if buySell == 'b': #If Player wants to buy
            player, numbCards, inShop = buy(player, numbCards, buySell, inShop)
                    
        elif buySell == 's': #If Player wants to sell
            pass
        
        elif buySell != 'L': #If improper input
            print("--- Improper Input ")

    return player

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

    elif pick.getCardType() == 1: #if shop card, enter shop
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
