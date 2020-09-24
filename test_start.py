from unittest import TestCase

from start import make_banner


class Test(TestCase):
    def test_make_banner(self):
        banner = make_banner('-', " TEXT ")
        self.assertEqual("\n------\n TEXT \n------", banner)
