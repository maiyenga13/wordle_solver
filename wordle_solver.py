start_words = ["tones", "lions", "adieu"]
wordlisti = open('combined_wordlist.txt').readlines()

def find_new_words (wordlist, greens, yellows, greys):
    
    def letter_correct(word):
        for (letter, index) in greens:
            if(word[index] != letter):
                return False
        return True
        
    wordlist = filter(letter_correct, wordlist)
    
    def letter_incorrect(word):
        for letter in greys:
            if(letter in word):
                return False
        return True
    wordlist = list(filter(letter_incorrect, wordlist))
    
    print("after gray: ", len(wordlist))
    #print(wordlist)
    def letter_yellow(word):
        #print("hi")
        for (letter, indexList) in yellows:
            #print(letter)
            if(letter not in word):
                return False
            if(letter in word):
                for index in indexList:
                    if(word[index] == letter):
                        return False
        return True

    wordlist = list(filter(letter_yellow, list(wordlist)))
    print(len(wordlist))
    
    # for (letter, indexList) in yellows:
    #     print(letter, indexList)
    #     for index in indexList:
    #         def letter_correct_y(word):
    #             return letter in word 
    #         
    #         print(len(list(wordlist)))
    #print(list(wordlist))
    return list(wordlist)
print("initial len: ", len(wordlisti))
wordlist_1= find_new_words(wordlisti, [], [("r", [2])], ["f", "a", "t", "s"])
wordlist_2 = find_new_words(wordlist_1, [("r", 1)], [("c", [0]), ("p", [3])], ["e", "y"])
#wordlist_3 = find_new_words(wordlist_2, [("o", 1)], [("r", [2, 4]), ("t", [3, 2]), ("b", [0])])
print(wordlist_2[0])



    
