import unittest

from translator import en_to_fr, fr_to_en

class engtofr(unittest.TestCase):
    def test1(self):
        self.assertEqual(en_to_fr("Hello"),"Bonjour")
        self.assertEqual(en_to_fr("Bye"),"Au revoir")
        self.assertNotEqual(en_to_fr("Hello"),"Hello")        
class frtoeng(unittest.TestCase):
    def test2(self):
        self.assertEqual(fr_to_en("Bonjour"),"Hi")
        self.assertEqual(fr_to_en("Au revoir"),"Good bye")
        self.assertNotEqual(fr_to_en("Bonjour"),"Bonjour")

unittest.main()