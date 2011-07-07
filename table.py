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
    for i in liste:
      result.append(self.donnee[i])
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
  sortie = [[int(x) for x in ligne.split()] for ligne in fichier]
  #~ sortie = []
  #~ for ligne in fichier:
    #~ aux = ligne.split()
    #~ aux = map (int, aux)
    #~ sortie.append(aux)
  #~ fichier.close()
  #~ sortie = transposeData(sortie)
  #~ 
  return Table(transposeData(sortie))

def reorderLC(table, ordrel, ordrec):
  """
  on donne la table, un ordre sur les lignes et sur les colonnes et on reordonne
  entrée : liste de listes + ordre ligne + ordre colonne
  sortie : liste de listes
  """
  sortie =[[] for i in ordrec]
  for c in range(len(ordrec)):
    for l in range(len(ordrel)):
      sortie[c].append(table[ordrec[c]][ordrel[l]])
  return sortie

def choixPivot(table, ensemble_ligne, ensemble_colonne):
  """
  On entend par pivot la ligne qui a le plus grand poid
  Exemple :
        * 
  1 0 0 1 0 1
  1 1 1 0 1 1
  0 0 1 0 1 1
  1 1 0 0 0 0
  
  qui est t = [[1, 1, 0, 1], [0, 1, 0 ,1], [0, 1, 1, 0], [1, 0, 0, 0], [0, 1, 1, 0], [1, 1, 1, 0]]
  on a choixPivot(t, set([0, 1, 3]), set([0, 1, 2, 3, 4, 5])) = 1 car le poid de la ligne 1 est 
  (selon les colonnes : set([0, 1, 2, 3, 4, 5])) cinq et est supérieur ou égal au poid des autres lignes. 
  le choix du pivot est fait parmi les lignes autorisées et les colonnes autorisées
  
  retourner la ligne pivot et l'ensemble des colonnes où elle a des 1
  """
  resultat = -1
  somme = 0
  for k in ensemble_ligne:
    aux = sum(table[i][k] for i in ensemble_colonne)
    if aux >= somme:
      somme = aux
      resultat = k
  colonnes_elues = set([j for j in ensemble_colonne if table[j][resultat] == 1])
  return resultat, colonnes_elues
  
  
def entasserLigne(table, ligne, colonnes_autorisees):
  """
  entasser une ligne selon un ensemble de colonnes revient à mettre tous ses 1 à droite et ses zero 
  à gauche en changeant ainsi l'ordre des colonnes autorisée.
    """
  zero, un = [], []
  for i in colonnes_autorisees:
    if table[i][ligne] == 0:
      zero.append(i)
    else:
      un.append(i)
  nouvel_ordre_colonnes_autorisees = [set(zero), set(un)] # il peut y avir des ensembles vides
  
  return nouvel_ordre_colonnes_autorisees

def decoupage(indice_ligne, indice_colonne, L, C, T):
  """
  à partir de indice_colonne, indice_ligne, L (liste d'ensemble), C (liste d'ensemble) et la 
  table ; retourner c0, c1, l0, l1 (ensembles)
  
  Explications:
  1) choisir pivot in L[indice_ligne] tq le nombre de 1 de la ligne pivot soit max dans C[indice_colonne]
  2) c1 = ensemble de colonnes de C[indice_colonne] tq pivot à un 1 sur celles ci
  3) c0 = ...
  4) l1 = ensemble des elts de L[indice_ligne] qui ont des 1 sur ts les element de c1 (EXTENSION du pivot)
  5) l0 = L[indice_ligne] \ l1
  
  Exemple:
 
           * 0 1 2 3 4 5
         * * * * * * * *
  T =     0* 1 0 0 1 0 1
          1* 1 1 1 0 1 1
          2* 0 0 1 0 1 1
          3* 1 1 0 0 0 0
  
  C = [{2, 3, 4}, {0, 1, 5}]
  L = [{3}, {0, 2}, {1}]
  indice_ligne = 1
  indice_colonne = 0
  pivot = 2 (in L[1] = {0, 2} qui maximise C[0] = {2, 3, 4})
  c1 = {2, 4}
  c0 = {3}
  l1 = {2}
  l0 = {0}
  """
  pivot, c1 = choixPivot(T, L[indice_ligne], C[indice_colonne])
  c0 = C[indice_colonne] - c1
  l1 = []
  for i in L[indice_ligne]:
    for j in c1:
      if T[j][i] == 1:
        l1.append(i)
  l1 = set(l1)
  l0 = L[indice_ligne] - l1
  
  return c0, c1, l0, l1

def maj(pos_c, pos_l, L, C, c0, c1, l0, l1):
  """
  methode auxiliaire pour le programme principal
  """
  if (c0 != set([]) and c1 != set([])):
    C = C[:pos_c] + [c0, c1] + C[pos_c + 1:]
    new_pos_c = pos_c + 1
  else:
    new_pos_c = pos_c
    
  if (l0 != set([]) and l1 != set([])):
    L = L[:pos_l] + [l1, l0] + L[pos_l + 1:]
    new_pos_l = pos_l + 1
  else:
    new_pos_l = pos_l
  
  return new_pos_c, new_pos_l, L, C
