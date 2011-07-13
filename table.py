#! /usr/bin/python
# -*- coding: utf-8 -*-

def nouvelOrdre(table, liste):
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
    result.append(table[i])
  return result

def reorderTab(table):
  """
  ordonner la table itérativement.
  On a besoin de deux listes intermédiaires L(n+1) et L(n). on les appellera LL et L
  la sortie est une liste d'ordre
  """
  nombre_colonnes = len(table)
  nombre_lignes = len(table[0])
  LL = [set(range(1, nombre_colonnes + 1))]
  liste_aux = range(1, nombre_lignes + 1)
  liste_aux.reverse()
  for i in liste_aux:
    L = []
    for A in LL:
      E0 = set()
      E1 = set()
      for j in list(A):
        if table[j - 1][i - 1] == 0:
          E0 = E0 | set([j])
        else:
          E1 = E1 | set([j])
      L.append(E0)
      L.append(E1)
    LL = L
  liste_ordre = goodListe(L)
  #indice mini = 0
  aux = []
  for i in liste_ordre:
    aux.append(i - 1)
  resultat = nouvelOrdre(table, aux)
  return resultat


def goodListe(liste):
  """
  [set([]), set([3]), set([]), set([4]), set([1]), set([]), set([]), set([2])]
  se transforme en 
  [3, 4, 1, 2]
  """
  sortie = []
  for u in liste:
    sortie.extend(u)
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
  cette méthode retourne un tableau de tableau
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
  return transposeData(sortie)
  

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
  /!\ cette méthode donne bien un élèment maximal, mais il faut aussi tenir compte des autres
  /!\ élèments maximaux qui n'ont pas un poid maximal
  /!\ 
  /!\ Exemple :
  /!\ 1 0 1
  /!\ 0 1 0
  /!\ les deux lignes sont maximales (aucune n'est incluse dans l'autre) même si la première a plus de 
  /!\ poid que la seconde.
  /!\ La méthode actuelle ne tient pas compte de ce fait !
  
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
  
  Remarque : Dans l'algo, quand on ne peut pas découper (en retour), on laisse l'ensemble tel quel et il est finalement découpé
   avec goodListe.
   exemple : 
  lors du test_alogo1 les colonnes {2, 4} ne sont pas séparées ni en allé ni en retour (car en plus les deux colonnes sont identiques)
  cette non séparation ne disaprait qu'à l'étape de la méthode goodListe 
  """
  pivot, c1 = choixPivot(T, L[indice_ligne], C[indice_colonne])
  c0 = C[indice_colonne] - c1
  l1, l0 = [], []
  aux = 0
  for i in L[indice_ligne]:
    for j in c1:
      aux += T[j][i]
      
    if aux == len(c1):
      l1.append(i)
      aux = 0
    else:
      l0.append(i)
      aux = 0
  
  l1, l0 = set(l1), set(l0)
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

def algo(T):
  """
  à partir d'une table, on rend la liste des lignes et des colonnes après application de l'algo
  Si on veux, on peut appliquer la méthode nouvelOrdreLC pour réordonner ainsi la table.
  Exemple :
  à partir de :
      c0 c1 c2 c3 c4 c5
  l0* 1  0  0  1  0  1
  l1* 1  1  1  0  1  1
  l2* 0  0  1  0  1  1
  l3* 1  1  0  0  0  0
   qui est t = [[1, 1, 0, 1], [0, 1, 0 ,1], [0, 1, 1, 0], [1, 0, 0, 0], [0, 1, 1, 0], [1, 1, 1, 0]]
  
  rendre l'ordre de 
      c3 c1 c0 c2 c4 c5
  l3* 0  1  1  0  0  0
  l0* 1  0  1  0  0  1
  l2* 0  0  0  1  1  1
  l1* 0  1  1  1  1  1
  
  la sortie doit donc être : L, C = [3, 0, 2, 1], [3, 1, 0, 2, 4, 5]
  """
  
  #LE T passé en argument est tel que la première ligne est d'indice 0 (adoption de cet ardre pour toutes les méthodes dès le début)
  #Mais l'algo est tel que la dernière ligne est d'indice 0
  #on commence donc par inverser les ligne de T
  #T = invLigne(T)
  L, C = [set(range(len(T[0])))], [set(range(len(T)))]
  pos_l, pos_c = 0, 0
  pile = [-1]
  
  while pile:
    c0, c1, l0, l1 = decoupage(pos_l, pos_c, L, C, T)
    new_pos_c, new_pos_l, L, C = maj(pos_c, pos_l, L, C, c0, c1, l0, l1)
    #reculer
    if (new_pos_l == pos_l) and (pos_l + 1 >= len(L)):
      pos_c -= 1
      pos_l = pile.pop() + 1
    else:
      if (new_pos_c > pos_c):
        pile.append(pos_c)
        pos_c += 1
      pos_l +=  1
  #l'algo considère que le première ligne de la atble est d'indice le plus grand : il faut donc inverser L
  L.reverse()
  #
  return goodListe(L), goodListe(C)
