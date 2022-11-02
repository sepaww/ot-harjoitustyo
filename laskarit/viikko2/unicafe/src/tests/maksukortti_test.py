import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
             
    def test_saldo_nousee_lisattaessa(self):
        temp=self.maksukortti.saldo
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")
        
    def test_saldo_vah(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 8.00 euroa")
        
    def test_saldon_otto_onnistui(self):
        temp=self.maksukortti.ota_rahaa(200)
        self.assertEqual(temp, True)
        
    def test_liian_vahan_rahaa(self):
        self.maksukortti=Maksukortti(0)
        temp=self.maksukortti.ota_rahaa(100)
        self.assertEqual(temp, False)
        
        
