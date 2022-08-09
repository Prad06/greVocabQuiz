from operator import le
import random
import itertools

def returnOptions(correctOption):
    options = [correctOption]
    while(len(options)!=4):
        randomOption = random.randint(0, 29)
        if randomOption != correctOption and randomOption not in options:
            options.append(randomOption)
    
    possiblePerms = list(itertools.permutations(options))

    return list(possiblePerms[random.randint(0, len(possiblePerms)-1)])
    

def learnSet(df):
    setNumber = int(input("Which set do you learn?"))

    start = setNumber*30 - 30

    questions = {}
    answers = {}
    learningSet = []

    for i in range(start, start+30):
        questions[i] = df.loc[i, "Meaning"].strip().capitalize()
        answers[i] = df.loc[i, "Word"].strip()
    
    for i in range(len(questions)):
        learningSet.append([questions[i], i])


    while(learningSet):
        randomNo = random.randint(0, len(learningSet)-1)
   
        indexInQuestionsArray = learningSet[randomNo][1]

        print(f"\nQ. {questions[indexInQuestionsArray]}")
        options = returnOptions(indexInQuestionsArray)
        
        optionsDict = {}
        for i in range(1, 5):
            optionsDict[i] = answers[options[i-1]]
        
        for counter in range(1, 5):
            print(f"{counter}) {optionsDict[counter]}", end="  ")

        userAnswer = optionsDict[int(input("\nYour Answer: "))]

        if userAnswer == answers[indexInQuestionsArray]:
            learningSet.pop(randomNo)
        else:
            wrongAttempt = learningSet.pop(randomNo)
            learningSet.append(wrongAttempt)


