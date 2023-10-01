"""
Exam 2, Problem 6.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. Put your name in the line above

import testing_helper
import time


def main():
    """ Calls the TEST functions for this module """
    run_test_problem6()


def run_test_problem6():
    """ Tests the   problem6   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem6   function:")
    print("--------------------------------------------------")

    format_string = "    problem6( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 50 + 80  # which is 130
    numbers = [50, 20, 30, 80, 20, 40]
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem6(numbers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 50 + 30 + 50 + 40  # which is 170
    numbers = [50, 20, 30, 50, 20, 40]
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem6(numbers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 6 + 6 + 4  # which is 16
    numbers = [6, 2, 3, 6, 2, 4]
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem6(numbers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 50 + 30 + 50 + 40 + 26  # which is 196
    numbers = [50, 20, 30, 50, 20, 40, 10, 10, 25, 24, 10, 26]
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem6(numbers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 50 + 40 + 30 + 30 + 50 + 40 + 26  # which is 266
    numbers = [50, 40, 30, 20, 30, 50, 20, 40, 10, 10, 25, 24, 10, 26]
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem6(numbers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Summary:
    print_summary_of_test_results(test_results)


###############################################################################
# Be sure to read the IMPORTANT note in the following specification!
###############################################################################
def problem6(integers):
    """
    What comes in:
      -- A non-empty sequence of numbers
    What goes out:
       Returns the sum of the numbers in the sequence that are
       strictly greater than 1/2 times the biggest number in the sequence.
    Side effects: None
    Examples:
      -- problem6( [50, 20, 30, 80, 20, 40] )   returns 130   because
           1/2 of the biggest number is 1/2 x 80, which is 40,
           and the sum of the numbers in the sequence that are strictly
           greater than 40 is  50 + 80, which is 130.

      -- problem6( [50, 20, 30, 50, 20, 40] )   returns 170   because
           1/2 of the biggest number is 1/2 x 50, which is 25,
           and the sum of the numbers in the sequence that are strictly
           greater than 25 is  50 + 30 + 50 + 40, which is 170.

       ** ASK YOUR INSTRUCTOR FOR HELP **
       ** IF YOU DO NOT UNDERSTAND THE ABOVE SPECIFICATION. **

    Type hints:
      :type integers: list[int] | tuple[int]
    """
    ###########################################################################
    # TODO: 2. Implement and test this function.
    #          Tests have been written for you (above).
    ###########################################################################


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
