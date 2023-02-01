import random  
from hangmanWords import words

def hangman():
    choosen_words = []
    word_list = []
    guess_list = []
    correct_count = 0
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    #USER CHOOSES WORD LENGTH
    word_length = int(input("Hello, wanna play hangman with me? Then please type in a number from 3 to 14, to let me know, how long the words should be, that I choose>>>  "))
    while word_length < 3 or word_length > 14:
        word_length = int(input("Please type in a number between 3 and 14>>>  "))
    
    #COMPUTER CHOOSES WORD
    for i in words:
        if len(i) == word_length:
            choosen_words.append(i)
    random_word = random.choice(choosen_words)
    word_list = list(random_word)

    #EMPTY LIST OF WORD LENGTH TO BE FILLED IN BY THE USER
    for letter in random_word:
        guess_list.append(" - ")
    print(random_word)

    #USED LETTERS WITH ACCOUNT TO DOUBLE LETTERS
    used_letters = []
    
    #USER GUESSES
    while correct_count < word_length:
        user_guess = input("\nGuess a letter>>>  ").lower()
    
        #CORRECT GUESS
        if user_guess in word_list and alphabet:
            used_letters.append(user_guess) #will be used later if user_guess is no longer in word 
            correct_count += 1
            index = word_list.index(user_guess) #index of user_guess in word
            word_list[index] = "-" #canceling out correct user_guess of the word list
            guess_list[index] = user_guess #adding correct user_guess to the displayed list
            guess_string = "".join(guess_list) #displaying the list as a nice word
            print("\nDisplay chart: ", guess_string, "\n")

        #NOT IN THE WORD
        elif user_guess not in random_word and user_guess in alphabet: 
            print("---Not in the word!---")
            print("\nDisplay chart: ", guess_string, "\n")

        #ALREADY USED LETTER AND NOT MULTIPLE TIMES IN WORD
        elif user_guess in used_letters and user_guess in alphabet:
            print("---You have already used this letter sufficiently!---")
            print("\nDisplay chart: ", guess_string, "\n")

        #NOT IN THE ALPHABET
        elif user_guess not in alphabet:
            print("---Not in the alphabet!---")
            print("\nDisplay chart: ", guess_string, "\n")
        
        #UNKNOWN ERROR
        else:
            print("---Error---")
            print("\nDisplay chart: ", guess_string, "\n")

    if guess_string == random_word:
        print(f"\nNice Job! The word was:  {random_word}")

    
    return random_word

