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
    l = Table([1, 1, 0, 1, 0])
    self.assertEquals(l.reorderListe(),[0, 0, 1, 1, 1])

  
  def test_reorderTab(self):
    #~ t = liste de listes
    #~ self.assertEquals(t.reorderTab(),liste de listes ordonnées)
    pass

if __name__ == '__main__':
  unittest.main()
