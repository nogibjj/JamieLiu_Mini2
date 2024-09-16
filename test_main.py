import unittest
import pandas as pd
from main import (
    load_dataset,
    process_mean,
    process_median,
    process_max,
    process_min,
    process_std,
    bar_visual,
    hist_visual,
    g_describe,
)


class TestMainFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Load the dataset once for all tests."""
        cls.df = load_dataset()

    def test_load_dataset(self):
        """Test if the dataset loads correctly."""
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertEqual(self.df.shape, (56, 8))

    def test_process_mean(self):
        """Test the mean calculation."""
        col = "incidents_85_99"
        expected_mean = self.df[col].mean()
        self.assertEqual(process_mean(self.df, col), expected_mean)

    def test_process_median(self):
        """Test the median calculation."""
        col = "incidents_85_99"
        expected_median = self.df[col].median()
        self.assertEqual(process_median(self.df, col), expected_median)

    def test_process_max(self):
        """Test the max value calculation."""
        col = "fatalities_85_99"
        expected_max = self.df[col].max()
        self.assertEqual(process_max(self.df, col), expected_max)

    def test_process_min(self):
        """Test the min value calculation."""
        col = "fatal_accidents_85_99"
        expected_min = self.df[col].min()
        self.assertEqual(process_min(self.df, col), expected_min)

    def test_process_std(self):
        """Test the standard deviation calculation."""
        col = "incidents_00_14"
        expected_std = self.df[col].std()
        self.assertEqual(process_std(self.df, col), expected_std)

    def test_g_describe(self):
        """Test the descriptive statistics output."""
        desc = g_describe()
        # Number of rows in the description (count, mean, std, etc.)
        self.assertEqual(desc.shape[0], 8)

    def test_visuals(self):
        """Test if visual functions run without errors (basic functionality)."""
        try:
            bar_visual(self.df, "incidents_85_99", jupyter_render=False)
            hist_visual(self.df, "fatal_accidents_85_99", jupyter_render=False)
        except Exception as e:
            self.fail(f"Visualization functions raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()
