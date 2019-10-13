#import array as arr
#from enum import Enum
import random
import try1
#import final1

class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value
    def getColor(self):
        return self.color
    def getNumber(self):
        return self.value
    
hand = []
pd = True
first = 1
##ohand=[]

def rec_card(model, lb):
    opp_card = try1.recognise(model, lb)
    l = opp_card.split("-")
    return Card(l[1], l[0])

deck = 0

#for testing purpose

def power(s): #s is a card object
    a=s.getNumber()
    return (a=="+4" or a=="+2" or a=="skip") 

def best(data):
    for i in data:
        if i.getNumber()=="+2" or i.getNumber()=="skip" or i.getNumber()=="+4":
            return i
    return data[0]

def play_card(model, lb):
    sameNum = []
    sameColor = []
    sameBoth = []
    blacks = []
    
    global deck
    global hand
    global pd
    global first
    
    if deck.getNumber()=="skip" and not(pd) :
        pd=True
        return "skip-C"
    elif deck.getNumber()=="+2" and not(pd):
        pd=True
        print("picking 1")
        hand.append(rec_card(model, lb))
        print("picking 2")
        hand.append(rec_card(model, lb))
        return "skip-C"
    elif deck.getNumber()=="+4" and not(pd) :
        pd=True
        for i in range(4):
            print("picking",i)
            hand.append(rec_card(model, lb))
        return "skip-C"
    
    for i in hand:
    
        if i.getColor()==deck.getColor():
            if i.getNumber()==deck.getNumber():
                sameBoth.append(i)
            else:
                sameColor.append(i)
        elif i.getNumber()==deck.getNumber():
            sameNum.append(i)
        elif i.getColor()=="black":
            blacks.append(i)
    #print(len(sameNum))
#    print(sameNum)
#    print(sameColor)
#    print(sameBoth)
#    print(blacks)
    if len(sameNum)<len(sameColor):
        if len(sameNum)!=0:
            deck = best(sameNum)
            first = 1
            hand.remove(deck)
            pd=not(power(deck))
            return deck
        else:
            deck = best(sameColor)
            first = 1
            hand.remove(deck)
            pd=not(power(deck))
            return deck
    elif len(sameColor)!=0:
        deck = best(sameColor)
        first = 1
        hand.remove(deck)
        pd=not(power(deck))
        return deck
    elif len(sameNum)!=0:
        deck = best(sameNum)
        first = 1
        hand.remove(deck)
        pd=not(power(deck))
        return deck
    elif len(sameBoth)!=0:
        deck = best(sameBoth)
        first = 1
        hand.remove(deck)
        pd=not(power(deck))
        return deck
    elif len(blacks)!=0:
        deck = best(blacks)
        first = 1
        hand.remove(deck)
        pd=not(power(deck))
        deck = Card(chooseColor(hand), deck.getNumber())
        return deck 
        #print(deck.getNumber())    
    else:
        if first == 1:
            hand.append(rec_card(model, lb))
            first = 0
            return play_card(model, lb)
        else:
            first = 1
            print("computer passed",end=" ")
            return "pass-C"
        #hand.append(rec_card(model, lb))

def draw_card():
    colors = ["red", "red", "blue", "blue", "yellow", "yellow", "green", "green", "black"]
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "skip", "reverse", "+2"]
    nums2 = ["+4", "10"]
    x = random.choice(colors)
    if x == "black":
        y = random.choice(nums2)
    else:
        y = random.choice(nums)
    random.shuffle(colors)
    random.shuffle(nums2)
    random.shuffle(nums)
    return Card(x, y)

#for x in range(7):
#    hand.append(draw_card())
#    ohand.append(draw_card())

def chooseColor(hand):
    numColors = {}
    for i in hand:
        if i.getColor() in numColors:
            numColors[i.getColor()]+=1
        elif not(i.getColor()=="black"):
            #i love you shreya 
            numColors[i.getColor()]=1
    num = max(numColors.values())
    for i in numColors:
        if numColors[i]==num:
            return i
    
num_opp_card = 7    

def check_opp_card(opp_card) : #tell if a card has been played
    global deck
    global num_opp_card
    global pd
    #global ohand
    
    if opp_card == "pass":
        #print("Pick a card")
        #num_opp_card += 1
        print("user passed")
        return 
        #ohand.append(draw_card())
    elif opp_card.color == "black" :
        u = input("new color: ")
        deck = Card(u, opp_card.getNumber())
        num_opp_card-= 1
        pd=not(power(deck))
        #ohand.remove(opp_card)
        print("User played :")
        print(opp_card.color + " " + opp_card.value)
    elif deck.color == opp_card.color or deck.value == opp_card.value :
        deck = opp_card
        num_opp_card -= 1
        pd=not(power(deck))
        #ohand.remove(opp_card)
        print("User played :")
        print(opp_card.color + " " + opp_card.value)
    else: 
        print("wrong card")
        


def check_pre():
    global num_opp_card
    if deck.getNumber() == "skip":
        return False
    elif deck.getNumber() == "+2":
        print("pick 2 cards")
        num_opp_card += 2
        return False
    elif deck.getNumber() == "+4" :
        print("pick 4 cards")
        num_opp_card += 4
        return False
    else:
        return True
        
    

#while True:    
#    play_card()
#   
#    if len(hand) == 0:
#        print("Computer wins")
#        break
#    if check_pre() == True :
#        a = input("pass(y/n): ")
#        if a == "yes" or a== "y" :
#            check_opp_card("pass")
#        else:
#            p = input("color you want to play: ")
#            q = input("color you want to play: ")
#            opp_card = Card(p, q)
#            check_opp_card(opp_card)
#    if len(ohand) == 0:
#        print("User wins")
#        break
    

#to-do - write a check pre in case user is skipped draw4 or draw2 
# write what exactly to do in wrong card whether to give opponent second chacne or draw
        
    
    

    
        
            
    
