from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


def trainBot():
    my_bot = ChatBot(name='PyBot', read_only=True,
                    logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                    'chatterbot.logic.BestMatch'])

    talks = []
    small_talk = ['hi there!',
                'hi!',
                'how do you do?',
                'how are you?',
                'i\'m cool.',
                'fine, you?',
                'always cool.',
                'i\'m ok',
                'glad to hear that.',
                'i\'m fine',
                'glad to hear that.',
                'i feel awesome',
                'excellent, glad to hear that.',
                'not so good',
                'sorry to hear that.',
                'what\'s your name?',
                'i\'m mathbot. ask me a math question, please.']

    farewell_talk = ['bye',
                    'goodbye! you did so well!',
                    'adios',
                    'you have improved so much!',
                    'end',
                    'i hope this was helpful!',
                    'This was great!',
                    'hope to see you soon!',
                    ]
                
    math_talk_1 = ['pythagorean theorem',
                'a squared plus b squared equals c squared.']

    math_talk_2 = ['law of cosines',
                'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']

    math_talk_3 = ['All identities',
                'sin(a +/- b) = sin(a) * cos(b) +/- cos(a) * sin(b); cos(a +/- b) = cos(a) * sin(b) -/+ sin(a) * sin(b); tan(a +/- b) = (tan(a) +/- tan(b))/(1 -/+ tan(a) * tan(b))']

    math_talk_4 = ['Sin Identity', 
    'sin(a +/- b) = sin(a) * cos(b) +/- cos(a) * sin(b)']

    math_talk_5 = ['Cosin Identity',
        'cos(a +/- b) = cos(a) * sin(b) -/+ sin(a) * sin(b)']
    
    math_talk_6 = ['Tan Identity'
                'tan(a +/- b) = (tan(a) +/- tan(b))/(1 -/+ tan(a) * tan(b))']
                
    talks.extend((small_talk, math_talk_1, math_talk_2, math_talk_3, math_talk_4, math_talk_5, math_talk_6, farewell_talk))
    list_trainer = ListTrainer(my_bot)
    for item in talks:
        list_trainer.train(item)
    return my_bot 

if __name__ == "__main__":
    my_bot = trainBot()
    inputString = input("Hi I'm MathBot! Ask me a math question. I can do basic arithemtic and give you some cool theorems and laws!")
    while inputString != "exit":
        print(my_bot.get_response(inputString))
        inputString = input("What else would you like me to do?")

    print("I had a great time! Run me again for some more dope math.")
        

