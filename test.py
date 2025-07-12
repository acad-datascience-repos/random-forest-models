import unittest
from assignment import train_random_forest_on_wine

class TestRandomForest(unittest.TestCase):
    def test_train_random_forest_on_wine(self):
        accuracy = train_random_forest_on_wine()
        self.assertIsInstance(accuracy, float)
        # Check for a reasonable accuracy
        self.assertGreater(accuracy, 0.9)

if __name__ == '__main__':
    unittest.main()
