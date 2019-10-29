from unittest import TestCase

from ListPuzzles import same_end
from ListPuzzles import list_sum
from ListPuzzles import backwards
from ListPuzzles import average
from ListPuzzles import count_evens
from ListPuzzles import big_diff
from ListPuzzles import centered_average


class TestListPuzzles(TestCase):
    # same_end Tests
    def test_same_end1(self):
        self.assertEqual(same_end([1, 2, 3], [7, 3]), True)

    def test_same_end2(self):
        self.assertEqual(same_end([1, 2, 3], [7, 3, 2]), False)

    def test_same_end3(self):
        self.assertEqual(same_end([1, 2, 3], [1, 3]), True)

    def test_same_end4(self):
        self.assertEqual(same_end(["pig"], ["dog", "Pig"]), False)

    def test_same_end5(self):
        self.assertEqual(same_end(["Madison", "Marshall", "Frank", 1],["Francine", 1]), True)

    # list_sum Tests
    def test_list_sum1(self):
        self.assertEqual(list_sum([1, 2, 3]), 6)

    def test_list_sum2(self):
        self.assertEqual(list_sum([5, 11, 2]), 18)

    def test_list_sum3(self):
        self.assertEqual(list_sum([7, 0, 0]), 7)

    def test_list_sum4(self):
        self.assertEqual(list_sum([2,5,-3,6,10]), 20)

    def test_list_sum5(self):
        self.assertEqual(list_sum([-3, -5, 10, -2]), 0)

    # backwards Tests
    def test_backwards1(self):
        self.assertEqual(backwards([1, 3]), [3, 1])

    def test_backwards2(self):
        self.assertEqual(backwards([5, 11, 2]), [2, 11, 5])

    def test_backwards3(self):
           self.assertEqual(backwards([5, 11, 9, 8]), [8, 9, 11, 5])

    def test_backwards4(self):
        self.assertEqual(backwards(["pig", "horse", "cat"]), ["cat", "horse", "pig"])

    def test_backwards5(self):
        self.assertEqual(backwards([123]), [123])

    # average Tests
    def test_average1(self):
        self.assertAlmostEqual(average([1, 3]), 2, 5)

    def test_average2(self):
        self.assertAlmostEqual(average([5, 11, 2]), 6, 5)

    def test_average3(self):
        self.assertAlmostEqual(average([7, 0, 1]), 2.66667, 5)

    def test_average4(self):
        self.assertAlmostEqual(average([12,-4,5,9]), 5.5, 5)

    def test_average5(self):
        self.assertAlmostEqual(average([123]), 123, 5)

    # count_evens Tests
    def test_count_evens1(self):
        self.assertEqual(count_evens([1, 3]), 0)

    def test_count_evens2(self):
        self.assertEqual(count_evens([5, 11, 2]), 1)

    def test_count_evens3(self):
        self.assertEqual(count_evens([2, 2, 0]), 3)

    def test_count_evens4(self):
        self.assertEqual(count_evens([12, -4, 5, 9]), 2)

    def test_count_evens5(self):
        self.assertEqual(count_evens([1230]), 1)

    # big_diff Tests
    def test_big_diff1(self):
        self.assertEqual(big_diff([10, 3, 5, 6]), 7)

    def test_big_diff2(self):
        self.assertEqual(big_diff([7, 2, 10, 9]), 8)

    def test_big_diff3(self):
        self.assertEqual(big_diff([-20, -10, -7, -2]), 18)

    def test_big_diff4(self):
        self.assertEqual(big_diff([12, -4, 5, 9]), 16)

    def test_big_diff5(self):
        self.assertEqual(big_diff([1, 1, 1, 1, 1]), 0)

    # centered_average Tests
    def test_centered_average1(self):
        self.assertAlmostEqual(centered_average([1, 2, 3, 4, 100]), 3, 5)

    def test_centered_average2(self):
        self.assertAlmostEqual(centered_average([1, 1, 5, 10, 8, 7]), 5.25, 5)

    def test_centered_average3(self):
        self.assertAlmostEqual(centered_average([-10, -4, -2, -4, -2, 1]), -3, 5)

    def test_centered_average4(self):
        self.assertAlmostEqual(centered_average([1, 8, 50]), 8, 5)

    def test_centered_average5(self):
        self.assertAlmostEqual(centered_average([-10, -34, -5, 0, -3, -4]), -5.5, 5)
