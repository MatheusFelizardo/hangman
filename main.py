import random
import art
import words

random_word = random.sample(words.word_list, 1)[0]
random_word_array = [*random_word]
lives = 6
chosen_letter = []
recreated_word = []
run_loop = True
for letter in random_word_array:
    recreated_word.append('_')

print(art.logo + "\n\n")
print(recreated_word)
print("\n")

while run_loop:
    guess = input("Try to guess a letter: ").lower()
    has_letter = False
    for letter in chosen_letter:
        if letter == guess:
            print(f"Letter '{guess}' already chosen")
            has_letter = True

    if (not has_letter):
        amountOfLetter = 0
        for index, letter in enumerate(random_word_array):
            if letter == guess:
                recreated_word[index] = letter
                amountOfLetter += 1
        if (amountOfLetter > 0):
            print(f"There are {amountOfLetter} letters {guess}")
            print(recreated_word)
            print('\n')
        else:
            lives -= 1
            print(art.stages[lives])
        chosen_letter.append(guess)
        if lives == 0:
            run_loop = False
            print('You lose!')
            print(f'The word was {random_word}')
        elif recreated_word == random_word_array:
            run_loop = False
            print('You win!')
