#! /usr/bin/python
# -*- coding: utf-8 -*-

from utils import transposeData
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
  
  nb_ligne = len(label_ligne) + 1
  
  #trouver les indices pour couper les colonnes
  indice_separation_colonnes = []
  for ens in ordre_colonne[:-1]:
    indice_separation_colonnes.append(list(ens).pop())
    
  #trouver les indices pour couper les lignes
  indice_separation_lignes = []
  for ens in ordre_ligne[:-1]:
    indice_separation_lignes.append(list(ens).pop())
    
  sortie = " " * nb_ligne
  for j, y in enumerate(label_colonne):
    sortie += y + " "
    # séparer label colonnes
    # si les labels colonnes existent
    if set(label_colonne) != set([""]):
      if j in indice_separation_colonnes:
          sortie += "| "
  
  sortie += "\n"
  
  for i, x in enumerate(label_ligne):
    sortie += x.ljust(nb_ligne)
    nb_cols = len(x.ljust(nb_ligne))
    for j, y in enumerate(label_colonne):
      sortie += str(table[j][i]).center(len(y)) + " "
      nb_cols += len(str(table[j][i]).center(len(y)) + " ")
      # séparer colonnes table
      if j in indice_separation_colonnes:
        sortie += "| "
        nb_cols += 2
    # séparer lignes table
    if i in indice_separation_lignes:
        sortie += "\n" + ("-" * nb_cols)
    sortie += "\n"
    
  print sortie
  
#~ #EXEMPLE :
#~ table, label_ligne, label_colonne = imporTable_generique(open('Examples/table_7_10.txt'), False, False)
#~ ordre_ligne = [set([0, 1]), set([2, 3])]
#~ ordre_colonne = [set([0, 1, 2]), set([3, 4]), set([5])]
#~ tabletostr(table, label_ligne, label_colonne, ordre_ligne, ordre_colonne)

def creerFicTable(chemin_repertoire_parent, nom_fic, nb_l, nb_c):
  """
  chemin_repertoire_parent = chemin absou ou relatif sans le / à la fin
  nom_fic = nom fichier sans extension
  
  Exemple : creerFicTable('./Examples', 'table', 10, 20)
  """
  nom_complet_fichier = chemin_repertoire_parent + "/" + nom_fic + "_" + str(nb_l) + "_" + str(nb_c) + ".txt"
  fichier = open(nom_complet_fichier, 'w')
  #générer la liste des lignes
  listelignes = ["" for i in range(nb_l)]
  ligne = ""
  for i in range(nb_l):
    for j in range(nb_c - 1):
      ligne += str(random.randint(0, 1)) + " "
    ligne += str(random.randint(0, 1)) + "\n"
    listelignes[i] = ligne
    ligne = ""
    
  #~ print listelignes
  fichier.writelines(listelignes)
  fichier.close()
  

#~ Exemple :
#~ creerFicTable('./Examples', 'table', 7, 10)
