#! /usr/bin/python
# -*- coding: utf-8 -*-

class Table(object):
  
  """ Une Table 0/1
  """
  def __init__(self, liste):
    self.donnee = liste
  
  def affiche(self):
    return self.donnee
