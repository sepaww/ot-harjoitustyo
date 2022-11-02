
import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.maksu = Maksukortti(0)
        
    def test_kassa_alku(self):
      self.assertEqual(self.kassa.kassassa_rahaa, 100000)
      
    def test_kassa_alku_edu(self):
      self.assertEqual(self.kassa.edulliset, 0)
      
    def test_kassa_alku_kal(self):
      self.assertEqual(self.kassa.maukkaat, 0)
      
    def test_edulkat(self):
      kat=0
      self.kassa.syo_edullisesti_kateisella(kat)
      self.assertEqual(kat, 0)
      self.assertEqual(self.kassa.kassassa_rahaa, 100000)
      self.assertEqual(self.kassa.edulliset, 0)
      
    
    def test_edulkatiso(self):
      kat=241
      self.kassa.syo_edullisesti_kateisella(kat)
      self.assertEqual(kat, 1)
      self.assertEqual(self.kassa.edulliset, 1)
      self.assertEqual(self.kassa.kassassa_rahaa, 100240)
    
    def test_kalliskat(self):
      kat=0
      self.kassa.syo_edullisesti_kateisella(kat)
      self.assertEqual(kat, 0)
      self.assertEqual(self.kassa.maukkaat, 0)
      self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_kalliskatiso(self):
      kat=401
      self.kassa.syo_edullisesti_kateisella(kat)
      self.assertEqual(kat, 1)
      self.assertEqual(self.kassa.maukkaat, 1)
      self.assertEqual(self.kassa.kassassa_rahaa, 100400)
      
    def test_edulkortpien(self):
      self.maksu.lataa_rahaa(0)
      self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.maksu), False)
      self.assertEqual(self.kassa.edulliset, 0)
      self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        
    def test_edulkortiso(self):
      self.maksu.lataa_rahaa(240)
      self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.maksu), True)
      self.assertEqual(self.kassa.edulliset, 1)
      self.assertEqual(self.kassa.kassassa_rahaa, 100240)
      
    def test_maukaskortpien(self):
      self.maksu.lataa_rahaa(0)
      self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.maksu), False)
      self.assertEqual(self.kassa.maukkaat, 0)
      self.assertEqual(self.kassa.kassassa_rahaa, 100000)
     
    def test_maukaskortiso(self):
      self.maksu.lataa_rahaa(400)
      self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.maksu), True)
      self.assertEqual(self.kassa.maukkaat, 1)
      self.assertEqual(self.kassa.kassassarahaa, 100400)
    def test_lataa_vahan(self):
      summa=-1
      self.assertEqual(self.kassa.lataa_rahaa_kortille(maksu, summa), None)
      self.assertEqual(self.kassa.kassassarahaa, 100000)
      
        
    def test_lataa_vahan(self):
      summa=5
      self.assertEqual(self.kassa.lataa_rahaa_kortille(maksu, summa), None)
      self.assertEqual(self.kassa.kassassarahaa, 100005)
      
