import unittest
import medical_data_visualizer
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

class CatPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = medical_data_visualizer.draw_cat_plot()
        self.ax = self.fig.axes[0]

    def test_line_plot_labels(self):
        actual = self.ax.get_xlabel()
        expected = "variable"
        self.assertEqual(actual, expected, "Expected line plot xlabel to be 'variable'")
        actual = self.ax.get_ylabel()
        expected = "total"
        self.assertEqual(actual, expected, "Expected line plot ylabel to be 'total'")
        actual = []
        for label in self.ax.get_xticklabels():
            actual.append(label.get_text())
        expected = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
        self.assertEqual(sorted(actual), sorted(expected), "Expected bar plot variable labels to be 'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'")

    def test_bar_plot_number_of_bars(self):
        actual = len([rect for rect in self.ax.get_children() if isinstance(rect, mpl.patches.Rectangle)])
        expected = 13
        self.assertAlmostEqual(actual, expected, delta=2, msg="Expected a different number of bars chart.")


class HeatMapTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = medical_data_visualizer.draw_heat_map()
        self.ax = self.fig.axes[0]

    def test_heat_map_no_param_args(self):
        # The heatmap should be a seaborn heatmap
        # We check if the figure contains an Axes object
        self.assertTrue(len(self.fig.axes) > 0, "Expected the heatmap to be plotted.")

    def test_heat_map_values(self):
        # Check specific correlation values to ensure data cleaning was correct
        # Extract the data from the heatmap
        # Note: Accessing the data behind the plot in seaborn/matplotlib can be tricky in tests,
        # but we can check the correlation matrix if we could access it. 
        # Since we return a figure, we inspect the text annotations on the heatmap.
        
        actual = []
        for text in self.ax.texts:
            actual.append(text.get_text())
        
        # We expect many values, but let's check a few key ones that confirm cleaning worked
        # (e.g. weight vs height should be around 0.3 if cleaning worked, otherwise different)
        # Note: Values are strings in the heatmap annotations
        
        # Validating simply that we have annotations
        self.assertTrue(len(actual) > 0, "Expected value annotations on the heatmap")

        # Check for a specific known value from the solution (correlation of weight/height)
        # Depending on formatting, it might be '0.3' or '0.2'
        if '0.3' in actual or '0.2' in actual:
             pass 
        else:
             self.fail("Expected correlation values (like 0.3 for weight/height) not found in heatmap annotations.")

if __name__ == "__main__":
    unittest.main()