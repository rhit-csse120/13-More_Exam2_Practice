"""
Exam 2, Problem 3.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. Put your name in the line above

import testing_helper
import time


def main():
    """ Calls the TEST functions for this module """
    run_test_problem3()


def run_test_problem3():
    """ Tests the    problem3    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3  function:')
    print('--------------------------------------------------')

    format_string = '    problem3( {!r}, {!r} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = [40, 30, 91, 12, 11, 22, 25]
    sequence1 = [40, 22, 91, 80, 11, 40, 25]
    sequence2 = [10, 30, 20, 12, 10, 22, 27]
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = problem3(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = ["a", "h", "c", "j", "e", "l"]
    sequence1 = "abcdef"
    sequence2 = "ghijkl"
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = problem3(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = [40, 30, 91, 12, 11, 22, 25, 99]
    sequence1 = (40, 22, 91, 80, 11, 40, 25, 26)
    sequence2 = [10, 30, 20, 12, 10, 22, 27, 99]
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = problem3(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = [10, 22, 20, 80, 10, 40, 27]
    sequence1 = [10, 30, 20, 12, 10, 22, 27]
    sequence2 = (40, 22, 91, 80, 11, 40, 25)

    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = problem3(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = [333]
    sequence1 = [333]
    sequence2 = [100]
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = problem3(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = []
    sequence1 = []
    sequence2 = []
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = problem3(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = list(range(1, 101))
    sequence1 = list(range(1, 101))
    sequence2 = list(range(1, 101))
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = problem3(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = [1, 2] * 50
    sequence1 = [1] * 100
    sequence2 = [2] * 100
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = problem3(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem3(sequence1, sequence2):
    """
    What comes in:
      Two sequences, where both have the same length.
    What goes out:
      Returns a list containing the items in the sequences
      in a pattern like this:
        If  sequence1 is [r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, ...]
        and sequence2 is [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, ...]
        then this problem returns:
          [r0, s1, r2, s3, r4, s5, r6, s7, r8, s9, ...]
    Side effects: None.
    Examples:
      If the sequences are:
         [40, 22, 91, 80, 11, 40, 25]
         [10, 30, 20, 12, 10, 22, 27]
      then this function returns the list:
         [40, 30, 91, 12, 11, 22, 25]

      If the sequences are:
         "abcdef"
         "ghijkl"
      then this function returns the list:
         ["a", "h", "c", "j", "e", "l"]
    Type hints:
      :type sequence1: (list | tuple | str)
      :type sequence2: (list | tuple | str)
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
