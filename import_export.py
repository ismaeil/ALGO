#! /usr/bin/python
# -*- coding: utf-8 -*-

from utils import *
from table import *
import random

def imporTable(fichier):
  """
  Cas table sans labels
  importer le fichier Examples/table1.txt
  et construire la table correspondante
  cette méthode retourne un tableau de tableau
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
  
  
def imporTable_generique(fichier, label_lignes=False, label_colonnes=False):
  """
  Cas table sans labels
  importer le fichier Examples/table1.txt
  et construire la table correspondante
  cette méthode retourne un tableau de tableau
  sortie = liste de listes de lignes
  """

  if label_colonnes:
    label_table_colonnes = fichier.readline().split()
    
  sortie = []
  label_table_lignes = []
  for ligne in fichier:
    elems = ligne.split()
    if label_lignes:
      label_table_lignes.append(elems.pop(0))
    else:
      label_table_lignes.append("")
    
    sortie.append([int(x) for x in elems])

  if not label_colonnes:
    label_table_colonnes = ["" for x in sortie[0]]
    
  return transposeData(sortie), label_table_lignes, label_table_colonnes
  


def tabletostr(table, label_ligne, label_colonne, ordre_ligne, ordre_colonne):
  
  label_l = [label_ligne[i] for i in goodListe(ordre_ligne)]
  label_c = [label_colonne[i] for i in goodListe(ordre_colonne)]
  ordre_l = customap(ordre_ligne)
  ordre_c = customap(ordre_colonne)
  t = reorderLC(table, goodListe(ordre_ligne), goodListe(ordre_colonne))
  
  nb_ligne = len(label_l) + 1
  
  #trouver les indices pour couper les colonnes
  indice_separation_colonnes = []
  for ens in ordre_c[:-1]:
    indice_separation_colonnes.append(list(ens).pop())
    
  #trouver les indices pour couper les lignes
  indice_separation_lignes = []
  for ens in ordre_l[:-1]:
    indice_separation_lignes.append(list(ens).pop())
    
  sortie = " " * nb_ligne
  for j, y in enumerate(label_c):
    sortie += y + " "
    # séparer label colonnes
    # si les labels colonnes existent
    if set(label_c) != set([""]):
      if j in indice_separation_colonnes:
          sortie += "| "
  
  sortie += "\n"
  
  for i, x in enumerate(label_l):
    sortie += x.ljust(nb_ligne)
    nb_cols = len(x.ljust(nb_ligne))
    for j, y in enumerate(label_c):
      sortie += str(t[j][i]).center(len(y)) + " "
      nb_cols += len(str(t[j][i]).center(len(y)) + " ")
      # séparer colonnes t
      if j in indice_separation_colonnes:
        sortie += "| "
        nb_cols += 2
    # séparer lignes t
    if i in indice_separation_lignes:
        sortie += "\n" + ("-" * nb_cols)
    sortie += "\n"
    
  print sortie
  
#~ #EXEMPLE :
#~ table, label_ligne, label_colonne = imporTable_generique(open('Examples/table_7_10.txt'), True, True)
#~ ordre_ligne = [set([0, 1]), set([2, 3]), set([4, 5, 6])]
#~ ordre_colonne = [set([0, 1, 2]), set([3, 4]), set([5, 6, 7, 8, 9])]
#~ tabletostr(table, label_ligne, label_colonne, ordre_ligne, ordre_colonne)

def creerTable(nb_l, nb_c):
  """
  créer une table aléatoire à partir qui a nb_l lignes et nb_c colonnes
  """
  listecolonnes = [[] for j in range(nb_c)]
  for j in range(nb_c):
    for i in range(nb_l):
      listecolonnes[j].append(random.randint(0, 1))
    
  return listecolonnes
  
