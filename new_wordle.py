import random
with open("valids.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
  
    # print random string
    wordle = random.choice(words)
    #print(wordle)

    #wordleDict = dict.fromkeys(wordle,0)
    wordleList = list(wordle)
    #print(wordleList)

    letterList = [' ',' ',' ',' ',' ']

    tries = 1
    correct = False
    while tries < 7 and correct is False:
        attempt = input(f"{tries}. Enter your attempt: ")
        while len(attempt) != 5 or attempt not in words:
            print("attempt needs to be a five letter word or a valid word")
            attempt = input(f"{tries}. Enter yout attempt: ")
        attemptList = list(attempt)
        tries += 1
        for index in range(len(wordleList)):
            if wordleList[index] == attemptList[index]:
                print(f"\t{attemptList[index]} is in the correct position")
                #letterList.insert(index, wordleList[index])
            elif wordleList[index] in attemptList:
                print(f"\t{wordleList[index]} is in the word but not in the correct position")
            else:
                None
        #print(f"Current progress: {letterList}")

        if attemptList == wordleList:
            correct = True
            print("congrats")
    print(f"The wordle for your game was {wordle}")

