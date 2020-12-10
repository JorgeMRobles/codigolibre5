import random
from words import words 
import string 

def getword(words):
	word = random.choice(words) #from the list
	while '-' in word or ' ' in word:
		word = random.choice(words)
	return word.upper()

def hangmanmain():
	word = getword(words)	
	word_letters = set(word)
	alphabet = set(string.ascii_uppercase)
	used_letters = set()
	lives = 6

	while len(word_letters) > 0 and lives > 0:
		print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
		print('You have used these letters: ', ' '.join(used_letters))
		word_list = [letter if letter in used_letters else '-' for letter in word]
		userletter = input('Guess a letter: ').upper()
		if userletter in alphabet - used_letters:
			used_letters.add(userletter)
			if userletter in word_letters:
				word_letters.remove(userletter)
			else:
				lives = lives - 1 
				print('It is not in word')
		elif userletter in used_letters:
			print('You have already used that letter! Try again')
		else: 
			print('Invalid. Try again')
	if lives == 0:
		print('Game over. The word was', word)
	else:
		print('You guessed the word', word,'!')