# MyDabloons-Gameplay-Prototype
This is the GitHub repository that will track the development of the gameplay prototype for the card game implementation of the game concept "My Dabloons!" Currently, the game is being developed as the final project for Manhattan College's COMM 365 - Game Design and Development course. This game is in early alpha.

ASCII Cat art by Joan Stark from The ASCII Art Archive: https://www.asciiart.eu/animals/cats

## VERSION a1.3.1

### FEATURES:
    - Deck of cards
    - Main gameplay loop
    - "Haunt" Mechanic: After the "Haunt" counter reaches 10 the game will end in 10 turns
    - Shop to buy and sell items
    - Go bankrupt to end the game early
    - Limited number of chances to gain card bonuses
    
### So why Python?
Python was chosen simply because it is a language that I am currently learning this semester as a Computer Science elective course for my undergraduate degree. This prototype is also not meant to be directly translated into another digital format at this time, so choosing another language that I know such as C++ or Java was not put into consideration.

## Changelog for Version a1.3.1
    - Added phaseTwo() function and moved code from phaseOne() to phaseTwo()
    - Added a limit to the number of challenges a Player can make in a game
    - Changed balancing of Fight and Armor for cards in deck and Class starting stats
    - Changed cardTypes to reflect changes in Card class
    - Added private variable numbLives
    - Added setter and getter for numbLives
    - Changed expected values for cardType to accomodate new phaseTwo() implementation
