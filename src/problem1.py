"""
Exam 2, Problem 1.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. Put your name in the line above
import math

import testing_helper
import time
import random


def main():
    """ Calls the TEST functions for this module """
    run_test_problem1()


###############################################################################
# TODO: 2. Right-click on the  src  folder and
#              Mark Directory as ... Sources Root,
#          if you have not already done so.
###############################################################################


def run_test_problem1():
    """ Tests the   problem1   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem1   function:")
    print("--------------------------------------------------")

    format_string = "    problem1 ( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 3 * 2 * 3 * 6 * 2 * 4 * 5 * 1 * 6  # which is 25920
    sequence = ["all", "we", "are", "saying",
                "is", "give", "peace", "a", "chance"]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:  Same as Test 1, but uses a tuple (which is immutable)
    expected = 3 * 2 * 3 * 6 * 2 * 4 * 5 * 1 * 6  # which is 25920
    sequence = ("all", "we", "are", "saying",
                "is", "give", "peace", "a", "chance")
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 3 * 2 * 3 * 6 * 2 * 4 * 5 * 1 * 6  # which is 25920
    sequence = ["all", "we", "are", "saying",
                "is", "give", "peace", "a", "chance"]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 6 * 10 * 7 * 5 * 8  # which is 16800
    sequence = ["all we", "are saying", "is give", "peace", "a chance"]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 17 * 0 * 7 * 14  # which is 0
    sequence = ["all we are saying", "", "is give", "peace a chance"]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 3
    sequence = ["abc"]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 3 * 2 * 3 * 6 * 2 * 4 * 5 * 8  # which is 34560
    sequence = ["all", "we", "are", "saying",
                "is", "give", "peace", "a chance"]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 6 * 10 * 2 * 4 * 5 * 8  # which is 19200
    sequence = ["all we", "are saying",
                "is", "give", "peace", "a chance"]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 40
    sequence = ["all we are saying is give peace a chance"]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = 1 * 1 * 1  # which is 1
    sequence = ["a", "c", "b"]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = 2 * 1 * 1  # which is 2
    sequence = ["ab", "c", "b"]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = 2 * 2 * 1 * 3  # which is 12
    sequence = ["ab", "cd", "b", "abc"]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 13:
    expected = 3 * 0 * 1  # which is 0
    sequence = ["abc", "", "b"]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 14:
    expected = 1 * 1 * 0 * 0  # which is 0
    sequence = ["a", "b", "", ""]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 15:
    expected = 0
    sequence = [""]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Tests 16 and following:
    #   Tests that use many random permutations of factorials
    number_of_permutations = 1000
    number_of_distinct_tests = 100

    random.seed(42)  # To make the tests reproducible
    has_failed = False
    for j in range(2, 11):
        if has_failed:
            break

        numbers = [x * str(x) for x in range(1, j)]
        expected = math.factorial(j - 1)

        for k in range(number_of_permutations):
            random.shuffle(numbers)
            actual = problem1(numbers)
            if actual != expected:
                print()
                print("Test {}:".format(
                    16 + ((j - 2) * number_of_permutations) + k))
                print("  This test case calls   problem1   on:")
                print("    ", numbers)
                print("  Expected:", expected)
                print("  Actual:  ", actual)
                print("  *** FAILED the above test. ***", color="red")
                test_results = [test_results[0], test_results[1] + 1]
                has_failed = True
                break

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem1(strings):
    """
    What comes in:
      -- a non-empty sequence of strings
    What goes out: Returns the product of the lengths of the strings.
    Side effects: None.
    Examples:
      If the argument is:
        ["all", "we",  "are", "saying", "is", "give", "peace", "a", "chance"]
      then this function returns:
         3 x 2 x 3 x 6 x 2 x 4 x 5 x 1 x 6, which is 25920.

      If the argument is:
        ["all we",  "are saying", "is give", "peace", "a chance"]
      then this function returns  6 x 10 x 7 x 5 x 8, which is XXX.

      If the argument is:
        ["all we are saying", "", "is give", "peace a chance"]
      then this function returns  17 x 0 x 7 x 14, which is 0.

      If the argument is ["abc"], then this function returns  3.

     ** ASK YOUR INSTRUCTOR FOR HELP **
        ** IF YOU DO NOT UNDERSTAND THE ABOVE SPECIFICATION. **

    Type hints:
      :type strings: list[str]   or tuple(str)
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #     The testing code is already written for you (above).
    # -------------------------------------------------------------------------


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################
def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string, suffix=""):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string,
                                                 suffix)


def print_actual_result_of_test(expected, actual, test_results,
                                precision=None):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results, precision)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print("ERROR - While running this test,", color="red")
    print("your code raised the following exception:", color="red")
    print()
    time.sleep(1)
    raise
