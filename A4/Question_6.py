"""
Six most appropriate unittests for question_6:

1. Parallel Lines, AKA there are no intersections, so test two lines with the exact same slope but at different
points. The expected output is None, because the two lines never intersect.

2. A set of parallel lines that are really close together, but never meet. This should sill return None. In this case we
would test lines that are 0.1 units away to ensure the program considers the slightest difference, and that no accuracy
is lost throughout any calculations within the program.

3. A set of lines like in case 2, but this time, with two lines with negative slopes (going down and to the right).
We need to ensure the program still recognizes these lines as parallel and should return None.

4. A regular set of lines, one with a negative slope (i.e. moving down and to the right) and a positive slope (i.e.
moving up and to the left). This should return ONE POINT as there is only one clear intersection.

5. A set of lines with slopes so close, that the difference between them is 0.00001. The lines will eventually meet,
so we need to ensure the program recognizes such a small difference and returns one point of intersection.

6. Test two lines with the same exact slopes, with the same points. These lines are laying on top of one another and
this should return the first line argument.

"""
