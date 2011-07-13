#! /usr/bin/python
# -*- coding: utf-8 -*-

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

  
