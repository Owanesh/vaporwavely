from vaporwavely import vaporize
import unittest

class VaporwavelyTestCase(unittest.TestCase):

    def test_lower(self):
        self.assertEqual('Ｔａｓｓｏｎｉ, ｐａｔｒｉｍｏｎｉｏ ｉｔａｌｉａｎｏ', vaporize('Tassoni, patrimonio italiano'))

    def test_mixed(self):
        self.assertEqual('ａｅｓｔｈｅｔｉｃ ｎｉｎｔｅｎｄｏ', vaporize('aesthetic nintendo'))

    def test_upper(self):
        self.assertEqual('ＶＩＯＬＥＴ ＡＲＥ ＲＥＤ, ＲＯＳＥＳ ＡＲＥ ＢＬＵＥ', vaporize('VIOLET ARE RED, ROSES ARE BLUE'))




if __name__ == '__main__':
    unittest.main()
