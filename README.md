# MyDabloons-Gameplay-Prototype
This is the GitHub repository that will track the development of the gameplay prototype for the card game implementation of the game concept "My Dabloons!" Currently, the game is being developed as the final project for Manhattan College's COMM 365 - Game Design and Development course. This game is in early alpha.

ASCII Cat art by Joan Stark from The ASCII Art Archive: https://www.asciiart.eu/animals/cats

## VERSION a1.3.0

### FEATURES:
    - Deck of cards
    - Main gameplay loop
    - "Haunt" Mechanic: After the "Haunt" counter reaches 10 the game will end in 10 turns
    - Shop to buy *and sell* items
    - Go bankrupt to end the game early
    
### So why Python?
Python was chosen simply because it is a language that I am currently learning this semester as a Computer Science elective course for my undergraduate degree. This prototype is also not meant to be directly translated into another digital format at this time, so choosing another language that I know such as C++ or Java was not put into consideration.

## Changelog for Version a1.3.0
    - Added private variable charClass
    - Added setter and getter for charClass
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
