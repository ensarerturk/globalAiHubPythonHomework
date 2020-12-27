import random
wordlist = ["global","python","breed","tree","coding","notebook","course","sleep","choice"]
word_chosen = ""
word_visualization = ""
max_guesses = 10
counter = 0
letters_guessed = []
current_guess = ""

name=input("What's your name :")
while True:
    #wordlist is randomly selected. "_" as long as the selected value is put.
    word_chosen = random.choice(wordlist)
    letters_guessed = len(word_chosen) * "_"
    current_guesses = 0
    print(f"Welcome to hangman! {name}")
    print("Rules :\n-There are words of more than 6 letters and you are given 12 rights.")
    print("This word is ", len(letters_guessed), " letters")
    
    while counter <= max_guesses+1:
        current_guess = input("Enter a letter: ")
        #returns the length of the selected letter. if it knows, the rest of the screen will print what it needs to know.
        for i in range(0, len(word_chosen)):
            if word_chosen[i] == current_guess:
                letters_guessed = letters_guessed[:i] + current_guess + letters_guessed[i+1:]
                print("You got a letter!")
                print(letters_guessed)
        #"Congratulations" will be printed on the screen.
        if word_chosen == letters_guessed:
            print("Congratulations! You won")
            exit()
        counter+=1
        print(f"You have {12-counter} rights left")
    print("Maybe next time, the word was:", word_chosen)
    exit()