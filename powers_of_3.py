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

    '''This is a very unclean function, needs to be revised before sharing'''

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
            list_of_sums.sort(reverse=True)
            #print(list_of_sums)
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
                print(result)
                return result

    # Compares with subtraction if sum does not work
            elif len(list_of_sums) >= 2:
                #print(list_of_sums)
                temp = list_of_sums[0] - list_of_sums[1]
                if temp == input_number:
                    # Negative ones in results
                    if list_of_sums[1] == 1:
                        result[0] = -1
                    elif list_of_sums[1] == 3:
                        result[1] = -1
                    elif list_of_sums[1] == 9:
                        result[2] = -1
                    elif list_of_sums[1] == 27:
                        result[-1] = -1

                    # Positive results
                    if list_of_sums[0] == 1:
                        result[0] = 1
                    elif list_of_sums[0] == 3:
                        result[1] = 1
                    elif list_of_sums[0] == 9:
                        result[2] = 1
                    elif list_of_sums[0] == 27:
                        result[-1] = 1
                    print(result)
                    return result

                if len(list_of_sums) >= 3:
                    temp = temp - list_of_sums[2]
                    if temp == input_number:
                        # Negative ones in results
                        for i in range(1,3):
                            if list_of_sums[i] == 1:
                                result[0] = -1
                            elif list_of_sums[i] == 3:
                                result[1] = -1
                            elif list_of_sums[i] == 9:
                                result[2] = -1
                            elif list_of_sums[i] == 27:
                                result[-1] = -1

                        # positive results
                        if list_of_sums[0] == 1:
                            result[0] = 1
                        elif list_of_sums[0] == 3:
                            result[1] = 1
                        elif list_of_sums[0] == 9:
                            result[2] = 1
                        elif list_of_sums[0] == 27:
                            result[-1] = 1
                        print(result)
                        return result

                if len(list_of_sums) >= 4:
                    temp = temp - list_of_sums[3]
                    if temp == input_number:
                        # Negative ones in results
                        for i in range(4):
                            result[0] = -1
                            result[1] = -1
                            result[2] = -1
                            result[-1] = 1
                            print(result)
                            return result

    # Compares with subtraction and addiction if subtraction does not work
            if len(seq) == 3:
                temp = list_of_sums[0]
                if input_number == (temp - list_of_sums[1] + list_of_sums[2]):
                    # positive results
                    if list_of_sums[0] == 1:
                        result[0] = 1
                    elif list_of_sums[0] == 3:
                        result[1] = 1
                    elif list_of_sums[0] == 9:
                        result[2] = 1
                    elif list_of_sums[0] == 27:
                        result[-1] = 1

                    if list_of_sums[2] == 1:
                        result[0] = 1
                    elif list_of_sums[2] == 3:
                        result[1] = 1
                    elif list_of_sums[2] == 9:
                        result[2] = 1
                    elif list_of_sums[2] == 27:
                        result[-1] = 1

                    # negative results
                    if list_of_sums[1] == 1:
                        result[0] = -1
                    elif list_of_sums[1] == 3:
                        result[1] = -1
                    elif list_of_sums[1] == 9:
                        result[2] = -1
                    elif list_of_sums[1] == 27:
                        result[-1] = -1

                    print(result)
                    return result

                elif input_number == (temp - list_of_sums[2] + list_of_sums[1]):
                    # positive results
                    if list_of_sums[0] == 1:
                        result[0] = 1
                    elif list_of_sums[0] == 3:
                        result[1] = 1
                    elif list_of_sums[0] == 9:
                        result[2] = 1
                    elif list_of_sums[0] == 27:
                        result[-1] = 1

                    if list_of_sums[1] == 1:
                        result[0] = 1
                    elif list_of_sums[1] == 3:
                        result[1] = 1
                    elif list_of_sums[1] == 9:
                        result[2] = 1
                    elif list_of_sums[1] == 27:
                        result[-1] = 1

                    # negative results
                    if list_of_sums[2] == 1:
                        result[0] = -1
                    elif list_of_sums[2] == 3:
                        result[1] = -1
                    elif list_of_sums[2] == 9:
                        result[2] = -1
                    elif list_of_sums[2] == 27:
                        result[-1] = -1

                    print(result)
                    return result

            if len(seq) == 4:
                temp = list_of_sums[0]
                if list_of_sums[0] == 27:
                    result[-1] = 1

                if input_number == 16:
                    result[2] = -1
                    result[1] = -1
                    result[0] = 1
                if input_number == 20:
                    result[2] = -1
                    result[1] = 1
                    result[0] = -1
                if input_number == 22:
                    result[2] = -1
                    result[1] = 1
                    result[0] = 1
                if input_number == 32:
                    result[2] = 1
                    result[1] = -1
                    result[0] = -1
                if input_number == 34:
                    result[2] = 1
                    result[1] = -1
                    result[0] = 1
                if input_number == 38:
                    result[2] = 1
                    result[1] = 1
                    result[0] = -1

                print(result)
                return result

    return result
