'''
Created on Sep 1, 2022
@author: carlos.anguiano
calculate string solutions
Generate a method that will take an input of integers separated by multiplication or addition operators that will return correct solution for the string.
example input: '6*4+3+1'
i added to solutions


"calculate_string" is the one i was trying to finish but ran out of itme (long answear)
"calculate_string_v2" one is the  one i think i was actually expected to write (short answear)  

both answers work, but i failed to recognize the pattern i was being guide towards during the interview
and so my interview answer was not the best.

'''


import unittest

# NOTE: this is an implementation closer to what i think Chen was hinting too (split by +)


def calculate_string_v2(string_val):
    """
    this is the one i think i was meant to implement but didn't 

    this implementation relies on a pattern I failed to see in the data.
    if you split by '+' the addition data becomes isolated 
    i wish i had seen this pattern sooner (i got caught of over thinking and the guidance provided did not sync until hours later)

    :param string_val:
    """
    split_vals = string_val.split('+')
    total = 0

    for sub_val in split_vals:
        mult_vals = sub_val.split('*')
        if len(mult_vals) < 2:
            total += int(mult_vals[0])
            continue
        mult_val = 1
        for mlt in mult_vals:
            mult_val = mult_val * int(mlt)

        total += mult_val

    return total


def calculate_string(string_val):
    """
    3 step implementation (2 loops) 
    this one the long way i got to explain my inital approuch but did not get to work out all the details of the code (i was  over thinking).

    step one (loop 1) get_a list of indexes for each operator
    step two (loop 2) loop through that smaller list of index and use some simple index math to find the neighbors
    step three (loop 2) add or multiply the neighbor values as needed making sure to avoid values that have been processed already


    :param str string_val: string value with integers and operator characters 
    """
    char_look_up = {'+', '*'}  # a set containing the supported  operators

    # NOTE: generate an list of indexes that marks the position of the operator characters in the string
    operator_index = [index for index, char in enumerate(string_val) if char in char_look_up]

    # NOTE: setup some static vars to add up our results
    mult_total = 0
    add_total = 0
    use_a = True  # NOTE: this helps me track when i've already handled the a_value for the next operation

    # NOTE: next i loop through the operators and find the neighbors values

    for i, op_index in enumerate(operator_index):
        op_type = string_val[op_index]
        prev_op_index = None
        next_op_index = None

        # NOTE: I attempt to find the previous and next operator to setup logic that will allow mix typing of operators
        # NOTE: it also helps support int values with more than one digit
        if i:
            prev_op_index = operator_index[i - 1]

        if i != len(operator_index) - 1:
            next_op_index = operator_index[i + 1]

        # NOTE: i use this code to find out when the first value digit should begin
        start_index = 0
        if prev_op_index is not None:
            start_index = prev_op_index

        # NOTE: i collect the neighbors
        val_a = string_val[start_index:op_index]
        val_b = string_val[op_index + 1:next_op_index]

        # NOTE: if a process the a value in the previous operation i empty this value
        if not use_a:
            val_a = None  # NOTE: i think i can do with out this, but i really wanted to complete the exercise.

        # NOTE: handle multiplication
        if op_type == '*':
            use_a = False

            if not val_a:
                mult_total = int(mult_total) * int(val_b)
                continue

            mult_total += int(val_a) * int(val_b)

            continue

        # NOTE handle adding values?
        if val_a:
            if prev_op_index is None or string_val[prev_op_index] == '+':
                add_total += int(val_a)

        if next_op_index is None or string_val[next_op_index] == '+':
            add_total += int(val_b)
            use_a = False
            continue

        use_a = True
    # NOTE: the big finish.
    return mult_total + add_total


# NOTE: create some test cases for my self to make sure i'm addressing multiple permutations of the problem.

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = calculate_string

    def test_basic(self):
        test = '6*4+3+1'
        out = calculate_string(test)
        self.assertEqual(out, 28)

    def test_more_mult(self):
        test = '10*6*4+3+1'
        out = self.calc(test)
        self.assertEqual(out, 244)

    def test_more_add(self):
        test = '10*6*4+3+1+20'
        out = self.calc(test)
        self.assertEqual(out, 264)

    def test_out_of_order(self):
        test = '1+6*4+3+1'
        out = self.calc(test)
        self.assertEqual(out, 29)

    def test_out_of_order_extra_mult(self):
        test = '1+6*4+3+1*2'
        out = self.calc(test)
        self.assertEqual(out, 30)

    def test_multiple_char_ints(self):
        test = '10+60*40+35+12*1'
        out = self.calc(test)
        self.assertEqual(out, 2457)


class TestCalcV2(TestCalc):
    def setUp(self):
        TestCalc.setUp(self)
        self.calc = calculate_string_v2


if __name__ == '__main__':
    unittest.main()
