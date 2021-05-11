'''Sometimes some words like "localization" or "internationalization" are so long that writing them many times in one text is quite tiresome.

Let's consider a word too long, if its length is strictly more than 10 characters. All too long words should be replaced with a special abbreviation.

This abbreviation is made like this: we write down the first and the last letter of a word and between them we write the number of letters between the first and the last letters. That number is in decimal system and doesn't contain any leading zeroes.

Thus, "localization" will be spelt as "l10n", and "internationalization» will be spelt as "i18n".

You are suggested to automatize the process of changing the words with abbreviations. At that all too long words should be replaced by the abbreviation and the words that are not too long should not undergo any changes'''

#code for accepting input

num_of_words = int(input("Enter the number of words you wish to enter: \n"))

listt = []

while len(listt) < num_of_words:
	x = input(f"Enter word {len(listt) + 1} \n")
	listt.append(x)

#code for abbreviate lengthy words

new_list = []

for x in listt:
	if len(x) > 10:		 
		new_list.append(x[0] + str(len(x)) + x[len(x)-1])
	else:
		new_list.append(x)

print(new_list)
