
from random import randrange
import random
import BotAnswers
from BotQuestions import questions
from TriggerWords import greetings, insults, happyWords, sadWords, angryWords, apologeticWords
from BotAnswers import neutralGreetings, neutralQuestions, angryBotReactionArray

# Returns true if user answer was found in list
def find(answer, list):
    return any(item in answer.lower().strip() for item in list)


# current state
state = "neutral"

# list of all states
stateArray = ["neutral", "happy", "angry", "sad"]

# counter for how many angry reactions the bot gave
angerCounter = 0

# counter for how many sad reactions the bot gave
sadCounter = 0


print("You are now talking with a chatbot! Say hi!")
answer = input()  # I am asking the user to say something

# If the user insults the robot, the robot becomes angry
if find(answer, insults):
    print("What a rude way to start a conversation!")
    state = "angry"

# If the user greets the robot with a neutral or friendly way, the robot becomes happy
elif find(answer, greetings):
    print(random.choice(neutralGreetings) + random.choice(neutralQuestions))

# Otherwise the chatbot stays in a neutral state
else:
    print("Okayyy... Do you have any questions for me?")

while 1 == 1:
    answer = input()
    # if the user asks the chatbot to shut down the program shuts down
    if answer == "shut down":
        print("Okay, shutting down")
        break

    foundQuestion = False

    # if the user asks a question, the chatbot will answer it depending on the current state
    for key in questions:
        if key in answer:
            print(questions[key][state])
            foundQuestion = True
            break

    if foundQuestion:
        continue

    # if the user apologises when the chatbot is angry, it becomes neutral
    if state == "angry":
        if find(answer, apologeticWords):
            print("It's okay")
            state = "neutral"
        else:
            print(random.choice(angryBotReactionArray))
    # TODO: elif state == "sad" implement the sad counter system and print sad answers randomly
    else:
        if find(answer, angryWords):
            state = "angry"
            print(random.choice(angryBotReactionArray))
        elif find(answer, sadWords):
            state = "sad"
            print("Oh no") # TODO: This needs to be a list of different answers (just like random.choice(angryBotReactionArray))
        elif find(answer, happyWords):
            state = "happy"
            print("That's nice") # TODO: This needs to be a list of different answers (just like random.choice(angryBotReactionArray))
        else:
            state = "neutral"
            print("I don't understand") # TODO: This needs to be a list of different answers (just like random.choice(angryBotReactionArray))

    # TODO: when the code below this comment is implemented to the code above, this old code can be deleted
    """
    
    elif(state == "angry"):
        print(random.choice(angryBotGreetingArray))
        answer = input("Say something, stupid: ")

         # if the user reaction is good the robot goes into a random mood
        for user_answer in apologeticReaction:
                if user_answer.lower() in answer.lower():
                    print("It's okay")
                    while state == "angry":
                        state = random.choice(stateArray)
                        
                
                else:
                        while answer not in apologeticReaction:
                                answer = input(random.choice(angryBotReactionArray))
                                if answer in apologeticReaction:
                                        state = "neutral"
                                        
                                else:
                                     angerCounter = angerCounter + 1   
                                     if angerCounter == 2:
                                        state = "sad"
                                        
        


    elif(state == "sad"):
        answer = input(random.choice(sadBotGreetingArray) + " ") 
        for user_answer in apologeticReaction:
                if user_answer.lower() in answer.lower():
                        state = "happy"
                        print("Thank you for apologising")
        
        if state == "sad":
                sadCounter = sadCounter + 1
                if sadCounter == 3:
                        print("I have calmed down now")
                        while state == "sad":
                                state = random.choice(stateArray)
    """


