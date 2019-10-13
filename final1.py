import playingalgo1
import try1
#from keras.preprocessing.image import img_to_array
from keras.models import load_model
#import numpy as np
import argparse
#import imutils
import pickle
#import cv2

#python3 final1.py --model pokedex.model --labelbin lb.pickle

def convert_strtocard(card):
    l = card.split("-")
    return playingalgo1.Card(l[1], l[0])
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained model model")
ap.add_argument("-l", "--labelbin", required=True,
	help="path to label binarizer")
#ap.add_argument("-i", "--image", required=True,
#	help="path to input image")
args = vars(ap.parse_args())

# load the trained convolutional neural network and the label
# binarizer
print("[INFO] loading network...")
model = load_model(args["model"])
lb = pickle.loads(open(args["labelbin"], "rb").read())

for i in range(7):
    card = try1.recognise(model,lb)
    print(i)
    playingalgo1.hand.append(convert_strtocard(card))
    
playingalgo1.deck = convert_strtocard(try1.recognise(model, lb))

first = 1 #tells whether it teh firats or not

while True:
    if playingalgo1.deck.getColor()=="black" or playingalgo1.deck.getNumber()=="+2" or playingalgo1.deck.getNumber()=="+4":
        print("pick another starting card")
        playingalgo1.deck = convert_strtocard(try1.recognise(model, lb))
    else:
        break

playingalgo1.pd= True
while True:
    if len(playingalgo1.hand)==0:
        print("Computer won")
        try1.print_image("won-C")
        break
    if len(playingalgo1.hand)==1 :
        print("UNO")
        try1.print_image("UNO-C")       
    print(playingalgo1.deck.getColor())
    print(playingalgo1.deck.getNumber())
    print("************")
    print(playingalgo1.pd," ",len(playingalgo1.hand))
    print("*********")
    if playingalgo1.check_pre() or playingalgo1.pd :
        ans = input("Do you want to play? Y/N")
        if ans == "Y" or ans=="y":
            card = try1.recognise(model, lb)
            x = convert_strtocard(card)
            forward= "n" 
            while True :
                print("is your card", x.getNumber() , "of" , x.getColor(),"?")
                forward = input("y/n")
                if forward=="y" or forward=="Y":
                    first = 1 #
                    print("card registered")
                    break
                else :
                    card = try1.recognise(model, lb)
                    x = convert_strtocard(card)
        elif ans == "N" or ans=="n":
            if first == 1:
                first = 0
                print("Pick a card")
                playingalgo1.num_opp_card+=1
                continue
            else:
                first = 1      
            x = "pass"
        else :
            print("Unknown Input")
            continue
        playingalgo1.check_opp_card(x)
        if playingalgo1.num_opp_card == 0 :
            print("User won")
            try1.print_image("won-U")
            break
        print("out of opp")
    else:
        playingalgo1.pd=True
    print("fin")
    card = playingalgo1.play_card(model, lb)
    if card == "pass-C" or card == "skip-C" :
        try1.print_image(card)
    else:
        try1.print_image(card.getColor()+"-"+card.getNumber())









 
