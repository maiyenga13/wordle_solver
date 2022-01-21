
import random
wordlist = open('combined_wordlist.txt').readlines()
word = (random.choice(wordlist)).upper()

def check(guess):
    greens = []
    for i in range(5):
        actual = word[i]
        guessed = guess[i]
        if(actual == guessed):
            greens.append(actual)
        else:
            greens.append("_")
    yellows = ["_", "_", "_", "_", "_"]
    for letter in word:
        if(letter in guess and letter not in greens):
            id = guess.find(letter)
            yellows[id] = letter
        
            
    return (greens, yellows)

def get_guess():
    return input("Guess: ").upper()

print(" W O R D L E")
for i in range(6):
    try_word = get_guess()
    g,y = check(try_word)
    if("_" not in g):
        print("Greens: ", " ".join(g))
        print("You guessed it in ", i + 1, " guesses!")
        break
    print("Greens: ", " ".join(g))
    print("yellows: ", " ".join(y))

print("The word was ", word)
