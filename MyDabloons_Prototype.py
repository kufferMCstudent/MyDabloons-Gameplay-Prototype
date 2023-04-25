"""
Katherine Uffer
April 25, 2023

GAME TITLE: My Dabloons!
VERSION a1.3.2

Main Class

FEATURES:
    - Deck of cards
    - Main gameplay loop
    - Character Classes
    - "Haunt" Mechanic: After the "Haunt" counter reaches 10 the game will end in 10 turns
    - Shop to buy *and sell* items
    - Go bankrupt to end the game early
    - Limited number of chances to gain card bonuses
    - Class-Specific end-game goal

CHANGELOG:
    - Changed printout order in gameplayLoop() to make stats per turn more clear
    - Added cladd goal check at end of main()
    - Changed makePlayer() to get values from different variables and print starting stats and goals
    - Changed CLASSES list to match makePlayer() goals

"""
import random
import Card #cardName, cardType, fightStat, armorStat, flavorText, effect/buyPrice, challengeEffect/ sellPrice, haunt
import Player #name, fightStat, armorStat, balance, hand, class

DECK = [ Card.Card("Plus 1 Coin", 0, 1, 1, "Challenge: Plus 1 extra coin", 1, 2, 1), Card.Card("Minus 1 Coin", 0, 1, 1, "Challenge: Loose no coins", -1, 0, 0), 
         Card.Card("Plus 1 Coin", 1, 1, 2, "Challenge: Plus 2 extra coin", 1, 3, 0), Card.Card("Minus 1 Coin", 1, 1, 2, "Challenge: Loose no coins", -1, 0, 1),
         Card.Card("Plus 1 Coin", 0, 2, 1, "Challenge: Plus 3 extra coin", 1, 4, 0), Card.Card("Minus 1 Coin", 0, 2, 1, "Challenge: Loose no coins", -1, 0, 1),
         Card.Card("Plus 3 Coin", 1, 3, 3, "Challenge: Plus 1 extra coin", 3, 4, 1), Card.Card("Minus 2 Coin", 1, 2, 2, "Challenge: Loose no coins", -2, 0, 0), 
         Card.Card("Plus 3 Coin", 1, 3, 4, "Challenge: Plus 2 extra coin", 3, 5, 0), Card.Card("Minus 2 Coin", 1, 2, 3, "Challenge: Loose no coins", -2, 0, 1),
         Card.Card("Plus 3 Coin", 0, 4, 3, "Challenge: Plus 3 extra coin", 3, 6, 0), Card.Card("Minus 2 Coin", 0, 3, 2, "Challenge: Loose no coins", -2, 0, 1),
         Card.Card("Shop", 2, 0, 0, "", 0, 0, 0), 
         Card.Card("Armor", 3, 0, 1, "Plus 1 Armor Stat", 7, 5, 0), Card.Card("Sword", 3, 1, 0, "Plus 1 Fight Stat", 7, 5, 0),
         Card.Card("Armor", 3, 0, 1, "Plus 1 Armor Stat", 7, 5, 0), Card.Card("Sword", 3, 1, 0, "Plus 1 Fight Stat", 7, 5, 0)  ]

SHOPDECK = [ Card.Card("Armor", 2, 0, 1, "Plus 1 Armor Stat", 7, 5, 0), Card.Card("Sword", 2, 1, 0, "Plus 1 Fight Stat", 7, 5, 0),
             Card.Card("Armor", 2, 0, 2, "Plus 2 Armor Stat", 14, 9, 0), Card.Card("Sword", 2, 2, 0, "Plus 2 Fight Stat", 14, 9, 0),
             Card.Card("Armor", 2, 0, 3, "Plus 3 Armor Stat", 18, 11, 0), Card.Card("Sword", 2, 3, 0, "Plus 3 Fight Stat", 18, 11, 0)  ]

CLASSES = [["Attacker", "Fight", 2, 1], ["Defender", "Armor", 1, 2]]

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
    while True:
        print(f"Please pick a class:")
        for i in range(0, len(CLASSES)):
            print("\t", i+1, ")", CLASSES[i][0], "\tFight Stat:", CLASSES[i][2], "\tArmor Stat", CLASSES[i][3])
            print("\t  GOAL: Get a", CLASSES[i][1], "stat to 10 or higher.")
            print()
            print()
        classChoice = input("Input: ").strip()
    
        if classChoice == "1": #If Attacker chosen
            return Player.Player(name, 2, 1, 5, [], 0, 5)
        elif classChoice == "2": #If Defender Chosen
            return Player.Player(name, 1, 2, 5, [], 1, 5)

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
FUNCTION: phaseTwo()
PARAMETERS: Player object, Card object
RETURN: Player object
PURPOSE: Run through Phase 2 of the gameplay loop. If the player is able to make a challenge, do the following:
                - If Fight Card, ask user of they want to challenge the card using their fight stat
                - If Armor Card, ask user of they want to challenge the card using their armor stat
                - If player wins the challenge, apply bonus
                - If player loses the challenge, decrement their chances and do basic card action
         If the player has no more challenges to make, just do the basic card action
