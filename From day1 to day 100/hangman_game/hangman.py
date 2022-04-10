import random
from hangman_game import hangman_art, hangman_words_list


#Next setting up our bollian and looping with while/for loops till we get the word
end_of_game = False
chosen_word = random.choice(hangman_words_list.word_list)
word_length = len(chosen_word)

lives = 6

print(hangman_art.logo) #Printing the logo from the other file.

#Creating a blanks
display_symbols = []
for symbol in range(word_length):
    display_symbols += "_"


while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    #In this care all the letters we input are goin to be a lower letters!
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            print(f"You've already guessed {letter}!")
            display_symbols[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word. You lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display_symbols)}")

    if "_" not in display_symbols:
        end_of_game = True
        print("You win!")
    #Printing the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(hangman_art.stages[lives])