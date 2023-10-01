"""
Exam 2, Problem 8.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. Put your name in the line above

import testing_helper
import time
import rosegraphics as rg


def main():
    """ Calls the TEST functions for this module """
    run_test_problem8()


def run_test_problem8():
    """ Tests the   problem8   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem8   function:")
    print("--------------------------------------------------")

    format_string = "    problem8( {}, m={} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1
    expected = 3 + 11  # which is 14
    points = [rg.Point(3, 10), rg.Point(22, 6), rg.Point(11, 20)]
    m = 10
    print_expected_result_of_test([points, m], expected, test_results,
                                  format_string)
    actual = problem8(points, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2
    expected = 11
    points = [rg.Point(3, 10), rg.Point(22, 6), rg.Point(11, 20)]
    m = 18
    print_expected_result_of_test([points, m], expected, test_results,
                                  format_string)
    actual = problem8(points, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3
    expected = 3 + 22 + 11  # which is 36
    points = [rg.Point(3, 10), rg.Point(22, 6), rg.Point(11, 20)]
    m = 6
    print_expected_result_of_test([points, m], expected, test_results,
                                  format_string)
    actual = problem8(points, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4
    expected = 2 + 10 + 3 + 5  # which is 20
    points = [rg.Point(3, 5), rg.Point(2, 6), rg.Point(10, 8), rg.Point(30, 3),
              rg.Point(3, 100), rg.Point(4, 4), rg.Point(5, 6), rg.Point(40, 1)]
    m = 6
    print_expected_result_of_test([points, m], expected, test_results,
                                  format_string)
    actual = problem8(points, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4
    expected = 2 + 10 + 3 + 5  # which is 20
    points = (rg.Point(3, 5), rg.Point(2, 6), rg.Point(10, 8), rg.Point(30, 3),
              rg.Point(3, 100), rg.Point(4, 4), rg.Point(5, 6), rg.Point(40, 1))
    m = 6
    print_expected_result_of_test([points, m], expected, test_results,
                                  format_string)
    actual = problem8(points, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6
    expected = 3 + 2 + 10 + 30 + 3 + 4 + 5 + 40  # which is 97
    points = (rg.Point(3, 5), rg.Point(2, 6), rg.Point(10, 8), rg.Point(30, 3),
              rg.Point(3, 100), rg.Point(4, 4), rg.Point(5, 6), rg.Point(40, 1))
    m = 1
    print_expected_result_of_test([points, m], expected, test_results,
                                  format_string)
    actual = problem8(points, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7
    expected = 3 + 2 + 10 + 30 + 3 + 4 + 5  # which is 57
    points = (rg.Point(3, 5), rg.Point(2, 6), rg.Point(10, 8), rg.Point(30, 3),
              rg.Point(3, 100), rg.Point(4, 4), rg.Point(5, 6), rg.Point(40, 1))
    m = 2
    print_expected_result_of_test([points, m], expected, test_results,
                                  format_string)
    actual = problem8(points, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8
    expected = 3 + 2 + 10 + 30 + 3 + 4 + 5  # which is 57
    points = (rg.Point(3, 5), rg.Point(2, 6), rg.Point(10, 8), rg.Point(30, 3),
              rg.Point(3, 100), rg.Point(4, 4), rg.Point(5, 6), rg.Point(40, 1))
    m = 3
    print_expected_result_of_test([points, m], expected, test_results,
                                  format_string)
    actual = problem8(points, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9
    expected = 3 + 2 + 10 + 3 + 5  # which is 23
    points = (rg.Point(3, 5), rg.Point(2, 6), rg.Point(10, 8), rg.Point(30, 3),
              rg.Point(3, 100), rg.Point(4, 4), rg.Point(5, 6), rg.Point(40, 1))
    m = 5
    print_expected_result_of_test([points, m], expected, test_results,
                                  format_string)
    actual = problem8(points, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10
    expected = 2 + 10 + 3 + 5  # which is 20
    points = (rg.Point(3, 5), rg.Point(2, 6), rg.Point(10, 8), rg.Point(30, 3),
              rg.Point(3, 100), rg.Point(4, 4), rg.Point(5, 6), rg.Point(40, 1))
    m = 6
    print_expected_result_of_test([points, m], expected, test_results,
                                  format_string)
    actual = problem8(points, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11
    expected = 10 + 3  # which is 13
    points = (rg.Point(3, 5), rg.Point(2, 6), rg.Point(10, 8), rg.Point(30, 3),
              rg.Point(3, 100), rg.Point(4, 4), rg.Point(5, 6), rg.Point(40, 1))
    m = 7
    print_expected_result_of_test([points, m], expected, test_results,
                                  format_string)
    actual = problem8(points, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12
    expected = 10 + 3  # which is 13
    points = (rg.Point(3, 5), rg.Point(2, 6), rg.Point(10, 8), rg.Point(30, 3),
              rg.Point(3, 100), rg.Point(4, 4), rg.Point(5, 6), rg.Point(40, 1))
    m = 8
    print_expected_result_of_test([points, m], expected, test_results,
                                  format_string)
    actual = problem8(points, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 13
    expected = 3
    points = (rg.Point(3, 5), rg.Point(2, 6), rg.Point(10, 8), rg.Point(30, 3),
              rg.Point(3, 100), rg.Point(4, 4), rg.Point(5, 6), rg.Point(40, 1))
    m = 9
    print_expected_result_of_test([points, m], expected, test_results,
                                  format_string)
    actual = problem8(points, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 14
    expected = 0
    points = (rg.Point(3, 5), rg.Point(2, 6), rg.Point(10, 8), rg.Point(30, 3),
              rg.Point(3, 100), rg.Point(4, 4), rg.Point(5, 6), rg.Point(40, 1))
    m = 101
    print_expected_result_of_test([points, m], expected, test_results,
                                  format_string)
    actual = problem8(points, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Summary:
    print_summary_of_test_results(test_results)


def problem8(points, m):
    """
    What comes in:
      -- A sequence of rg.Point objects, and
      -- A positive integer m.
    What goes out:
       Returns the sum of the x-coordinates of all of the Point objects
       in the given sequence whose y-coordinate is greater than or equal to
       the given integer m.  Returns 0 if NONE of the Point objects has
       y-coordinate greater than or equal to m.
    Side effects: None.
    Examples:
      points = [rg.Point(3, 10),
                rg.Point(22, 6),
                rg.Point(11, 20)]
      if the sequence is the above sequence:
        -- if m = 10, then this function returns 3 + 11, which is 14,
             since the two Points with y-coordinate >= 10 are
             rg.Point(3, 10) and rg.Point(11, 20),
             and the x-coordinates of those Points are 3 and 11,
             whose sum is 3 + 11, that is, 14
        -- if m = 18, then this function returns 11,
             since only rg.Point(11, 20) has y-coordinate >= 18,
             and the sum of the (only) x-coordinates is 11.
        -- if m = 6 (or anything less than or equal to 6),
             then all three Points have y-coordinate less than or equal to m,
             and so the function returns the sum of the three x-coordinates,
             3 + 22 + 11, which is 36.
        -- if m = 21 (or anything greater than or equal to 21),
             then NONE of the Points have y-coordinate less than or equal to m,
             and so the function returns 0 (by definition).

      Another example:
        if points = [rg.Point(3, 5),  rg.Point(2, 6),   rg.Point(10, 8),
                     rg.Point(30, 3), rg.Point(3, 100), rg.Point(4, 4),
                     rg.Point(5, 6),  rg.Point(40, 1)]
        and m = 6, then this function returns  2 + 10 + 3 + 5, which is 20

     ** ASK YOUR INSTRUCTOR FOR HELP **
        ** IF YOU DO NOT UNDERSTAND THE ABOVE SPECIFICATION. **
    Type hints:
      :type points: list[rg.Point] | tuple[rg.Point]
      :type m: int
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
