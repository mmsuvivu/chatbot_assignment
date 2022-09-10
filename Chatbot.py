
from random import randrange
import random
#current state
state = "neutral"
#array of possible arrays
stateArray = ["neutral", "happy", "angry", "sad"]

# These are greetings the chatbot can use when it's in a neutral state
neutralGreetings = ["Hello. ", "Hi. ", "Nice to meet you. ", "Hey. "]
neutralQuestions = ["How are you?", "How are you feeling?", "How is your day?"]

# These are feelings the user can have if they are in a good mood
goodUserAnswers = ["Good", "Well", "Fine", "Not bad", "Ok"]

# These are feelings the user can have if they are in a sad mood
sadUserAnswers = ["Horrible", "Terrible", "Bad", "Sad"]

# These are feelings the user can have if they are in an angry mood
angryUserAnswers = ["Why do you care?", "Shut up", "I'm not going to tell you", "You're dumb"]

# Happy reactions the user may have to a happy chatbot
happyUserReaction = ["That's nice!", "That makes me happy too!", "That is good", "thats nice"]

# Angry reactions the user may have to a happy chatbot
angryUserReaction = ["I don't care", "Why should I care?", "dumb robots can't have feelings", "You suck", "I don't like you"]

# Apologetic reatcion the user may have
apologeticReaction = ["I'm sorry", "I apologize", "Sorry for being rude", "My bad", "Excuse me please", "sorry"]

# Random angry Reactions the bot may have to an angry User
angryBotReactionArray = ["F you. ", "Go away. ", "Back off. ", "Apologise. ", "No. ", "I don't like you. ", "Log off. "]
angryBotGreetingArray = ["No need to be rude. ", "I'm angry now. ", "Why would you say that?! ", "I can't believe you said that. "]

# counter for how many angry reactions the bot gave
angerCounter = 0

# counter for how many sad reactions the bot gave
sadCounter = 0

#
sadBotGreetingArray = ["Why do you hate me? ", "I wanna be alone right now. ", "I feel like crying. ", "Please leave me alone. "]

while 1 == 1:
    if (state == "neutral"):
        answer = input("Greet the robot: ") #I am asking the user to say something
        if("hi" in answer or "hello" in answer or "hey" in answer):
            print(random.choice(neutralGreetings) + random.choice(neutralQuestions))

            answer = input()
            
            # if the user answers that they are good, the chatbot becomes happy
            for user_answer in goodUserAnswers:
                if user_answer.lower() in answer.lower():
                    print("That's nice to hear!")
                    state = "happy"
                    
        

            # if the user answers that they are not good, the chatbot becomes sad
            for user_answer in sadUserAnswers:
                if user_answer.lower() in answer.lower():
                        answer = input("Oh no! What's wrong? ")
                        state = "sad"
                        print("That's really sad! I think I am sad now too.")
                    

                # if the user answers in an angry way, the chatbot becomes angry
            for user_answer in angryUserAnswers:
                if user_answer.lower() in answer.lower():
                    print("There's no need to be rude.")
                    state = "angry"
        
        # TODO: replace these with better ones:
        elif("are you alive" in answer):
                print("yes i am alive")

        else:
                print("Sorry I don't understand")

        
#--------------------------------------------------------------------

    elif(state == "happy"):
        answer = input("I am happy now! ")
        while state == "happy":
                state = random.choice(stateArray)

        # if the user reaction is good the robot goes into a random mood
        for user_answer in happyUserReaction:
                if user_answer.lower() in answer.lower():
                    print("Thank you!")

        # if the user answers in an angry way, the chatbot becomes angry
        for user_answer in angryUserAnswers:
                if user_answer.lower() in answer.lower():
                    print("There's no need to be rude.")
                    state = "angry"
                    

        

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
                        
                        