"""
def phaseTwo(player, card):

    print(card.getCardName())
    print(card.getFlavorText())

    if player.getNumbLives() > 0: #if the player can make a challenge

        if card.getCardType() == 0: #Fight Card
            
            choice = input(f"\nYour current Fight stat is {player.getFightStat()}.\n\nWould you like to take a chance and challenge this card?\nYou have {player.getNumbLives()} chances left to take (y/n): ")

            if choice == 'y':
                if(player.getFightStat() > card.getFightStat()): #if Player is stronger
                    print("You win the challenge! Bonus activated.")
                    player.setBalance(player.getBalance() + card.getChallengeEffect())

                else:
                    print("You were not strong enough to win the challenge. You lose 1 chance.")
                    player.setBalance(player.getBalance() + card.getEffect())
                    player.setNumbLives(player.getNumbLives() - 1)

            else: #if no challenge made
                player.setBalance(player.getBalance() + card.getEffect())

        elif card.getCardType() == 1: #Armor Card
            choice = input(f"\nYour current Armor stat is {player.getArmorStat()}.\n\nWould you like to take a chance and challenge this card?\nYou have {player.getNumbLives()} chances left to take (y/n): ")

            if choice == 'y':
                if(player.getArmorStat() > card.getArmorStat()): #if Player is stronger
                    print("You win the challenge! Bonus activated.")
                    player.setBalance(player.getBalance() + card.getChallengeEffect())

                else:
                    print("You were not strong enough to win the challenge. You lose 1 chance.")
                    player.setBalance(player.getBalance() + card.getEffect())
                    player.setNumbLives(player.getNumbLives() - 1)

            else: #if no challenge made
                player.setBalance(player.getBalance() + card.getEffect())

    else: #if no challenge can be made
        player.setBalance(player.getBalance() + card.getEffect())

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
    
    if pick.getCardType() == 0 or pick.getCardType() == 1: #if coin card, check haunt and offer challenge(Phase 2) and update stats

        if pick.getHaunt() > 0: #if there is a Haunt value to the card
            b += pick.getHaunt()

        a = phaseTwo(a, pick)

    elif pick.getCardType() == 2: #if shop card, enter shop
        a = enterShop(a)

    elif pick.getCardType() == 3: #if item card, print text, and add to hand
        print(pick.getCardName())
        print(pick.getFlavorText())

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
    print("Balance: " + str(player.getBalance()) + "\tFight Stat: " + str(player.getFightStat()) + "\tArmor Stat: " + str(player.getArmorStat()) + "\tChances: " + str(player.getNumbLives()))
    print()
    haunt = phaseOne(player, haunt)
    phaseThree(player)
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
    print('     ((____|    )_-\ \_-`         Version a1.3.2')
    print("     `-----'`-----` `--`")

    player = makePlayer()
    counter = 0
    haunt = 0

    #print()
    #print(player.getName(), "the", CLASSES[player.getClass()][0])
    #print("Balance: " + str(player.getBalance()) + "\tFight Stat: " + str(player.getFightStat()) + "\tArmor Stat: " + str(player.getArmorStat()) + "\tChances: " + str(player.getNumbLives()))
    print()

    while haunt != 10:
        counter += 1
        print("--------------------------- Turn", counter)
        haunt = gameplayLoop(player, haunt)

    if haunt == 12: #If the player went Bankrupt
        print("\nYou went BANKRUPT!!!\n\nTry better next time!\n\nThanks for Playing!!!")
        print(player.getName(), "the", CLASSES[player.getClass()], "'s Final Stats:")
        print("Balance: " + str(player.getBalance()) + "\tFight Stat: " + str(player.getFightStat()) + "\tArmor Stat: " + str(player.getArmorStat()) + "\tChances: " + str(player.getNumbLives()))
    else: #If the haunt was actually triggered
        for i in range(10, 0, -1):
            print("---------------------------", i, "Turns Left!")
            gameplayLoop(player, haunt)

        if player.goalReached():
            print()
            print("You have acheived your goal! You won the game!")
            print()
        else:
            print()
            print("You have not acheived your goal. Better luck next time!")
            print()


        print("Thanks for Playing!!!")
        print(player.getName(), "the", CLASSES[player.getClass()][0], "'s Final Stats:")
        print("Balance: " + str(player.getBalance()) + "\tFight Stat: " + str(player.getFightStat()) + "\tArmor Stat: " + str(player.getArmorStat()) + "\tChances: " + str(player.getNumbLives()))
        

if __name__ == "__main__":
    #enterShop(Player.Player("Kate", 3, 0, 100, [Card.Card("Armor", 2, 0, 1, "Plus 1 Armor Stat", 7, 5, 0), Card.Card("Sword", 2, 1, 0, "Plus 1 Fight Stat", 7, 5, 0)], 0))
    main()