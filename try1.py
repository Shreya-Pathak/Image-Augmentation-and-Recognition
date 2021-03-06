# USAGE
# python classify.py --model pokedex.model --labelbin lb.pickle --image examples/charmander_counter.png

# import the necessary packages
#from keras import prepocessing
from keras.preprocessing.image import img_to_array
#from keras.models import load_model
import numpy as np
#import argparse
import imutils
#import pickle
import cv2
#import os

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-m", "--model", required=True,
#	help="path to trained model model")
#ap.add_argument("-l", "--labelbin", required=True,
#	help="path to label binarizer")
##ap.add_argument("-i", "--image", required=True,
##	help="path to input image")
#args = vars(ap.parse_args())

def recognise(model, lb):
    print("Taking picture")
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")
    
    img_counter = 0
    
    #url = "http://192.168.43.169:8080/shot.jpg"
    
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
    
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
            break
    
    cam.release()
    
    cv2.destroyAllWindows()
    
    # load the image
    image = cv2.imread(img_name)
    output = image.copy()
     
    # pre-process the image for classification
    image = cv2.resize(image, (96, 96))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
        
    # load the trained convolutional neural network and the label
    # binarizer
    #print("[INFO] loading network...")
    #model = load_model(args["model"])
    #lb = pickle.loads(open(args["labelbin"], "rb").read())
    
    # classify the input image
    print("[INFO] classifying image...")
    proba = model.predict(image)[0]
    idx = np.argmax(proba)
    label = lb.classes_[idx]
    
    # we'll mark our prediction as "correct" of the input image filename
    # contains the predicted label text (obviously this makes the
    # assumption that you have named your testing image files this way)
    #filename = args["image"][args["image"].rfind(os.path.sep) + 1:]
    #correct = "correct" if filename.rfind(label) != -1 else "incorrect"
    
    # build the label and draw the label on the image
    label1 = "{}: {:.2f}% ({})".format(label, proba[idx] * 100, "correct")
    output = imutils.resize(output, width=400)
    cv2.putText(output, label1, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
    	0.7, (0, 255, 0), 2)
    
    # show the output image
    print("[INFO] {}".format(label))
    #cv2.imshow("Output", output)
    #cv2.waitKey(0)
    return label

def print_image(color_num):
    
    l= color_num.split("-")
    if l[1] == "+4" or l[1] == "10":
        color_num = l[1]+"-black"
    else:
        color_num = l[1]+"-"+l[0]

    img = cv2.imread("./uno-dataset/"+color_num+"/"+color_num+".jpg",1)
   # img = imutils.resize(img, width=400)
    img = cv2.resize(img, (500,500))
    
    font                   = cv2.FONT_HERSHEY_TRIPLEX
    bottomLeftCornerOfText = (10,25)
    fontScale              = 1
    fontColor              = (0,255,0)
    lineType               = 2
    
    cv2.putText(img,'Press Enter', 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)
    
#    l = color_num.split("-")
    if l[1] == "+4" or l[1] == "10" :
        cv2.putText(img, "Color chosen is "+l[0], 
                    (10,250), 
                    font, 
                    fontScale,
                    fontColor,
                    lineType)
    elif l[0] == "skip" :
        cv2.putText(img, "Chance skipped",
                    (120,250),
                    font,
                    fontScale,
                    fontColor,
                    lineType)
    
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

