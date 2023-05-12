"""
Katherine Uffer
April 25, 2023

GAME TITLE: My Dabloons!
VERSION a1.4.0

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
    - Changed PhaseThree to implement new addEquip function
    - Changed the equip items prompt in PhaseThree to prompt until there are no more items/the user says no
    - Added checkEquiped() function to shop to allow for users to see which items they have equiped and to
      unequip them to sell
    - Changed game structure to that PhaseThree() is only called when the player wants to see their inventory during
      PhaseTwo before a challenge
    - Added another shop card to the deck to increase frequency
    - Added tutorial() so that new/returning users can see the game layout and changes
    - Sleepy cat for losing by Felix Lee
    - Added a second deck for challenges to become harder
    - Changed PhaseOne to call the original deck when the player has either stat below 5, and a new, more difficult
      deck when one of the player's stats is above 5
    - Added bits to printouts to make some things easier to see

"""
import random
import Card #cardName, cardType, fightStat, armorStat, flavorText, effect/buyPrice, challengeEffect/sellPrice, haunt
import Player #name, fightStat, armorStat, balance, hand, class

DECK = [ Card.Card("Plus 1 Coin", 0, 1, 1, "Challenge: Plus 1 extra coin", 1, 2, 1), Card.Card("Minus 1 Coin", 0, 1, 1, "Challenge: Loose no coins", -1, 0, 0), 
         Card.Card("Plus 1 Coin", 1, 1, 2, "Challenge: Plus 2 extra coin", 1, 3, 0), Card.Card("Minus 1 Coin", 1, 1, 2, "Challenge: Loose no coins", -1, 0, 1),
         Card.Card("Plus 1 Coin", 0, 2, 1, "Challenge: Plus 3 extra coin", 1, 4, 0), Card.Card("Minus 1 Coin", 0, 2, 1, "Challenge: Loose no coins", -1, 0, 1),
         Card.Card("Shop", 2, 0, 0, "", 0, 0, 0), 
         Card.Card("Plus 3 Coin", 1, 3, 3, "Challenge: Plus 1 extra coin", 3, 4, 1), Card.Card("Minus 2 Coin", 1, 2, 2, "Challenge: Loose no coins", -2, 0, 0), 
         Card.Card("Plus 3 Coin", 1, 3, 4, "Challenge: Plus 2 extra coin", 3, 5, 0), Card.Card("Minus 2 Coin", 1, 2, 3, "Challenge: Loose no coins", -2, 0, 1),
         Card.Card("Plus 3 Coin", 0, 4, 3, "Challenge: Plus 3 extra coin", 3, 6, 0), Card.Card("Minus 2 Coin", 0, 3, 2, "Challenge: Loose no coins", -2, 0, 1),
         Card.Card("Shop", 2, 0, 0, "", 0, 0, 0), 
         Card.Card("Armor", 3, 0, 1, "Plus 1 Armor Stat", 7, 5, 0), Card.Card("Sword", 3, 1, 0, "Plus 1 Fight Stat", 7, 5, 0),
         Card.Card("Armor", 3, 0, 1, "Plus 1 Armor Stat", 7, 5, 0), Card.Card("Sword", 3, 1, 0, "Plus 1 Fight Stat", 7, 5, 0)  ]
