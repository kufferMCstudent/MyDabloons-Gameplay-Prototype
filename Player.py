"""
Katherine Uffer
April 15, 2023

GAME TITLE: My Dabloons!
VERSION a1.3.0

Player Class

FEATURES:
    - Name
    - Fight Stat
    - Armor Stat
    - Coin Balance
    - Card Hand
    - Class

CHANGELOG:
    - Added private variable charClass
    - Added setter and getter for charClass

"""
class Player:
    def __init__(self, a, b, c, d, e, f):
        self.__name = a #string
        self.__fightStat = b #int
        self.__armorStat = c #int
        self.__balance = d #int
        self.__hand = e #list
        self.__charClass = f #int, 0 = Attacker, 1 = Defender

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

    def setClass(self, a):
        self.__charClass = a

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
    
    def getClass(self):
        return self.__charClass