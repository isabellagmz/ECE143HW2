# Isabella Gomez A15305555
# ECE143 HW 2

# Instructions:
# Using corpus of 10,000 common English words, create a new file that
# consists of each consecutive non-overlapping sequence of five lines merged
# into one line. If the last group has less than five at the end, just write
# out the last group. Here is your function signature:
# write_chunks_of_five(words,fname). The words is a list of words from the
# above corpus and fname is the output filename string.

import csv
def write_chunks_of_five(words,fname):
    '''
    Creates a file with 10,000 English words arranged in rows of 5
    :param words: list of words that will be arranged
    :param fname: name of the file that will be created
    :return: none
    '''

    # Check words is a list and fname is a string
    assert type(words) == list
    assert type(fname) == str

    # Checks that the elements in the list are str
    for elements in range(len(words)):
        check_str = isinstance(words[elements], str)
        assert check_str

    file_entry = "" # formatting string for file
    words_per_line = 0
    extra_counter = 0
    new_lines = 0 # new_line counter

    # To arrange incoming words
    for word in range(len(words)):
        extra_counter = extra_counter + 1  # increments extra counter
        # Brings word counter to 0 and enters the line after 5 words
        if words_per_line == 5:
            words_per_line = 0
            file_entry = file_entry + "\n"
        file_entry = file_entry + words[word] + " "
        words_per_line = words_per_line + 1 # increments counter of words
    # print(file_entry)

    # remove last space in file
    file_entry = file_entry[:-1]

    # Making the file
    with open(fname, 'w', newline='') as file:
        writer = csv.writer(file)
        #writer.writerow([file_entry])
        file.write(file_entry)

    return 0
