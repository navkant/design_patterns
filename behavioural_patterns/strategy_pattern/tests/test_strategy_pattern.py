import unittest


class ExampleTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_function(self):
        self.assertEqual(1, 2)


if __name__ == "__main__":
    unittest.main()
