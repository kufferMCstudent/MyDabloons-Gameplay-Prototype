"""
Katherine Uffer
April 15, 2023

GAME TITLE: My Dabloons!
VERSION a1.3.0

Card Class

FEATURES:
    - Name of Card
    - Type of Card
    - Fight Stat
    - Armor Stat
    - Flavor text
    - Effect/Buy Price
    - Challenge Effect/Sell Price
    - Haunt

CHANGELOG:
    - n/a

"""
class Card:
    def __init__(self, a, b, c, d, e, f, g, h):
        self.__cardName = a #string
        self.__cardType = b #int: 0 = Coin, 1 = Shop, 2 = Item
        self.__fightStat = c #int
        self.__armorStat = d #int
        self.__flavorText = e #string
        self.__effect = f #int
        self.__challengeEffect = g #int
        self.__haunt = h #int

    def getCardName(self):
        return self.__cardName
    
    def getCardType(self):
        return self.__cardType 
        
    def getFightStat(self):
        return self.__fightStat
    
    def getArmorStat(self):
        return self.__armorStat
    
    def getFlavorText(self):
        return self.__flavorText
    
    def getEffect(self):
        return self.__effect
    
    def getChallengeEffect(self):
        return self.__challengeEffect
    
    def getHaunt(self):
        return self.__haunt
    
    def printItemCard(self):
            temp = "Name: "
            temp = temp + self.__cardName + "\t"
            temp = temp + self.__flavorText + "\tFight: +"
            temp = temp + str(self.__fightStat) + "\tArmor: +" + str(self.__armorStat)
            return temp
    
    def printBuyCard(self):
            temp = "Name: "
            temp = temp + self.__cardName + "\t"
            temp = temp + self.__flavorText + "\tFight: +"
            temp = temp + str(self.__fightStat) + "\tArmor: +" + str(self.__armorStat)
            temp = temp + "\tPRICE:" + str(self.__effect)
            return temp
    
    def printSellCard(self):
            temp = "Name: "
            temp = temp + self.__cardName + "\t"
            temp = temp + self.__flavorText + "\tFight: +"
            temp = temp + str(self.__fightStat) + "\tArmor: +" + str(self.__armorStat)
            temp = temp + "\tVALUE:" + str(self.__challengeEffect)
            return temp