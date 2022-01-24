
# Python code to pick a random
# word from a text file
import random

def compare_strings(a, b):
    correct = False
    
    size = min(len(a), len(b)) # Finding the minimum length
    count = 0 # A counter to keep track of same characters
    i = 0
    

    while i < size:
        if a[i] == b[i]:
            count += 1 # Updating the counter when characters are same at an index
            print(f"{a[i]} is in the correct position")
        
        i += 1

    #print("Number of Same Characters:", count)
    if count == 5:
        correct = True

    return correct
  
# Open the file in read mode
with open("fives.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
  
    # print random string
    wordle = random.choice(words)
    #print(wordle)

    correct = False
    tries = 1

    while tries < 7 and correct is False:
        # check the word
        attempt = input("Enter your attempt: ")
        correct = compare_strings(wordle, attempt)
        for letter in attempt:
            if letter in wordle:
                print(f"{letter} is in the word")
        tries += 1
    print(wordle)
