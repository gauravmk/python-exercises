import re, functools, unittest, math


# LIST COMPREHENSION EXERCISES
# 
# Each one of these can be solved using list comprehension
# See: https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
# This also means each one of these can be done in a single line.
# Go for doing one-liners, don't worry about readability for now.
# I've done the first one for you


##### Sample Problem #####
# Double each element of the list
# e.g. [1,4,6] => [2,8,12]
def double_list(list):
        return [x * 2 for x in list]


##### Problem 1 #####
# Cube each element of the list
# e.g. [1,3,5] => [1,9,125]
def cube_list(list):
        raise NotImplementedError


##### Problem 2 #####
# Only return log lines that are critical errors.
# Here's a helper function to check if a log is critical
# Use it to filter a set of log lines just to the critical ones
def is_critical_log(log_line):
        return re.match(r'Log line:(.*)level=critical', log_line) != None

def get_critical_logs(log_lines):
        raise NotImplementedError


##### Problem 3 #####
# Checks if a string is a palindrome
# That means it reads the same backwards and forwards
# e.g. racecar
# Yes this can be done as a one liner using list comprehension
def is_palindrome(sentence):
        raise NotImplementedError
        

##### Problem 4 #####
# The distance between two points 
# In 2D space, you use pythagoreans theorem. Square the differences in 
# the x coordinates plus the square of the differences in the y coords
# and square root that whole thing (c = sqrt(a^2 + b^2)). 
# The same principle applies in N dimensional space. For two points
# a = (a1, a2, a3, a4, a5)
# b = (b1, b2, b3, b4, b5)
# then distance(a, b) = sqrt((a1 - b1)^2 + (a2 - b2)^2 + (a3 - b3)^2 ....)
# you're given a and b as two arrays of the same length: [a1, a2, a3...] and [b1, b2, b3...]
# return the distance between these two points
def distance(a, b):
        raise NotImplementedError

class ListComprehensionTest(unittest.TestCase):
        def test_double(self):
                self.assertEqual(double_list([1,5,7]), [2,10,14])

        def test_cube(self):
                self.assertEqual(cube_list([1,3,5]), [1,27,125])

        def test_critical_logs(self):
                self.assertEqual(get_critical_logs(
                        [
                                "Log line: Lunch is ready level=critical",
                                "Log line: A shipped a bug level=warning",
                                "Log line: Everything's on fire level=critical",
                                "Log line: B pushed a fix level=info"
                        ]),
                        [
                                "Log line: Lunch is ready level=critical",
                                "Log line: Everything's on fire level=critical" 
                        ]
                )

        def test_palindrome(self):
                self.assertEqual(is_palindrome("madamimadam"), True)
                self.assertEqual(is_palindrome("lool"), True)
                self.assertEqual(is_palindrome("thisshouldfailsiht"), False)

        def test_distance(self):
                self.assertEqual(distance([6,12,20], [3, 16, 32]), 13)
                self.assertEqual(distance([102,120], [99, 124]), 5)

if __name__ == '__main__':
    unittest.main()