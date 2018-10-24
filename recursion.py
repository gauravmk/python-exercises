import re, functools, unittest


# RECURSION EXERCISES
# 
# Each one of these can be solved using recursion


##### Problem 1 #####
# choose via Pascal's Triangle
# The "choose" operation in combinatorics means the number of ways you can
# choose k items. For example: The number of unique pairs of socks you can
# generate from 10 disparate socks is "10 choose 2". One way to compute
# "choose" is surprisingly using Pascal's Triangle:
# https://en.wikipedia.org/wiki/Pascal%27s_triangle
#
# (gaurav edit: Sorry this is an unnecessary long-winded explanation but I 
# just think it's the coolest thing. You're free skip the explanation. The 
# math isn't that relevant. It just blows my mind)
#
# N choose K is the number in the Nth row and the Kth column of pascals
# triangle. Pascal's triangle is recursively defined (each element is the sum
# of the two above it). Compute N choose K knowing this recursive relationship
def choose(n, k):
    raise NotImplementedError


##### LIST EXERCISES #####
# Here's a basic implementation of a linked list
# example usage:
# list = ListNode('r', ListNode('e', ListNode('g'))) ## looks like r -> e -> g
# list.first            ## r
# list.rest             ## e -> g
# list.rest.rest.first  ## g
class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def first(self):
        return self.data

    def rest(self):
        return self.next


##### Problem 2 #####
# Get the length of a singly linked list
# Remember to use recursion!
def list_length(list):
    raise NotImplementedError


##### Problem 3 #####
# Returns true if the two lists have 
# all the same elements.
def lists_equal(a, b):
    raise NotImplementedError


##### Problem 4 #####
# Get the maximum number in a singly linked list
# e.g. 4 -> 3 -> 6 -> 2 => 6
def list_max(list):
    raise NotImplementedError


##### Problem 5 #####
# Return the last element of the list
# e.g. 4 -> 3 -> 6 -> 2 => 2
def last_elt(list):
    raise NotImplementedError


def test_list():
    return ListNode(2, ListNode(6, ListNode(4, None)))

class RecursionTest(unittest.TestCase):
        def test_choose(self):
                self.assertEqual(choose(10, 5), 252)
                self.assertEqual(choose(6, 6), 1)

        def test_list_length(self):
                self.assertEqual(list_length(test_list()), 3)

        def test_lists_equal(self):
                self.assertEqual(lists_equal(test_list(), test_list()), True)
                self.assertEqual(lists_equal(test_list().rest, test_list()), True)

        def test_list_max(self):
                self.assertEqual(list_max(test_list()), 6)

        def test_last_elt(self):
                self.assertEqual(list_max(test_list()), 4)

if __name__ == '__main__':
    unittest.main()