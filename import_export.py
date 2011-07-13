#! /usr/bin/python
# -*- coding: utf-8 -*-

from utils import transposeData

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

#~ def tabletostr(table, label_ligne, label_colonne, ordre_ligne, ordre_colonne):
  #~ 
  
