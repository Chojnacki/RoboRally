# -*- coding: utf-8 -*-
"""
Created on Thu May 18 10:14:17 2017

@author: Chojnacki
"""

import unittest
import IA as ia

class TestIA(unittest.TestCase):
    
    def scalaire(self):
        v1 = (1,0)
        v2 = (1,0)
        self.assertEqual(scalaire(v1,v2),1)
        v1 = (1,0)
        v2 = (-1,0)
        self.assertEqual(scalaire(v1,v2),-1)
        v1 = (0,1)
        v2 = (0,1)
        self.assertEqual(scalaire(v1,v2),1)
        v1 = (0,1)
        v2 = (0,-1)
        self.assertEqual(scalaire(v1,v2),-1)
        v1 = (0,1)
        v2 = (1,0)
        self.assertEqual(scalaire(v1,v2),0)
        v1 = (1,0)
        v2 = (0,1)
        self.assertEqual(scalaire(v1,v2),0)
        
    def ditance(self):
        p1 = (0,0)
        p2 = (0,0)
        self.assertEqual(scalaire(v1,v2),0)
        p1 = (0,0)
        p2 = (1,0)
        self.assertEqual(scalaire(v1,v2),1)
        p1 = (0,0)
        p2 = (2,0)
        self.assertEqual(scalaire(v1,v2),4)
        p1 = (0,0)
        p2 = (0,1)
        self.assertEqual(scalaire(v1,v2),1)
        p1 = (0,0)
        p2 = (1,0)
        self.assertEqual(scalaire(v1,v2),1)
        p1 = (0,0)
        p2 = (0,1)
        self.assertEqual(scalaire(v1,v2),1)
        
        
if __name__ == '__main__':
    unittest.main()