from unittest import TestCase
from ..build import jointplot
from inspect import getargspec


class TestPlot_with_Pearson_correlation(TestCase):
    def test_plot_with_Pearson_correlation(self):  # Input parameters tests
        args = getargspec(jointplot)
        self.assertEqual(len(args[0]), 6, "Expected argument(s) %d, Given %d" % (6, len(args[0])))

    def test_plot_with_Pearson_correlation_default(self):  # Input parameters defaults
    	args = getargspec(jointplot)
        self.assertEqual(args[3], (0.95, 'hex', 10), "Expected default values do not match given default values")

        # Return data type
        # Nothing to test here

        # Return value tests
        # Nothing to test here