DECKTWO = [ Card.Card("Plus 1 Coin", 0, 5, 5, "Challenge: Plus 1 extra coin", 1, 2, 1), Card.Card("Minus 2 Coin", 0, 4, 4, "Challenge: Minus 1 Coin instead", -2, -1, 0), 
            Card.Card("Plus 1 Coin", 1, 5, 6, "Challenge: Plus 2 extra coin", 1, 3, 0), Card.Card("Minus 2 Coin", 1, 4, 5, "Challenge: Minus 1 Coin instead", -2, -1, 1),
            Card.Card("Plus 1 Coin", 0, 6, 5, "Challenge: Plus 3 extra coin", 1, 4, 0), Card.Card("Minus 2 Coin", 0, 5, 4, "Challenge: Minus 1 Coin instead", -2, -1, 1),
            Card.Card("Shop", 2, 0, 0, "", 0, 0, 0), 
            Card.Card("Plus 3 Coin", 1, 8, 8, "Challenge: Plus 1 extra coin", 3, 4, 1), Card.Card("Minus 3 Coin", 1, 5, 5, "Challenge: Minus 1 Coin instead", -3, -1, 0), 
            Card.Card("Plus 3 Coin", 1, 8, 9, "Challenge: Plus 2 extra coin", 3, 5, 0), Card.Card("Minus 3 Coin", 1, 5, 7, "Challenge: Minus 1 Coin instead", -3, -1, 1),
            Card.Card("Plus 3 Coin", 0, 9, 8, "Challenge: Plus 3 extra coin", 3, 6, 0), Card.Card("Minus 3 Coin", 0, 6, 5, "Challenge: Minus 1 Coin instead", -3, -1, 1),
            Card.Card("Shop", 2, 0, 0, "", 0, 0, 0), 
            Card.Card("Armor", 3, 0, 1, "Plus 1 Armor Stat", 7, 5, 0), Card.Card("Sword", 3, 1, 0, "Plus 1 Fight Stat", 7, 5, 0),
            Card.Card("Armor", 3, 0, 1, "Plus 1 Armor Stat", 7, 5, 0), Card.Card("Sword", 3, 1, 0, "Plus 1 Fight Stat", 7, 5, 0)  ]

SHOPDECK = [ Card.Card("Armor", 2, 0, 1, "Plus 1 Armor Stat", 7, 5, 0), Card.Card("Sword", 2, 1, 0, "Plus 1 Fight Stat", 7, 5, 0),
             Card.Card("Armor", 2, 0, 2, "Plus 2 Armor Stat", 14, 9, 0), Card.Card("Sword", 2, 2, 0, "Plus 2 Fight Stat", 14, 9, 0),
             Card.Card("Armor", 2, 0, 3, "Plus 3 Armor Stat", 18, 11, 0), Card.Card("Sword", 2, 3, 0, "Plus 3 Fight Stat", 18, 11, 0)  ]

CLASSES = [["Attacker", "Fight", 2, 1], ["Defender", "Armor", 1, 2]]

