'''
Created on Sep 1, 2022
@author: carlos.anguiano
calculate string solutions
Generate a method that will take an input of integers separated by multiplication or addition operators that will return correct solution for the string.
example input: '6*4+3+1'
basic rules 
  string value is always solvable 
  only multi or add 
  order of operations matters (Mult before add)
  
features i added not discussed in the test
*add support for ints with more than one digit
*add support for out order operations mult before add add before mult
'''

import unittest


def calculate_string(string_val):
    char_look_up = {'+', '*'}  # a set containing the supported  operators

    # NOTE: generate an index of character that represent mathematics operations
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


# NOTE: create some test cases for my self to make sure i'm adressing multiple permutations of the problem.

class TestCalc(unittest.TestCase):
    def test_basic(self):
        test = '6*4+3+1'
        out = calculate_string(test)
        self.assertEqual(out, 28)

    def test_more_mult(self):
        test = '10*6*4+3+1'
        out = calculate_string(test)
        self.assertEqual(out, 244)

    def test_more_add(self):
        test = '10*6*4+3+1+20'
        out = calculate_string(test)
        self.assertEqual(out, 264)

    def test_out_of_order(self):
        test = '1+6*4+3+1'
        out = calculate_string(test)
        self.assertEqual(out, 29)

    def test_out_of_order_extra_mult(self):
        test = '1+6*4+3+1*2'
        out = calculate_string(test)
        self.assertEqual(out, 30)

    def test_out_of_order(self):
        test = '10+60*40+35+12*1'
        out = calculate_string(test)
        self.assertEqual(out, 2457)


if __name__ == '__main__':
    unittest.main()
