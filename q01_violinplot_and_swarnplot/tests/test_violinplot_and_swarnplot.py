from unittest import TestCase
from ..build import plot
from inspect import getargspec

class TestPlot_violinplot_and_swarnplot(TestCase):
    def test_violinplot_and_swarnplot(self):
                # Input parameters tests
        args = getargspec(plot)
        self.assertEqual(len(args[0]), 4, "Expected argument(s) %d, Given %d" % (4, len(args[0])))
        self.assertEqual(args[3], None, "Expected default values do not match given default values")
		
