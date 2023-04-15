"""
Katherine Uffer
April 15, 2023

GAME TITLE: My Dabloons!
VERSION a1.3.0

Main Class

FEATURES:
    - Deck of cards
    - Main gameplay loop
    - Character Classes
    - "Haunt" Mechanic: After the "Haunt" counter reaches 10 the game will end in 10 turns
    - Shop to buy *and sell* items
    - Go bankrupt to end the game early

CHANGELOG:
    - Added CLASSES global list
    - Added class selection to makePlayer() and modifed returned Player object based on class choice
    - Added class to statement at the beginning of the game and end of game
    - Fixed hand printing bug in PhaseThree()
    - Fixed user input prompt in PhaseThree()
    - Implemented enterShop() in PhaseOne()
    - Added Shop Card to DECK
    - Fixed buy() bug where Player couldn't buy an item equal to their balance
    - Added bankrup feature if Player balance goes below 0
    - Added bankrupt check in PhaseOne()
    - Added bankrupt check in main() to print different end screen
    - Changed "Plus 1 Coins" cards to have different challenge effects
    - Added "Plus 3 Coins" and "Minus 2 Coins" cards with varying challenge difficulty and rewards
    - Fixed bug in sell() where printing loop would index out of range after an item was sold
    - Added Balance print to the top of every buy, sell, and shop action

"""
import random
import Card #cardName, cardType, fightStat, armorStat, flavorText, effect/buyPrice, challengeEffect/ sellPrice, haunt
import Player #name, fightStat, armorStat, balance, hand, class

DECK = [ Card.Card("Plus 1 Coin", 0, 3, 0, "Challenge: Plus 1 extra coin", 1, 2, 1), Card.Card("Minus 1 Coin", 0, 3, 0, "Challenge: Loose no coins", -1, 0, 0), 
         Card.Card("Plus 1 Coin", 0, 4, 0, "Challenge: Plus 2 extra coin", 1, 3, 0), Card.Card("Minus 1 Coin", 0, 4, 0, "Challenge: Loose no coins", -1, 0, 1),
         Card.Card("Plus 1 Coin", 0, 5, 0, "Challenge: Plus 3 extra coin", 1, 4, 0), Card.Card("Minus 1 Coin", 0, 5, 0, "Challenge: Loose no coins", -1, 0, 1),
         Card.Card("Plus 3 Coin", 0, 4, 0, "Challenge: Plus 1 extra coin", 3, 4, 1), Card.Card("Minus 2 Coin", 0, 3, 0, "Challenge: Loose no coins", -2, 0, 0), 
         Card.Card("Plus 3 Coin", 0, 5, 0, "Challenge: Plus 2 extra coin", 3, 5, 0), Card.Card("Minus 2 Coin", 0, 4, 0, "Challenge: Loose no coins", -2, 0, 1),
         Card.Card("Plus 3 Coin", 0, 6, 0, "Challenge: Plus 3 extra coin", 3, 6, 0), Card.Card("Minus 2 Coin", 0, 5, 0, "Challenge: Loose no coins", -2, 0, 1),
         Card.Card("Shop", 1, 0, 0, "", 0, 0, 0), Card.Card("Armor", 2, 0, 1, "Plus 1 Armor Stat", 7, 5, 0), Card.Card("Sword", 2, 1, 0, "Plus 1 Fight Stat", 7, 5, 0)  ]

SHOPDECK = [ Card.Card("Armor", 2, 0, 1, "Plus 1 Armor Stat", 7, 5, 0), Card.Card("Sword", 2, 1, 0, "Plus 1 Fight Stat", 7, 5, 0),
             Card.Card("Armor", 2, 0, 2, "Plus 2 Armor Stat", 14, 9, 0), Card.Card("Sword", 2, 2, 0, "Plus 2 Fight Stat", 14, 9, 0),
             Card.Card("Armor", 2, 0, 3, "Plus 3 Armor Stat", 18, 11, 0), Card.Card("Sword", 2, 3, 0, "Plus 3 Fight Stat", 18, 11, 0)  ]

