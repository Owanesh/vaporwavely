import unittest
from vaporwavely import vaporize


class VaporwavelyTestCase(unittest.TestCase):

    def test_lower(self):
        self.assertEqual('Ｔａｓｓｏｎｉ， ｐａｔｒｉｍｏｎｉｏ ｉｔａｌｉａｎｏ',
                         vaporize('Tassoni, patrimonio italiano'))

    def test_mixed(self):
        self.assertEqual('ａｅｓｔｈｅｔｉｃ ｎｉｎｔｅｎｄｏ', vaporize('aesthetic nintendo'))

    def test_upper(self):
        self.assertEqual('ＶＩＯＬＥＴ ＡＲＥ ＲＥＤ， ＲＯＳＥＳ ＡＲＥ ＢＬＵＥ',
                         vaporize('VIOLET ARE RED, ROSES ARE BLUE'))

    def test_ascii(self):
        # test all vaporizable characters
        for char in range(33, 127):  # '!' is 33 and '~' is 126
            self.assertNotEqual(chr(char),
                                vaporize(chr(char)))
        # test limits of vaporizable range
        self.assertEqual(chr(127),
                         vaporize(chr(127)))
        self.assertEqual(chr(32),
                         vaporize(chr(32)))


if __name__ == '__main__':
    unittest.main()
