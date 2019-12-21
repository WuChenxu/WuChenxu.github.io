#!/user/bin/env python3
# coding=utf-8
__author__ = "wu_chenxu@126.com"
__version__ = "1.0"
__date__ = "2019-12-21"

import unittest
#import crc8_calc_runtime as CRC8
import crc8_calc_table as CRC8
class TestCrc8_Poly_1D(unittest.TestCase):
    def test_SWS_Crc_00052_MagicNumber(self):
        self.assertEqual(0xC4, 0xFF ^ CRC8.crc_byte([0, 0, 0, 0, CRC8.crc_byte([0, 0, 0, 0])]))

    def test_SWS_Crc_00052_01(self):
        self.assertEqual(0x59, CRC8.crc_byte([0, 0, 0, 0]))

    def test_SWS_Crc_00052_02(self):
        self.assertEqual(0x37, CRC8.crc_byte([0xF2, 0x01, 0x83]))

    def test_SWS_Crc_00052_03(self):
        self.assertEqual(0x79, CRC8.crc_byte([0x0f, 0xaa, 0x00, 0x55]))

    def test_SWS_Crc_00052_04(self):
        self.assertEqual(0xcb, CRC8.crc_byte([0x33, 0x22, 0x55, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]))

    def test_SWS_Crc_00052_05(self):
        self.assertEqual(0x8c, CRC8.crc_byte([0x92, 0x6b, 0x55]))

    def test_SWS_Crc_00052_06(self):
        self.assertEqual(0x74, CRC8.crc_byte([0xff, 0xff, 0xff, 0xff]))






if __name__ == '__main__':
    unittest.main()