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

    '''Needs dot quotes'''

    # Check that the input is an integer between 1 and 40
    assert type(input_number) == int
    assert input_number >= 1
    assert input_number <= 40

    # the weights for the formation of integer
    weights = {1,3,9,27}
    result = [0, 0, 0, 0]  # to store result

    # makes every possible combination with the weights
    for i in range(1,5):
        combinations = list(itertools.combinations(weights, i))
    # checks if the sum of the elements in the combinations is input
        for seq in combinations:
            list_of_sums = list(seq)
            if sum(seq) == input_number:
                # make the return list
                for element in list_of_sums:
                    if element == 1:
                        result[0] = 1
                    elif element == 3:
                        result[1] = 1
                    elif element == 9:
                        result[2] = 1
                    elif element == 27:
                        result[-1] = 1
                print(seq)

    a = [[0, 0, 0, 0], [1, 3, 9, 27]]



    print(result)



    return result
