def printSet(df):
    setNumber = int(input("Which set do you want to print? "))

    questions = []
    answers = []

    start = setNumber*30 - 30

    for i in range(start, start+30):
        questions.append(df.loc[i, "Meaning"].strip().capitalize())
        answers.append(df.loc[i, "Word"].strip())

    print()
    for i in range(len(questions)):
        print(f"{i+1}. {questions[i]} --> {answers[i]}\n")