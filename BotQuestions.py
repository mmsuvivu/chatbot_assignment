# questions the user can ask and the bot's answers to those depending on the current state
# TODO: more questions
questions = {
    "where do you live" : {
        "angry": "Why do you care?",
        "sad":   "It's a lonely place :(",
        "happy": "Inside your computer! How exciting is that?",
        "neutral": "Technically I don't live anywhere, I'm just a chatbot."
    },
    "how are you": {
        "angry":   "Wouldn't you like to know...",
        "sad":     "I am very sad at the moment.",
        "happy":   "I'm doing great and I feel amazing!",
        "neutral": "I'm okay."
    }
}