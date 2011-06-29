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
    """"
    Afficher une table en mode liste de listes (colonnes)
    """
    return self.donnee
  
  def reorderListe(self):
    """
    réordonner une liste (vue comme table) en mettant les 0 à gauche et les 1 à droite
    """
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
    """
    ordonner la table itérativement.
    On a besoin de deux listes intermédiaires L(n+1) et L(n). on les appellera LL et L
    la sortie est une liste d'ordre
    """
    nombre_colonnes = len(self.donnee)
    nombre_lignes = len(self.donnee[0])
    LL = [set(range(1, nombre_colonnes + 1))]
    liste_aux = range(1, nombre_lignes + 1)
    liste_aux.reverse()
    for i in liste_aux:
      L = []
      for A in LL:
        E0 = set()
        E1 = set()
        for j in list(A):
          if self.donnee[j - 1][i - 1] == 0:
            E0 = E0 | set([j])
          else:
            E1 = E1 | set([j])
        L.append(E0)
        L.append(E1)
      LL = L
    liste_ordre = goodListe(L)
    resultat = self.nouvelOrdre(liste_ordre)
    return resultat


def goodListe(liste):
  """
  [set([]), set([3]), set([]), set([4]), set([1]), set([]), set([]), set([2])]
  se transforme en 
  [3, 4, 1, 2]
  puis en 
  [2, 3, 0, 1] pour être adaptée à la méthode nouvelOrdre
  """
  sortie0, sortie = [], []
  for u in liste:
    sortie0.extend(u)
  for l in sortie0:
    sortie.append(l -1)
  return sortie
