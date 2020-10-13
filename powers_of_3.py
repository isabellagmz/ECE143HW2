# Isabella Gomez A15305555
# ECE143 HW 2

# Instructions:
# Given a set of weights {1,3,9,27}, write a function to construct any number
# between 1 and 40. In other words, using the set above and the addition and
# subtraction operations, construct any integer between 1 and 40 without
# re-using elements.

##############################################################################
# Will take an integer as input and construct any integer between 1 and 40   #
# without re-using elements.                                                 #
##############################################################################
import itertools
def get_power_of3(input_number):

    '''Need dot quotes'''

    # Check that the input is an integer between 1 and 40
    assert type(input_number) == int
    assert input_number >= 1
    assert input_number <= 40

    # the weights for the formation of integer
    weights = {1,3,9,27}

    # makes every possible combination with the weights
    for i in range(1,5):
        combinations = list(itertools.combinations(weights, i))
    # checks if the sum of the elements in the combinations is input
        for seq in combinations:
            list_of_sums = list(seq)
            if sum(seq) == input_number:
                print(seq)



    return 0