"""
FUNCTION: tutorial()
PARAMETERS: none
RETURN: none
PURPOSE: Show the User what things mean and how they print
"""
def tutorial():
    print('                   _ |\_')
    print("                   \` ..\ ")
    print('              __,.-" =__Y=')
    print('            ."        )             My Dabloons!')
    print('      _    /   ,    \/\_   The Prorotype for the card game.')
    print('     ((____|    )_-\ \_-`         Version a1.4.0')
    print("     `-----'`-----` `--`")
    userChoice = input("\nWould you like to go through the tutorial (y/n)?: ")
    if userChoice == 'y':
        player = Player.Player("Tutorial Cat", 2, 1, 5, [], 0, 5, [])
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('\tWelcome to the tutorial for "My Dabloons!", a game that is in early in its development.')
        print('\tThe main way to interact with this game is through the command line interface that you')
        print('\tare using right now. When you have a choice to make, you will be given numbers or letters')
        print('\tas options to select things. Be careful what you put in! You may crash the game.')
        input('\n(Press enter to continue)')
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('\tAt the beginning of the game, you will be able to make a character with a name and a')
        print("\tclass. Your character will be given stats based on the class, start with 5 coins in your")
        print("\tbalance, and 5 chances that will be explained later.")
        input('\n(Press enter to continue)')
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\tYour character's class will determine the goal you are trying to reach to win the game.")
        print("\tThere are currently two classes in the game: (1) Attacker and (2) Defender. Each class ")
        print("\twill give you a stat boost for Fight or Armor, respectively.")
        input('\n(Press enter to continue)')
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\tHere is the structure of how most turns go: the number of the turns will be printed, along")
        print("\twith your stats. Then, the Environment's action will be printed along with a couple of")
        print("\tprompts. You can enter (c) to equip items before the turn continues. You can take a chance")
        print("\tto challenge a card to get the benefits of the second Environment action: if you lose")
        print("\tonly the first action happens and you lose a chance; if you win, the second action will")
        print("\tgo into effect and you keep your chance. Once you are out of chances, you cannot make any more.")
        print("\tWhether or not you win or lose is based on your stats versus the hidden stats for the card.\n")
        print("--------------------------- Turn 1 ---------------------------\t<--- Turn counter")
        print("Balance: " + str(player.getBalance()) + "\tFight Stat: " + str(player.getFightStat()) + "\tArmor Stat: " + str(player.getArmorStat()) + "\tChances: " + str(player.getNumbLives()) + "\t<--- Your stats\n")
        print(DECK[2].getCardName(), "\t<--- The main effect that will happen no matter what")
        print(DECK[2].getFlavorText(), "\t<--- The secondary effect that can happen if you win the challenge")
        print(f"\nPress c to equip items.\nYour current Fight stat is {player.getFightStat()}.\t<--- Your stat that is used to challenge the card\n\nWould you like to take a chance and challenge this card?\nYou have {player.getNumbLives()} chances left to take (y/n/c): \t<--- Where you will input")
        input('\n(Press enter to continue)')
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\tYou may also come across ites that you automatically pick up. You will have the option of")
        print("\tequiping it right then or later by pressing (c) at any turn.")
        print("--------------------------- Turn 2 ---------------------------")
        print("Balance: " + str(player.getBalance()) + "\tFight Stat: " + str(player.getFightStat()) + "\tArmor Stat: " + str(player.getArmorStat()) + "\tChances: " + str(player.getNumbLives()) + "\n")
        print(DECK[15].getCardName(), "\t<--- The type of item")
        print(DECK[15].getFlavorText(), "\t<--- How much it raises your stats")
        player.addCard(DECK[15])
        print("The card was added to your hand.")
        print("\n\tYour Inventory:")
        counter = 1
        for card in player.getHand():
            text = str(card.printItemCard())
            print("\t\t" + str(counter) + ".\t" + text)
            counter += 1
        print("\t---- Would you like to use any of these cards? (y/n): y\t<--- If you want to equip any cards")
        print("\t---- Which card would you like to use (1 - " + str(len(player.getHand())) + "): \t\t<--- Your input using numbers")
        input('\n(Press enter to continue)')
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\tThe final thing you will come across is the Shop, where you can buy and sell itmes. You")
        print("\tcan unequip any items to sell them by going to the (c) option in the Shop. Items that are")
        print("\tnot equiped will show up in the Sell (s) menu, and new items will be shown in the Buy (b)")
        print("\tmenu. You can leave the shop from the main menu by pressing Leave (l). Just as before, you")
        print("\twill be able to select items to unequip, buy, or sell using numbers.\n")
        print("--------------------------- Turn 3 ---------------------------\n")
        print("\n--- Welcome to the Shop!---\n")
        print("--- Current Balance:", player.getBalance(), "\t<--- Your current balance\n")
        print("--- Would you like to Buy (b), Sell (s), Check Equiped (c), or Leave (l)?: b\t<--- things to do in the shop")
        printNumb = ""
        for i in range(0, 3): #Print cards
                print(f"{i+1}: {SHOPDECK[random.randrange(0,6)].printBuyCard()}")
                printNumb = printNumb + str(i+1) + ","
        print(f"--- What would you like to buy (n for none)? ({printNumb} n): \t<--- choose a card to buy")
        input('\n(Press enter to continue)')
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\tTwo more things: there is a secret counter that is ticking down behind the scenes. Once")
        print("\tit reaches 0, you will have 10 more turns to complete your class goal, so don't slack")
        print("\toff! you never know when the game will end until it is just about to end.")
        print("\tAnd finally, DON'T GO BANKRUPT!")
        input('\n(Press enter to continue)')


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
            return Player.Player(name, 2, 1, 5, [], 0, 5, [])
        elif classChoice == "2": #If Defender Chosen
            return Player.Player(name, 1, 2, 5, [], 1, 5, [])

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
                print(f"--- {i+1}: {playerHand[i].printSellCard()}")
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
FUNCTION: checkEquiped()
PARAMETERS: Player Object
RETURN: Player object
PURPOSE: - Prompt player with all cards that are equiped and number them
         - Player will select card to uneqiip by number
         - Update hand and remove card from Equiped
         - If no cards equiped, state that you have nothing on
