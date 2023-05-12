# MyDabloons-Gameplay-Prototype
This is the GitHub repository that will track the development of the gameplay prototype for the card game implementation of the game concept "My Dabloons!" Currently, the game is being developed as the final project for Manhattan College's COMM 365 - Game Design and Development course. This game is in early alpha.

ASCII Cat art by Joan Stark from The ASCII Art Archive: https://www.asciiart.eu/animals/cats

## VERSION a1.4.0

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

## Changelog for Version a1.4.0
    - Added addEquip, removeEquip, getEquiped, setEquiped
    - Changed getFightStat and getArmorStat to now parse through equiped cards
    - Changed PhaseThree to implement new addEquip function
    - Changed the equip items prompt in PhaseThree to prompt until there are no more items/the user says no
    - Added checkEquiped() function to shop to allow for users to see which items they have equiped and to unequip them to sell
    - Changed game structure to that PhaseThree() is only called when the player wants to see their inventory during PhaseTwo before a challenge
    - Added another shop card to the deck to increase frequency
    - Added tutorial() so that new/returning users can see the game layout and changes
    - Sleepy cat for losing by Felix Lee
    - Added a second deck for challenges to become harder
    - Changed PhaseOne to call the original deck when the player has either stat below 5, and a new, more difficult deck when one of the player's stats is above 5
    - Added bits to printouts to make some things easier to see