CLASSES = ["Attacker", "Defender"]

"""
FUNCTION: makePlayer()
PARAMETERS: none
RETURN: Player object
PURPOSE: Propmt user for string to name their character, then string for their class, and return
         Player object with given name and stats based on class
"""
def makePlayer():
    name = input("Type your character's name here: ")
    
    classChoice = "a"
    while classChoice not in CLASSES:
        print(f"Please pick a class:")
        for i in range(0, len(CLASSES)):
            print(f"\t-", CLASSES[i])
        classChoice = input("Input: ").strip()
    
    if classChoice == CLASSES[0]: #If Attacker chosen
        return Player.Player(name, 3, 0, 5, [], 0)
    elif classChoice == CLASSES[1]: #If Defender Chosen
        return Player.Player(name, 0, 3, 5, [], 1)

"""
FUNCTION: buy()
PARAMETERS: Player Object, int Number of Cards, string Input, list Shop Deck
RETURN: Player object, Number of Cards
PURPOSE:- Propmt Player with 3 items from SHOPDECK the Player can buy using balance. 
        - If balance insufficent, tell Player purchase not made. 
        - If balance sufficient, update balance and add card to Player Hand. 
        - If no more cards to buy, state shop empty
"""
def buy(player, numbCards, buySell, inShop):
    if numbCards > 0: #If there is still things to buy

        while buySell != 'n' and numbCards != 0:
            print("--- Current Balance:", player.getBalance())
            printNumb = ""
            for i in range(0, numbCards): #Print cards
                print(f"{i+1}: {inShop[i].printBuyCard()}")
                printNumb = printNumb + str(i+1) + ","

            buySell = input(f"--- What would you like to buy (n for none)? ({printNumb} n): ").strip() #Get input
                    
            if buySell.isnumeric(): #if number
                buySell = int(buySell) #turn into int from string
                if buySell <= numbCards and buySell > 0: #if selected number in in range
                    if inShop[buySell-1].getEffect() <= player.getBalance(): #if the player can afford the item
                        player.addCard(inShop[buySell-1]) #add card to hand
                        player.setBalance(player.getBalance() - inShop[buySell-1].getEffect()) #Update player balance
                        print("---Thanks for purchasing", inShop[buySell-1].getCardName())
                        inShop.remove(inShop[buySell-1]) #remove card from shop
                        numbCards -= 1 #subtract number of cards
                    else:
                        print("--- Sorry! Looks like you cannot afford that item.")
                else:
                     print("--- Incorrect Input.")
    else: #if there are no mare cards in the deck
        print("--- You've bought out the whole shop!")
    return player, numbCards, inShop

"""
FUNCTION: sell()
PARAMETERS: Player Object, str
RETURN: Player object
PURPOSE: - Prompt player with all cards in Hand and number them
         - Player will select card to sell by number
         - Update balance and remove card from Hand
         - If no cards in hand, state hand is empty
"""
def sell(player, buySell):
    playerHand = player.getHand() #Get player's current hand
    handSize = len(playerHand)
    if handSize > 0: #If the player has cards in their hand
        while buySell != 'n' and handSize != 0:
            print("--- Current Balance:", player.getBalance())
            printNumb = ""
            for i in range(0, handSize): #Print cards
                print(f"{i+1}: {playerHand[i].printSellCard()}")
                printNumb = printNumb + str(i+1) + ","
            
            buySell = input(f"--- What would you like to sell (n for none)? ({printNumb} n): ").strip() #Get input

            if buySell.isnumeric(): #if number
                buySell = int(buySell) #turn into int from string
                if buySell <= handSize and buySell > 0: #if selected number in in range
                    player.setBalance(player.getBalance() + playerHand[buySell-1].getChallengeEffect())#Add card value to balance
                    print("---Thanks for selling", playerHand[buySell-1].getCardName())
                    player.removeCard(playerHand[buySell-1])#Update Hand in Player Object
                    playerHand = player.getHand()#Remove Card from local variable
                    handSize = len(playerHand) #decrement hand size
                else:
                    print("--- Incorrect Input.")
            else:
                print("--- Incorrect Input.")

    else: #If the player has no more cards
        print("--- You don't have anything to sell!")
    
    return player

