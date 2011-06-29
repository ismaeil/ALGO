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

  def test_nouvelOrdre(self):
    """
    ordonne les colonnes dans l'ordre passé en argument à l'aide d'une liste
    ATTENTION : le min de la liste d'ordre est un 0
    """
    t = Table([[0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 0]])
    self.assertEquals(t.nouvelOrdre([3, 1, 0, 2]),[[1, 1, 0], [1, 1, 1], [0, 0, 1], [1, 0, 0]])
    
  def test_goodListe(self):
    """
    [set([]), set([3]), set([]), set([4]), set([1]), set([]), set([]), set([2])]
    se transforme en 
    [3, 4, 1, 2]
    puis en 
    [2, 3, 0, 1] pour être adaptée à la méthode nouvelOrdre
    """
    t = goodListe([set([]), set([3]), set([]), set([4]), set([1]), set([]), set([]), set([2])])
    self.assertEquals(t, [2, 3, 0, 1] )
  
  def test_reorderTab1(self):
    """
    0 1 1 1                           1 1 0 1
    0 1 0 1     se transforme en      0 1 0 1
    1 1 0 0                           0 0 1 1
    """
    t = Table([[0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 0]])
    self.assertEquals(t.reorderTab(),[[1, 0, 0], [1, 1, 0], [0, 0, 1], [1, 1, 1]])

  def test_reorderTab2(self):
    """
    1 0 0 0                           0 0 0 1
    1 1 0 1     se transforme en      1 0 1 1
    1 1 1 0                           0 1 1 1
    """
    t2 = Table([[1, 1, 1], [0, 1, 1], [0, 0, 1], [0, 1, 0]])
    self.assertEquals(t2.reorderTab(),[[0, 1, 0], [0, 0, 1], [0, 1, 1], [1, 1, 1]])

if __name__ == '__main__':
  unittest.main()
