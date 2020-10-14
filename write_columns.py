# Isabella Gomez A15305555
# ECE143 HW 2

# Instructions:
# Here is some sample data
# data=[5,4,6,1,9,0,3,9,2,7,10,8,4,7,1,2,7,6,5,2,8,2,0,1,1,1,2,10,6,2]
# Write a function that can write the following formula to three columns
# to a comma-separated file:
# data_value, data_value**2, (data_value+data_value**2)/3.
# Here is your function signature write_columns(data,fname). Your written
# floating-point values should be formatted to the hundreths place. Your
# function can only accept lists of integers/floats as input. Note that
# fname is a string and data must be a list.

##############################################################################
# Will take an integer as input and construct any integer between 1 and 40   #
# without re-using elements.                                                 #
##############################################################################
import csv
def write_columns(data, fname):

    '''Making sure fname is a string, data a list of ints/floats'''
    assert type(fname) == str
    assert type(data) == list
    # Checks that the elements in the list are ints or floats
    for elements in range(len(data)):
        check_int = isinstance(data[elements], int)
        check_float = isinstance(data[elements], float)
        assert (check_int or check_float)

    file_entry = ""

    # Making the 3 variables to be printed to the file
    for data_value in data:
        first_column = float(data_value)
        second_column = float(data_value**2)
        third_column = float((data_value+data_value**2)/3)

        # Formatting to hundreds place
        first_column = "%.2f" % first_column
        second_column = "%.2f" % second_column
        third_column = "%.2f" % third_column

        # Make file entries
        file_entry = file_entry + str(first_column) + ',' + str(second_column) + ',' + str(third_column) + '\n'

    # Making file
    with open(fname, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([file_entry])

    return 0
