
from random import randrange
import random

state = "neutral"
stateArray = ["neutral", "happy", "angry", "sad"]

# These are greetings the chatbot can use when it's in a neutral state
neutralGreetings = ["Hello. ", "Hi. ", "Nice to meet you. ", "Hey. "]

# These are feelings the user can have if they are in a good mood
goodUserAnswers = ["Good", "Well", "Fine", "Not bad", "Ok"]

# These are feelings the user can have if they are in a sad mood
sadUserAnswers = ["Horrible", "Terrible", "Bad", "Sad"]

# These are feelings the user can have if they are in an angry mood
angryUserAnswers = ["Why do you care?", "Shut up", "I'm not going to tell you", "You're dumb"]

while 1 == 1:
    if (state == "neutral"):
        answer = input("Greet the robot:") #I am asking the user to say something
        if ("hi" or "hello" or "hey" in answer):
            print(random.choice(neutralGreetings) + "How are you?")
            answer = input()
            # if the user answers that they are good, the chatbot becomes happy
            for user_answer in goodUserAnswers:
                if user_answer.lower() in answer.lower():
                    print("That's nice to hear!")
                    state = "happy"
            # if the user answers that they are not good, the chatbot becomes sad
            for user_answer in sadUserAnswers:
                if user_answer.lower() in answer.lower():
                    print("Oh no! What's wrong?")
                    state = "sad"
                # if the user answers in an angry way, the chatbot becomes angry
            for user_answer in angryUserAnswers:
                if user_answer.lower() in answer.lower():
                    print("There's no need to be rude.")
                    state = "angry"
        # TODO: replace these with better ones:
        if("are you alive" in answer):
                print("yes i am alive")
        if("turn off" in answer):
            print("Turning off")


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

    # state = stateArray[int(randrange(3))]

#This is a comment