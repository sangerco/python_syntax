def print_upper_words(words, letters):
    ''' Given a list of words, print out each word, but in a 
        separate line. Use string.upper() to change all letters 
        to uppercase before printing.

        Use string.startswith() to filter all words that start with 'e'.

        Use nested for loops to filter out all letters that start with letters
        in set.
        '''

    for word in words:
        for letter in letters:
            if word.upper().startswith(letter.upper()):
                print(word.upper())


# should print 'ETHEREUM', 'EARTH', 'COAL', 'CRASH', 'COCA-COLA'

print_upper_words(['ethereum', 'earth', 'coal', 'crash', 'Coca-Cola', 'ship', 'boat'], {'e', 'c'})