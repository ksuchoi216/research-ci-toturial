import unittest
# import sys

from main import hello_world


class TestMain(unittest.TestCase):
    def test_hello(self):
        ret = hello_world('Test')
        self.assertEqual(ret, "Hello")


if __name__ == "__main__":
    # sys.path.append('/Volumes/ssd/code/research-ci-toturial/')
    # print(sys.path)
    unittest.main()