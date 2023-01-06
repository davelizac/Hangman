#Step 5

import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
from replit import clear

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)


end_of_game = False
lives = 6

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    
    if guess in display:
        print("You already guessed that letter!") #This line of code was problematic for me, not because I could not find its logic, but because I didn't know where to place the line. The placement here makes the code work as expected becasue it checks if the guess is already in the 'display' before running the whole app. 

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]              
        if letter == guess:
            display[position] = letter

        
        #Check if user is wrong.
    if guess not in chosen_word:
        
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print(f"\nThe answer is {chosen_word}...\n")
            print("Game over!")
    
        


    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}\n")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")


    print(stages[lives])