import unittest
import estimator


class TestTimeInDays(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it returns time in days
        """
        timeToElapse = 35
        periodType = "days"
        result = estimator(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()