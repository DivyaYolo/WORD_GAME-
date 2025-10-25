import random
word_bank = ['apple', 'tiger', 'cloud', 'music', 'light', 'dream', 'river', 
    'smile', 'chair', 'book', 'planet', 'silver', 'mirror', 'garden', 
    'castle', 'pencil', 'ocean', 'forest', 'camera', 'cookie', 'python', 
    'github', 'binary', 'server', 'router', 'packet', 'logic', 'matrix']
word = random.choice(word_bank)
guessedWord = ['_'] * len(word)
attempts = 10
while attempts > 0:
    print('\nCurrent word:' + ' '.join(guessedWord))
    guess = input('Guess a letter: ').lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
    if '_' not in guessedWord:
        print('\nCongratutlations!! You guessed the word:' + word)
        break
if attempts == 0 and '_' in guessedWord:
    print('\nYou\'ve run out of attempts! The word was: ' + word)