"""
FUNCTION: enterShop()
PARAMETERS: Player Object
RETURN: Player object
PURPOSE: Propmt Player to Buy Items, Sell items, or leave. First, generate the cards that the shop has
         to sell that is passed to the buy() function if it is called. Then, take Player input to buy, 
         sell, leave, or neither. Player may leave the shop by typing 'L'
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
        print("--- Current Balance:", player.getBalance())
        buySell = input("--- Would you like to Buy (b), Sell (s), or Leave (L)?: ").strip() #Prompt input
        
        if buySell == 'b': #If Player wants to buy
            player, numbCards, inShop = buy(player, numbCards, buySell, inShop)
                    
        elif buySell == 's': #If Player wants to sell
            player = sell(player, buySell)
        
        elif buySell != 'L': #If improper input
            print("--- Improper Input ")

    return player

"""
FUNCTION: phaseOne()
PARAMETERS: Player object, int haunt
RETURN: int haunt
PURPOSE: Check if Player is backrupt at the start of every turn. If they are, break loop.
         Run player through Phase 1 of the core gameplay loop. This includes: 
            - Drawing a card from the deck
            - (Based on card type) Prompting the user to enter Phase 2
            - If Phase 2 is entered, take in choice and update stats according to win or loose
            - If Phase 2 is NOT entered, update stats or add Item card to player's hand
            - If card with a haunt value is pulled, increment haunt
         Returns haunt value back to where it was called from.
"""
def phaseOne(a, b):

    if a.getBalance() < 0: #if the Player goes bankrupt, return a haunt of 12 to end the game early
        return 12

    pick = DECK[random.randrange(0, len(DECK), 1)]
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
        a = enterShop(a)

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
    counter = 1
    if len(currentHand) != 0:
        for card in currentHand:
            text = str(card.printItemCard())
            print(str(counter) + ".\t" + text)
            counter += 1
        choice = input("---- Would you like to use any of these cards? (y/n): ")
        if choice == 'y':
            while choice.isalpha(): #dummy-proof myself lmao
                choice = input("Which card would you like to use (1 - " + str(len(currentHand)) + "): ").strip()
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
    print('     ((____|    )_-\ \_-`         Version a1.2.1')
    print("     `-----'`-----` `--`")

    player = makePlayer()
    counter = 0
    haunt = 0
    print(player.getName(), "the", CLASSES[player.getClass()])
    print("Balance: " + str(player.getBalance()) + "\tFight Stat: " + str(player.getFightStat()) + "\tArmor Stat: " + str(player.getArmorStat()))

    while haunt != 10:
        counter += 1
        print("--------------------------- Turn", counter)
        haunt = gameplayLoop(player, haunt)

    if haunt == 12: #If the player went Bankrupt
        print("\nYou went BANKRUPT!!!\n\nTry better next time!\n\nThanks for Playing!!!")
        print(player.getName(), "the", CLASSES[player.getClass()], "'s Final Stats:")
        print("Balance: " + str(player.getBalance()) + "\tFight Stat: " + str(player.getFightStat()) + "\tArmor Stat: " + str(player.getArmorStat()))
    else: #If the haunt was actually triggered
        for i in range(10, 0, -1):
            print("---------------------------", i, "Turns Left!")
            gameplayLoop(player, haunt)

        print("Thanks for Playing!!!")
        print(player.getName(), "the", CLASSES[player.getClass()], "'s Final Stats:")
        print("Balance: " + str(player.getBalance()) + "\tFight Stat: " + str(player.getFightStat()) + "\tArmor Stat: " + str(player.getArmorStat()))
        

if __name__ == "__main__":
    #enterShop(Player.Player("Kate", 3, 0, 100, [Card.Card("Armor", 2, 0, 1, "Plus 1 Armor Stat", 7, 5, 0), Card.Card("Sword", 2, 1, 0, "Plus 1 Fight Stat", 7, 5, 0)], 0))
    main()