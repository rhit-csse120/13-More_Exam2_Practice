"""
Exam 2, Problem 2.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. Put your name in the line above

import testing_helper
import time


def main():
    """ Calls the TEST functions for this module """
    run_test_problem2()


def run_test_problem2():
    """ Tests the   problem2   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem2   function:")
    print("--------------------------------------------------")

    format_string = "    problem2( {}, {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    m = 2
    n = 5
    expected = [1, 2, 4, 8, 16, 32]
    print_expected_result_of_test([m, n], expected, test_results, format_string)
    actual = problem2(m, n)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    m = 7
    n = 3
    expected = [1, 7, 49, 343]
    print_expected_result_of_test([m, n], expected, test_results, format_string)
    actual = problem2(m, n)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    m = 8
    n = 6
    expected = [1, 8, 64, 512, 4096, 32768, 262144]
    print_expected_result_of_test([m, n], expected, test_results, format_string)
    actual = problem2(m, n)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    m = 5
    n = 0
    expected = [1]
    print_expected_result_of_test([m, n], expected, test_results, format_string)
    actual = problem2(m, n)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    m = 1
    n = 4
    expected = [1, 1, 1, 1, 1]
    print_expected_result_of_test([m, n], expected, test_results, format_string)
    actual = problem2(m, n)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Tests 6 and following (using list comprehension):
    has_failed = False
    for m in range(1, 10):
        if has_failed:
            break
        for n in range(20):
            expected = [m ** k for k in range(n + 1)]
            actual = problem2(m, n)
            if actual != expected:
                print()
                print("Test {}:".format(
                    6 + ((m - 1) * 20) + n))
                print("  This test case calls  problem2( {}, {} )".format(m, n))
                print("  Expected:", expected)
                print("  Actual:  ", actual)
                print("  *** FAILED the above test. ***", color="red")
                test_results = [test_results[0], test_results[1] + 1]
                has_failed = True
                break

    # Summary:
    print_summary_of_test_results(test_results)


def problem2(m, n):
    """
    What comes in:
      -- Non-negative integers m and n
    What goes out: Returns the list:
         [m ** 0,  m ** 1,  m ** 2, ...  m ** n]
    Side effects: None.
    Examples:
        problem2(2, 5) returns the list:
           [2 ** 0,  2 ** 1,  2 ** 2,  2 ** 3,  2 ** 4,  2 ** 5],
           that is, [1, 2, 4, 8, 16, 32]

        problem2(7, 3) returns the list:
           [7 ** 0,  7 ** 1,  7 ** 2,  7 ** 3],
           that is, [1, 7, 49, 343]

        problem2(8, 6) returns the list:
           [8 ** 0,  8 ** 1,  8 ** 2,  8 ** 3,  8 ** 4,  8 ** 5,  8 ** 6],
           that is, [1, 8, 64, 512, 4096, xxx]

        problem2(5, 0) returns the list:
           [5 ** 0],
           that is, [1]

     ** ASK YOUR INSTRUCTOR FOR HELP **
        ** IF YOU DO NOT UNDERSTAND THE ABOVE SPECIFICATION. **

    Type hints:
      :type m: int
      :type n: int
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
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
