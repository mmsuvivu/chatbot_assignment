
from random import randrange


state = "neutral"
stateArray = ["neutral", "happy", "angry", "sad"]

while 1 == 1:
    if(state == "neutral"):
        answer = input("Say something:") #I am asking the user to say something
        if( "hi" in answer or "hello" in answer or "hey" in answer):
             print("Hi")
        if("hello" in answer):
                print("Hey brov")
        if("no" in answer):
              print("yes")
        if("yes" in answer):
                print("no")
        if("are you alive" in answer):
                print("yes i am alive")
        

    elif(state == "happy"):
        answer = input("Say something, my friend:")
        if("hi" in answer):
             print("Hi")
        if("hello" in answer):
                print("Hey brov")
        if("no" in answer):
              print("yes")
        if("yes" in answer):
                print("no")
        if("are you alive" in answer):
                print("yes i am alive")
        if("turn off" in answer):
            print("Turning off")

    elif(state == "angry"):
        answer = input("Say something, stupid:")
        if("hi" in answer):
             print("Go away")
        if("hello" in answer):
                print("Hey brov")
        if("no" in answer):
              print("yes")
        if("yes" in answer):
                print("no")
        if("are you alive" in answer):
                print("yes i am alive")
        if("turn off" in answer):
            print("Turning off")

    state = stateArray[int(randrange(3))]

#This is a comment