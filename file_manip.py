#python project on a testfile in directory

array = []
##########################################
## depunctuate the words filechange.txt ##
##########################################
def depunc_words(array):
    new_word = ''
    my_rad_words = []

    #######################################################################################################################################################################
    ## For loops are to make sure characters in the file are lowercased and that they are alpha numeric, then go through the words and add them to the list my_rad_words ##
    #######################################################################################################################################################################
    for word in array:
        new_word = ''
        for char in word.lower():
            if not char.isalnum():
                continue
            else:
                new_word += char
        else:
            my_rad_words.append(new_word)
    print(my_rad_words)
    print(len(my_rad_words))
    my_rad_words_dict = count_words(my_rad_words)
    print(my_rad_words_dict)

############################################################################################################
## open the file for read access, then split each word into a line. append each line into the list "word" ##
############################################################################################################
with open('filechange.txt', 'r') as filename:
	for line in filename:
		for word in line.split():
			array.append(word)

################################
## make a count for the words ##
################################
def count_words(lizt_words):
    my_rad_words_dict = {}
    for word in lizt_words:
        if word in my_rad_words_dict:
            my_rad_words_dict[word] += 1
        else:
            my_rad_words_dict[word] = 1
    return my_rad_words_dict




filename.close()
cleaned_array = depunc_words(array)

#is alphanum
