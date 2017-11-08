from unittest import TestCase
from inspect import getargspec
from ..build import pairgrid


class TestPlot_pairgrid_plot(TestCase):
    def test_pairgrid_plot(self):

        # Input parameters tests
        args = getargspec(pairgrid)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args[0])))
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

        # Return data type
        # Nothing to test here

        # Return value tests
        # Nothing to test here

