#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import os
import sys

dirname = os.path.dirname(__file__)
if dirname == '':
    dirname = '.'
dirname = os.path.realpath(dirname)
updir = os.path.split(dirname)[0]
if updir not in sys.path:
    sys.path.append(updir)


from table import *

class TableAffichageTest(unittest.TestCase):
  
  """
  Classe de tests du réordonnancement de la table 0/1.
  """

  def test_affiche1(self):
    table1 = Table([1, 0])
    self.assertEquals(table1.affiche(),[1,0])
    #~ self.assertEquals(reorder([1,0]),[0,1])
    #~ self.assertRaises(ZeroDivisionError, division, 10, 0)    

if __name__ == '__main__':
  unittest.main()
