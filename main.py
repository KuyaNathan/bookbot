import re

def countWords(string):
	words = string.split()
	return len(words)

def countCharacters(string):
	filtered_string = string.lower()
	filtered_string = re.sub('[^A-Za-z0-9]+', '', filtered_string)
	char_dictionary = dict()
	for char in filtered_string:
		if char in char_dictionary:
			char_dictionary[char] += 1
		else:
			char_dictionary[char] = 1
	return char_dictionary	
	
def makeReport(book, word_count, char_dictionary):
	print(f"--- Begin report of {book} ---")
	print(f"{word_count} words found in the document\n\n")
	for char in char_dictionary:
		print(f"The '{char}' character was found {char_dictionary[char]} times")	
	print("--- End report ---")


def main():
	book_title = "books/frankenstein.txt"
	with open(book_title) as f:
		file_contents = f.read()
		word_count = countWords(file_contents)
		char_dictionary = countCharacters(file_contents)
		makeReport(book_title, word_count, char_dictionary)

main()
