Algorithme de réordonnancement d'une table 0/1 ordonnable ou pas !
Dans cet algorithme on réordonne que les colonnes

    0 1 1 1                           1 1 0 1
    0 1 0 1     se transforme en      0 1 0 1
    1 1 0 0                           0 0 1 1
    
Pour celà on créé un tableau de colonnes t :
>>>t = [[0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 0]]

Méthode 1 : suppose qu'on connait l'ordre de démontabilité des individus
>>>reorderTab(t)
[[1, 0, 0], [1, 1, 0], [0, 0, 1], [1, 1, 1]]

Méthode 2 : générale, rend l'ordonnancement des lignes et colonnes
>>>t = [[1, 1, 0, 1], [0, 1, 0 ,1], [0, 1, 1, 0], [1, 0, 0, 0], [0, 1, 1, 0], [1, 1, 1, 0]]
>>>algo(t)
([3, 0, 2, 1], [3, 1, 0, 2, 4, 5])
