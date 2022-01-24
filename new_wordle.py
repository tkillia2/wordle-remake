import random
with open("fives.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
  
    # print random string
    wordle = random.choice(words)
    #print(wordle)

    #wordleDict = dict.fromkeys(wordle,0)
    wordleList = list(wordle)
    #print(wordleList)

    letterList = []

    tries = 1
    correct = False
    while tries < 7 and correct is False:
        attempt = input("Enter your attempt: ")
        attemptList = list(attempt)
        tries += 1
        for index in range(len(wordleList)):
            if wordleList[index] == attemptList[index]:
                print(f"{attemptList[index]} is in the correct position")
            elif wordleList[index] in attemptList:
                print(f"{wordleList[index]} is in the word but not in the correct position")
            else:
                None

        if attemptList == wordleList:
            correct = True
            print("congrats")
    print(f"The wordle for your game was {wordle}")

