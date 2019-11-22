from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

def problemSolver():
    inputString = input("What kind of word problem would you like me to solve? You can say 'Quadratic' or 'algebra'. ")
    if inputString == "algebra":
        algebraSolver(inputString)
    else: 
        quadraticSolver(inputString)

def algebraSolver(inputString):
    digitFlag = False
    variable = {}
    listOfDigits = []
    listOfDigitsIndex = -1
    for word in inputString.split():
        if word.isdigit():
            digitFlag = True
            listOfDigits.append(int(word))
            listOfDigitsIndex+=1
        elif digitFlag:
            digitFlag = False
            if variable[word] is None:
                variable[word] = []
                variable[word].append(listOfDigits[listOfDigitsIndex])
            else:
                variable[word].append(listOfDigits[listOfDigitsIndex])
    if product in inputString:
        for key in variable:
            productList = variable[key]
            result = 1 
            for x in productList:
                result = result * x 
            print("The product of all the " + key + " is " + result + '\n')

        


def quadraticSolver(inputString):
    return None 

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

    math_talk_10= ['what is the law of cosines',
            'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']

    math_talk_11 = ['law of cosines, what is it?',
        'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']

    math_talk_3 = ['All identities',
                'sin(a +/- b) = sin(a) * cos(b) +/- cos(a) * sin(b); cos(a +/- b) = cos(a) * sin(b) -/+ sin(a) * sin(b); tan(a +/- b) = (tan(a) +/- tan(b))/(1 -/+ tan(a) * tan(b))']

    math_talk_4 = ['Sin Identity', 
    'sin(a +/- b) = sin(a) * cos(b) +/- cos(a) * sin(b)']

    math_talk_5 = ['Cosin Identity',
        'cos(a +/- b) = cos(a) * sin(b) -/+ sin(a) * sin(b)']
    
    math_talk_6 = ['Tan Identity'
                'tan(a +/- b) = (tan(a) +/- tan(b))/(1 -/+ tan(a) * tan(b))']

    math_talk_function = ['Solve a problem for me!', problemSolver()]
    math_talk_function2 = ["I'd like you to solve a problem for me", problemSolver()]
    math_talk_function3 = ["Can you solve a word problem?", problemSolver()]
                
    talks.extend((small_talk, math_talk_1, math_talk_2, math_talk_3, 
        math_talk_4, math_talk_5, math_talk_6, math_talk_10, math_talk_11, 
        math_talk_function, math_talk_function2, math_talk_function3,
        farewell_talk))
    
    corpus_trainer = ChatterBotCorpusTrainer(my_bot)
    corpus_trainer.train('chatterbot.corpus.english')
    
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
        