"""
def checkEquiped(player):
    playerEquip = player.getEquiped() #Get player's equiped cards
    equipSize = len(playerEquip)
    userInput = 'y'
    if equipSize > 0: #If the player has cards equiped
        while userInput != 'n' and equipSize != 0:
            #print("--- Current Balance:", player.getBalance())
            printNumb = ""
            for i in range(0, equipSize): #Print cards
                print(f"--- {i+1}: {playerEquip[i].printSellCard()}")
                printNumb = printNumb + str(i+1) + ","
            
            userInput = input(f"--- What would you like to unequip (n for none)? ({printNumb} n): ").strip() #Get input

            if userInput.isnumeric(): #if number
                userInput = int(userInput) #turn into int from string
                if userInput <= equipSize and userInput > 0: #if selected number in in range
                    #player.setBalance(player.getBalance() + playerHand[userInput-1].getChallengeEffect())#Add card value to balance
                    print("---You have unequiped", playerEquip[userInput-1].getCardName())
                    player.addCard(playerEquip[userInput-1]) #add equiped card to hand
                    player.removeEquip(playerEquip[userInput-1])#remove card from equiped
                    #playerHand = player.getHand()#Remove Card from local variable
                    equipSize = len(playerEquip) #decrement hand size
                else:
                    print("--- Incorrect Input.")
            else:
                print("--- Incorrect Input.")

    else: #If the player has no more cards
        print("--- You don't have anything to unequip!")
    
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

    while buySell != 'l': #Exit loop when Player want to leave shops
        print("--- Current Balance:", player.getBalance())
        buySell = input("--- Would you like to Buy (b), Sell (s), Check Equiped (c), or Leave (l)?: ").strip() #Prompt input
        
        if buySell == 'b': #If Player wants to buy
            player, numbCards, inShop = buy(player, numbCards, buySell, inShop)
                    
        elif buySell == 's': #If Player wants to sell
            player = sell(player, buySell)
        
        elif buySell == 'c':
            player = checkEquiped(player)
        
        elif buySell != 'l': #If improper input
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

    choice = 'c' #default value for check inventory while loops

    print("Main Effect:",card.getCardName())
    print("Challenge Effect:",card.getFlavorText())

    if player.getNumbLives() > 0: #if the player can make a challenge

        if card.getCardType() == 0: #Fight Card
            
            while choice == 'c': #to repeat loop if check inventory is chosen
                choice = input(f"\nPress c to equip items.\nYour current Fight stat is {player.getFightStat()}.\n\nWould you like to take a chance and challenge this card?\nYou have {player.getNumbLives()} chances left to take (y/n/c): ")

                if choice == 'c':
                    phaseThree(player)

                    print(card.getCardName())
                    print(card.getFlavorText())

                elif choice == 'y':
                    if(player.getFightStat() > card.getFightStat()): #if Player is stronger
                        print("\nVERDICT: You win the challenge! Bonus activated.\n")
                        player.setBalance(player.getBalance() + card.getChallengeEffect())

                    else:
                        print("\nVERDICT: You were not strong enough to win the challenge. You lose 1 chance.\n")
                        player.setBalance(player.getBalance() + card.getEffect())
                        player.setNumbLives(player.getNumbLives() - 1)
                else: #if no challenge made
                    player.setBalance(player.getBalance() + card.getEffect())

        elif card.getCardType() == 1: #Armor Card
            
            while choice == 'c': #to repeat loop if check inventory is chosen

                choice = input(f"\nPress c to equip items.\nYour current Armor stat is {player.getArmorStat()}.\n\nWould you like to take a chance and challenge this card?\nYou have {player.getNumbLives()} chances left to take (y/n/c): ")

                if choice == 'c':
                    phaseThree(player)
                    print(card.getCardName())
                    print(card.getFlavorText())
                elif choice == 'y':
                    if(player.getArmorStat() > card.getArmorStat()): #if Player is stronger
                        print("\nVERDICT: You win the challenge! Bonus activated.\n")
                        player.setBalance(player.getBalance() + card.getChallengeEffect())

                    else:
                        print("\nVERDICT: You were not strong enough to win the challenge. You lose 1 chance.\n")
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
def phaseOne(a, b, deck):

    if a.getBalance() < 0: #if the Player goes bankrupt, return a haunt of 12 to end the game early
        return 12

    pick = deck[random.randrange(0, len(deck), 1)]
    
    if pick.getCardType() == 0 or pick.getCardType() == 1: #if coin card, check haunt and offer challenge(Phase 2) and update stats

        if pick.getHaunt() > 0: #if there is a Haunt value to the card
            b += pick.getHaunt()

        a = phaseTwo(a, pick)

    elif pick.getCardType() == 2: #if shop card, enter shop
        a = enterShop(a)

    elif pick.getCardType() == 3: #if item card, print text, and add to hand
        print(pick.getCardName())
        print(pick.getFlavorText())
        print("The card was added to your hand.")

        a.addCard(pick)

        phaseThree(a)

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

    if len(currentHand) == 0:
        print("\nYou have no cards to equip!\n")

    while len(currentHand) != 0: #while there are still cards to equip
        print("\n\tYour Inventory:")
        for card in currentHand:
            text = str(card.printItemCard())
            print("\t\t" + str(counter) + ".\t" + text)
            counter += 1
        
        choice = input("\t---- Would you like to use any of these cards? (y/n): ")
        if choice == 'y':
            while choice.isalpha(): #dummy-proof myself lmao
                choice = input("\t---- Which card would you like to use (1 - " + str(len(currentHand)) + "): ").strip()
            a.addEquip(currentHand[int(choice)-1])
            #a.setFightStat((a.getFightStat() + currentHand[int(choice)-1].getFightStat()))
            #a.setArmorStat((a.getArmorStat() + currentHand[int(choice)-1].getArmorStat()))
            currentHand.remove(currentHand[int(choice)-1])
            a.setHand(currentHand)
        else:
            break #stop prompting for cards

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
    if(player.getFightStat() > 5 or player.getArmorStat() > 5):
        haunt = phaseOne(player, haunt, DECK)
    else:
        haunt = phaseOne(player, haunt, DECKTWO)
    #phaseThree(player)
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

    tutorial()
    print("\nWELCOME TO THE GAME!\n")

    player = makePlayer()
    counter = 0
    haunt = 0

    #print()
    #print(player.getName(), "the", CLASSES[player.getClass()][0])
    #print("Balance: " + str(player.getBalance()) + "\tFight Stat: " + str(player.getFightStat()) + "\tArmor Stat: " + str(player.getArmorStat()) + "\tChances: " + str(player.getNumbLives()))
    print()

    while haunt != 10:
        counter += 1
        print("--------------------------- Turn", counter, "---------------------------")
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
            print('          _,-"""`-._')
            print("(,-.`._,'(       |\`-/|")
            print("    `-.-' \ )-`( , o o)")
            print("          `-    \`_`w'-")
            print("You have acheived your goal! You won the game!")
            print()
        else:
            print()
            print('      |\      _,,,---,,_')
            print("     /,`.-'`'    -.  ;-;;,_")
            print("    |,4-  ) )-,_. ,\ (  `'-'")
            print("    '---''(_/--'  `-'\_) ")
            print("You have not acheived your goal. Better luck next time!")
            print()


        print("Thanks for Playing!!!")
        print(player.getName(), "the", CLASSES[player.getClass()][0], "'s Final Stats:")
        print("Balance: " + str(player.getBalance()) + "\tFight Stat: " + str(player.getFightStat()) + "\tArmor Stat: " + str(player.getArmorStat()) + "\tChances: " + str(player.getNumbLives()))
        

if __name__ == "__main__":
    #enterShop(Player.Player("Kate", 3, 0, 100, [Card.Card("Armor", 2, 0, 1, "Plus 1 Armor Stat", 7, 5, 0), Card.Card("Sword", 2, 1, 0, "Plus 1 Fight Stat", 7, 5, 0)], 0))
    main()