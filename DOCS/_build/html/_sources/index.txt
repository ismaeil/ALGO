.. Algorithme de réordonnancement d'une table 0/1 master file, created by
   sphinx-quickstart on Fri Jul 29 01:20:12 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. toctree::
   :maxdepth: 1
   

Table de matières
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Quick start
===========

Algorithme de réordonnancement d'une table 0/1

#. On commence par avoir une table t en la créant ou en l'important d'un fichier:

    * On créé un tableau de colonnes t ::
    
        t = [[0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 0]]
        
    * Ou encore on importe une table depuis un fichier texte ::
    
        t, label_ligne, label_colonne = imporTable_generique(open('Examples/table1.txt'), False, False)
    
#. Puis on l'ordonne selon l'une des deux méthodes suivante

    * Méthode 1 : suppose qu'on connait l'ordre de démontabilité des individus ::
    
        reorderTab(t)
        
        [[1, 0, 0], [1, 1, 0], [0, 0, 1], [1, 1, 1]]
    
    * Méthode 2 : générale, rend l'ordonnancement des lignes et colonnes ::
    
        t = [[1, 1, 0, 1], [0, 1, 0 ,1], [0, 1, 1, 0], [1, 0, 0, 0], [0, 1, 1, 0], [1, 1, 1, 0]]
        
        algo(t)
        
        ([3, 0, 2, 1], [3, 1, 0, 2, 4, 5])
        
    Puis on ordonne la table celon ce nouvel ordre des lignes et colonnes grâce à la fontion reorderLC ::
    
        reorderLC(t, [3, 0, 2, 1], [3, 1, 0, 2, 4, 5])
        
        [[0, 1, 0, 0], [1, 0, 0, 1], [1, 1, 0, 1], [0, 0, 1, 1], [0, 0, 1, 1], [0, 1, 1, 1]]
    


Documentation
=============
.. automodule:: table
   :members:
   
.. automodule:: import_export
   :members:
   
.. automodule:: utils
   :members:


