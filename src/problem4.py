"""
Exam 2, Problem 4.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. Put your name in the line above

import testing_helper
import time


def main():
    """ Calls the TEST functions for this module """
    print()
    print("--------------------------------------------------")
    print("Un-comment the tests one by one")
    print("as you work the problems.")
    print("--------------------------------------------------")

    run_test_problem4a()
    run_test_problem4b()


###############################################################################
# TODO: 2.  READ the green doc-string for the:
#     - sum_of_digits
#   function defined below.
#   It is the same   sum_of_digits   function that you have seen previously.
#   You do NOT need to understand its implementation,
#   just its specification (per the doc-string).
#   You should  ** CALL **  this function as needed in implementing the
#   other functions.  After you have READ this, change its _TODO_ to DONE.
###############################################################################
def sum_of_digits(number):
    """
    What comes in:  An integer.
    What goes out:  Returns the sum of the digits in the given integer.
    Side effects:   None.
    Example:
      If the integer is 83135,
      this function returns (8 + 3 + 1 + 3 + 5), which is 20.
    """
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  sum_of_digits function - it has no _TODO_.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------
    if number < 0:
        number = -number

    digit_sum = 0
    while True:
        if number == 0:
            break
        digit_sum = digit_sum + (number % 10)
        number = number // 10

    return digit_sum


def run_test_problem4a():
    """ Tests the   problem4a   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem4a   function:")
    print("--------------------------------------------------")

    format_string = "    problem4a( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    numbers = [182, 203, 4444, 99, 511, 74, 25]
    m = 2
    n = 5
    s = 18
    expected = 99
    print_expected_result_of_test([numbers, m, n, s], expected, test_results,
                                  format_string)
    actual = problem4a(numbers, m, n, s)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:  Same as Test 1, but using a tuple (which is immutable)
    numbers = (182, 203, 4444, 99, 511, 74, 25)
    m = 2
    n = 5
    s = 18
    expected = 99
    print_expected_result_of_test([numbers, m, n, s], expected, test_results,
                                  format_string)
    actual = problem4a(numbers, m, n, s)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    numbers = [182, 203, 4444, 99, 511, 74, 25]
    m = 2
    n = 5
    s = 17
    expected = -1
    print_expected_result_of_test([numbers, m, n, s], expected, test_results,
                                  format_string)
    actual = problem4a(numbers, m, n, s)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    numbers = [182, 203, 4444, 99, 511, 74, 25]
    m = 0
    n = 6
    s = 7
    expected = 511
    print_expected_result_of_test([numbers, m, n, s], expected, test_results,
                                  format_string)
    actual = problem4a(numbers, m, n, s)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    numbers = [182, 203, 4444, 99, 25, 74, 511]
    m = 0
    n = 6
    s = 7
    expected = 25
    print_expected_result_of_test([numbers, m, n, s], expected, test_results,
                                  format_string)
    actual = problem4a(numbers, m, n, s)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    numbers = [222, 111, 529, 334, 1111, 999, 99, 123, 55]
    m = 0
    n = 0
    s = 6
    expected = 222
    print_expected_result_of_test([numbers, m, n, s], expected, test_results,
                                  format_string)
    actual = problem4a(numbers, m, n, s)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    numbers = [222, 111, 529, 334, 1111, 999, 99, 123, 55]
    m = 0
    n = 8
    s = 6
    expected = 222
    print_expected_result_of_test([numbers, m, n, s], expected, test_results,
                                  format_string)
    actual = problem4a(numbers, m, n, s)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    numbers = [222, 111, 529, 334, 1111, 999, 99, 123, 55]
    m = 1
    n = 8
    s = 6
    expected = 123
    print_expected_result_of_test([numbers, m, n, s], expected, test_results,
                                  format_string)
    actual = problem4a(numbers, m, n, s)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    numbers = [222, 111, 529, 334, 1111, 999, 99, 123, 55]
    m = 1
    n = 6
    s = 6
    expected = -1
    print_expected_result_of_test([numbers, m, n, s], expected, test_results,
                                  format_string)
    actual = problem4a(numbers, m, n, s)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Summary:
    print_summary_of_test_results(test_results)


