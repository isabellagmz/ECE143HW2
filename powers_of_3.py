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
    '''weights = {1,3,9,27}

    # makes every possible combination with the weights
    for i in range(1,5):
        combinations = list(itertools.combinations(weights, i))
    # checks if the sum of the elements in the combinations is input
        for seq in combinations:
            list_of_sums = list(seq)
            if sum(seq) == input_number:
                print(seq)'''

    a = [[0, 0, 0, 0], [1, 3, 9, 27]]
    result = [0, 0, 0, 0]  # to store result
    for i in range(2):  # generating pattern
        for op1 in range(2):
            for j in range(2):
                if (op1 == 0):
                    s = a[i][0] + a[j][1]
                else:
                    s = a[i][1] - a[j][0]
        for op2 in range(2):
            for k in range(2):
                if (op2 == 0):
                    t = s + a[k][2]
                else:
                    t = a[k][2] - s
        for op3 in range(2):
            for l in range(2):
                if (op3 == 0):
                    u = t + a[l][3]
                else:
                    u = a[l][3] - t
        # print(u)
        if (u == input_number):
            result = [i, j, k, l]

    print(result)



    return result
