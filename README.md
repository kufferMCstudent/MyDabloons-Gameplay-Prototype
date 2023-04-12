# MyDabloons-Gameplay-Prototype
This is the GitHub repository that will track the development of the gameplay prototype for the card game implementation of the game concept "My Dabloons!" Currently, the game is being developed as the final project for Manhattan College's COMM 365 - Game Design and Development course. This game is in early alpha.

ASCII Cat art by Joan Stark from The ASCII Art Archive: https://www.asciiart.eu/animals/cats

## VERSION a1.2.0

### FEATURES:
    - Deck of cards
    - Main gameplay loop
    - "Haunt" Mechanic: After the "Haunt" counter reaches 10 the game will end in 10 turns
    - Shop to buy items
    
### So why Python?
Python was chosen simply because it is a language that I am currently learning this semester as a Computer Science elective course for my undergraduate degree. This prototype is also not meant to be directly translated into another digital format at this time, so choosing another language that I know such as C++ or Java was not put into consideration.

## Changelog for Version a1.2.0
    - Updated Armor and Sword cards in DECK with buy and sell values
    - Created SHOPDECK constant list to include exclusive shop cards
    - Added enterShop() and description
    - Added buy() and description
    - Modified Effect and Challenge Effect to double as Buy Price and Sell Price
    - Updated cardType value 1 to mean Shop
