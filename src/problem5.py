"""
Exam 2, Problem 5.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. Put your name in the line above

import testing_helper
import time


def main():
    """ Calls the TEST functions for this module """
    run_test_problem5()


def run_test_problem5():
    """ Tests the   problem5   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem5   function:")
    print("--------------------------------------------------")

    format_string = "    problem5( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1
    expected = "r"
    words = ["ok", "one", "four"]
    print_expected_result_of_test([words], expected, test_results,
                                  format_string)
    actual = problem5(words)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2
    expected = "e"
    words = ["a", "hello", "one"]
    print_expected_result_of_test([words], expected, test_results,
                                  format_string)
    actual = problem5(words)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3
    expected = "s"
    words = ["robots"]
    print_expected_result_of_test([words], expected, test_results,
                                  format_string)
    actual = problem5(words)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4
    expected = "n"
    words = ["these", "robots", "are", "lots", "of", "fun"]
    print_expected_result_of_test([words], expected, test_results,
                                  format_string)
    actual = problem5(words)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5
    expected = "r"
    words = ("ok", "one", "four")
    print_expected_result_of_test([words], expected, test_results,
                                  format_string)
    actual = problem5(words)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6
    expected = "a"
    words = ["zebra"]
    print_expected_result_of_test([words], expected, test_results,
                                  format_string)
    actual = problem5(words)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7
    expected = "i"
    words = ["i"]
    print_expected_result_of_test([words], expected, test_results,
                                  format_string)
    actual = problem5(words)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8
    expected = "t"
    words = ["hello" * 100, "goodnight"]
    print_expected_result_of_test([words], expected, test_results,
                                  format_string)
    actual = problem5(words)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9
    expected = "y"
    words = ["goodnight" * 50, "lady"]
    print_expected_result_of_test([words], expected, test_results,
                                  format_string)
    actual = problem5(words)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10
    expected = "h"
    words = [("a" * 100) + "rgh"]
    print_expected_result_of_test([words], expected, test_results,
                                  format_string)
    actual = problem5(words)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Summary:
    print_summary_of_test_results(test_results)


def problem5(words):
    """
    What comes in: A non-empty sequence of words, where a "word"
      is a non-empty string containing only the letters a through z.
    What goes out:
      -- Returns the last letter of the last word in the given sequence.
    Side effects:   None.
    Examples:
      -- problem5( ["ok", "one", "four"] )  returns  "r"
      -- problem5( ["a", "hello", "one"] )  returns  "e"
      -- problem5( ["robots"] )             returns  "s"
      -- problem5( ["these", "robots", "are", "lots", "of", "fun"] )
            returns  "n"
      -- problem5( ["i"] )   returns "i"

        ** ASK YOUR INSTRUCTOR FOR HELP **
        ** IF YOU DO NOT UNDERSTAND THE ABOVE SPECIFICATION. **

    Type hints:
      :type words: list[str] | tuple[str]
      :rtype: str
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
