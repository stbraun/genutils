# coding=utf-8
"""
Tests for number related utilities.
"""
# Copyright (c) 2015 Stefan Braun
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE
# AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import unittest
import genutils.numbers as gn


class TestNumbers(unittest.TestCase):

    def setUp(self):
        self.evens = (0, 2, 4, 10, 102, 10000472, -2, -49026)
        self.odds = (1, 7, 23, 10481, -1, -173, 597104865)

    def test_is_odd(self):
        for x in self.evens:
            self.assertFalse(gn.is_odd(x))
        for x in self.odds:
            self.assertTrue(gn.is_odd(x))

    def test_is_even(self):
        for x in self.odds:
            self.assertFalse(gn.is_even(x))
        for x in self.evens:
            self.assertTrue(gn.is_even(x))

    def test_type_error(self):
        invalid_types = (1.2, -6.37, 'abc', [1, 2, 3], {'a': 2}, (1, 2, 3))
        for x in invalid_types:
            with self.assertRaises(TypeError):
                self.assertTrue(gn.is_odd(x))
