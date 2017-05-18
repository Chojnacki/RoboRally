# -*- coding: utf-8 -*-
"""
Created on Wed May 17 17:51:10 2017

@author: Corazza
"""

import unittest
import MatriceD as Md

class TestMatrice(unittest.TestCase):
    
    def test_mul(self):
        matrice = Md.MatriceD(2,2,1,[[(1,0,0,1),(0,0,0,0)],[(3,0,1,0),(0,0,1,2)]])
        self.assertEqual((9,0,0,0)*matrice, (9,0,0,0))
        self.assertEqual((9,1,0,0)*matrice, (9,1,0,0))
        self.assertEqual((9,0,1,0)*matrice, (9,0,1,0))
        self.assertEqual((9,1,1,0)*matrice, (9,0,1,2))
        state = (9,0,0,0)
        self.assertEqual(matrice(state), (8,0,0,1))
        
if __name__ == '__main__':
    unittest.main()