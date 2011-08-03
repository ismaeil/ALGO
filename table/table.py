#! /usr/bin/python
# -*- coding: utf-8 -*-

from utils import *

def algo(T):
    """
    À partir d'une table, on rend la liste des lignes et des colonnes après application de l'algo
    Si on veux, on peut appliquer la méthode nouvelOrdreLC pour réordonner ainsi la table.

    Exemple :

    à partir de :
        === === === === === === ===
        \   c0  c1  c2  c3  c4  c5
        === === === === === === ===
        l0  1   0   0   1   0   1 
        l1  1   1   1   0   1   1 
        l2  0   0   1   0   1   1 
        l3  1   1   0   0   0   0 
        === === === === === === ===

    qui est ::

        t = [[1, 1, 0, 1], [0, 1, 0 ,1], [0, 1, 1, 0], [1, 0, 0, 0], [0, 1, 1, 0], [1, 1, 1, 0]]

    rendre :
        === === === === === === ===
        \   c3  c1  c0  c2  c4  c5 
        === === === === === === ===
        l3  0   1   1   0   0   0 
        l0  1   0   1   0   0   1 
        l2  0   0   0   1   1   1 
        l1  0   1   1   1   1   1 
        === === === === === === ===
    
    la sortie doit donc être :: 

        L, C = [3, 0, 2, 1], [3, 1, 0, 2, 4, 5]
        
    """

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
    #l'algo considère que le première ligne de la table est d'indice le plus grand : il faut donc inverser L
    L.reverse()
    #
    return goodListe(L), goodListe(C)
  
