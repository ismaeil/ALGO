#! /usr/bin/python
# -*- coding: utf-8 -*-

class Table(object):
  
  """ Une Table 0/1 ser aconsidérée comme une liste de listes (colonnes).
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
    pass
