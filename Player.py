"""
Katherine Uffer
March 26, 2023

GAME TITLE: My Dabloons!
VERSION a1.0.1

Player Class

FEATURES:
    - Name
    - Fight Stat
    - Armor Stat
    - Coin Balance
    - Card Hand

CHANGELOG:
    - Added Name private variable
    - Added Fight Stat private variable
    - Added Armor Stat private variable
    - Added Balance private variable
    - Added Hand private variable
    - Added constructor function
    - Added getters for all private variables
    - Added setters for fightStat, ArmorStat, balance, and hand
    - Added removeCard function to remove a card from the hand
    - Added addCard function to add card to the hand

"""
class Player:
    def __init__(self, a, b, c, d, e):
        self.__name = a #string
        self.__fightStat = b #int
        self.__armorStat = c #int
        self.__balance = d #int
        self.__hand = e #list

    def removeCard(self, a):
        self.__hand.remove(a)

    def addCard(self, a):
        self.__hand.append(a)

    def setFightStat(self, a):
        self.__fightStat = a

    def setArmorStat(self, a):
        self.__armorStat = a

    def setBalance(self, a):
        self.__balance = a

    def setHand(self, a):
        self.__hand = a

    def getName(self):
        return self.__name
    
    def getFightStat(self):
        return self.__fightStat
    
    def getArmorStat(self):
        return self.__armorStat
    
    def getBalance(self):
        return self.__balance
    
    def getHand(self):
        return self.__hand