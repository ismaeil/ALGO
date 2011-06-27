#! /usr/bin/python
# -*- coding: utf-8 -*-

class Table(object):
  
  """ Une Table 0/1 sera considérée comme une liste de listes (colonnes).
  Exemple : 
  1 1 1 0 0
  1 0 0 0 1
  0 0 1 1 0
  est :
  [[1, 1, 0], [1, 0, 0], [1, 0, 1], [0, 0, 1], [0, 1, 0]]
  """
  def __init__(self, liste):
    self.donnee = liste
  
  def affiche(self):
    return self.donnee

  def reorderListe(self):
    li = self.donnee
    li.sort()
    return li
    
  def reorderTab(self):
    #~ nligne = len(self.donnee)
    #~ ncolonne = len(self.donnee[0])
    pass
  
  def permCol(self, i, j):
    """
    échange les colonnes i et j
    """
    self.donnee[i], self.donnee[j] = self.donnee[j], self.donnee[i]
    return self.donnee