def problem4a(numbers, m, n, s):
    """
    What comes in:
      - A sequence of non-negative numbers
      - Non-negative integers m and n,
           where m <= n < length of the given sequence
      - Non-negative integer s
    What goes out:
      -- Returns the first number in the list:
          -- that is between indices m and n, inclusive, and
          -- whose sum of digits equals the given s.
         Breaks ties in favor of the first (i.e., lowest-index) such number.
         Returns -1 if there is no number in the list that satisfies
                    the given conditions.
    Side effects:   None.
    Examples:
      -- problem4a( [182, 203, 4444, 99, 511, 74, 25],
                    2, 5, 18 )
             looks at the items from indices 2 to 5, that is,
             the items 4444, 99, 511 and 74,
             and tries to find the first whose sum-of-digits is 18,
             so returns 99 (since the sum-of-digits of 4444 is 16
                            and the sum-of-digits of 99 is 18)

      -- problem4a( [182, 203, 4444, 99, 511, 74, 25],
                    2, 5, 17 )
             looks at the items from indices 2 to 5, that is,
             the items 4444, 99, 511 and 74,
             and tries to find the first whose sum-of-digits is 17,
             so returns -1
                (since none of those numbers has sum-of-digits equal to 17)

      -- problem4a( [182, 203, 4444, 99, 511, 74, 25],
                    0, 6, 7 )
             looks at the items from indices 0 to 7, that is,
             all the items in the list,
             and tries to find the first whose sum-of-digits is 7.
             There are two such numbers:  511 and 25, with the 511
             encountered first, so the function returns 511 in this example.

      -- If we reverse the 511 and 25 in the preceding example, that is,
         problem4a( [182, 203, 4444, 99, 25, 74, 511],
                    0, 6, 7 )
             the function returns 25 (instead of 511)
             since the 25 is encountered first in this example.

        ** ASK YOUR INSTRUCTOR FOR HELP **
        ** IF YOU DO NOT UNDERSTAND THE ABOVE SPECIFICATION. **

    Type hints:
      :type numbers: list[int] | tuple[int]
      :type m: int
      :type n: int
      :type s: int
    """
    ###########################################################################
    # TODO: 3. Implement and test this function.
    #          Tests have been written for you (above).
    ###########################################################################


def run_test_problem4b():
    """ Tests the   problem4b   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem4b   function:")
    print("--------------------------------------------------")

    format_string = "    problem4b( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    numbers = [182, 203, 511, 74, 55, 30, 25]
    expected = 511
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem4b(numbers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    numbers = [182, 203, 74, 55, 30, 25]
    expected = 25
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem4b(numbers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:  Same as the previous test but using a tuple (which is immutable)
    numbers = (182, 203, 74, 55, 30, 25)
    expected = 25
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem4b(numbers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    numbers = [5032]
    expected = 5032
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem4b(numbers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Summary:
    print_summary_of_test_results(test_results)


# See the IMPORTANT NOTE in the _TODO_ for the following problem.
def problem4b(numbers):
    """
    What comes in:
      - A non-empty sequence of non-negative numbers
    What goes out:
      -- Returns the first number in the list whose sum-of-digits
           equals the sum-of-digits of the last number in the list.

      See the IMPORTANT NOTE in the _TODO_ for this problem.

    Side effects:   None.
    Examples:
      -- problem4a( [182, 203, 511, 74, 55, 30, 25] )
           The last item (25) has 7 as its sum-of-digits,
           so the function returns 511
           (the first item whose sum-of-digits is 7) in this example.

      -- problem4a( [182, 203, 74, 55, 30, 25] )
           The last item (25) has 7 as its sum-of-digits,
           so the function returns 25
           (the first item whose sum-of-digits is 7) in this example.

        ** ASK YOUR INSTRUCTOR FOR HELP **
        ** IF YOU DO NOT UNDERSTAND THE ABOVE SPECIFICATION. **

    Type hints:
      :type numbers: list[int] | tuple[int]
    """
    ###########################################################################
    # TODO: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #  IMPORTANT NOTE:  This problem is only 1 point.
    #    You earn that point ONLY if you solve this problem
    #    by calling   problem4a   (that you implemented above)
    #    with appropriate arguments.
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
