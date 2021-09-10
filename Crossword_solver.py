### This very basic crossword solver simply parses through a dictionary
### and returns any possible words where spaces as input have replaced letters

dictionary = open('DictionaryE.txt', 'r').read().split()
	
def checkWord(clue, dictionary):
	Blanks = len(testWord) - testWord.count(" ")
	for word in dictionary:
		incLetter = 0
		incMatch = 0
		if len(word) == len(testWord):
			for letter in testWord:
				if letter == word[incLetter]:
					incMatch += 1
				incLetter += 1
			if incMatch == Blanks:
				print(word)
	return
	
clue = input("Input a word to solve.\nUse spaces to denote unknown letters: ").lower()

checkWord(clue, dictionary)
