"""
Exam 2, Problem 7.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. Put your name in the line above

import testing_helper
import time


def main():
    """ Calls the TEST functions for this module """
    run_test_problem7()


###############################################################################
# TODO: 2.  READ the green doc-strings below for the:
#      is_prime
#      get_prime_factorization
#   functions defined below. You do NOT need to understand their
#   implementations, just their specifications (per the doc-strings).
#   You should  ** CALL ** those functions as needed in implementing other
#   function(s) in this module.
#   After you have READ this, change its _TODO_ to DONE.
###############################################################################
def is_prime(n):
    """
    What comes in:  An integer n >= 2.
    What goes out:
      -- Returns True if the given integer is prime,
         else returns False.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
    Note: The algorithm used here is simple and clear but slow.
    """
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  is_prime  function - it has no _TODO_.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------


def get_prime_factorization(n):
    """
    What comes in:  A positive integer that is at least 2.
    What goes out:
      -- Returns the list of the prime numbers that,
            when multiplied together, equals the given integer.
            The numbers in the list are returned in ascending order.
    Side effects:   None.
    Examples:
      -- get_prime_factorization(140)  returns  [2, 2, 5, 7]
      -- get_prime_factorization(11)   returns  [11]
      -- get_prime_factorization(91)   returns  [7, 13]
      -- get_prime_factorization(825)  returns  [3, 5, 5, 11]
      -- get_prime_factorization(32)   returns  [2, 2, 2, 2, 2]
      -- get_prime_factorization(210)  returns  [2, 3, 5, 7]
      -- get_prime_factorization(211)  returns  [211]
      -- get_prime_factorization(212)  returns  [2, 2, 53]
    Note: The algorithm used here is simple and clear but not very fast.
    """
    factorization = []
    remaining = n
    for k in range(2, n + 1):
        if is_prime(k):
            while True:
                if remaining % k == 0:
                    factorization.append(k)
                    remaining = remaining // k
                else:
                    break
    return factorization

    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  get_prime_factorization  function
    #   - it has no _TODO_.  Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------


def run_test_problem7():
    """ Tests the   problem7   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem7   function:")
    print("--------------------------------------------------")

    format_string = "    problem7( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1
    expected = 6
    integers = [825, 11, 140, 32, 91, 72, 64, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2
    expected = 0
    integers = [825, 11, 140, 91, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3
    expected = 1
    integers = [11, 140, 91, 6, 202]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4
    expected = 0
    integers = [64, 825, 11, 140, 32, 91, 72, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5
    expected = 1
    integers = [825, 64, 11, 140, 32, 91, 72, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6
    expected = 2
    integers = [825, 11, 64, 140, 32, 91, 72, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7
    expected = 3
    integers = [825, 11, 140, 64, 32, 91, 72, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8
    expected = 4
    integers = [825, 11, 140, 32, 64, 91, 72, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9
    expected = 5
    integers = [825, 11, 140, 32, 91, 64, 72, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10
    expected = 6
    integers = [825, 11, 140, 32, 91, 72, 64, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11
    expected = 7
    integers = [825, 11, 140, 32, 91, 72, 6, 64]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12
    expected = 0
    integers = [96, 64, 825, 11, 140, 32, 91, 72, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 13
    expected = 1
    integers = [825, 96, 64, 11, 140, 32, 91, 72, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 14
    expected = 2
    integers = [825, 11, 96, 64, 140, 32, 91, 72, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 15
    expected = 3
    integers = [825, 11, 140, 96, 64, 32, 91, 72, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 16
    expected = 4
    integers = [825, 11, 140, 32, 96, 64, 91, 72, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 17
    expected = 5
    integers = [825, 11, 140, 32, 91, 96, 64, 72, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 18
    expected = 6
    integers = [825, 11, 140, 32, 91, 72, 96, 64, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 19
    expected = 7
    integers = [825, 11, 140, 32, 91, 72, 6, 96, 64]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 20
    expected = 7
    integers = [825, 11, 140, 32, 91, 72, 6, 64, 96]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 21
    expected = 0
    integers = [576, 825, 11, 9997, 140, 32, 91, 72, 6, 64, 96]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 22
    expected = 2
    integers = [825, 11, 576, 9997, 140, 32, 91, 72, 6, 64, 96]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 23
    expected = 3
    integers = [825, 11, 9997, 576, 140, 32, 91, 72, 6, 64, 96]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 24
    expected = 10
    integers = [825, 11, 9997, 140, 32, 91, 72, 6, 64, 96, 576]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 25
    expected = 10
    integers = [825, 11, 9997, 140, 32, 91, 72, 6, 64, 96, 576, 9997]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 26
    expected = 6
    integers = [825, 11, 140, 32, 91, 72, 64, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 27
    expected = 3
    integers = [825, 11, 140, 32, 91, 72, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 28
    expected = 0
    integers = [64, 825, 11, 140, 32, 91, 72, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 29
    expected = 1
    integers = [825, 64, 11, 140, 32, 91, 72, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 30
    expected = 2
    integers = [825, 11, 64, 6, 140, 72, 91, 32]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 31
    expected = 7
    integers = [825, 11, 6, 140, 72, 91, 32, 64]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 32
    expected = 0
    integers = [825]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 33
    expected = 0
    integers = [10000, 2]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 34
    expected = 1
    integers = [2, 10000]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 35
    expected = 4
    integers = [6, 8, 6, 9, 625, 6, 70]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 36
    expected = 1
    integers = [6, 8, 6, 9, 6, 70]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 37
    expected = 8
    integers = [8, 6, 9, 6, 70, 2, 12, 6, 60]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 38
    expected = 4
    integers = [6, 9, 625, 6, 1920, 7000]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 39
    expected = 4
    integers = [6, 9, 625, 6, 192, 70]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 40
    expected = 5
    integers = [192, 6, 9, 625, 6, 384, 128, 70]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 41
    expected = 2
    integers = [2, 3, 4, 5, 6]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem7(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Summary:
    print_summary_of_test_results(test_results)


###############################################################################
# Be sure to read the IMPORTANT note in _TODO_ of the following problem!
###############################################################################
def problem7(integers):
    """
    What comes in: A non-empty sequence of positive integers,
                   where each integer is guaranteed to be at least 2.
    What goes out:
       Returns the index of the item in the sequence whose prime
       factorization is longest.  Break ties in favor of the smallest index.
    Side effects: None
    Examples:

    Note that you are GIVEN (ABOVE) a function to compute prime factorization.

      Consider [825, 11, 140, 32, 91, 72, 64, 6].
      Note that the prime factorizations of those integers are:
        for 825: [3, 5, 5, 11]
        for 11:  [11]
        for 140: [2, 2, 5, 7]
        for 32:  [2, 2, 2, 2, 2]
        for 91:  [7, 13]
        for 72:  [2, 2, 2, 3, 3]
        for 64:  [2, 2, 2, 2, 2, 2]
        for 6:   [2, 3]
      - problem7( [825, 11, 140, 32, 91, 72, 64, 6] )
           returns 6  because the longest prime factorization for those
           integers is 64 = [2, 2, 2, 2, 2, 2], and 64 is at index 6
      - problem7( [825, 11, 140, 91, 6] )
           returns 0  because the longest prime factorization for those
           integers is 825 = [3, 5, 5, 11], and 825 is at index 0
      - problem7( [11, 140, 91, 6, 202] )
           returns 1  because the longest prime factorization for those
           integers is 140 = [2, 2, 5, 7], and 140 is at index 1

       ** ASK YOUR INSTRUCTOR FOR HELP **
       ** IF YOU DO NOT UNDERSTAND THE ABOVE SPECIFICATION. **
    Type hints:
      :type integers: list[int] | tuple[int]
    """
    ###########################################################################
    # TODO: 3. Implement and test this function.
    #          Tests have been written for you (above).
    #   IMPORTANT:
    #    **  For full credit you must appropriately use (call)
    #    **  the   get_prime_factorization   function that is DEFINED ABOVE.
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
