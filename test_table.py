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

  def test_affiche(self):
    #~ t = Table([1, 0, 1, 0])
    t1 = Table([[1, 1, 0], [1, 0, 0], [1, 0, 1], [0, 0, 1], [0, 1, 0]])
    #~ self.assertEquals(t.affiche(),[1, 0, 1, 0])
    self.assertEquals(t1.affiche(),[[1, 1, 0], [1, 0, 0], [1, 0, 1], [0, 0, 1], [0, 1, 0]])
  
  def test_reorderListe(self):
    """cette méthode ne sert à rien puisque dans une vrai table on 
    échangera les colonnes
    """
    l = Table([1, 1, 0, 1, 0])
    self.assertEquals(l.reorderListe(),[0, 0, 1, 1, 1])

  
  def test_reorderTab(self):
    """
    0 1 1 1                           1 1 0 1
    0 1 0 1     se transforme en      0 1 0 1
    1 1 0 0                           0 0 1 1
    """
    pass
    #~ t = Table([[0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 0]])
    #~ self.assertEquals(t.reorderTab(),[[1, 0, 0], [1, 1, 0], [0, 0, 1], [1, 1, 1]])

  def test_permCol(self):
    t = Table([[0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 0]])
    self.assertEquals(t.permCol(0, 2),[[1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 0]])

  def test_keyZeroUn(self):
    t = Table([1, 0, 0, 0, 1])
    self.assertEquals(t.keyZeroUn(),[[1, 2, 3], [0, 4]])
    t2 = Table([1, 0, 0, 0, 1, 1, 1, 1])
    self.assertEquals(t2.keyZeroUn(),[[1, 2, 3], [0, 4, 5, 6, 7]])
    
  def test_getLigne(self):
    t = Table([[0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 0]])
    self.assertEquals(t.getLigne(2),[1, 1, 0, 0])
    self.assertEquals(t.getLigne(1),[0, 1, 0, 1])



if __name__ == '__main__':
  unittest.main()
