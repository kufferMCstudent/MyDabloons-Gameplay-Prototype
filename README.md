# MyDabloons-Gameplay-Prototype
This is the GitHub repository that will track the development of the gameplay prototype for the card game implementation of the game concept "My Dabloons!" Currently, the game is being developed as the final project for Manhattan College's COMM 365 - Game Design and Development course. This game is in early alpha.

ASCII Cat art by Joan Stark from The ASCII Art Archive: https://www.asciiart.eu/animals/cats

## VERSION a1.3.2

### FEATURES:
    - Deck of cards
    - Main gameplay loop
    - "Haunt" Mechanic: After the "Haunt" counter reaches 10 the game will end in 10 turns
    - Shop to buy and sell items
    - Go bankrupt to end the game early
    - Limited number of chances to gain card bonuses
    - Class-Specific end-game goal
    
### So why Python?
Python was chosen simply because it is a language that I am currently learning this semester as a Computer Science elective course for my undergraduate degree. This prototype is also not meant to be directly translated into another digital format at this time, so choosing another language that I know such as C++ or Java was not put into consideration.

## Changelog for Version a1.3.2
    - Added goalReached() to determine if Player has reached class goal
    - Changed printout order in gameplayLoop() to make stats per turn more clear
    - Added cladd goal check at end of main()
    - Changed makePlayer() to get values from different variables and print starting stats and goals
    - Changed CLASSES list to match makePlayer() goals
