"""
Exam 2, Problem 9.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. Put your name in the line above

import testing_helper
import time


def main():
    """ Calls the TEST functions for this module """
    run_test_problem9()


###############################################################################
# TODO: 2.  READ the green doc-string below for the:
#      is_prime
#   function defined below.  It is the same  is_prime  function that you have
#   seen previously.  You do NOT need to understand its implementation,
#   just its specifications (per the doc-string).  You should  ** CALL **
#   that function as needed in implementing other function(s) in this module.
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


def run_test_problem9():
    """ Tests the   problem9   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem9   function:")
    print("--------------------------------------------------")

    format_string = "    problem9( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1
    expected = True
    integers = [12, 5, 22, 5, 21, 11, 10, 13, 13, 4, 23]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem9(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2
    expected = True
    integers = [12, 5, 22, 21, 11, 10, 13, 4, 23]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem9(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3
    expected = False
    integers = [12, 5, 22, 21, 11, 10, 23, 4, 13, 3]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem9(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4
    expected = True
    integers = [3, 5, 7, 11]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem9(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5
    expected = True
    integers = (10, 8, 6, 4)
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem9(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6
    expected = False
    integers = (11, 2, 6, 4, 10, 21, 15)
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem9(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7
    expected = True
    integers = [3, 10, 8, 6, 5, 4]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem9(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8
    expected = True
    integers = [7, 14, 7, 14, 7]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem9(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9
    expected = False
    integers = [7, 14, 7, 14, 7, 5]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem9(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10
    expected = False
    integers = [7, 14, 7, 14, 7, 14, 5]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem9(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11
    expected = False
    integers = [7, 14, 3, 14, 7, 14, 7]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem9(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12
    expected = True
    integers = [18, 4, 13, 27, 4, 21, 4, 13, 4, 4, 4]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem9(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 13
    expected = False
    integers = [18, 4, 14, 7, 7, 14, 4, 4, 4, 3, 4]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem9(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 14
    expected = False
    integers = [18, 4, 14, 8, 7, 11, 4, 13, 4, 4, 3, 5, 23, 4]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem9(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)
    # Summary:
    print_summary_of_test_results(test_results)

    # Test 15
    expected = False
    integers = [11, 2]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem9(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 16
    expected = False
    integers = [18, 4, 14, 8, 8, 11, 20, 4, 4, 2, 4]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem9(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 17
    expected = True
    integers = [18, 4, 14, 8, 8, 11, 11]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem9(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 18
    expected = True
    integers = [18, 4, 14, 8, 8, 11, 22]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem9(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 19  (note: I should have included this test case but did not do so)
    expected = True
    integers = [18]
    print_expected_result_of_test([integers], expected, test_results,
                                  format_string)
    actual = problem9(integers)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Summary
    print_summary_of_test_results(test_results)


###############################################################################
# Be sure to read the IMPORTANT note in _TODO_ of the following problem!
###############################################################################
def problem9(integers):
    """
    What comes in: A non-empty sequence of integers,
       where each integer in the sequence is guaranteed to be at least 2.
    What goes out:
       Returns True if the prime numbers in the sequence form an increasing
       sequence, that is, each prime number in the sequence is greater than
       or equal to the preceding prime number in the sequence
       except possibly for the first prime number in the sequence
       (which has no preceding prime number).
       Otherwise, the function returns False.
       Note:  If there are zero or one prime numbers in the sequence,
       this function returns True.
    Side effects: None
    Examples:
      - problem9( [12, 5, 22, 5, 21, 11, 10, 13, 13, 4, 23] )  returns True
           - since the prime numbers in the sequence are
                5, 5, 11, 13, 13, and 23,
             and that forms an increasing sequence
             (each number is greater than or equal to its predecessor)
      - problem9( [12, 5, 22, 21, 11, 10, 13, 4, 23] )    returns  True
            - since the prime numbers in the sequence are
                 5, 11, 13, 23,
              and that forms an increasing sequence
              (each number is greater than or equal to its predecessor)
      - problem9( [12, 5, 22, 21, 11, 10, 23, 4, 13, 3]  returns False
            - since the prime numbers in the sequence are
                 5, 11, 23, and 13
              and that does NOT form an increasing sequence
              (because the last item, 13, is NOT greater than or equal to
              the preceding item, 23)
      - problem9( [3, 5, 7, 11] )      returns  True
      - problem9( [10, 8, 6, 4] )      returns  True
          (no primes, so the condition is satisfied for "all" of them)
      - problem9( [11, 2, 6, 4, 10, 21, 15] )  returns True
           (just one prime, so the condition is satisfied for "all" of them)
      - problem9( [3, 10, 8, 6, 5, 4] )  returns  True  (3 <= 5)
      - problem9( [7, 14, 7, 14, 7] )    returns True  (7 <= 7 <= 7)
      - problem9( [7, 14, 7, 14, 7, 5] ) returns False
           (since the  5  is less than the  7  that precedes it)
       - problem9( [7, 14, 7, 14, 7, 14, 5] ) returns False
           (since the  5  is less than the  7  that precedes it)
      - problem9( [7, 14, 3, 14, 7, 14, 7] ) returns False
           (since the  3  is less than the  7  that precedes it)

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
    #    **  the   is_prime   function that is DEFINED ABOVE.
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
