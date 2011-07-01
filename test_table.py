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
   
  def test_transposeData(self):
    """
    entree = [[1, 2, 3, 4, 5],[11, 12, 13, 14, 15],[21, 22, 23, 24, 25]]
    sortie = [[1, 11, 21], [2, 12, 22], [3, 13, 23], [4, 14, 24], [5, 15, 25]]
    """
    t = [[1, 2, 3, 4, 5],[11, 12, 13, 14, 15],[21, 22, 23, 24, 25]]
    self.assertEquals(transposeData(t), [[1, 11, 21], [2, 12, 22], [3, 13, 23], [4, 14, 24], [5, 15, 25]])
  
  def test_imporTable(self):
    """
    importer le fichier Examples/table1.txt
    et construire l'objet Table correspondant
    """
    t = imporTable('Examples/table1.txt')
    self.assertEquals(t.donnee, [[1, 1, 0, 1], [0, 1, 0 ,1], [0, 1, 1, 0], [1, 0, 0, 0], [0, 1, 1, 0], [1, 1, 1, 0]])

  def test_reorderLC(self):
    """
    on donne la table, un ordre sur les lignes et sur les colonnes et on reordonne
    entrée : liste de listes + ordre ligne + ordre colonne
    sortie : liste de listes
    """
    t = [[1, 2, 3, 4, 5],[11, 12, 13, 14, 15],[21, 22, 23, 24, 25]]
    result = [[23, 22, 25, 24, 21], [3, 2, 5, 4, 1], [13, 12, 15, 14, 11]]
    self.assertEquals(reorderLC(t, [2, 1, 4, 3, 0], [2, 0, 1]), result)
  
if __name__ == '__main__':
  unittest.main()
