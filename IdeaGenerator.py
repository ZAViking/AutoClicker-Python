# Ultimate Idea Generator
# -------------------------
# Use at your own risk...
import os
from random import randint
from os import linesep

x = ['Extreme', 'Random', 'Epic', 'Strange', 'Ultimate', 'Cool', 'Challenging', 'Easy', 'Impossible', 'Funny', 'Generic', 'Boring']
y = ['Dice', 'Life', 'Programming', 'Person', 'Fishing', 'Eating', 'Fighting', 'Idea', 'Car', 'Math', 'Minesweeper', 'Argument', 'Excuse', 'Hair', 'War', 'TV', 'Radio', 'Texting', 'Smartphone', 'Farming', 'Typing', 'Talking', 'Toilet', 'Sleeping', 'Spelling', 'Grammar', 'Driving', 'Thinking', 'Movie', 'Photo', 'Dancing', 'Bottle Flip', 'Video', 'Emoji', 'Biking', 'Music', 'Trivia', 'Book', 'Monster', 'Video', 'Hashtag', 'Airplane', 'Food', 'Politics', 'Planting', 'Stock Market', 'Sandwich', 'Business', 'Money', 'Baking', 'Brain']
z = ['Simulator', 'Game' , 'Maker', 'Generator', 'Editor', 'Helper', 'Enigma', 'Puzzle', 'Thing', 'App', 'Website', 'Improver', 'Guide', 'Program', 'Project']

try:
	a = input('How many ideas? ')
	a = int(a)
	if a > 99:
		raise ValueError
	print('---Generating ' + str(a) + ' Ideas---')
	for i in range(a):
		xn = randint(1, len(x)) - 1
		yn = randint(1, len(y)) - 1
		zn = randint(1, len(z)) - 1
		print(linesep + x[xn] + ' ' + y[yn] + ' ' + z[zn])
except:
	print('Error: Invalid Input! (Maximum value of ideas is 99)')
print(" ")
os.system("pause")