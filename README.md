# MyDabloons-Gameplay-Prototype
This is the GitHub repository that will track the development of the gameplay prototype for the card game implementation of the game concept "My Dabloons!" Currently, the game is being developed as the final project for Manhattan College's COMM 365 - Game Design and Development course. This game is in early alpha.

ASCII Cat art by Joan Stark from The ASCII Art Archive: https://www.asciiart.eu/animals/cats

## VERSION a1.1.0

### FEATURES:
    - Deck of cards
    - Main gameplay loop
    - "Haunt" Mechanic: After the "Haunt" counter reaches 10 the game will end in 10 turns
    
### So why Python?
Python was chosen simply because it is a language that I am currently learning this semester as a Computer Science elective course for my undergraduate degree. This prototype is also not meant to be directly translated into another digital format at this time, so choosing another language that I know such as C++ or Java was not put into consideration.

## Changelog for Version a1.1.0
    - Added Haunt value to main()
    - Changed gameplay while loop to call gameplayLoop() function instade of Phase1() and Phase3()
    - Changed while loop condition to go until haunt = 10
    - Added endgame while loop in main() where game will end in 10 turns
    - Added haunt variable parameter to Phase1()
    - Added positive Haunt value to 3 cards
    - Added end-game spash screen to show final stats
    - Added description of main() function
    - Added Haunt private variable
    - Added Haunt as a variable in constructor
    - Added getter for Haunt
