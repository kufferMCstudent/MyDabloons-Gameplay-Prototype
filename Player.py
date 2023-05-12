"""
Katherine Uffer
April 25, 2023

GAME TITLE: My Dabloons!
VERSION a1.4.0

Player Class

FEATURES:
    - Name
    - Fight Stat
    - Armor Stat
    - Coin Balance
    - Card Hand
    - Equiped Items
    - Class
    - Lives

CHANGELOG:
    - Added addEquip, removeEquip, getEquiped, setEquiped
    - Changed getFightStat and getArmorStat to now parse through equiped cards

"""
class Player:
    def __init__(self, a, b, c, d, e, f, g, h):
        self.__name = a #string
        self.__fightStat = b #int
        self.__armorStat = c #int
        self.__balance = d #int
        self.__hand = e #list
        self.__charClass = f #int, 0 = Attacker, 1 = Defender
        self.__numbLives = g
        self.__equipedCards = h #list

    def removeCard(self, a):
        self.__hand.remove(a)

    def addCard(self, a):
        self.__hand.append(a)

    def addEquip(self, a):
        self.__equipedCards.append(a)
    
    def removeEquip(self, a):
        self.__equipedCards.remove(a)

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

    def setNumbLives(self, a):
        self.__numbLives = a

    def setEquiped(self, a):
        self.__equipedCards = a

    def getName(self):
        return self.__name
    
    def getFightStat(self):
        itemFight = 0
        for i in range(len(self.__equipedCards)):
            itemFight += self.__equipedCards[i].getFightStat()
        return self.__fightStat + itemFight
    
    def getArmorStat(self):
        itemArmor = 0
        for i in range(len(self.__equipedCards)):
            itemArmor += self.__equipedCards[i].getArmorStat()
        return self.__armorStat + itemArmor
    
    def getBalance(self):
        return self.__balance
    
    def getHand(self):
        return self.__hand
    
    def getEquiped(self):
        return self.__equipedCards
    
    def getClass(self):
        return self.__charClass
    
    def getNumbLives(self):
        return self.__numbLives

    def goalReached(self):
        if self.__charClass == 0: #Attacker
            return self.__fightStat >= 10
        elif self.__charClass == 1: #Defender
            return self.__armorStat >= 10