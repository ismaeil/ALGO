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
  sortie = []
  for ligne in fichier:
    aux = ligne.split()
    aux = map (int, aux)
    sortie.append(aux)
  fichier.close()
  sortie = transposeData(sortie)
  
  return Table(sortie)

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

def choixPivot(table, ensemble_ligne):
  """
  On entend par pivot la ligne qui a le plus grand poid
  Exemple :
  1 0 0 1 0 1
  1 1 1 0 1 1
  0 0 1 0 1 1
  1 1 0 0 0 0
  
  qui est table = [[1, 1, 0, 1], [0, 1, 0 ,1], [0, 1, 1, 0], [1, 0, 0, 0], [0, 1, 1, 0], [1, 1, 1, 0]]
  on a choixPivot(table, set([0, 1, 3])) = 1 car le poid de la ligne 1 est cinq et est supérieur ou égal 
  au poid des autres lignes. 
  """
  resultat = -1
  somme = 0
  for k in ensemble_ligne:
    aux = sum(table[i][k] for i in range(len(table)))
    if aux >= somme:
      somme = aux
      resultat = k
  return resultat
  
  
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


def monter(table):
  """
  Monter la table suivante :
  1 0 0 1 0 1
  1 1 1 0 1 1
  0 0 1 0 1 1
  1 1 0 0 0 0
  suivant le nouvel algorithme et rendre les listes semi-triée des lignes et colonnes sous forme d'une
  liste de listes ligne puis colonne.
  """
  ordre_lignes = [set(range(len(table[0])))]
  ordre_colonnes = [set(range(len(table)))]
  lignes_autorisees = ordre_lignes[0] #set
  colonnes_autorisees = ordre_colonnes[-1] #set
  
  #~ #monter c'est parcourir les lignes !
  for i in range(len(table[0])):
    #les lignes non vues sont toujours dans le premier set de la liste
    ligne_elue = choixPivot(table, lignes_autorisees)
    
    #mettre ligne_elue en bas et donc redéfinir ordre_lignes
    ordre_lignes = [lignes_autorisees - set([ligne_elue]), set([ligne_elue])] + ordre_lignes[1:]   
    #redéfinir lignes_autorisees
    lignes_autorisees = ordre_lignes[0]
    
    #entasser la ligne elue et donc redéfinir ordre_colonnes
    ordre_colonnes = ordre_colonnes[:-1] + entasserLigne(table, ligne_elue, colonnes_autorisees)
    #redéfinir lignes_autorisees
    colonnes_autorisees = ordre_colonnes[-1]
  
  return [ordre_lignes, ordre_colonnes]

############################################################
#                          WARNING                          
############################################################
#  Le choix du pivot doit t-il se faire selon le poid des   
#  lignes autorisées seulement ou faut-il prendre  en compte 
#  les colonnes autorisées aussi ? 
#
#  Doit-on laisser les vides dans le resultat de monter                         
#                                                           
############################################################  
