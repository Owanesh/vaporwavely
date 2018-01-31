from vaporwavely import vaporipsum
import unittest


class VaporwavelyTestCase(unittest.TestCase):

    def test_mocked(self):
        pass

    def test_empty(self):
        self.assertNotEqual('', vaporipsum())


if __name__ == '__main__':
    unittest.main()
