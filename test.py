import random 
from time import sleep
import datetime

def testSet(df):
    setNumber = int(input("Which set do you test?"))

    start = setNumber*30 - 30

    questions = []
    answers = []
    askedTillNow = set()
    correctAnswers = {}
    wrongAnswers = {}

    for i in range(start, start+30):
        questions.append(df.loc[i, "Meaning"].strip().capitalize())
        answers.append(df.loc[i, "Word"].strip())

    for i in range(3, 0, -1):
        print(f"Starting in {i}")
        sleep(1)
    
    counter = 1

    while(len(askedTillNow)!=30):
        i = random.randint(0, 29)
        
        if i in askedTillNow:
            continue
        
        askedTillNow.add(i)

        print(counter, questions[i])
        counter += 1
        userAnswer = input().lower()

        if userAnswer == (answers[i]):
            correctAnswers[i+1] = userAnswer
        else:
            wrongAnswers[i+1] = userAnswer
    
    file = open("report.txt", "w")

    percentage = (len(correctAnswers)/5)*100
    
    ct = datetime.datetime.now()
    file.write(f"{ct}\nResult: {percentage}%\n")

    file.write("\nMistakes make you stronger for the D-Day!\n")
    counter = 1
    for i in wrongAnswers:
        file.write(f"\n{counter}. {questions[i-1]}: {wrongAnswers[i]}\n{answers[i-1]}\n")
        counter += 1

    counter = 1
    file.write("\nCorrect Onces\n")
    for i in correctAnswers:    
        file.write(f"\n{counter}. {questions[i-1]}: {correctAnswers[i]}\n{answers[i-1]}\n")
        counter += 1