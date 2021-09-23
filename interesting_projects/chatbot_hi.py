import nltk
from nltk.chat.util import Chat, reflections

# reflections
"""
The other import you did above was Reflections,
which is a dictionary that contains a set of input text and its corresponding output values
"""
# to see reflection contains uncomment below code
"""
for i,k in enumerate(reflections):
    print(i,k)
"""
# TODO 1.First step is creating a rules that will be used to train the chatbot
# The lines of code below create a simple set of rules. The first element of the list is the user input, whereas the second element is the response from the bot
set_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you doing today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["You can call me a chatbot ?",]
    ],
    [
        r"how are you ?",
        ["I am fine, thank you! How can i help you?",]
    ],
    [
        r"I am fine, thank you",
        ["great to hear that, how can i help you?",]
    ],
    [
        r"how can i help you? ",
        ["i am looking for online guides and courses to learn data science, can you suggest?", "i am looking for data science training platforms",]
    ],
    [
        r"i'm (.*) doing good",
        ["That's great to hear","How can i help you?:)",]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Pluralsight is a great option to learn data science. You can check their website",]
    ],
    [
        r"thanks for the suggestion. do they have great authors and instructors?",
        ["Yes, they have the world class best authors, that is their strength;)",]
    ],
    [
        r"(.*) thank you so much, that was helpful",
        ["Iam happy to help", "No problem, you're welcome",]
    ],
    [
        r"quit",
    ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]

# After creating the pairs of rules above, we define the chatbot using the code below
# this is starter message for chatbot.
def chatbot():
    print("Hi BOSS, I'm the Chat Bot")
chatbot()


# TODO 2.The next step is to instantiate the Chat() function containing the pairs and reflections.
chat = Chat(set_pairs, reflections)

chat.converse()
if __name__ == "__main__":
    chatbot()
