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

def transposeData(listedelistes):
  """
  l'entrée est la liste des colonnes et la sortie est la liste des lignes
  entrée = [[1, 2, 3, 4, 5],[11, 12, 13, 14, 15],[21, 22, 23, 24, 25]]
  sortie = [[1, 11, 21], [2, 12, 22], [3, 13, 23], [4, 14, 24], [5, 15, 25]]
  """
  nbcolonnes = len(listedelistes) #3
  nblignes = len(listedelistes[0]) #5
  sortie = [[] for i in range(nblignes)] #5 lignes
  
  for col in listedelistes:
    for ligne in range(nblignes):
      sortie[ligne].append(col[ligne])
  return sortie 
  
def imporTable(chemin):
  """
  importer le fichier Examples/table1.txt
  et construire l'objet Table correspondant
  cette méthode retourne un objet Table
  """
  fichier = open(chemin ,'r')
  """
  sortie = liste de listes de lignes
  """
  sortie = []
  for ligne in fichier:
    aux = ligne.split()
    aux = map (int, aux)
    sortie.append(aux)
  fichier.close()
  sortie = transposeData(sortie)
  
  return Table(sortie)
