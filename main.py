from art import hangman_stages
from word import pick_random_word, valid_theme, display_themes

def update_display(stage, word):
    print(stage)
    print(word)

def get_word(theme):
    return pick_random_word(theme)

def word_guessed(correct_word, current_word):
    if correct_word.lower() == current_word.lower():
        return True
    return False

def valid_guess(guess):
    if len(guess) > 0 and len(guess) < 2:
        return True
    return False

def word_string(list):
    return ''.join(list)
    
game_running = True
MAX_TRIES = len(hangman_stages) - 1

while game_running:
    ''' While the game is running, we want the user to pick the right letter while 
    the word isn't finished and the user hasn't used up his tries'''
    
    display_themes()
    theme = None
    
    while not valid_theme(theme):
        theme = input("What theme would you like to play with? ")
    
    word = pick_random_word(theme)
    
    current_word = []
    for i in range(len(word)):
        current_word.append('_')
    
    tries = 0
    while tries < MAX_TRIES and not word_guessed(word, word_string(current_word)):
        current_stage = hangman_stages[tries]
        update_display(current_stage, word_string(current_word))
        
        user_guess = input('Guess a letter in the word: ')
        contained_letter = False
        if valid_guess(user_guess):
            for i in range(len(word)):
                letter = word[i]
                if user_guess.lower() == letter.lower():
                    current_word[i] = letter
                    contained_letter = True

        if not contained_letter:
            tries += 1
    
    if word_guessed(word, ''.join(current_word)): 
        print("Congratulations, you guessed the word!")
        update_display(current_stage, word_string(current_word))
    else:
        # In the case that the user lost display the final stage
        update_display(hangman_stages[-1], word_string(current_word))

    replay = input('Do you wish to play again? y/n: ').lower()
    if not replay == 'y':
        game_running = False
