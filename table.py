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

  def permCol(self, i, j):
    """
    échange les colonnes i et j
    """
    self.donnee[i], self.donnee[j] = self.donnee[j], self.donnee[i]
    return self.donnee
    
  def keyZeroUn(self):
    """
    à priori cette méthode est indépendante de la classe Table
    entrée = une liste de 0 1 par exemple [1, 0, 0, 0, 1]
    sortie = une liste de deux liste la première contient les clés des 0 et la seconde
    les clés de 1 donc : [[1,2,3], [0,4]]
    """
    li = self.donnee
    un =[]
    zero =[]
    for i in range(len(li)):
      if li[i] == 1:
        un += [i]
      else:
        zero += [i]
    return [zero, un]
       
  def getLigne(self, ligne):
    li = []
    for i in range(len(self.donnee)):
      li.append(self.donnee[i][ligne])
    return li

  def nouvelOrdre(self, liste):
    """
    réordonner les colonnes suivant la liste en tant qu'index
    exemple :
    la résultat du réordonnancement de 
    [[0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 0]]
    suivant la table [3, 1, 0, 2]
    est
    [[1, 1, 0], [1, 1, 1], [0, 0, 1], [1, 0, 0]]
    """
    result = []
    for i in range(len(self.donnee)):
      result.append(self.donnee[liste[i]])
    return result
    
  def reorderTab(self):
    #~ nligne = len(self.donnee)
    #~ ncolonne = len(self.donnee[0])
    pass
  
